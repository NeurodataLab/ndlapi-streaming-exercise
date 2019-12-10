# Neurodata Lab API streaming exercise
Exercise using Neurodata Lab API streaming capabilities


### General description

In this exercise you will learn how to use Neurodata Lab API tool, how to process
images and videos, and how to create your own real-time
stream processing tool using Neurodata Lab API.


#### Requirements

Python >3.5 is highly recommended, but you can also work
with unsupported python 2 version.


#### Installation

`pip install ndl-api`


#### Key generation

1. Register on [Neurodata Lab API site](https://api.neurodatalab.dev)
2. Create a new key. You can create as many keys
as you need with as many permissions as you want.
3. Download the keys to your computer
(assume you download it to the `KEYS` folder)


#### First try

Assume that you have the key with FaceDetector permission and you have
a video by `video.mp4` path. To process this video using FaceDetector
service via Neurodata Lab API package for python >3.5 run

`python3 -m ndlapi.process_video --keys-path KEYS --video-path video.mp4
--service FaceDetector --result-path ndlapi_results`

When the video will be successfully processed,
results will appear in the `ndlapi_results` folder

More information about the usage and results structure is available in
[docs](https://api.neurodatalab.dev/docs)


### Streaming exercise

The main goal of this exercise is to learn how to use Neurodata Lab API
capabilities to create real-time video processing program. There is an
example in this git which can handle webcam stream, process images
via Face Detector service and visualize results.

We suggest that you come up with what functionality you want to implement,
but we also have several examples sorted in increasing order of complexity:

1. Change Face Detector service to Emotion Recognition service and visualize
every face and emotions in the image
2. Using Emotion Recognition service detect all faces and emotions and
change happy faces to smiling emoticons, sad faces to sad emoticons, etc.
3. Process and visualize several services simultaneously,
i.e. Face Detector + Person Detector
4. Create the tool for collecting statistics of emotions,
gender and age for all the people in the camera vision area

You can choose one of the several services that could work
with streaming requests. Note that some services are working slower
than others. Available services are:
* Face Detector (~ 12 frames per second)
* Person Detector (~ 6 frames per second)
* Emotion Recognition (~ 10 frames per second)
* Satisfaction Index (~ 10 frames per second)
* Sex & Age Detector (~ 10 frames per second)
* Body Pose Estimation (~ 5 frames per second)
