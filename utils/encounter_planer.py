"""
BATTLE GUIDE
Base Battle Points = 3 x Players in Combat +2 (though I use +Tier here, so +4 at level 8-10)

 Add 2 Points for a Challenging Encounter.

 Subtract 1 for a shorter fight.

 Subtract 2 to increase all damage rolls by +1D4.

 Add 1 Point if you don't use Hordes, Bruisers, Leaders, or Solos.

 Adversaries from a lower Tier cost 1 Point less.

Then spend your Battle Points on the following:

Solo - 5pts

Leader - 3pts

Bruiser - 4pts

Hordes / Standards / Ranged / Skulks - 2pts

Minions (= to number of Players) / Supports - 1pt

Minions and Hordes are very efficient at showing a huge number of adversaries, supports should have gnarly fear moves, and skulks can drop into combat half way through if you need to bolster a pushover fight.

I gain battle points to throw enemies at my group once per Rest, unless they're really hurting and their Short Rest wasn't great, then I might subtract the +Tier part (or drop the +2 if using it flat).

Players in Daggerheart can restore a LOT on a Rest, whether Long or Short, so don't be afraid to keep pelting things at them between Rests.
"""
from dataclasses import dataclass
from typing import List

@dataclass
class adversarie:
    name: str
    tier: int
    cost: int

@dataclass
class encounter:
    partysize: int
    partytier: int
    adversaries: List[adversarie]
    battlepoints: int = field(init=False)

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

