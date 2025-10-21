import pandas as pd
import os
from utils.extract_DaggerHeart_Database_sheets import extract_adversaries

def create_adversery_cards():

    if not os.path.exists("adversaries.tar"):
        df = extract_adversaries()
        df.to_pickle("adversaries.tar")
        df = pd.read_pickle("adversaries.tar")

    else:
        df = pd.read_pickle("adversaries.tar")

    print(df.keys())

    for _ , line in df.iterrows():
        if line["Type"] == "Horde":
            print("Hord Monster")

        else:
            print(standard_template(line))
            print()

def standard_template(line):
    return f'''---
tags:
  - dh
  - adversary
type: {line["Type"]}
tier: {line["Tier"].replace("Tier","")}
cover: https://www.freepik.com/premium-vector/silhouette-monster-with-scary-face-horns_324187044.htm
---

## {line["Adversary"]}
{line["Tier"]} {line["Type"]}

![](https://www.freepik.com/premium-vector/silhouette-monster-with-scary-face-horns_324187044.htm)

'''

def hord_template():
    pass

create_adversery_cards()

"""
Index(['Adversary', 'Tier', 'Type', 'Horde HP', 'Description',
       'Motives & Tactics', 'Difficulty', 'Thresholds', 'HP', 'Stress',
       'Attack', 'Weapon', 'Range', 'Experience', 'Features', 'Damage Dice',
       'Damage Type']

"""