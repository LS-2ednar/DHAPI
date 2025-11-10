from fillpdf import fillpdfs

def new_char(char_class=None, character_data):

    #1 check files for identical naming
    #2 if identical get from source everytime -> otherwise do it yourself using sedja
    #3 Use character creation process to generate the first bases of the character

    form_fields = fillpdfs.get_form_fields("templates/character_sheet.pdf").keys()
    print(form_fields)
    for field in form_fields:
        if "_" in field:
            continue
        print(field)

    pass

    fillpdfs.write_fillable_pdf("character_sheet.pdf","test_char.pdf", character_data)


#Example
"""
form_fields = fillpdfs.get_form_fields("character_sheet.pdf").keys()

for field in form_fields:
    if "_" in field:
        continue
    print(field)


data = {
    'character_name': "TEST",
    'level': 10,
    'heritage': "Fugril",
    'subclass': "Testinator 500",
    'class': "T35T3R"

}

print(form_fields)

fillpdfs.write_fillable_pdf("character_sheet.pdf","test_char.pdf", data)
"""
if __name__ == "__main__":
    new_char()