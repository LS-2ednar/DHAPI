from fillpdf import fillpdfs

def new_char(character_data):

    #character_data = {'charname': 'Fudibudi', 'pronouns': '', 'level': '', 'heritage': 'Giant | Loreborne', 'subclass': 'Call Of The Slayer', 'class': 'Warrior', 'domain1': 'Blade', 'domain2': ' Bone', 'agility_cb': None, 'strenght_cb': None, 'finesse_cb': None, 'instinct_cb': None, 'presence_cb': None, 'knowledge_cb': None, 'cb_armor_1': None, 'cb_armor_2': None, 'cb_armor_3': None, 'agility': '100', 'strength': '100', 'finesse': '100', 'instinct': '100', 'presence': '100', 'knowledge': '100', 'evasion': '11', 'armor': None, 'cb_armor_4': None, 'cb_armor_5': None, 'cb_armor_6': None, 'cb_armor_7': None, 'cb_armor_8': None, 'cb_armor_9': None, 'cb_armor_10': None, 'cb_armor_11': None, 'cb_armor_12': None, 'checkbox_134qxsk': None, 'checkbox_135idma': None, 'checkbox_136chxg': None, 'checkbox_137yxtk': None, 'checkbox_138hqgr': None, 'checkbox_139mrvk': None, 'checkbox_140tpwj': None, 'minor_th': None, 'major_th': None, 'pwname': None, 'pwtrra': None, 'pwddt': None, 'pwfeature1': None, 'maxHP': '6', 'hp_1_cb': None, 'hp_2_cb': None, 'hp_3_cb': None, 'hp_4_cb': None, 'hp_5_cb': None, 'hp_6_cb': None, 'hp_7_cb': None, 'hp_8_cb': None, 'hp_9_cb': None, 'hp_10_cb': None, 'hp_11_cb': None, 'hp_12_cb': None, 'pwfeature2': None, 'maxStress': '6', 'stress_1_cb': None, 'stress_2_cb': None, 'stress_3_cb': None, 'stress_4_cb': None, 'stress_5_cb': None, 'stress_6_cb': None, 'stress_7_cb': None, 'stress_8_cb': None, 'stress_9_cb': None, 'stress_10_cb': None, 'stress_11_cb': None, 'stress_12_cb': None, 'swname': None, 'swtrra': None, 'swddt': None, 'hope_1_cb': None, 'hope_2_cb': None, 'hope_3_cb': None, 'hope_4_cb': None, 'hope_5_cb': None, 'hope_6_cb': None, 'swfeature1': None, 'hopefeature': 'No Mercy: \nSpend 3 Hope to gain a +1 bonus to your attack rolls until your next rest.', 'swfeature2': None, 'experience_1': None, 'exp_mod_1': None, 'armorname': None, 'armorthresholds': None, 'armorbasescore': None, 'experience_2': None, 'exp_mod_2': None, 'armorfeature1': None, 'experience_3': None, 'exp_mod_3': None, 'experience_4': None, 'exp_mod_4': None, 'armorfeature2': None, 'experience_5': None, 'exp_mod_5': None, 'inventory1': None, 'checkbox_115mojr': None, 'checkbox_116culy': None, 'checkbox_117bgni': None, 'checkbox_118btia': None, 'checkbox_119qqlc': None, 'checkbox_120qbs': None, 'checkbox_121fjlr': None, 'checkbox_122iqws': None, 'checkbox_123wbqn': None, 'checkbox_124gbxs': None, 'checkbox_125kree': None, 'checkbox_126elyr': None, 'checkbox_127kmqg': None, 'checkbox_128bpny': None, 'checkbox_129fyio': None, 'checkbox_130ozcn': None, 'checkbox_131poot': None, 'checkbox_132spwc': None, 'checkbox_133lfoy': None, 'inventory2': None, 'inventory3': None, 'inventory4': None, 'inventory5': None, 'checkbox_141ijwb': None, 'checkbox_142rhps': None, 'checkbox_145yrsm': None, 'checkbox_146ckx': None, 'text_104anhi': None, 'text_105ulk': None, 'text_106pnol': None, 'text_107ejpz': None, 'text_108cjeh': None, 'checkbox_143tvgm': None, 'checkbox_144vlmj': None, 'checkbox_147keyp': None, 'checkbox_148awkh': None, 'text_109fepd': None, 'text_110ytuu': None, 'text_111izga': None, 'text_112naav': None, 'text_113apmb': None, 'classfeatures': 'Attack of Opportunity: \nIf an adversary within Melee range attempts to leave that range, make a reaction roll using a trait of your choice against their Difficulty. Choose one effect on a success, or two if you critically succeed:\n- They can’t move from where they are.\n- You deal damage to them equal to your primary weapon’s damage.\n- You move with them.\n\nCombat Training: \nYou ignore burden when equipping weapons. When you deal physical damage, you gain a bonus to your damage roll equal to your level.', 'questions': 'Answer any of the following background questions. You can also create your own questions.\n\n- Who taught you to fight, and why did they stay behind when you left home?\n- Somebody defeated you in battle years ago and left you to die. Who was it, and how did they betray you?\n- What legendary place have you always wanted to visit, and why is it so special?', 'connections': 'Ask your fellow players one of the following questions for their character to answer, or create your own questions.\n\n- We knew each other long before this party came together. How?\n- What mundane task do you usually help me with off the battlefield?\n- What fear am I helping you overcome?', 'checkbox_147jlzl': None, 'checkbox_148rfvs': None, 'checkbox_149yepy': None, 'checkbox_157ewr': None, 'checkbox_158teiu': None, 'checkbox_159szrk': None, 'checkbox_172xrrd': None, 'checkbox_173ftcs': None, 'checkbox_174vdve': None, 'checkbox_150tmab': None, 'checkbox_151lndy': None, 'checkbox_160anjf': None, 'checkbox_161mxmj': None, 'checkbox_175fws': None, 'checkbox_176cqej': None, 'checkbox_152rtnl': None, 'checkbox_153hfmz': None, 'checkbox_162qeit': None, 'checkbox_163qpkf': None, 'checkbox_177rvqt': None, 'checkbox_178jgsc': None, 'checkbox_154jqo': None, 'checkbox_164amjp': None, 'checkbox_179hrbr': None, 'checkbox_155ldey': None, 'checkbox_165uavx': None, 'checkbox_180zfsr': None, 'checkbox_156uwop': None, 'checkbox_166xq': None, 'checkbox_181nxws': None, 'checkbox_167fbum': None, 'checkbox_182nrjn': None, 'checkbox_168esos': None, 'checkbox_169awvb': None, 'checkbox_183rlfs': None, 'checkbox_184rhcs': None, 'checkbox_170udmg': None, 'checkbox_171vaii': None, 'checkbox_185wena': None, 'checkbox_186it': None}

    #1 check files for identical naming
    #2 if identical get from source everytime -> otherwise do it yourself using sedja
    #3 Use character creation process to generate the first bases of the character

    try:
        filename = f'{character_data["charname"]}'
    except:
        filename = "newchar"

    fillpdfs.write_fillable_pdf(
        "templates/character_sheet.pdf",
        f"temp/{filename}.pdf", 
        character_data,
        flatten=False)

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