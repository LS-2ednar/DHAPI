import os
from PyPDF2 import PdfReader

def find_srd():
    #locate the SRD file in the root of this project.
    cwd = os.getcwd()
    for item in os.listdir(cwd):
        if os.path.isfile(item) and ".pdf" in item:
            print(f"SRD Document to use: {item}\n")
            return item

def extract_domain_cards(srd):

    domain_cards = {}

    page_reference_count = -1
    reader = PdfReader(srd)
    for page in reader.pages:
        page_reference_count += 1
        if "This section contains additional information and reference sheets/period.tab\nDomain Card reference" in page.extract_text():
            page_count = page_reference_count
            print(f"Number of Pages: {page_reference_count}\n")
        
    
    #Firstpage is different then following pages therefore considered as a special case.
    domaincard_page = reader.pages[page_count].extract_text().split("Domain Card reference\n")[1]
    while page_count < len(reader.pages)-1:

        def tnum_to_number(tnum):
            #replacement numbers 
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
            number = ""
            for tnum in tnum.split("/"):
                if tnum != "":
                    number += str(word_to_num[tnum.replace(".tnum","")])
            return number

        def card_text_refresher(text):

            cleaned_numbers = text.replace("/one.tnum","1").replace("/two.tnum","2").replace("/three.tnum","3").replace("/four.tnum","4").replace("/five.tnum","5").replace("/six.tnum","6").replace("/seven.tnum","7").replace("/eight.tnum","8").replace("/nine.tnum","9").replace("/zero.tnum","0")
            cleaned_punctuations = cleaned_numbers.replace("/comma.tab",",").replace("/period.tab",".").replace("/hyphen.tab","-")
            cleaned_text = cleaned_punctuations.replace("/uni00A0"," ").replace("        ","")
            return cleaned_text

        CARD_TEXT = ""
        for line in domaincard_page.split("\n"):

            """
            #lines to ignore
            if "SRD" in line or "DOMAIN" in line:
                print("IGNORED LINE -> DOMAIN or SRD")
                continue
            """

            #identify domaincard name
            if line.isupper() or "/hyphen.tab" in line:
                print(f"CARDTEXT:\n{card_text_refresher(CARD_TEXT)}")
                print(f"\nDOMAINCARD NAME LINE:{line.capitalize()}")
                CARDNAME = card_text_refresher(line.capitalize())
                CARD_TEXT = ""
                continue

            # identify cardlevel, domain and type
            if "Level /" in line:
                LEVEL = tnum_to_number(line.split(" ")[1])
                DOMAIN = line.split(".tnum")[-1].split(" ")[1]
                TYPE = line.split(".tnum")[-1].split(" ")[2]
                print(f"DOMAINCARD INFORMATION LINE: LEVEL={LEVEL}, DOMAIN={DOMAIN}, TYPE={TYPE}")
                continue

            if "Recall Cost:" in line:
                RECALL = tnum_to_number(line.split("Recall Cost:")[1].strip())
                print(f"Recall Cost={RECALL}")
                continue

            # update cardtext
            CARD_TEXT += line

            # hacky way of writing the contents to the dict -> is updated multiple times
            if DOMAIN not in domain_cards:
                domain_cards[DOMAIN]={}

            domain_cards[DOMAIN][CARDNAME] = [LEVEL, RECALL, TYPE, card_text_refresher(CARD_TEXT)]

        page_count += 1
        domaincard_page = reader.pages[page_count].extract_text()

    
    for domain in domain_cards:
        print(len(domain_cards[domain]))
    print(domain_cards["Arcana"])
    return domain_cards

def read_srd_contents(srd):
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
        #replacement numbers 
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
    extract_domain_cards(srd) # <--- We need to double check for MIDNIGHT-TOUCHED / GRACE-TOUCHED <- Approach... first clean SRD then continue? I do not know
    #extract_acestries(srd) <--- Next to do
    #read_srd_contents(srd)

extract_srd()
