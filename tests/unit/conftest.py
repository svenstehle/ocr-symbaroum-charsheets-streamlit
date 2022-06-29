import pytest
from src.process_text.extract_info import InformationExtractor
from tests.unit.input_ocr_texts import (
    ocr_text_aeber, ocr_text_baiagorn, ocr_text_brand, ocr_text_draghul, ocr_text_fairy, ocr_text_guard,
    ocr_text_hunter, ocr_text_mixed_language, ocr_text_sikander, ocr_text_unknown_language
)

# pylint: disable=protected-access


@pytest.fixture(params=[ocr_text_draghul()])
def prep_ocr_text_draghul(request):
    text = request.param
    IE = InformationExtractor(text)
    IE._preprocess_text()
    yield IE.text
    del IE


@pytest.fixture(params=[ocr_text_baiagorn()])
def prep_ocr_text_baiagorn(request):
    text = request.param
    IE = InformationExtractor(text)
    IE._preprocess_text()
    yield IE.text
    del IE


@pytest.fixture(params=[ocr_text_guard()])
def prep_ocr_text_guard(request):
    text = request.param
    IE = InformationExtractor(text)
    IE._preprocess_text()
    yield IE.text
    del IE


@pytest.fixture(params=[ocr_text_fairy()])
def prep_ocr_text_fairy(request):
    text = request.param
    IE = InformationExtractor(text)
    IE._preprocess_text()
    yield IE.text
    del IE


@pytest.fixture(params=[ocr_text_brand()])
def prep_ocr_text_brand(request):
    text = request.param
    IE = InformationExtractor(text)
    IE._preprocess_text()
    yield IE.text
    del IE


@pytest.fixture(params=[ocr_text_hunter()])
def prep_ocr_text_hunter(request):
    text = request.param
    IE = InformationExtractor(text)
    IE._preprocess_text()
    yield IE.text
    del IE


@pytest.fixture(params=[ocr_text_sikander()])
def prep_ocr_text_sikander(request):
    text = request.param
    IE = InformationExtractor(text)
    IE._preprocess_text()
    yield IE.text
    del IE


@pytest.fixture(params=[ocr_text_unknown_language()])
def prep_ocr_text_unknown_language(request):
    text = request.param
    IE = InformationExtractor(text)
    IE._preprocess_text()
    yield IE.text
    del IE


@pytest.fixture(params=[ocr_text_aeber()])
def prep_ocr_text_aeber(request):
    text = request.param
    IE = InformationExtractor(text)
    IE._preprocess_text()
    yield IE.text
    del IE


@pytest.fixture(params=[ocr_text_mixed_language()])
def prep_ocr_text_mixed_language(request):
    text = request.param
    IE = InformationExtractor(text)
    IE._preprocess_text()
    yield IE.text
    del IE


@pytest.fixture(params=[ocr_text_draghul()])
def prep_ocr_text_draghul_raw(request):
    text = request.param
    yield text
    del text


@pytest.fixture(params=[ocr_text_baiagorn()])
def prep_ocr_text_baiagorn_raw(request):
    text = request.param
    yield text
    del text


@pytest.fixture(params=[ocr_text_guard()])
def prep_ocr_text_guard_raw(request):
    text = request.param
    yield text
    del text


@pytest.fixture(params=[ocr_text_fairy()])
def prep_ocr_text_fairy_raw(request):
    text = request.param
    yield text
    del text


@pytest.fixture(params=[ocr_text_brand()])
def prep_ocr_text_brand_raw(request):
    text = request.param
    yield text
    del text


@pytest.fixture(params=[ocr_text_hunter()])
def prep_ocr_text_hunter_raw(request):
    text = request.param
    yield text
    del text


@pytest.fixture(params=[ocr_text_sikander()])
def prep_ocr_text_sikander_raw(request):
    text = request.param
    yield text
    del text


@pytest.fixture(params=[ocr_text_unknown_language()])
def prep_ocr_text_unknown_language_raw(request):
    text = request.param
    yield text
    del text


@pytest.fixture(params=[ocr_text_aeber()])
def prep_ocr_text_aeber_raw(request):
    text = request.param
    yield text
    del text


@pytest.fixture(params=[ocr_text_mixed_language()])
def prep_ocr_text_mixed_language_raw(request):
    text = request.param
    yield text
    del text
