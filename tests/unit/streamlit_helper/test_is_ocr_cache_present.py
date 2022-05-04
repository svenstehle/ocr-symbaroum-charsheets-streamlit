from src.streamlit_helper import is_ocr_cache_present


def test_is_ocr_cache_present_false():
    assert not is_ocr_cache_present("test_key")
