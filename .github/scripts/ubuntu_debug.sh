sudo apt update &&
    sudo apt upgrade &&
    sudo apt install -y tesseract-ocr tesseract-ocr-eng tesseract-ocr-deu &&
    mkdir /usr/local/share/tessdata &&
    cd /usr/local/share/tessdata &&
    wget https://github.com/tesseract-ocr/tessdata_best/raw/main/eng.traineddata &&
    wget https://github.com/tesseract-ocr/tessdata_best/raw/main/deu.traineddata &&
    export TESSDATA_PREFIX=/usr/local/share/tessdata &&
    tesseract --list-langs
