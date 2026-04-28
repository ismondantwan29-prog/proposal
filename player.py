import random
# This is the Player class that represents the player's character in the game. It has attributes for GPA, stress, readiness, peer respect, and whether the player is alive or not. The class also has methods to update stats and check for survival conditions based on the player's attributes. 
class Player:
    def __init__(self, name="Twan"):
        self.name = name
        self.gpa = 4.0
        self.stress = 20
        self.readiness = 50
        self.peer_respect = 10
        self.is_alive = True
        self.has_internship = False
        self.death_reason = ""

    def update_stats(self, gpa_change=0, stress_change=0, readiness_change=0, respect_change=0):
        self.gpa += gpa_change
        self.stress += stress_change
        self.readiness += readiness_change
        self.peer_respect += respect_change
        
        if self.gpa > 4.5: 
            self.gpa = 4.5
            
        self.check_survival()

    def check_survival(self):
        if self.gpa < 3.0:
            self.is_alive = False
            self.death_reason = "Your GPA dropped below 3.0. Scholarship lost. Head exploded!"
        elif self.stress >= 100:
            self.is_alive = False
            self.death_reason = "Stress reached {0}. You couldn't handle it. Head exploded!".format(self.stress)
        elif self.peer_respect < 0:
            self.is_alive = False
            self.death_reason = "Peer respect below 0. You died from loneliness."

    def get_status(self):
        return "\n--- STATUS: GPA: {0:.2f} | Stress: {1} | Readiness: {2} | Respect: {3} ---".format(
            self.gpa, self.stress, self.readiness, self.peer_respect
        )