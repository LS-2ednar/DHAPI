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
        for page in reader.pages:
            text += page.extract_text() or ""
    
    print(text)

parse_from_url("https://www.daggerheart.com/wp-content/uploads/2025/07/Daggerheart-Homebrew-Kit-v1.0-July-31-2025.pdf")