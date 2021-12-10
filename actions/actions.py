# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
from typing import Any, Text, Dict, List

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher



class ActionSearch(Action):

    def name(self) -> Text:
        return "action_search"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        a1 = tracker.get_slot('a1')
        a2 = tracker.get_slot('a2')
        a3 = tracker.get_slot('a3')
        a4 = tracker.get_slot('a4')
        a5 = tracker.get_slot('a5')
        a6 = tracker.get_slot('a6')
        a7 = tracker.get_slot('a7')
        a8 = tracker.get_slot('a8')
        a9 = tracker.get_slot('a9')
        a10 = tracker.get_slot('a10')

        dispatcher.utter_message(text='Here are your search results'+str(a1)+","+str(a2)+"."+str(a3)+","+str(a4))

        return []


from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
