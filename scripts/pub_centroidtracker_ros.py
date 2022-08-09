#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import os
from darknet_ros_msgs.msg import BoundingBoxes
from sensor_message_getter import SensorMessageGetter
from centroidtracker import CentroidTracker
from centroidtracker_ros.msg import Ctr, Ctrs

class CentroidtrackerRos(object):
    def __init__(self, object_name, topic_darknet, topic_ct_ros='ct_ros', msg_wait=1.0):
        self.darknet_msg = SensorMessageGetter(topic_darknet, BoundingBoxes, msg_wait)
        self.object_name = object_name
        self.ct = CentroidTracker()
        self.knownID = []
        self.publish = rospy.Publisher(topic_ct_ros, Ctrs, queue_size=10)

    def spin(self):
        msg_darknet = self.darknet_msg.get_msg()
        if msg_darknet is None:
            return
        ctrs = Ctrs()
        ctrs_list = []
        rects = []
        for box in msg_darknet.bounding_boxes:
            if box.Class == self.object_name:
                bbox = [box.xmin, box.ymin, box.xmax, box.ymax]
                rects.append(bbox) 
        objects = self.ct.update(rects)
        for (objectID, centroid) in objects.items():
            ctr = Ctr()
            ctr.key = objectID
            ctr.value = centroid
            ctrs_list.append(ctr)
        ctrs.ctrs = ctrs_list
        self.publish.publish(ctrs)

def main():
    script_name = os.path.basename(__file__)
    node_name = os.path.splitext(script_name)[0]
    rospy.init_node(node_name)
    # param
    object_name = rospy.get_param("~object_name")
    topic_darknet = rospy.get_param("~topic_darknet")

    rate = rospy.Rate(50)
    ct_ros = CentroidtrackerRos(object_name, topic_darknet)

    while not rospy.is_shutdown():
        ct_ros.spin()
        rate.sleep()

if __name__ == '__main__':
    main()