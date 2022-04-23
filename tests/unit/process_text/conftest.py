import pytest


def create_input_result_get_attribute_value_from_text_draghul():
    input_result_pairs = [
        ("Stärke", "3"),
        ("Scharfsinn", "4"),
        ("Gewandtheit", "15"),
        ("Aufmerksamkeit", "10"),
        ("Ausstrahlung", "5"),
        ("Präzision", "9"),
        ("Willenskraft", "13"),
        ("Heimlichkeit", "10"),
    ]
    return input_result_pairs


@pytest.fixture(params=create_input_result_get_attribute_value_from_text_draghul())
def prep_input_result_get_attribute_value_from_text_draghul(request):
    target_attribute = request.param[0]
    expected_result = request.param[1]
    yield target_attribute, expected_result
    del target_attribute, expected_result


def create_input_result_get_attribute_value_from_text_baiagorn():
    input_result_pairs = [
        ("Stärke", "15"),
        ("Scharfsinn", "10"),
        ("Gewandtheit", "7"),
        ("Aufmerksamkeit", "11"),
        ("Ausstrahlung", "5"),
        ("Präzision", "10"),
        ("Willenskraft", "13"),
        ("Heimlichkeit", "9"),
    ]
    return input_result_pairs


@pytest.fixture(params=create_input_result_get_attribute_value_from_text_baiagorn())
def prep_input_result_get_attribute_value_from_text_baiagorn(request):
    target_attribute = request.param[0]
    expected_result = request.param[1]
    yield target_attribute, expected_result
    del target_attribute, expected_result


def create_input_result_get_attribute_value_from_text_guard():
    input_result_pairs = [
        ("Stärke", "15"),
        ("Scharfsinn", "7"),
        ("Gewandtheit", "10"),
        ("Aufmerksamkeit", "11"),
        ("Ausstrahlung", "9"),
        ("Präzision", "13"),
        ("Willenskraft", "10"),
        ("Heimlichkeit", "5"),
    ]
    return input_result_pairs


@pytest.fixture(params=create_input_result_get_attribute_value_from_text_guard())
def prep_input_result_get_attribute_value_from_text_guard(request):
    target_attribute = request.param[0]
    expected_result = request.param[1]
    yield target_attribute, expected_result
    del target_attribute, expected_result


@pytest.fixture
def create_input_extract_all_attributes_from_text_ger_general():
    attribute_names = [
        "Stärke",
        "Scharfsinn",
        "Gewandtheit",
        "Aufmerksamkeit",
        "Ausstrahlung",
        "Präzision",
        "Willenskraft",
        "Heimlichkeit",
    ]
    yield attribute_names
    del attribute_names


@pytest.fixture
def create_input_extract_all_attributes_from_text_eng_general():
    attribute_names = ["ACC", "CUN", "DIS", "PER", "QUI", "RES", "STR", "VIG"]
    yield attribute_names
    del attribute_names


