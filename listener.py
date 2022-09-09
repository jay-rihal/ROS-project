
from google.cloud import dialogflow
import rospy
from std_msgs.msg import String
#from robin_input import *
#from Google STT.py import recog
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/ubuntu/Downloads/calcium-vector-356712-2d6ff4e0c0bf.json"
global text
global tts_string
flag = True

pub = rospy.Publisher('/speech', String, queue_size = 10)
rospy.init_node('listener', anonymous=True)


def detect_intent_texts(project_id, session_id,text, language_code):
    """Returns the result of detect intent with texts as inputs.
    Using the same `session_id` between requests allows continuation
    of the conversation."""
    global tts_string
    global flag
    while flag:

        #text = input("please input your text: ")
        session_client = dialogflow.SessionsClient()
        
        session = session_client.session_path(project_id, session_id)
        print("Session path: {}\n".format(session))
    
        #for text in texts:
        text_input = dialogflow.TextInput(text=text, language_code=language_code)
    
        query_input = dialogflow.QueryInput(text=text_input)
    
        response = session_client.detect_intent(
            request={"session": session, "query_input": query_input}
        )
        tts_string = response.query_result.fulfillment_text
    
        print("=" * 20)
        print("Query text: {}".format(response.query_result.query_text))
        print(
            "Detected intent: {} (confidence: {})\n".format(
                response.query_result.intent.display_name,
                response.query_result.intent_detection_confidence,
            )
        )
        print("Fulfillment text: {}\n".format(response.query_result.fulfillment_text))
     
        #while not rospy.is_shutdown():
        pub.publish(tts_string)
        break
        #if response.query_result.query_text !=
        


def callback(data):
    text = data.data
    if text == "None":
        callback(data)
    detect_intent_texts("robin-rrul", "12346", text, "en-US")
    #rospy.loginfo(rospy.get_caller_id() + 'I heard %s', response.query_result.fulfillment_text.text)


def listener():
    #rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('chatter', String, callback)
    
    # spin() simply keeps python from exiting until this node is stopped
    #while not rospy.is_shutdown():
    #    pub.publish(tts_string)
    rospy.spin()

if __name__ == '__main__':
    listener()
    
