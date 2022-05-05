import pytest
from src.process_text.extract_info import TextProcessor


@pytest.mark.parametrize(
    "text, pattern, expected_result", [
        (
            "fähigkeiten, test, dies ist blablablabla waffen",
            pytest.lazy_fixture("create_german_regex_weapon_matching_pattern"),
            [(41, 47)],
        ),
        (
            "Bla watfen",
            pytest.lazy_fixture("create_german_regex_weapon_matching_pattern"),
            [(4, 10)],
        ),
        (
            "Bla wäfden",
            pytest.lazy_fixture("create_german_regex_weapon_matching_pattern"),
            [(4, 10)],
        ),
        (
            "Blaa wäfen",
            pytest.lazy_fixture("create_german_regex_weapon_matching_pattern"),
            [],
        ),
        (
            "Bleaa wften",
            pytest.lazy_fixture("create_german_regex_weapon_matching_pattern"),
            [],
        ),
        (
            "Bl wfden",
            pytest.lazy_fixture("create_german_regex_weapon_matching_pattern"),
            [],
        ),
        (
            "Bla watfons",
            pytest.lazy_fixture("create_german_regex_weapon_matching_pattern"),
            [],
        ),
        (
            "Bl wfden filler waften",
            pytest.lazy_fixture("create_german_regex_weapon_matching_pattern"),
            [(16, 22)],
        ),
        (
            "Bl wpoeons filler waften",
            pytest.lazy_fixture("create_english_regex_weapon_matching_pattern"),
            [(3, 10)],
        ),
        (
            "Bl weopons filler waften",
            pytest.lazy_fixture("create_english_regex_weapon_matching_pattern"),
            [(3, 10)],
        ),
        (
            "Bl wopaons filler waffen",
            pytest.lazy_fixture("create_english_regex_weapon_matching_pattern"),
            [(3, 10)],
        ),
        (
            "Bla watfons",
            pytest.lazy_fixture("create_english_regex_weapon_matching_pattern"),
            [],
        ),
        (
            "Bla wäfdons",
            pytest.lazy_fixture("create_english_regex_weapon_matching_pattern"),
            [],
        ),
        (
            "Blaa wäfons",
            pytest.lazy_fixture("create_english_regex_weapon_matching_pattern"),
            [],
        ),
        (
            "Bleaa wftons",
            pytest.lazy_fixture("create_english_regex_weapon_matching_pattern"),
            [],
        ),
        (
            "Bleaa willen",
            pytest.lazy_fixture("create_english_regex_weapon_matching_pattern"),
            [],
        ),
        (
            "Bleaa warmen",
            pytest.lazy_fixture("create_english_regex_weapon_matching_pattern"),
            [],
        ),
        (
            "Bleaa warmen",
            pytest.lazy_fixture("create_german_regex_weapon_matching_pattern"),
            [],
        ),
        (
            "Bleaa willen",
            pytest.lazy_fixture("create_german_regex_weapon_matching_pattern"),
            [],
        ),
        (
            "Bl wfdons",
            pytest.lazy_fixture("create_english_regex_weapon_matching_pattern"),
            [],
        ),
        (
            "Bleaa wften",
            pytest.lazy_fixture("create_english_regex_weapon_matching_pattern"),
            [],
        ),
    ]
)
def test_get_indices_of_weapon_strings(text, pattern, expected_result):
    TP = TextProcessor(text)
    all_results = TP.get_indices_of_weapon_strings(pattern)
    assert all_results == expected_result
