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
    text = """xysfjkj7\nScharfsinn 4 (-6), blablabla Stärke 3 (-7),
        trolol\nAufmerksamkeit 10 (0), olo Gewandtheit 15 (+5), --23%\n
        Ausstrahlung 5 (+5), Heimlichkeit 10 (0), Präzision 9 (+1),
        Willenskraft 13 (-3)"""
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
def create_input_get_all_attribute_names_values_from_text():
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
def create_expected_result_get_all_attribute_names_values_from_text():
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
def prep_get_all_attribute_names_values_from_text(
    create_output_ocr_text,
    create_input_get_all_attribute_names_values_from_text,
    create_expected_result_get_all_attribute_names_values_from_text,
):
    text = create_output_ocr_text
    attribute_names = create_input_get_all_attribute_names_values_from_text
    expected_result = create_expected_result_get_all_attribute_names_values_from_text
    yield text, attribute_names, expected_result
    del text, attribute_names, expected_result


@pytest.fixture()
def prep_get_roll20_setattr_str(create_expected_result_get_all_attribute_names_values_from_text):
    charname = "Gandalf"
    # TODO refactor this string formatting on both ends
    attributes = create_expected_result_get_all_attribute_names_values_from_text
    expected_result = " ".join(
        (
            "!setattr --name Gandalf --strong|3 --quick|15",
            "--vigilant|10 --resolute|13 --persuasive|5",
            "--cunning|4 --discreet|10 --accurate|9",
        )
    )
    yield charname, attributes, expected_result
    del charname, attributes, expected_result
