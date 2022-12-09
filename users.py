class User:

    def __init__(self, username, user_budget, door_preference,  ):
        self.name = username
        self.budget = user_budget
        self.doors = door_preference
        #TODO: create a user csv and append new user as log

        self.suggested_cars = []
