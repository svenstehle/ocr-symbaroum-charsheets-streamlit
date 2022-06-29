import pytest
from src.process_text.process_ocr import TextProcessor


@pytest.mark.parametrize(
    "equipment, expected_result", [
        (
            "keine",
            "keine",
        ),
        (
            "Ausrüstung 1wi10 Schillinge",
            "Ausrüstung 1w10 Schillinge",
        ),
        (
            "none",
            "none",
        ),
        (
            "order cloak, 1di0 thaler",
            "order cloak, 1d10 thaler",
        ),
    ]
)
def test_cleanup_dice_rolls(equipment, expected_result):
    # pylint: disable=protected-access
    TP = TextProcessor("dummy_text")
    result = TP._cleanup_dice_rolls(equipment)
    assert expected_result == result
