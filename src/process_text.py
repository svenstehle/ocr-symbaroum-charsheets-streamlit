def get_attribute_value_from_text(text: str, attribute_name: str) -> str:
    attribute_name_len = len(attribute_name)
    att_start_loc = text.find(attribute_name) + attribute_name_len + 1
    att_end_loc = att_start_loc + 2
    att_val = text[att_start_loc:att_end_loc].strip(" ")
    return att_val


def extract_all_attributes_from_text(text: str, attribute_names: str) -> dict:
    return {a: get_attribute_value_from_text(text, a) for a in attribute_names}


def extract_all_skills_from_text(text: str) -> dict:
    skills_str = "Fähigkeiten"
    length = len(skills_str)
    skills_start_loc = text.find(skills_str) + length + 1
    weapon_str = "Waffen"
    skills_end_loc = text.find(weapon_str, skills_start_loc) - 2
    all_skills = text[skills_start_loc:skills_end_loc].strip()
    all_skills = [s.strip() for s in all_skills.split(",")]
    all_skills = {s.split(" ")[0]: s.split(" ")[1][1:-1] for s in all_skills}
    return all_skills


def extract_tactics_from_text(text: str) -> str:
    tactics_str = "Taktik:"
    length = len(tactics_str)
    tactics_start_loc = text.find(tactics_str) + length + 1
    tactics = text[tactics_start_loc:].strip()
    tactics = [t.strip() for t in tactics.split(" ") if t.strip() != ""]
    tactics = " ".join(tactics)
    return tactics


def get_toughness(attributes: dict) -> int:
    strong = int(attributes["Stärke"])
    return max((strong, 10))


def get_roll20_chat_input_str(charname, attributes: dict) -> str:
    basic_string = f"!setattr --name {charname}"
    att_string = f" --strong|{attributes['Stärke']} --quick|{attributes['Gewandtheit']}" +\
                f" --vigilant|{attributes['Aufmerksamkeit']} --resolute|{attributes['Willenskraft']}" +\
                f" --persuasive|{attributes['Ausstrahlung']} --cunning|{attributes['Scharfsinn']}" +\
                f" --discreet|{attributes['Heimlichkeit']} --accurate|{attributes['Präzision']}"

    toughness_string = f" --toughness|{get_toughness(attributes)}"
    return basic_string + att_string + toughness_string
