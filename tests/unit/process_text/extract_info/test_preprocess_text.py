import pytest
from src.process_text.extract_info import InformationExtractor


@pytest.mark.parametrize(
    "unprocessed_ocr_text, expected_result", [
        (
            "test-\nstuff\nstuff2 more -\n\nstuff _ stufstuf\n\nand\n\n_more-\nstuff (=4)",
            "teststuff stuff2 more - stuff - stufstuf and _morestuff (-4)"
        ),
        (
            (
                "=(master), Ritua-\n\nlist (master: only re-\n"
                "levant is Dance of Death, new ritual),=\n"
                "Long-lived,\n\nEquipment = test"
            ),
            (
                "-(master), Ritualist (master: only relevant "
                "is Dance of Death, new ritual),"
                "Long-lived, Equipment - test"
            ),
        ),
    ]
)
def test_preprocess_text(unprocessed_ocr_text, expected_result):
    IE = InformationExtractor(unprocessed_ocr_text)
    IE.preprocess_text()
    assert IE.text == expected_result