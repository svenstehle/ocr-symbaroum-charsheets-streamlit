import pytest


@pytest.fixture()
def prep_ocr_text_draghul():
    text = (
        "Rasse Untoter\n\n"
        "Herausforderung _ Normal\n"
        "Merkmale Untot (I)\n"
        "xysfjkj7\nScharfsinn 4 (-6), blablabla Stärke 3 (-7),\n"
        "trolol\nAufmerksamkeit 10 (0), olo Gewandtheit 15 (+5), --23%\n"
        "Ausstrahlung 5 (+5), Heimlichkeit 10 (0), Präzision 9 (+1),\n"
        "Willenskraft 13 (-3)\n\n"
        "Fähigkeiten Eisenfaust (Adept),\n"
        "Schildkampf (Novize)\n\n"
        "Waffen Rostiges Schwert7\n\n"
        "Rüstung Beschlagene Leder-\n"
        "rüstung 2 (Behinderung)\n\n"
        "Verteidigung O(Schild)\n\n"
        "Zähigkeit 11 _ Schmerzgrenze -\n\n"
        "Ausrüstung 1W10 Orteg\n\n "
        "Schatten Gelbgrau wie abgestor-\n\n"
        "bene Haut mit dunklen\n"
        "Flecken, die sich aus-\n"
        "breiten, wenn der Körper\n"
        "des Untoten zusehends\n"
        "verfällt (durch und durch\n"
        "korrupt)\n\n"
        "Taktik: Der Untote verhält sich gemäß dem\n\n"
        "Willen seines Erschaffers oder nach seinem\n\n"
        "eigenen Willen. Er ist mmer auf der Suche nach\n"
        "warmen Fleisch und frischem Blut."
    )

    yield text
    del text


@pytest.fixture
def prep_ocr_text_baiagorn():
    text = (
        "BAIAGORN\n\n"
        "Rasse Bestie\n\n"
        "Herausforderung Normal\n\n"
        "Merkmale Natürliche Waffen (1),\n"
        "Robust ()\n\n"
        "Aufmerksamkeit 11 (-1), Ausstrahlung 5 (+5),\n"
        "Gewandtheit 7 (+3), Heimlichkeit 9 (+1),\n"
        "Präzision 10 (0), Scharfsinn 10 (0),\n\n"
        "Stärke 15 (-5), Willenskraft 13 (-3)\n\n"
        "Fähigkeiten Berserkerrausch (Adept)\n"
        "Waffen Krallen 8 (Kurz)\n"
        "Rüstung Bärenfell 4\n"
        "Verteidigung +7\n"
        "Zähigkeit 15 Schmerzgrenze 8\n"
        "Ausrüstung Keine\n\n"
        "Schatten Grün wie die Piniennadeln\n\n"
        "des letzten Jahres\n"
        "(Korruption: 0)\n\n"
        "Taktik: Normalerweise sind Baiagornen vor-\n"
        "sichtige Kreaturen, doch wenn sie verletzt oder\n"
        "verärgert werden, verwandeln sie sich brüllende\n"
        "Bestien, die wie wild mit ihren Krallen um sich\n"
        "schlagen und den nächsten Feind oder ihre\n"
        "Beute unerbittlich angreifen."
    )

    yield text
    del text


@pytest.fixture
def prep_ocr_text_guard():
    text = (
        "Karawanenwächter\n"
        "„Ich werde dir schon nicht zu sehr weh tun ...“\n\n"
        "Eine Gruppe von Männern und Frauen (Anzahl\n"
        "der Spielercharaktere +1), die alle schonmehrere\n"
        "Reisen über die Titanen überlebt haben. Es sind\n"
        "Aallesamt abgehärtete Kämpfer, die sich jeder\n"
        "Auseinandersetzung stellen. Im Gegenzug mangelt\n"
        "‚s ihnen ein wenig an Umgangsformen.\n\n"
        "Auftreten Grinst zuversichtlich und\n"
        "schwingt sein Schwert\n"
        "herausfordernd\n\n"
        "Rasse Mensch (Ambrier)\n\n"
        "Herausforderung _ Gering\n\n"
        "Merkmale Kontakte\n"
        "(Karawanerwächter)\n\n"
        "Aufmerksamkeit 11 (-1). Ausstrahlung 9 (+1).\n"
        "‚Gewandtheit 10 (0). Heimlichkeit 5 (+5).\n"
        "Präzision 13 (-3). Scharfsinn7 (+3).\n"
        "Stärke 15 (-5). Willenskraft 10 (0)\n\n"
        "Fähigkeiten Keine\n"
        "Waffen Schwert4\n\n"
        "Rüstung. Schuppenpanzer 3\n"
        "(Behinderung)\n"
        "+2(Schild)\n"
        "Schmerzgrenze 8\n"
        "IWIO Schillinge,\n\n"
        "Schatten Mattes Kupfer\n\n"
        "Taktik: Der Spielercharakter, der am größten\n"
        "\"oder stärksten wirkt, wird zuerst vonzwei Wäch-\n"
        "tern angegriffen. Jeder andere Spielercharakter\n"
        "\'wird von einem Wachter angegriffen."
    )
    yield text
    del text


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
def create_input_extract_all_attributes_from_text_general():
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
def create_expected_result_extract_all_skills_from_text_draghul():
    expected_result = {
        "Eisenfaust": "Adept",
        "Schildkampf": "Novize",
    }
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_all_skills_from_text_baiagorn():
    expected_result = {"Berserkerrausch": "Adept"}
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_all_skills_from_text_guard():
    expected_result = {"Skills found in text": "Zero"}
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
    expected_result = "Normalerweise sind Baiagornen vor- " +\
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
                        "\"oder stärksten wirkt, wird zuerst vonzwei Wäch- " +\
                        "tern angegriffen. Jeder andere Spielercharakter " +\
                        "\'wird von einem Wachter angegriffen."
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
        }, 10)
    ]
    return input_result_pairs


@pytest.fixture(params=create_input_result_pairs_get_toughness())
def prep_get_toughness(request):
    attributes = request.param[0]
    expected_result = request.param[1]
    yield attributes, expected_result
    del attributes, expected_result
