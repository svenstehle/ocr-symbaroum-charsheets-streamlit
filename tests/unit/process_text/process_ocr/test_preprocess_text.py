import pytest
from src.process_text.process_ocr import TextProcessor


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
                "-(master), ritualist (master: only relevant "
                "is dance of death, new ritual),"
                "long-lived, equipment - test"
            ),
        ),
    ]
)
def test_preprocess_text(unprocessed_ocr_text, expected_result):
    TP = TextProcessor(unprocessed_ocr_text)
    TP._preprocess_text()    # pylint: disable=protected-access
    assert TP.text == expected_result
