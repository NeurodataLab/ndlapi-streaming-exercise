"""
NeurodataLab LLC 09.12.2019
Created by Andrey Belyaev
"""
import argparse
from ndlapi.api import create_credentials, get_service_by_name, images_services_list
from streaming_processing import WebCamFaceDetectorStreamProcessing


def parse():
    """
    Parse command line arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--keys-path', required=True, type=str,
                        help='Path to folder with keys downloaded from api.neurodatalab.dev')
    parser.add_argument('--service', required=True, type=str,
                        help='Service to process video. Available services: %s' % str(images_services_list))
    return parser.parse_args()


if __name__ == '__main__':
    # Parse command line arguments
    args = parse()

    # Check service type. This example works only with Face Detector
    assert args.service in ('FaceDetector', 'fd'), 'Only Face Detector service is available in example'

    # Create ssl authorization token
    ssl_auth = create_credentials(args.keys_path)
    # Create service
    service = get_service_by_name(args.service, ssl_auth)

    # Initialize webcam streaming class
    webcam_streamer = WebCamFaceDetectorStreamProcessing(service)
    # Start streaming
    webcam_streamer.start_streaming()
