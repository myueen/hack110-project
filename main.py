"""Hack110 Project: Depending on the respondent's time, social state and energy, suggest an activity!"""
 
__author__: str = "Razmin Bari, YueEn Ma, Katherine Katsoudas"
 
import constants
 
 
class Social:
   """Whether respondent is up for socializing."""
   social_state: int
  
   def __init__(self, social_answer: str):
       """From a str input, assign a number to social_state attribute."""
       social_dict: dict[str, int] = {
           "Alone": constants.ALONE,
           "Surrounded by people, but no interactions with them": constants.SURROUNDED,
           "Small group": constants.SMALL_GROUP,
           "Large group": constants.LARGE_GROUP
       }
       for key in social_dict:
           if social_answer == key:
               self.social_state = social_dict[key]
              
 
class Energy:
   """What energy level does respondent feel now."""
   energy_level: int
 
   def __init__(self, energy: str):
       """"The user give a number of their energy level within a range of 1 to 10."""
       energy_dict: dict[str, int] = {
           "Low_energy": constants.LOW_ENERGY,
           "Moderate_energy": constants.MODERATE_ENERGY,
           "High_energy": constants.HIGH_ENERGY
       }
      
       for item in energy_dict:
           if energy == item:
               self.energy_level = energy_dict[item]
              
      
class Time:
   """How much time the respondent has."""
   time_span: int
  
   def __init__(self, time: str):
       """The amount of time the user have that allow them to complete an actibity."""
       time_dict: dict[str, int] = {
           "0 - 30 min": constants.THIRTY_MIN,
           "30 - 60 min": constants.SIXTY_MIN,
           "60 - 90 min": constants.NINETY_MIN
       }
 
       for key in time_dict:
           if time == key:
               self.time_span = time_dict[key]
 
 
def mask_and_suggest(places: dict[str, list[int]], mask_list: list[int]) -> list[bool]:
   """Returns list[bool]."""
   result: list[bool] = []
   if
  
   return result
 
 
 
energy_q: Energy = Energy(input("How energetic are you feeling for this activity?"))
social_q: Social = Social(input("What is your preferred surroundings in terms of people for this activity?"))
time_q: Time = Time(input("How much time would you like to dedicate to the activity?"))
 
respondent_list: list[bool] = mask(energy_q, social_q, time_q)
place: dict[str, list[int]] = {
   "Dining Hall": {
