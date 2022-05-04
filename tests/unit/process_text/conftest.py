import pytest


@pytest.fixture
def create_expected_result_extract_all_attributes_from_text_draghul():
    expected_result = {
        "stärke": "3",
        "scharfsinn": "4",
        "gewandtheit": "15",
        "aufmerksamkeit": "10",
        "ausstrahlung": "5",
        "präzision": "9",
        "willenskraft": "13",
        "heimlichkeit": "10",
    }
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_all_attributes_from_text_baiagorn():
    expected_result = {
        "stärke": "15",
        "scharfsinn": "10",
        "gewandtheit": "7",
        "aufmerksamkeit": "11",
        "ausstrahlung": "5",
        "präzision": "10",
        "willenskraft": "13",
        "heimlichkeit": "9",
    }
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_all_attributes_from_text_guard():
    expected_result = {
        "stärke": "15",
        "scharfsinn": "7",
        "gewandtheit": "10",
        "aufmerksamkeit": "11",
        "ausstrahlung": "9",
        "präzision": "13",
        "willenskraft": "10",
        "heimlichkeit": "5",
    }
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_all_attributes_from_text_aeber():
    expected_result = {
        "stärke": "15",
        "scharfsinn": "10",
        "gewandtheit": "13",
        "aufmerksamkeit": "9",
        "ausstrahlung": "5",
        "präzision": "10",
        "willenskraft": "11",
        "heimlichkeit": "7",
    }
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_all_attributes_from_text_eng_fairy():
    expected_result = {
        "acc": "10",
        "cun": "10",
        "dis": "15",
        "per": "9",
        "qui": "13",
        "res": "7",
        "str": "5",
        "vig": "11",
    }
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_all_attributes_from_text_eng_brand():
    expected_result = {
        "acc": "13",
        "cun": "7",
        "dis": "9",
        "per": "5",
        "qui": "11",
        "res": "10",
        "str": "15",
        "vig": "10",
    }
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_all_attributes_from_text_eng_hunter():
    expected_result = {
        "acc": "5",
        "cun": "10",
        "dis": "10",
        "per": "7",
        "qui": "11",
        "res": "16",
        "str": "9",
        "vig": "18",
    }
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_all_attributes_from_text_eng_sikander():
    expected_result = {
        "acc": "9",
        "cun": "11",
        "dis": "5",
        "per": "10",
        "qui": "13",
        "res": "15",
        "str": "7",
        "vig": "10",
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
        "stärke",
        "scharfsinn",
        "gewandtheit",
        "aufmerksamkeit",
        "ausstrahlung",
        "präzision",
        "willenskraft",
        "heimlichkeit",
    ]
    yield attribute_names
    del attribute_names


@pytest.fixture
def create_input_extract_all_attributes_from_text_eng_general():
    attribute_names = ["acc", "cun", "dis", "per", "qui", "res", "str", "vig"]
    yield attribute_names
    del attribute_names
