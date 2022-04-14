# Symbaroum character sheet generation with OCR

this repository allows you to read in symbaroum character sheets with tesseract OCR and provides preformatted commands for use in the roll20 API to create any charactersheet (& token?) you read in with the OCR functionality.

## Quickstart

To have an easy start you just need to install the dependencies in the project.

>TODO: add setup.py so we can install everything from poetry

And then run the streamlit app with

```bash
streamlit run ocr.py
```

## Setup

First, install dependencies with `poetry install` after you have installed [poetry](https://python-poetry.org/docs/basic-usage/).

To enable language support for German language, follow the guide on [this site](https://pyimagesearch.com/2020/08/03/tesseract-ocr-for-non-english-languages/) and clone the [tessdata](https://github.com/tesseract-ocr/tessdata) repository manually into this repository. It is slightly above 4GB total, so make sure you have ample space ;)

Make sure you have set the environment variable `TESSDATA_PREFIX` to the correct  cloned tessdata directory like for example:

```bash
export TESSDATA_PREFIX=/Users/<YourName>/<some_directory>/symbaroum-adventures/tessdata
```

## Usage

After successful setup, you can then process your images, e.g. from a symbaroum rulebook, by applying this command to a cut-out section of a charactersheet:

```bash
python -m src.ocr --OCRConfig.image images/draghul.png
```

or

```bash
python -m src --OCRConfig.image images/draghul.png
```

The `--lang` parameter of `pytesseract` specifies the input language. If you do not wish for translation, you can choose to leave `--to` blank.

The default option for `--psm` is `4`, which corresponds to `Assume a single column of text of variable sizes.`
You can also specify the OCR engine mode with `--oem`.

You can read up on possible fine-tuning options on [this page](https://ai-facets.org/tesseract-ocr-best-practices/).

## Contributing

Have fun and raise any issues you see. Feel free to contribute and extend.
