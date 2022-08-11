# centroidtracker_ros

**This package provides object tracking by centroidtracker algorithm and YOLOv3**

## Requirement
+ Ubuntu 18.04
+ ROS (Melodic)
+ Python 2.7.x

## Set Up
1. Download `centroidtracker_ros` package.

```shell
$ cd ~/catkin_ws/src/
$ git clone https://github.com/HHorimoto/centroidtracker_ros.git
$ cd ~/catkin_ws
$ catkin_make
```

2. Download `darknet_ros` pakage if you do not have.

Please follow [this](https://github.com/leggedrobotics/darknet_ros) instruction

## How to Use
Launch `centroidtracker_ros.launch`

```shell
$ roslaunch centroidtracker_ros centroidtracker_ros.launch
```

### Parameters

+ ***object_name*** : name of the object to be tracked.
    default : `bottle`

+ ***topic_darknet*** : an array of bounding boxes from yolo.
    default : `/darknet_ros/bounding_boxes`

+ ***max_disappeared*** : store the number of maximum consecutive frames a given　object is allowed to be marked as `disappeared` until we need to deregister the object from tracking. If the FPS is low, you should decrease the value.
    default : `5`

## References
[1] Adrian Rosebrock, Simple object tracking with OpenCV, PyImageSearch, https://pyimagesearch.com/2018/07/23/simple-object-tracking-with-opencv/, accessed on 11 August 2022

[2] Marko Bjelonic, YOLO ROS, https://github.com/leggedrobotics/darknet_ros, 2016--2018