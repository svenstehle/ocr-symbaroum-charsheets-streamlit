# OCR for Symbaroum Charactersheets with Streamlit

this repository allows you to read in symbaroum character sheets with tesseract OCR and provides preformatted commands for use in the roll20 API to create any charactersheet (& token?) you read in with the OCR functionality.

## Access the App on Streamlit cloud

Visit our site on the [Streamlit Cloud](https://share.streamlit.io/svenstehle/ocr-symbaroum-charsheets-streamlit/main/src/app.py).

Every push on the `main` branch will update the app on the Streamlit Cloud.

## Quickstart

To run the app locally, you have to do a bit of setup.
First, install the dependencies in the project. See the [Setup](#Setup) section for more information.

And then run the streamlit app with

```bash
streamlit run src/app.py
```

and switch to the browser.

## Setup

### Python Environment

First, install dependencies with `python -m pip install .`. This will make use of the `pyproject.toml` file to install the dependencies.

Then, to make use of poetry to manage environments and dependencies, you need to install the [poetry](https://python-poetry.org/docs/basic-usage/) package with `poetry install`.

### System Packages

#### Basic Language Support

If you want to install for example only the English and German language packages for tesseract, you can do so with `sudo apt-get install tesseract-ocr-eng tesseract-ocr-deu`. [Other languages](https://tesseract-ocr.github.io/tessdoc/Data-Files-in-different-versions.html) out of 100+ can be installed in the same manner 1-by-1 or you can just download the whole tessdata repository, see paragraph below.

#### Extended Language Support

To enable language support for any language that tesseract supports, follow the guide on [this site](https://pyimagesearch.com/2020/08/03/tesseract-ocr-for-non-english-languages/) and clone the [tessdata](https://github.com/tesseract-ocr/tessdata) repository manually, for example into this cloned repository as a "sub-repository". It is slightly above 4GB total, so make sure you have ample space ;)

Make sure you have set the environment variable `TESSDATA_PREFIX` to the correct cloned tessdata directory like for example:

```bash
export TESSDATA_PREFIX=~/coding/ocr-symbaroum-charsheets-streamlit/tessdata
```

or more generally, while in the root of the repository:

```bash
export TESSDATA_PREFIX=$(PWD)/tessdata
```

## Usage of OCR part only

After successful setup, you can then process your images, e.g. from a symbaroum rulebook, by applying this command to a cut-out section of a charactersheet:

```bash
python src/main.py --OCRConfig.image images/draghul.png
```

The `--lang` parameter of `pytesseract` specifies the input language. In the app, the default is `deu+eng` for German and English during the language detection run. In a subsequent OCR run the detected language from the first run will be used. In the OCR-only part in `main.py`, the default is `eng` for English.

The default option for `--psm` is `4`, which corresponds to `Assume a single column of text of variable sizes.`
You can also specify the OCR engine mode with `--oem`. Default is `1`, which corresponds to `Neural Nets and LSTM engine only`.

The `tessedit_char_whitelist` parameter of `tesseract` specifies the characters to be recognized. In the app, the whitelist characters can be passed to `pytesseract` with the `config` parameter and the syntax used in tesseract itself: `-c tessedit_char_whitelist="ABCDEFGHIJKLMNOPQRSTUVWXYZÄÜÖ   äöüabcdefghijklmnopqrstuvwxyz/|(+)-.,: 0123456789"`

Take care to notice the quotation marks around the whitelist string and the whitespaces inside the string. These are both necessary to tell `pytesseract` to also find whitespaces and output them. Otherwise it will output a string without any whitespaces.

You can read up on possible fine-tuning options on [this page](https://ai-facets.org/tesseract-ocr-best-practices/).

## Run the tests

Take care to set the `PYTHONPATH` like this

```bash
export PYTHONPATH=./src
```

to run tests from root with

```bash
pytest tests
```

I appreciate support in writing streamlit-related-tests for (at least visual?) regression testing. Testing every change by hand is tedious and time consuming.

## Contributing

Have fun and raise any issues you see. Feel free to contribute and extend.
Already identified possible improvements:

- Improve OCR detection performance by preprocessing with OpenCV (bounding boxes) or working with bounding boxes provided by pytesseract image_to_data based on confidence in results
- Extract more info from the OCR results
- Make more of the extracted information available to the roll20 API in the correct format/way to improve ease of character setup in roll20
- Add GitHub Actions for automatic tests and continuous integration

### Setup for Coding Style

Coding style and pre-commit can be setup with [pre-commit](https://pre-commit.com/):

```bash
pre-commit install
```

`pylint`, `yapf` and `mypy` should have been installed together with the dependencies.
