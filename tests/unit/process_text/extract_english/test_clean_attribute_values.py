import pytest
from src.process_text.extract_english import EnglishExtractor


@pytest.mark.parametrize(
    "attribute_values, expected_result", [
        (
            ",0O, |\"-5(41 |’-3] (+3[‘+5 | -1",
            ["0", "0", "-5", "41", "-3", "+3", "+5", "-1"],
        ),
        (
            ",-3,.[|+43] |/[+1 /+5|-1 |] (, ©] [{(-5 \"0",
            ["-3", "+43", "+1", "+5", "-1", "0", "-5", "0"],
        ),
        (
            "“+5 ,“0[ |©, []43 [”-1 \\-6 (4+1 -8\"",
            ["+5", "0", "0", "43", "-1", "-6", "4+1", "-8"],
        ),
        (
            "+1, -1/ +5 | [0 -3 -5|+3 | O",
            ["+1", "-1", "+5", "0", "-3", "-5", "+3", "0"],
        ),
    ]
)
def test_clean_attribute_values(attribute_values, expected_result):
    EE = EnglishExtractor("dummy_text")
    result = EE.clean_attribute_values(attribute_values)
    assert expected_result == result
