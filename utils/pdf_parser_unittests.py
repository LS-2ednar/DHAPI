import unittest
from pdf_parser import parse_from_url

class Testpdf_parser(unittest.TestCase):
    
    def test_parse_from_url(self):
        self.assertEqual(parse_from_url("https://www.eks-intec.com/wp-content/uploads/2025/01/Sample-pdf.pdf").split("\n")[0] == "Sample PDF Document" ,True)

if __name__ == "__main__":
    unittest.main()