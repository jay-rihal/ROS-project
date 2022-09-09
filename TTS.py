#Here we put TTS, this is a node that subscribes to the listener node

import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(data.data)
    
    
def TTS():
    rospy.init_node('tts', anonymous = True)
    rospy.Subscriber("TTS", String, callback)
    rospy.spin()
    
if __name__ == '__main__':
    TTS()
