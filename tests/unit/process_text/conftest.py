import pytest


@pytest.fixture()
def prep_ocr_text_draghul():
    text = """Rasse Untoter

        Herausforderung _ Normal
        Merkmale Untot (I)
        xysfjkj7\nScharfsinn 4 (-6), blablabla Stärke 3 (-7),
        trolol\nAufmerksamkeit 10 (0), olo Gewandtheit 15 (+5), --23%\n
        Ausstrahlung 5 (+5), Heimlichkeit 10 (0), Präzision 9 (+1),
        Willenskraft 13 (-3)

        Fähigkeiten Eisenfaust (Adept),
        Schildkampf (Novize)

        Waffen Rostiges Schwert7

        Rüstung Beschlagene Leder-
        rüstung 2 (Behinderung)

        Verteidigung O(Schild)

        Zähigkeit 11 _ Schmerzgrenze -

        Ausrüstung 1W10 Orteg

        Schatten Gelbgrau wie abgestor-

        bene Haut mit dunklen
        Flecken, die sich aus-
        breiten, wenn der Körper
        des Untoten zusehends
        verfällt (durch und durch
        korrupt)

        Taktik: Der Untote verhält sich gemäß dem

        Willen seines Erschaffers oder nach seinem

        eigenen Willen. Er ist mmer auf der Suche nach
        warmen Fleisch und frischem Blut.
        """

    yield text
    del text


@pytest.fixture
def prep_ocr_text_baiagorn():
    text = """BAIAGORN

        Rasse Bestie

        Herausforderung Normal

        Merkmale Natürliche Waffen (1),
        Robust ()

        Aufmerksamkeit 11 (-1), Ausstrahlung 5 (+5),
        Gewandtheit 7 (+3), Heimlichkeit 9 (+1),
        Präzision 10 (0), Scharfsinn 10 (0),

        Stärke 15 (-5), Willenskraft 13 (-3)

        Fähigkeiten Berserkerrausch (Adept)
        Waffen Krallen 8 (Kurz)
        Rüstung Bärenfell 4
        Verteidigung +7

        Zähigkeit 15 Schmerzgrenze 8
        Ausrüstung Keine

        Schatten Grün wie die Piniennadeln

        des letzten Jahres
        (Korruption: 0)

        Taktik: Normalerweise sind Baiagornen vor-
        sichtige Kreaturen, doch wenn sie verletzt oder
        verärgert werden, verwandeln sie sich brüllende
        Bestien, die wie wild mit ihren Krallen um sich
        schlagen und den nächsten Feind oder ihre
        Beute unerbittlich angreifen.
        """

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