@pytest.fixture
def create_expected_result_extract_all_attributes_from_text_draghul():
    expected_result = {
        "Stärke": "3",
        "Scharfsinn": "4",
        "Gewandtheit": "15",
        "Aufmerksamkeit": "10",
        "Ausstrahlung": "5",
        "Präzision": "9",
        "Willenskraft": "13",
        "Heimlichkeit": "10",
    }
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_all_attributes_from_text_baiagorn():
    expected_result = {
        "Stärke": "15",
        "Scharfsinn": "10",
        "Gewandtheit": "7",
        "Aufmerksamkeit": "11",
        "Ausstrahlung": "5",
        "Präzision": "10",
        "Willenskraft": "13",
        "Heimlichkeit": "9",
    }
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_all_attributes_from_text_guard():
    expected_result = {
        "Stärke": "15",
        "Scharfsinn": "7",
        "Gewandtheit": "10",
        "Aufmerksamkeit": "11",
        "Ausstrahlung": "9",
        "Präzision": "13",
        "Willenskraft": "10",
        "Heimlichkeit": "5",
    }
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_get_all_attribute_values_from_text_eng_fairy():
    expected_result = ["10", "10", "15", "9", "13", "7", "5", "11"]
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_get_all_attribute_values_from_text_eng_brand():
    expected_result = ["13", "7", "9", "5", "11", "10", "15", "10"]
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_get_all_attribute_values_from_text_eng_hunter():
    expected_result = ["5", "10", "10", "7", "11", "16", "9", "18"]
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_get_all_attribute_values_from_text_eng_sikander():
    expected_result = ["9", "11", "5", "10", "13", "15", "7", "10"]
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_all_attributes_from_text_eng_fairy():
    expected_result = {
        "ACC": "10",
        "CUN": "10",
        "DIS": "15",
        "PER": "9",
        "QUI": "13",
        "RES": "7",
        "STR": "5",
        "VIG": "11",
    }
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_all_attributes_from_text_eng_brand():
    expected_result = {
        "ACC": "13",
        "CUN": "7",
        "DIS": "9",
        "PER": "5",
        "QUI": "11",
        "RES": "10",
        "STR": "15",
        "VIG": "10",
    }
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_all_attributes_from_text_eng_hunter():
    expected_result = {
        "ACC": "5",
        "CUN": "10",
        "DIS": "10",
        "PER": "7",
        "QUI": "11",
        "RES": "16",
        "STR": "9",
        "VIG": "18",
    }
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_all_attributes_from_text_eng_sikander():
    expected_result = {
        "ACC": "9",
        "CUN": "11",
        "DIS": "5",
        "PER": "10",
        "QUI": "13",
        "RES": "15",
        "STR": "7",
        "VIG": "10",
    }
    yield expected_result
    del expected_result


@pytest.fixture
def create_input_get_roll20_chat_input_str_draghul(create_expected_result_extract_all_attributes_from_text_draghul):
    yield create_expected_result_extract_all_attributes_from_text_draghul


@pytest.fixture
def create_expected_result_get_roll20_chat_input_str_draghul():
    expected_result = "!setattr --name Gandalf --strong|3 --quick|15" +\
                        " --vigilant|10 --resolute|13 --persuasive|5" +\
                        " --cunning|4 --discreet|10 --accurate|9" +\
                        " --toughness|10"
    yield expected_result
    del expected_result


@pytest.fixture
def create_input_get_roll20_chat_input_str_baiagorn(create_expected_result_extract_all_attributes_from_text_baiagorn):
    yield create_expected_result_extract_all_attributes_from_text_baiagorn


@pytest.fixture
def create_expected_result_get_roll20_chat_input_str_baiagorn():
    expected_result = "!setattr --name Legolas --strong|15 --quick|7" +\
                        " --vigilant|11 --resolute|13 --persuasive|5" +\
                        " --cunning|10 --discreet|9 --accurate|10" +\
                        " --toughness|15"
    yield expected_result
    del expected_result


@pytest.fixture
def create_input_get_roll20_chat_input_str_fairy(create_expected_result_extract_all_attributes_from_text_eng_fairy):
    yield create_expected_result_extract_all_attributes_from_text_eng_fairy


@pytest.fixture
def create_expected_result_get_roll20_chat_input_str_fairy():
    expected_result = "!setattr --name Captain Marvel --strong|5 --quick|13" +\
                        " --vigilant|11 --resolute|7 --persuasive|9" +\
                        " --cunning|10 --discreet|15 --accurate|10" +\
                        " --toughness|10"
    yield expected_result
    del expected_result


@pytest.fixture
def create_input_get_roll20_chat_input_str_brand(create_expected_result_extract_all_attributes_from_text_eng_brand):
    yield create_expected_result_extract_all_attributes_from_text_eng_brand


