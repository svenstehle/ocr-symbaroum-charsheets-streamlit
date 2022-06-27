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
