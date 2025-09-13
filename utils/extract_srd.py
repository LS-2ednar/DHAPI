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
        print(domaincard_page) ### <---- CONTINUE HERE Extract Data from the page and repeat until the page_refernce_count is reached###

        """
        Pseudo Code:
        1. Ignore " " lines
        2. Ignore "Domain" Lines
        3. All CAPs -> DOMAIN CARD NAME
        4. If "Level" in Line -> Level, Domain & Type
        5. Unitl Next all CAPs -> Text for this Domain Card 
        """

        page_count += 1
        domaincard_page = reader.pages[page_count].extract_text()

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
    extract_domain_cards(srd)
    #read_srd_contents(srd)

extract_srd()
