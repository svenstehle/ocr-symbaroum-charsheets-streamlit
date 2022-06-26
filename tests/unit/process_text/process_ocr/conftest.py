import pytest


@pytest.fixture
def create_german_regex_weapon_matching_pattern():
    pattern = r"w[ä-üabdeft]{3}en"
    yield pattern
    del pattern


@pytest.fixture
def create_english_regex_weapon_matching_pattern():
    pattern = r"w[aeop]{3}ons"
    yield pattern
    del pattern


@pytest.fixture
def create_expected_result_extract_string_between_keywords_draghul():
    expected_result = "untot (i, siehe seite 231), robust (il, siehe seite 312)"
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_string_between_keywords_baiagorn():
    expected_result = "natürliche waffen (1), robust (), test1 (nl), test2 (ln), test3 (n)"
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_string_between_keywords_guard():
    expected_result = "kontakte (karawanerwächter)"
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_string_between_keywords_aeber():
    expected_result = "natürlicher panzer (il), natürliche waffen (il), robust (i|l, siehe seite 13)"
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_string_between_keywords_fairy():
    expected_result = "-"
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_string_between_keywords_brand():
    expected_result = "-"
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_string_between_keywords_hunter():
    expected_result = "bloodlust (ill. see p. 54), manifestation (in), spirit form (111)"
    yield expected_result
    del expected_result


@pytest.fixture
def create_expected_result_extract_string_between_keywords_sikander():
    expected_result = "test1 (ii), test2 (nl), test3 (ln), test4 (n), test5 (1il)"
    yield expected_result
    del expected_result
