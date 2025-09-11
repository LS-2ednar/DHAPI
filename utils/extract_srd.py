import os
from PyPDF2 import PdfReader

def find_srd():
    #locate the SRD file in the root of this project.
    cwd = os.getcwd()
    for item in os.listdir(cwd):
        if os.path.isfile(item) and ".pdf" in item:
            print(f"SRD Document to use: {item}")
            return item
    
def read_srd(srd):
    # extract the contents of the SRD
    reader = PdfReader(srd)
    for page in reader.pages:
        if "CONTENTS" in page.extract_text().upper():
            break

    Content_raw = page.extract_text().split("Welcome to DAGGERHEART")[0]

    for line in Content_raw.split("\n"):
        if ".tnum" in line:
            #print(" ".join(line.replace(".","").split()))
            tnum_to_int(" ".join(line.replace(".","").split()))


def tnum_to_int(tnum):
    #replace all wrong 
    word_to_num = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    }

    parts = tnum.split("/")
    section = parts[0]
    numbers = parts[1:]
    str_numbers = ""
    for number in numbers:
        if not "tnum" in number:
            section += number
            continue
        str_numbers+=str((word_to_num[number.replace("tnumINTRODUCTION","").replace("tnum","")]))

    print(section, str_numbers)

def extract_srd():
    srd = find_srd()
    read_srd(srd)

extract_srd()
