#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 200)
engine.setProperty('volume', 0.9)
r = sr.Recognizer()
speech = sr.Microphone(device_index=1)


def stt():
    with speech as source:    
         audio = r.adjust_for_ambient_noise(source, duration = 1)    
         audio = r.listen(source)
    try:    
        recog = r.recognize_google(audio, language = 'en-US')    
        print("You said: " + recog)    
        #engine.say("You said: " + recog)    
        engine.runAndWait()
    except sr.UnknownValueError:    
        recog = None   
        engine.runAndWait()
    except sr.RequestError as e:    
        recog = ("Could not request results from Google Speech Recognition service; {0}".format(e))    
        engine.runAndWait()
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    #if recog != None:
    while not rospy.is_shutdown():
        rospy.loginfo(recog)
        pub.publish(recog)
        rate.sleep()
        stt()


def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    reciever()
    while not rospy.is_shutdown():
        hello_str = string
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        stt()
    except rospy.ROSInterruptException:
        pass

