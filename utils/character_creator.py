from fillpdf import fillpdfs

def new_char(character_data):

    try:
        filename = f'{character_data["charname"]}'
    except:
        filename = "newchar"

    fillpdfs.write_fillable_pdf(
        "templates/character_sheet.pdf",
        f"temp/{filename}.pdf", 
        character_data,
        flatten=False)
    return f"temp/{filename}.pdf"