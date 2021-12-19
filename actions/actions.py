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
        required_slots = ["a1","a2","a3","a4","a5","a6","a7","a8","a9","a10","a11","a11","a12","a13","a14","a15","a16","a17","a18","a19","a20"]

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
        a8 = tracker.get_slot('a8')
        a9 = tracker.get_slot('a9')
        a10 = tracker.get_slot('a10')
        a11 = tracker.get_slot('a11')
        a12 = tracker.get_slot('a12')
        a13 = tracker.get_slot('a13')
        a14 = tracker.get_slot('a14')
        a15 = tracker.get_slot('a15')
        a16 = tracker.get_slot('a16')
        a17 = tracker.get_slot('a17')
        a18 = tracker.get_slot('a18')
        a19 = tracker.get_slot('a19')
        a20 = tracker.get_slot('a20')

        score=0

        if a1=='DDL(Data Definition Language)':
            score=score+1
        if a2=='Physical level':
            score=score+1
        if a3=='Database Administrator':
            score=score+1
        if a4=='Drop':
            score=score+1
        if a5=='Rollback':
            score=score+1
        if a6=='overlay network':
            score=score+1
        if a7=='broadcast network':
            score=score+1
        if a8=='circuit switching':
            score=score+1
        if a9=='personal area network':
            score=score+1
        if a10=='36.8':
            score=score+1
        if a11=='underflow':
            score=score+1
        if a12=='-18':
            score=score+1
        if a13=='Transaction Control Language':
            score=score+1
        if a14=='Foreign key':
            score=score+1
        if a15=='Gateway':
            score=score+1
        if a16=='8':
            score=score+1
        if a17=='shell':
            score=score+1
        if a18=='to prevent deadlock':
            score=score+1
        if a19=='ms-dos':
            score=score+1
        if a20=='all of these':
            score=score+1


        dispatcher.utter_message(template="utter_details_answer",
                                 q1=tracker.get_slot("a1"),
                                 q2=tracker.get_slot("a2"),
                                 q3=tracker.get_slot("a3"),
                                 q4=tracker.get_slot("a4"),
                                 q5=tracker.get_slot("a5"),
                                 q6=tracker.get_slot("a6"),
                                 q7=tracker.get_slot("a7"),
                                 q8=tracker.get_slot("a8"),
                                 q9=tracker.get_slot("a9"),
                                 q10=tracker.get_slot("a10"),
                                 q11=tracker.get_slot("a11"),
                                 q12=tracker.get_slot("a12"),
                                 q13=tracker.get_slot("a13"),
                                 q14=tracker.get_slot("a14"),
                                 q15=tracker.get_slot("a15"),
                                 q16=tracker.get_slot("a16"),
                                 q17=tracker.get_slot("a17"),
                                 q18=tracker.get_slot("a18"),
                                 q19=tracker.get_slot("a19"),
                                 q20=tracker.get_slot("a20"),
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
