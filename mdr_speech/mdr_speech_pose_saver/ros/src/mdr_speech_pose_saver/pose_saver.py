#!/usr/bin/env python
import roslib; roslib.load_manifest('mcr_navigation_tools')
import sys
import rospy
import tf

class PoseSaver():
    def __init__(self, file_name):
        self.file_name = file_name
        tf_received = False
        self.pose_name = "Default"

    def setPoseName(self, pose_name):
        self.pose_name = pose_name

    def isExitRequested(self):
        pass

    def savePose(self):
        tf_received = False
        print "Saving Pose"
        # get transformation between map and base_link
        while(not tf_received):
            tf_listener = tf.TransformListener()

            try:
                tf_listener.waitForTransform('map', '/base_link', rospy.Time.now(), rospy.Duration(1))
                (trans, rot) = tf_listener.lookupTransform('/map', '/base_link', rospy.Time(0));

                (roll, pitch, yaw) = tf.transformations.euler_from_quaternion(rot)

                pose_description = "%s: [%lf, %lf, %lf]\n" % (self.pose_name, trans[0], trans[1], yaw)
                print pose_description
                tf_received = True
            except Exception, e:
                rospy.sleep(1)
                tf_received = False

        #write position into a file
        if tf_received:
            pose_file = open(self.file_name, 'a')
            pose_file.write(pose_description)
            pose_file.close()

        tf_received = False
