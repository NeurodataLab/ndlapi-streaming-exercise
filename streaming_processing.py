"""
NeurodataLab LLC 09.12.2019
Created by Andrey Belyaev
"""
import cv2
import json
from queue import Empty
from multiprocessing import Event, Process, Queue


class IWebCamStreamProcessing:
    """
    Webcam stream processing interface.
    Takes images from webcam, process it via NDL API and visualize results
    :param service: NDL API service
    """
    def __init__(self, service):
        self.service = service

        # Assign streaming function to service. This function have to yield images and will be called from NDL API core
        self.service.set_streaming_function(self.iterate_webcam_images, 'image')

        # Create images and result sources for communication between several processes
        self.images_queue, self.result_queue = Queue(), Queue()

        # Create event for stopping the system
        self.stop_event = Event()
        self.stop_event.clear()

    def iterate_webcam_images(self):
        """
        Iterates over images stream.
        Takes images from input source (i.e. queue) and send it to NDL API
        Raises Empty if there are no images to send for at least 5 seconds
        """
        try:
            # Do until somebody stop event
            while not self.stop_event.is_set():
                # Get image from input source
                image = self.images_queue.get(timeout=5)

                # Yield image for NDL API
                yield image

        except Empty:
            print('Webcam timeout exceeded. Aborting.')
            raise
        except:
            print('Exception in iterating webcam images. Aborting')
            raise
        finally:
            print('Webcam iterating was successfully stopped')

    def iterate_api_responses(self):
        """
        Iterates over NDL API responses
        Takes response from NDL API, translates it to the correct format and puts to the target source (i.e. queue)
        Raises BaseException in case of postprocessing error
        """
        try:
            # Do until service stop processing
            for response in self.service.process_stream():
                # Get result and translate it to the correct format
                result = {i: json.loads(image_res.result) for i, image_res in enumerate(response[1])}
                processed_result = self.service._postprocess_result(result)

                # Put result to target source
                self.result_queue.put(processed_result)

                # Check system is not stopped
                if self.stop_event.is_set():
                    break
        except:
            print("Exception while iterating API response")
            raise
        finally:
            self.stop_event.set()

    def start_streaming(self):
        """
        Start webcam streaming.
        Open webcam stream and process images from it
        Creates additional process to iterate over NDL API responses
        :return:
        """
        # Create and start parallel process for iterating over NDL API response
        response_iterating_process = Process(target=self.iterate_api_responses)
        response_iterating_process.daemon = True
        response_iterating_process.start()

        # Last processed result
        last_result = None
        # Open webcam stream
        cap = cv2.VideoCapture(0)
        # Get first frame from webcam stream
        ret, frame = cap.read()

        # Check that webcam works normally and nobody stopped the system
        while ret and not self.stop_event.is_set():
            # Check if last putted images already processed
            if self.images_queue.empty():
                self.images_queue.put(frame)

            # Check if there is new processing result
            if not self.result_queue.empty():
                last_result = self.result_queue.get()

            # Visualize result on frame
            vis_frame = self.visualize_result(frame, last_result)
            # Show frame
            cv2.imshow('webcam', vis_frame)
            # Wait 50ms for any key pressed. Stops system if 'q' was pressed.
            if cv2.waitKey(50) & 0xff == ord('q'):
                break

            # Read next frame
            ret, frame = cap.read()

        # Stop system
        self.stop_event.set()
        # Release webcam
        cap.release()
        print('Webcam capture released')

    def visualize_result(self, image, res=None):
        """
        Visualizes data on image
        :param image: image from webcam stream
        :param res: result from NDL API
        :return: image with visualized data
        """
        raise NotImplementedError


class WebCamFaceDetectorStreamProcessing(IWebCamStreamProcessing):
    def visualize_result(self, image, res=None):
        # Check res is normal format
        if res is not None and len(res) > 0:
            # Visualize each faces in result
            for face in res[0]:
                # Get face coordinates
                x, y, w, h = list(map(int, [face[k] for k in ('x', 'y', 'w', 'h')]))
                # Draw rectangle on image
                cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 255))

        return image
