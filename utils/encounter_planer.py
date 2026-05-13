from dataclasses import dataclass
from typing import List

@dataclass
class Adversarie:
    name: str
    type: str
    tier: int

@dataclass
class Encounter:
    partysize: int
    partytier: int
    adversaries: List[adversarie] = []
    battlepoints: int = field(init=False)
    encounterpoints: int = field(init=False)

    def __post_init__(self):
        self.battlepoints = (3*self.partysize)+2

    def update_battlepoints(self, easier=False, extradmg=False, spicy=False):
        if easier == True and spicy == True:
            raise ValueError("Fight can not be easier and spicier at the same time")
        if easier == True:
            self.battlepoints -= 1
        if extradmg == True:
            self.battlepoints -= 2
        if spicy == True:
            self.battlepoints += 2

    def calculate_encounterpoints(self):
        self.encounterpoints += round(len(self.adversaries)/self.partysize)
        for adversarie in self.adversaries:
            if adversarie.type.lower() == "social" or adversarie.type.lower() == "support":
                self.encounterpoints += 1
            if adversarie.type.lower() == "horde" or adversarie.type.lower() == "ranged" or adversarie.type.lower() == "skulk" or adversarie.type.lower() == "standard":
                self.encounterpoints += 2
            if adversarie.type.lower() == "Leader":
                self.encounterpoints += 3
            if adversarie.type.lower() == "bruiser":
                self.encounterpoints += 4        
            if adversarie.type.lower() == "solo":
                self.encounterpoints += 5 

    def add_adversarie(self, adversarie Adversarie):
        self.adversaries += adversarie

    def encounter_check(self):
        self.calculate_encounterpoints()
        if self.battlepoints = self.encounterpoints:
            return 1
        elif self.battlepoints > self.encounterpoints:
            return -2
        else:
            return 0