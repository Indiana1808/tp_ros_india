#!/usr/bin/env python
"""import rospy
from geometry_msgs.msg import PoseStamped
import math 
class publisher:
	def __init__(self):
		rospy.init_node('publisher', anonymous = True)
		self.pub = rospy.Publisher('publish_topic',PoseStamped, queue_size=15)
		self.rate = rospy.Rate(20)

	def run(self):
		message=PoseStamped()
		rate=rospy.Rate(15)
		x=0,0
		y=0,0
		vx=-1,0
		vy=-1,0
		message.header.frame_id="map"
		while not rospy.is_shutdown():
			theta = theta+dt
			message.pose.position.x=math.cos(theta)
			message.pose.position.y=math.sin(theta)
			self.pub.publish(message)
			self.rate.sleep()

if __name__ == '__main__':
	try:
	    node=publisher()
	    node.run()
	except rospy.ROSInterruptException:
	    pass """

		 



























"""#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseStamped
import math 
class publisher:
	def __init__(self):
		rospy.init_node('publisher', anonymous = True)
		self.pub = rospy.Publisher('publish_topic',PoseStamped, queue_size=10)
		self.rate = rospy.Rate(20)

	def run(self):
		message=PoseStamped()
		rate=rospy.Rate(20)
		theta=0
		dt=0.1
		message.header.frame_id="map"
		while not rospy.is_shutdown():
			theta = theta+dt
			message.pose.position.x=math.cos(theta)
			message.pose.position.y=math.sin(theta)
			self.pub.publish(message)
			self.rate.sleep()

if __name__ == '__main__':
	try:
	    node=publisher()
	    node.run()
	except rospy.ROSInterruptException:
	    pass """

		 
			 
