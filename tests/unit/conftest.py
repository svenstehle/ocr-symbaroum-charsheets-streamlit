import pytest
from src.process_text import TextProcessor
from tests.unit.input_ocr_texts import (
    ocr_text_baiagorn, ocr_text_brand, ocr_text_draghul, ocr_text_fairy, ocr_text_guard, ocr_text_hunter,
    ocr_text_sikander, ocr_text_unknown_language
)


@pytest.fixture(params=[ocr_text_draghul()])
def prep_ocr_text_draghul(request):
    text = request.param
    TP = TextProcessor(text)
    yield TP.preprocess_text()
    del TP


@pytest.fixture(params=[ocr_text_baiagorn()])
def prep_ocr_text_baiagorn(request):
    text = request.param
    TP = TextProcessor(text)
    yield TP.preprocess_text()
    del TP


@pytest.fixture(params=[ocr_text_guard()])
def prep_ocr_text_guard(request):
    text = request.param
    TP = TextProcessor(text)
    yield TP.preprocess_text()
    del TP


@pytest.fixture(params=[ocr_text_fairy()])
def prep_ocr_text_fairy(request):
    text = request.param
    TP = TextProcessor(text)
    yield TP.preprocess_text()
    del TP


@pytest.fixture(params=[ocr_text_brand()])
def prep_ocr_text_brand(request):
    text = request.param
    TP = TextProcessor(text)
    yield TP.preprocess_text()
    del TP


@pytest.fixture(params=[ocr_text_hunter()])
def prep_ocr_text_hunter(request):
    text = request.param
    TP = TextProcessor(text)
    yield TP.preprocess_text()
    del TP


@pytest.fixture(params=[ocr_text_sikander()])
def prep_ocr_text_sikander(request):
    text = request.param
    TP = TextProcessor(text)
    yield TP.preprocess_text()
    del TP


@pytest.fixture(params=[ocr_text_unknown_language()])
def prep_ocr_text_unknown_language(request):
    text = request.param
    TP = TextProcessor(text)
    yield TP.preprocess_text()
    del TP
