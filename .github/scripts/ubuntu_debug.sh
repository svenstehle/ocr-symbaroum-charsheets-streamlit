export DATA_DIR=/usr/local/share/tessdata

sudo apt update &&
    sudo apt upgrade &&
    sudo apt install -y tesseract-ocr tesseract-ocr-eng tesseract-ocr-deu &&
    sudo mkdir ${DATA_DIR} &&
    cd ${DATA_DIR} &&
    wget https://github.com/tesseract-ocr/tessdata_best/raw/main/eng.traineddata &&
    wget https://github.com/tesseract-ocr/tessdata_best/raw/main/deu.traineddata &&
    export TESSDATA_PREFIX=${DATA_DIR} &&
    tesseract --list-langs

# sudo apt-get install -y libglib2.0-0 libnss3 libgconf-2-4 libfontconfig1 && \
# sudo apt-get install -y libswscale-dev libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libopenjp2-7-dev libavformat-dev libpq-dev && \
# sudo apt-get install -y tesseract-ocr tesseract-ocr-eng tesseract-ocr-deu libtesseract-dev libleptonica-dev ldconfig libsm6 libxext6 python-opencv