@pytest.fixture
def create_expected_result_get_roll20_chat_input_str_brand():
    expected_result = "!setattr --name Hulk --strong|15 --quick|11" +\
                        " --vigilant|10 --resolute|10 --persuasive|5" +\
                        " --cunning|7 --discreet|9 --accurate|13" +\
                        " --toughness|15"
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_all_abilities_from_text_draghul():
    expected_result = {
        "Eisenfaust": "Adept",
        "Schildkampf": "Novize",
        "Testskill": "Meister",
    }
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_all_abilities_from_text_baiagorn():
    expected_result = {"Berserkerrausch": "Adept"}
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_all_abilities_from_text_guard():
    expected_result = {"Abilities found in text": "Zero"}
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_all_abilities_from_text_fairy():
    expected_result = {"Abilities found in text": "Zero"}
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_all_abilities_from_text_brand():
    expected_result = {"Bodyguard": "master", "Iron Fist": "master", "Two-handed Force": "adept"}
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_all_abilities_from_text_hunter():
    expected_result = {"Acrobatics": "master", "Marksman": "master", "Sixth Sense": "master", "Steadfast": "master"}
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_all_abilities_from_text_sikander():
    expected_result = {"Brimstone Cascade": "master", "Flame Wall": "master"}
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_tactics_from_text_draghul():
    expected_result = "Der Untote verhält sich gemäß dem Willen seines " +\
                        "Erschaffers oder nach seinem eigenen Willen. " +\
                        "Er ist mmer auf der Suche nach warmen Fleisch und " +\
                        "frischem Blut."
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_tactics_from_text_baiagorn():
    expected_result = "Normalerweise sind Baiagornen vor" +\
                        "sichtige Kreaturen, doch wenn sie verletzt oder " +\
                        "verärgert werden, verwandeln sie sich brüllende " +\
                        "Bestien, die wie wild mit ihren Krallen um sich " +\
                        "schlagen und den nächsten Feind oder ihre " +\
                        "Beute unerbittlich angreifen."

    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_tactics_from_text_guard():
    expected_result = "Der Spielercharakter, der am größten " +\
                        "\"oder stärksten wirkt, wird zuerst vonzwei Wäch" +\
                        "tern angegriffen. Jeder andere Spielercharakter " +\
                        "\'wird von einem Wachter angegriffen."
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_tactics_from_text_fairy():
    expected_result = "Renn and his friends will not attack more " +\
                        "than one or two persons at a time. They wait for " +\
                        "the opportunity to arise before fearlessly assaul" +\
                        "ting the prey."
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_tactics_from_text_brand():
    expected_result = (
        "Brand protects his master by attacking "
        "an enemy in full force. Also, Brand will defend "
        "his master from all attacks and make counte"
        "rattacks against any attacker within range of "
        "melee, damage 8 (see the ability Bodyguard at "
        "master level)."
    )
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_tactics_from_text_hunter():
    expected_result = (
        "The Eternal Hunter moves among the "
        "death dancers, shooting single arrows for en"
        "couragement. When a worthy opponent emerges. "
        "the hunter begins his own, personal hunt. He alter"
        "nates between firing deadly arrows and trying to "
        "charm and drink warm. delightful blood from the "
        "victim, saturated with the sublime taste of despe"
        "ration and fear. As soon as Gylta's herd becomes "
        "occupied with fighting the death dancers he takes "
        "the opportunity to commence his fight against the "
        "forest goddess."
    )
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_tactics_from_text_sikander():
    expected_result = (
        "Sikander raises a Flame Wall around "
        "himself and his flaming servant. Anyone ente"
        "ring through the wall of fire encounters Brand in "
        "melee while Sikander maneuvers so he can cast a "
        "chain of Brimstone Cascades at the enemy. He is "
        "prepared to die for his claim and during the fight "
        "he accuses the attackers of wanting to steal his "
        "precious treasure."
    )
    yield expected_result
    del expected_result


def create_input_result_pairs_get_toughness():
    input_result_pairs = [
        ({
            "Stärke": "15"
        }, 15), ({
            "Stärke": "11"
        }, 11), ({
            "Stärke": "10"
        }, 10), ({
            "Stärke": "9"
        }, 10), ({
            "Stärke": "3"
        }, 10), ({
            "STR": "15"
        }, 15), ({
            "STR": "11"
        }, 11), ({
            "STR": "10"
        }, 10), ({
            "STR": "9"
        }, 10), ({
            "STR": "3"
        }, 10)
    ]
    return input_result_pairs


@pytest.fixture(params=create_input_result_pairs_get_toughness())
def prep_get_toughness(request):
    attributes = request.param[0]
    expected_result = request.param[1]
    yield attributes, expected_result
    del attributes, expected_result


@pytest.fixture
def prep_get_roll20_chat_input_str_not_supported_language(
    prep_ocr_text_unknown_language, create_expected_result_extract_all_attributes_from_text_eng_fairy
):
    charname = "Julie"
    attributes = create_expected_result_extract_all_attributes_from_text_eng_fairy
    text = prep_ocr_text_unknown_language
    yield text, charname, attributes
    del text, charname, attributes
