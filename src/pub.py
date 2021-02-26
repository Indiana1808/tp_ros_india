#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseStamped
import math
import turtle
class publisher:
	def __init__(self):
		rospy.init_node('publisher', anonymous = True)
		self.pub = rospy.Publisher('publish_topic',PoseStamped, queue_size=10)
		self.rate = rospy.Rate(20)

	def run(self):
		message=PoseStamped()
		rate=rospy.Rate(20)
		tur= turtle.Turtle()
		message.header.frame_id="map"
		while not rospy.is_shutdown():
			for i in range(4): 
				tur.forward(100) 
				tur.left(90) 
			
			
			"""message.pose.position.x=tur.forward(100) 
			message.pose.position.y=tur.left(90)
			message.pose.position.z=tur.forward(100)
			message.pose.position.e=tur.left(90)
			message.pose.position.a=tur.forward(100)
			message.pose.position.c=tur.left(90)
			message.pose.position.f=tur.forward(100)
			message.pose.position.e=tur.left(90)"""
			
			self.pub.publish(message)
			self.rate.sleep()

if __name__ == '__main__':
	try:
	    node=publisher()
	    node.run()
	except rospy.ROSInterruptException:
	    pass 

		 
			 
