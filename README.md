# NDL API streaming exercise
Exercise using NDL API streaming capabilities


### General description

In this exercise you will learn how to use NDL API tool, how to process
images and videos, and how to create your own real-time
streaming processing using NDL API.


#### Requirements

Python >3.5 is highly recommended, but you can also work
with unsupported python2 versions.


#### Installation

`pip install ndl-api`


#### Key generation

1. Register on [NDL API site](https://api.neurodatalab.dev)
2. Create new key with some permissions. You can create as many keys
as you need with any permissions you want.
3. Download keys to your PC (assume you download it to `KEYS` folder)


#### First try

Assume that you have key with FaceDetector permission and you have video
by `video.mp4` path. To process this video by FaceDetector service
via NDL API package for python >3.5 run

`python3 -m ndlapi.process_video --keys-path KEYS --video-path video.mp4
--service FaceDetector --result-path ndlapi_results`

When video will be successful processed results will appear in
`ndlapi_results` folder

More information about usage and results structure available in
[docs](https://api.neurodatalab.dev/docs)


### Streaming exercise

The main goal of this exercise is to learn how to use NDL API
capabilities to create real-time video processing program. There is an
example in this git which can handle webcam stream, processed images
via Face Detector service and visualize results.

We suggest that you come up what functionality you want to implement,
but we also have several examples sorted in increasing order of complexity:

1. Change Face Detector service to Emotion Recognition service and visualize
every face and emotions on image
2. With Emotion Recognition service detects all faces and emotions and
change happy faces to smiling emoticons, sad faces to sad emoticons etc.
3. Process and visualize several services simultaneously,
i.e. Face Detector + Person Detector
4. Create tool for collecting statistics of emotions,
gender and age for all people near the camera

You can choose one of several services which could work
with streaming requests. Note, that some services are working slower
than others. Available services are:
* Face Detector (~ 12 frames per second)
* Person Detector (~ 6 frames per second)
* Emotion Recognition (~ 10 frames per second)
* Satisfaction Index (~ 10 frames per second)
* Sex & Age Detector (~ 10 frames per second)
* Body pose estimation (~ 5 frames per second)
