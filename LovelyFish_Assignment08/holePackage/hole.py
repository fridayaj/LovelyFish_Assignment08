# Name: Kyle Hsu
# email: hsukt@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date:   10/31/24
# Course #/Section:   IS 4010 001
# Semester/Year:   Fall 2024
# Brief Description of the assignment:  Collaborate to model something

# Brief Description of what this module does. one of the classes, updates the distance from the hole.
# Citations: w3 schools, stackoverflow
# Anything else that's relevant:
class Hole:
    def __init__(self, par, distance):
        self.par = par
        self.distance = distance
        self.current_distance = distance  # Distance remaining for the player

    def update_distance(self, shot_distance):
        """Reduce the remaining distance by the distance of a shot, down to zero."""
        self.current_distance = max(0, self.current_distance - shot_distance)

    def __str__(self):
        return f"Hole(par={self.par}, distance={self.distance})"

    def __repr__(self):
        return f"Hole(par={self.par}, distance={self.distance})"
