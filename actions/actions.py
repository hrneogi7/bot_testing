# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.executor import CollectingDispatcher
import webbrowser




class InterviewForm(Action):
    def name(self) -> Text:
        return "interview_form"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        required_slots = ["a1","a2","a3","a4","a5","a6","a7"]

        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                # The slot is not filled yet. Request the user to fill this slot next.
                return [SlotSet("requested_slot", slot_name)]

        # All slots are filled.
        return [SlotSet("requested_slot", None)]

class ActionSubmit(Action):
    def name(self) -> Text:
        return "action_submit"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:


        a1 = tracker.get_slot('a1')
        a2 = tracker.get_slot('a2')
        a3 = tracker.get_slot('a3')
        a4 = tracker.get_slot('a4')
        a5 = tracker.get_slot('a5')
        a6 = tracker.get_slot('a6')
        a7 = tracker.get_slot('a7')

        score=0

        if a1=='DDL(Data Definition Language)':
            score+=1
        if a2=='Conceptual Level':
            score+=1
        if a3=='Database Administrator':
            score+=1
        if a4=='Drop':
            score+=1
        if a5=='Savepoint':
            score+=1
        if a6=='overlay network':
            score+=1
        if a7=='unicast network':
            score+=1


        dispatcher.utter_message(template="utter_details_answer",
                                 q1=tracker.get_slot("a1"),
                                 q2=tracker.get_slot("a2"),
                                 q3=tracker.get_slot("a3"),
                                 q4=tracker.get_slot("a4"),
                                 q5=tracker.get_slot("a5"),
                                 q6=tracker.get_slot("a6"),
                                 q7=tracker.get_slot("a7"),
                                 Score=score)

#from rasa_sdk import Action, Tracker
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
