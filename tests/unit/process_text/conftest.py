import pytest


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
def create_expected_result_extract_all_abilities_from_text_draghul():
    expected_result = {
        "Eisenfaust": "Adept",
        "Schildkampf": "Novize",
        "Testskill": "Meister",
    }
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_all_abilities_from_text_sikander():
    expected_result = {"Brimstone Cascade": "master", "Flame Wall": "master"}
    yield expected_result
    del expected_result


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
