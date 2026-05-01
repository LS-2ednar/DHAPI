import requests
import tempfile
from pypdf import PdfReader

def parse_from_url(URL):
    response = requests.get(URL, timeout=15)
    response.raise_for_status()

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(response.content)
        temp_path = tmp_file.name
    
    with open(temp_path, "rb") as file:
        reader = PdfReader(file)
        text = ""
        counter = 0
        for page in reader.pages:
            text += page.extract_text()
 
    return text


Testing = ["https://www.daggerheart.com/wp-content/uploads/2025/07/Daggerheart-Homebrew-Kit-v1.0-July-31-2025.pdf",
"https://www.daggerheart.com/wp-content/uploads/2025/09/Adversaries-Environments-v1.5-.pdf",
"https://www.daggerheart.com/wp-content/uploads/2025/07/Assassin-v1.5-The-Void.pdf",
"https://www.daggerheart.com/wp-content/uploads/2025/09/Daggerheart-SRD-9-09-25.pdf"]

for test in Testing:

    text = parse_from_url(test)
    count = 0
    Capswords = []
    for word in text.split(" "):
        
        if word.isupper() == True:
            Capswords.append(word)
            count += 1
        
    if count > 0:
        print(Capswords)
        print("\n\n")
