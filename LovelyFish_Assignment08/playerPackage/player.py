# Name: Greyson Barber
# email:  barbergn@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date:   10/31/24
# Course #/Section:   IS 4010-001
# Semester/Year:   Fall 2024
# Brief Description of the assignment:  Collaborate with a team to create a program

# Brief Description of what this module does: Simulates taking the shot 
# Citations: w3 schools, stackoverflow
# Anything else that's relevant: none



class Player:
    def __init__(self, name):
        self.name = name
        self.strokes = 0

    def take_shot(self, hole, shot):
        """Simulate taking a shot by decreasing the distance to the hole."""
        hole.update_distance(shot.distance)
        self.strokes += 1
        print(f"{self.name} took a shot of {shot.distance} meters.")

    def __str__(self):
        return f"Player(name={self.name}, strokes={self.strokes})"

    def __repr__(self):
        return f"Player({self.name})"
