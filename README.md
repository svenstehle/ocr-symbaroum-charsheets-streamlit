# OCR for Symbaroum Charactersheets with Streamlit

this repository allows you to read in symbaroum character sheets with tesseract OCR and provides preformatted commands for use in the roll20 API to create any charactersheet (& token?) you read in with the OCR functionality.

## Quickstart

To have an easy start you just need to install the dependencies in the project. See the [Setup](#Setup) section for more information.

And then run the streamlit app with

```bash
streamlit run src/app.py
```

And switch to the browser.

## Setup

First, install dependencies with `python -m pip install .`. This will make use of the `pyproject.toml` file to install the dependencies.

Then, to make use of poetry to manage environments and dependencies, you need to install the [poetry](https://python-poetry.org/docs/basic-usage/) package with `poetry install`.

To enable language support for German language, follow the guide on [this site](https://pyimagesearch.com/2020/08/03/tesseract-ocr-for-non-english-languages/) and clone the [tessdata](https://github.com/tesseract-ocr/tessdata) repository manually into this repository. It is slightly above 4GB total, so make sure you have ample space ;)

Make sure you have set the environment variable `TESSDATA_PREFIX` to the correct cloned tessdata directory like for example:

```bash
export TESSDATA_PREFIX=/Users/<YourName>/<some_directory>/symbaroum-adventures/tessdata
```

or more generally, while in the root of the repository:

```bash
export TESSDATA_PREFIX="$(PWD)/tessdata"
```

## Usage of OCR part only

After successful setup, you can then process your images, e.g. from a symbaroum rulebook, by applying this command to a cut-out section of a charactersheet:

```bash
python src/main.py --OCRConfig.image images/draghul.png
```

The `--lang` parameter of `pytesseract` specifies the input language. The default is `deu` for German. Future versions of this app will support language selection. I appreciate help in adding support for other languages by on-demand loading from tesseract/tessdata repository. The brute-force way to download >4GB of language data on each install is not very elegant or practical.

The default option for `--psm` is `4`, which corresponds to `Assume a single column of text of variable sizes.`
You can also specify the OCR engine mode with `--oem`.

You can read up on possible fine-tuning options on [this page](https://ai-facets.org/tesseract-ocr-best-practices/).

## Contributing

Have fun and raise any issues you see. Feel free to contribute and extend.
Already identified possible improvements:

- Add on-demand OCR language support for pytesseract without having to clone the whole tessdata repository
- make --lang a user-selectable option/input
- Improve OCR detection performance by preprocessing with OpenCV (bounding boxes) or working with bounding boxes provided by pytesseract image_to_data based on confidence in results
