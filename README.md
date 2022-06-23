# OCR for Symbaroum Charactersheets with Streamlit

[![lint](https://github.com/svenstehle/ocr-symbaroum-charsheets-streamlit/actions/workflows/lint.yml/badge.svg)](https://github.com/svenstehle/ocr-symbaroum-charsheets-streamlit/actions/workflows/lint.yml)
[![tests](https://github.com/svenstehle/ocr-symbaroum-charsheets-streamlit/actions/workflows/linting_and_tests.yml/badge.svg)](https://github.com/svenstehle/ocr-symbaroum-charsheets-streamlit/actions/workflows/linting_and_tests.yml)
[![codecov](https://codecov.io/gh/svenstehle/ocr-symbaroum-charsheets-streamlit/branch/main/graph/badge.svg?token=AK24E5TVTI)](https://codecov.io/gh/svenstehle/ocr-symbaroum-charsheets-streamlit)
[![Maintainability](https://api.codeclimate.com/v1/badges/8ecf59f184dc9c87564d/maintainability)](https://codeclimate.com/github/svenstehle/ocr-symbaroum-charsheets-streamlit/maintainability)
[![PythonVersion](https://img.shields.io/badge/python-3.8%20%7C%203.9%20-blue)](https://github.com/svenstehle/ocr-symbaroum-charsheets-streamlit)
[![yapf](https://img.shields.io/badge/code%20style-YAPF-lightgrey)](https://github.com/google/yapf)

This repository allows you to read in symbaroum character sheets with tesseract OCR and provides preformatted commands for use in the roll20 API to create character sheets with, e.g. with the `!setattr` script.

# TODO update with !token-mod info

## Access the App on Streamlit cloud

Visit our site on the [Streamlit Cloud](https://share.streamlit.io/svenstehle/ocr-symbaroum-charsheets-streamlit/main/src/app.py).

Every push on the `main` branch will update the app on the Streamlit Cloud.

**NOTE** OCR works best with high-quality images. Try to screenshot from a high-dpi monitor and ideally use `.tiff` or at least `.png` files. Image compression leads to poor OCR results. **NOTE**

## Quickstart

To run the app locally, you have to do a bit of setup.
First, install the dependencies in the project. See the [Setup](#setup) section for more information.

And then run the streamlit app with

```bash
streamlit run src/app.py
```

and switch to the browser.

## Setup

### Python Environment

We manage the Python environment and dependencies with [poetry](https://python-poetry.org/docs/basic-usage/). Detailed installation instructions can be found [here](https://python-poetry.org/docs/master/#installing-with-the-official-installer). Example of a quick setup:

```bash
# download and install poetry
curl -sSL https://install.python-poetry.org | python3 -
# check if poetry works
poetry --version
```

Make use of the `pyproject.toml` file to install dependencies automatically:

```bash
poetry install
```

### System Packages

#### Basic Language Support

If you want to install for example only the English and German language packages for tesseract on `ubuntu`, you can do so with `sudo apt-get install tesseract-ocr-eng tesseract-ocr-deu`. [Other languages](https://tesseract-ocr.github.io/tessdoc/Data-Files-in-different-versions.html) out of 100+ can be installed in the same manner 1-by-1 or you can just download the whole tessdata repository, see paragraph below.

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
python src/main.py --OCRConfig.image images/charactersheet_screenshot.png
```

The `--lang` parameter of `pytesseract` specifies the input language. In the app, the default is `deu+eng` for German and English during the language detection run. In a subsequent OCR run the detected language from the first run will be used. In the OCR-only part in `main.py`, the default is `eng` for English.

The default option for `--psm` is `4`, which corresponds to `Assume a single column of text of variable sizes.`
You can also specify the OCR engine mode with `--oem`. Default is `1`, which corresponds to `Neural Nets and LSTM engine only`.

The `tessedit_char_whitelist` parameter of `tesseract` specifies the characters to be recognized. In the app, the whitelist characters can be passed to `pytesseract` with the `config` parameter and the syntax used in tesseract itself: `-c tessedit_char_whitelist="ABCDEFGHIJKLMNOPQRSTUVWXYZÄÜÖ   äöüabcdefghijklmnopqrstuvwxyz/|(+)-.,: 0123456789"`

Take care to notice the quotation marks around the whitelist string and the whitespaces inside the string. These are both necessary to tell `pytesseract` to also find whitespaces and output them. Otherwise it will output a string without any whitespaces.

You can read up on possible fine-tuning options on [this page](https://ai-facets.org/tesseract-ocr-best-practices/).

## Contributing

Have fun and raise any issues you see. Feel free to contribute and extend. Also see [CONTRIBUTING.md](https://github.com/svenstehle/ocr-symbaroum-charsheets-streamlit/blob/main/CONTRIBUTING.md).
Already identified possible improvements:

- Improve the documentation
- Improve streamlit tests and test coverage of regression / visual tests
- Extract more info from the OCR results
- Use Regex to deal with some OCR inaccuracies in a better way
- Make more of the extracted information available to the roll20 API in the correct format/way to improve ease of character setup in roll20
- Add and improve GitHub Actions for automatic tests and continuous integration

### Developing

See [Python Environment](#python-environment) for the dependencies setup information.

This project uses `yapf` to format code, `pylint` for linting and `mypy` for type-checking. We also support `pre-commit` to ensure these have been run. To configure your local environment please install these development dependencies and set up the commit hooks.

Coding style checks and pre-commit are setup with [pre-commit](https://pre-commit.com/).

```bash
# download and install poetry
curl -sSL https://install.python-poetry.org | python3 -
poetry --version
```

```bash
# install project dependencies
poetry install
# setup pre-commit hooks
pre-commit install
```

```bash
# tesseract setup on ubuntu
sudo apt-get install tesseract-ocr tesseract-ocr-eng tesseract-ocr-deu
```

### Run the tests

1. Take care to set the `PYTHONPATH` like this

    ```bash
    export PYTHONPATH=./src
    ```

2. Start the streamlit app with

    ```bash
    streamlit run src/app.py
    ```

    By default, streamlit will start in headless mode according to `.streamlit/config.toml` and the `headless = true` value. If you want to change this, change the value to `false` temporarily. The GitHub Actions CI environment needs this on `true`, otherwise the tests will fail.

3. Run tests (including visual tests) from root with this script:

    ```bash
    sh tests/run_tests.sh
    ```

    or run manually:

    ```bash
    pytest tests --settings-file=tests/visual_testing.py --chromium-arg="force-device-scale-factor=1,headless"
    ```

    If you want to see what is happening, remove the `headless` from `--chromium-arg` before running the tests.

#### Visual testing with seleniumbase

To reset the baselines for visual tests run this script:

```bash
sh tests/generate_visual_baseline.sh
```

or run manually:

```bash
pytest tests/integration/app --settings-file=tests/visual_testing.py --chromium-arg="force-device-scale-factor=1,headless" --visual_baseline
```

#### Test Coverage

Get the test coverage by running this script:

```bash
sh tests/run_cov.sh
```

or run manually:

```bash
pytest tests --settings-file=tests/visual_testing.py --chromium-arg="force-device-scale-factor=1,headless" --cov-report term-missing --cov
```

#### Debugging Github Actions

To debug Github Actions, [act](https://github.com/nektos/act) can be a useful tool. Follow the install and usage instructions on its github.

See [this guide](https://mauricius.dev/run-and-debug-github-actions-locally/) for more information on how to use it in practice. Don't expect wonders from it however. Let's hope GitHub will implement remote debugging this year.
