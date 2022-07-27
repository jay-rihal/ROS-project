# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 11:18:30 2022

@author: jsrih
"""

import rospy
from std_msgs.msg import String

from flask import Flask, request

pub = rospy.Publisher('chatter', String, queue_size=10)
rospy.init_node('talker', anonymous=True)
rate = rospy.Rate(10) # 10hz
while not rospy.is_shutdown():
    app = Flask(__name__)
    def talker():
        pub = rospy.Publisher('chatter', String, queue_size=10)
        rospy.init_node('talker', anonymous=True)
        rate = rospy.Rate(1) # 10hz
        while not rospy.is_shutdown():
            @app.route('/', methods = ["POST","GET"])
            def webhook():
                if request.method == "GET":
                    return "Not connected"
                elif request.method == "POST":
                    payload = request.json
                    user_response = (payload["queryResult"]["queryText"])
                    bot_response = (payload["queryResult"]["fulfillmentText"])
                    if user_response or bot_response != "":
                        print(f"user response: {user_response}")
                        print(f"Bot response: {bot_response}")
                        rospy.loginfo(user_response)
                        pub.publish(user_response)
                        rate.sleep()
                    return "okay"
                else:
                    print(request.data)
                    return "200"
    
if __name__ == "__main__":
    app.run(debug = False)
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
