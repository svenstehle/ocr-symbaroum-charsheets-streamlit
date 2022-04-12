# symbaroum character sheet generation with OCR

this repository allows you to read in symbaroum character sheets with tesseract OCR and provides preformatted commands for use in the roll20 API to create any charactersheet (& token?) you read in with the OCR functionality.

## setup

First, install dependencies with `poetry install` after you have installed [poetry](https://python-poetry.org/docs/basic-usage/).

To enable language support for German language, follow the guide on [this site](https://pyimagesearch.com/2020/08/03/tesseract-ocr-for-non-english-languages/) and clone the [tessdata](https://github.com/tesseract-ocr/tessdata) repository manually into this repository. It is slightly above 4GB total, so make sure you have ample space ;)

Make sure you have set the environment variable `TESSDATA_PREFIX` to the correct  cloned tessdata directory like for example:

```bash
export TESSDATA_PREFIX=/Users/<YourName>/<some_directory>/symbaroum-adventures/tessdata
```

## usage

After successful setup, you can then process your images, e.g. from a symbaroum rulebook, by applying this command to a cut-out section of a charactersheet:

```bash
python src/ocr.py --image images/draghul.png --lang deu
```

The `--lang` parameter of `pytesseract` specifies the input language. If you do not wish for translation, you can choose to leave `--to` blank.

The default option for `--psm` is `4`, which corresponds to `Assume a single column of text of variable sizes.`
You can also specify the OCR engine mode with `--oem`.

You can read up on possible fine-tuning options on [this page](https://ai-facets.org/tesseract-ocr-best-practices/).
