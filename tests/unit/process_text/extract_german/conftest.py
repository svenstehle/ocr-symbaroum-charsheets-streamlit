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
