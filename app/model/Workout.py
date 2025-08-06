import time
from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class Workout:
    title: Optional[str]
    start_time: Optional[str]
    end_time: Optional[str]
    description: Optional[str]
    exercise_title: Optional[str]
    superset_id: Optional[str]
    exercise_notes: Optional[str]
    set_index: Optional[str]
    set_type: Optional[str]
    weight_lbs: Optional[str]
    reps: Optional[str]
    distance_miles: Optional[str]
    duration_seconds: Optional[str]
    rpe: Optional[str]
    created = datetime.now()
    updated = datetime.now()
                
def set_title(self, title):
    self.title = title
    self.mark_updated()
    
def set_start_time(self, start_time):
    self.start_time = start_time
    self.mark_updated()
    
def set_end_time(self, end_time):
    self.end_time = end_time
    self.mark_updated()
    
def set_description(self, description):
    self.description = description
    self.mark_updated()
    
def set_exercise_title(self, exercise_title):
    self.exercise_title = exercise_title
    self.mark_updated()
    
def set_superset_id(self, superset_id):
    self.superset_id = superset_id
    self.mark_updated()
    
def set_exercise_notes(self, exercise_notes):
    self.exercise_notes = exercise_notes
    self.mark_updated()
    
def set_set_number(self, set_number):
    self.set_number = set_number
    self.mark_updated()
    
def set_set_type(self, set_type):
    self.set_type = set_type
    self.mark_updated()
    
def set_weight_lbs(self, weight_lbs):
    self.weight_lbs = weight_lbs
    self.mark_updated()
    
def set_reps(self, reps):
    self.reps = reps
    self.mark_updated()
    
def set_distance_miles(self, distance_miles):
    self.distance_miles = distance_miles
    self.mark_updated()
    
def set_duration_seconds(self, duration_seconds):
    self.duration_seconds = duration_seconds
    self.mark_updated()
    
def set_rpe(self, rpe):
    self.rpe = rpe
    self.mark_updated()
    
def mark_updated(self):
    self.updated = time.time()
    