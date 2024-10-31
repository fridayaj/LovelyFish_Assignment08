# Name: Henry Gruber
# email:  gruberhw@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date:   10/31/24
# Course #/Section:   IS 4010 001
# Semester/Year:   Fall 2024
# Brief Description of the assignment:  Collaborate to model something

# Brief Description of what this module does. is the main, instantiates objects, invokes dunder
# Citations: w3 schools, stackoverflow
# Anything else that's relevant:

class Shot:
    def __init__(self, distance=100):
        self.distance = distance  # Fixed distance for each shot

    def __str__(self):
        return f"Shot(distance={self.distance})"

    def __repr__(self):
        return f"Shot({self.distance})"
