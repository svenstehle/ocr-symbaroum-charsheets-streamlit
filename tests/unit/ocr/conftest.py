import pytest


@pytest.fixture()
def prep_text_detection_and_recognition(prep_ocr_image, prep_spock_config):
    image = prep_ocr_image
    ocr_config = prep_spock_config
    yield ocr_config, image
    del ocr_config, image


def create_input_get_attribute_value_from_text():
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


@pytest.fixture()
def create_output_ocr_text():
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


@pytest.fixture(params=create_input_get_attribute_value_from_text())
def prep_get_attribute_value_from_text(request, create_output_ocr_text):
    text = create_output_ocr_text
    target_attribute = request.param[0]
    expected_result = request.param[1]
    yield text, target_attribute, expected_result
    del text, target_attribute, expected_result


@pytest.fixture()
def create_input_extract_all_attributes_from_text():
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


@pytest.fixture()
def create_expected_result_extract_all_attributes_from_text():
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


@pytest.fixture()
def prep_extract_all_attributes_from_text(
    create_output_ocr_text,
    create_input_extract_all_attributes_from_text,
    create_expected_result_extract_all_attributes_from_text,
):
    text = create_output_ocr_text
    attribute_names = create_input_extract_all_attributes_from_text
    expected_result = create_expected_result_extract_all_attributes_from_text
    yield text, attribute_names, expected_result
    del text, attribute_names, expected_result


@pytest.fixture()
def prep_get_roll20_chat_input_str(create_expected_result_extract_all_attributes_from_text):
    charname = "Gandalf"
    attributes = create_expected_result_extract_all_attributes_from_text
    expected_result = "!setattr --name Gandalf --strong|3 --quick|15" +\
                        " --vigilant|10 --resolute|13 --persuasive|5" +\
                        " --cunning|4 --discreet|10 --accurate|9" +\
                        " --toughness|10"

    yield charname, attributes, expected_result
    del charname, attributes, expected_result


@pytest.fixture()
def create_expected_result_extract_all_skills_from_text():
    expected_result = {
        "Eisenfaust": "Adept",
        "Schildkampf": "Novize",
    }
    yield expected_result
    del expected_result


@pytest.fixture
def prep_extract_all_skills_from_text(
    create_output_ocr_text,
    create_expected_result_extract_all_skills_from_text,
):
    text = create_output_ocr_text
    expected_result = create_expected_result_extract_all_skills_from_text
    yield text, expected_result
    del text, expected_result


@pytest.fixture()
def create_expected_result_extract_tactics_from_text():
    expected_result = "Der Untote verhält sich gemäß dem Willen seines " +\
                        "Erschaffers oder nach seinem eigenen Willen. " +\
                        "Er ist mmer auf der Suche nach warmen Fleisch und " +\
                        "frischem Blut."
    yield expected_result
    del expected_result


@pytest.fixture
def prep_extract_tactics_from_text(
    create_output_ocr_text,
    create_expected_result_extract_tactics_from_text,
):
    text = create_output_ocr_text
    expected_result = create_expected_result_extract_tactics_from_text
    yield text, expected_result
    del text, expected_result


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
