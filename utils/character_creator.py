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

def character_data(argument_pairs, df_classes, df_subclasses):

    data = {
        'charname':'',
        'heritage':'',
        'class':'',
        'subclass':'',
        'agility':'', 
        'strength':'',  
        'finesse':'', 
        'instinct':'', 
        'presence':'', 
        'knowledge':'', 
        'evasion':'',
        'maxHP':'',
        'maxStress':'6',
        'hopefeature':'',
        'classfeatures':'',
        'questions':'',
        'connections':'',
        'domain1':'',
        'domain2':'',
        'level':'1'
    }

    heritage_l = ['','']
    features = ['','','','']

    for argument in argument_pairs:

        if "name" in argument:
            data["charname"] = argument.split("=")[1].strip().title()

        if "ancestry" in argument:
            heritage_l[0] = argument.split("=")[1].strip().title()

        if "community" in argument:
            heritage_l[1] = argument.split("=")[1].strip().title()

        if "class" in argument and "subclass" not in argument:
            mask = df_classes["Class"] == argument.split("=")[1].strip().title()
            df_card = df_classes.loc[mask]
            idx = df_card.index[0]

            data["class"] = argument.split("=")[1].strip().title()
            data["evasion"] = str(df_card["Starting Evasion"][idx])
            data["maxHP"] = str(df_card["Starting HP"][idx])
            data["hopefeature"] = df_card["Hope Feature"][idx] 
            features[0] = df_card["Class Features"][idx]
            data["questions"] = df_card["Questions"][idx]
            data["connections"] = df_card["Connections"][idx]
            data["domain1"] = df_card["Domain_1"][idx]
            data["domain2"] = df_card["Domain_2"][idx]

            """
            Check the recommended values for agility, strength, finesse, instinct, presence, knowledge 
            This section might be updated in the future to ensure it works more efficient.
            """
            if argument.split("=")[1].strip().title() == "Bard":
                data["agility"] = "0"
                data["strength"] = "-1"
                data["finesse"] = "+1"
                data["instinct"] = "0"
                data["presence"] = "+2"
                data["knowledge"] = "+1"

            if argument.split("=")[1].strip().title() == "Druid":
                data["agility"] = "+1"
                data["strength"] = "0"
                data["finesse"] = "+1"
                data["instinct"] = "+2"
                data["presence"] = "-1"
                data["knowledge"] = "0"

            if argument.split("=")[1].strip().title() == "Guardian":
                data["agility"] = "+1"
                data["strength"] = "+2"
                data["finesse"] = "-1"
                data["instinct"] = "0"
                data["presence"] = "+1"
                data["knowledge"] = "0"

            if argument.split("=")[1].strip().title() == "Ranger":
                data["agility"] = "+2"
                data["strength"] = "0"
                data["finesse"] = "+1"
                data["instinct"] = "+1"
                data["presence"] = "-1"
                data["knowledge"] = "0"

            if argument.split("=")[1].strip().title() == "Rogue":
                data["agility"] = "+1"
                data["strength"] = "-1"
                data["finesse"] = "+2"
                data["instinct"] = "0"
                data["presence"] = "+1"
                data["knowledge"] = "0"

            if argument.split("=")[1].strip().title() == "Seraph":
                data["agility"] = "0"
                data["strength"] = "+2"
                data["finesse"] = "0"
                data["instinct"] = "+1"
                data["presence"] = "+1"
                data["knowledge"] = "-1"

            if argument.split("=")[1].strip().title() == "Sorcerer":
                data["agility"] = "0"
                data["strength"] = "-1"
                data["finesse"] = "+1"
                data["instinct"] = "+2"
                data["presence"] = "+1"
                data["knowledge"] = "0"

            if argument.split("=")[1].strip().title() == "Warrior":
                data["agility"] = "+2"
                data["strength"] = "+1"
                data["finesse"] = "0"
                data["instinct"] = "+1"
                data["presence"] = "-1"
                data["knowledge"] = "0"

            if argument.split("=")[1].strip().title() == "Wizard":
                data["agility"] = "-1"
                data["strength"] = "0"
                data["finesse"] = "0"
                data["instinct"] = "+1"
                data["presence"] = "+1"
                data["knowledge"] = "+2"
            
        if "subclass" in argument:
            mask = df_subclasses["Subclass"] == argument.split("=")[1].strip().title()
            df_card = df_subclasses.loc[mask]
            idx = df_card.index[0]

            data["subclass"] = argument.split("=")[1].strip().title()
            features[1] = f'{df_card["Foundation Features"][idx]}'
            if int(data["level"]) >= 5:
                features[2] = f'{df_card["Specialization Features"][idx]}'
            if int(data["level"]) >= 8:
                features[2] = f'{df_card["Mastery Features"][idx]}'

        if "level" in argument:
            data["level"] = argument.split("=")[1].strip().title()
    data["classfeatures"] = "\n".join(features)
    data["heritage"] = f'{heritage_l[0]} | {heritage_l[1]}'
    return data