from fillpdf import fillpdfs


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