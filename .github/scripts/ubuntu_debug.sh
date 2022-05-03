export TESSDATA_PREFIX=/usr/local/share/tessdata

apt-get update &&
    apt-get upgrade &&
    apt-get install -y tesseract-ocr tesseract-ocr-eng tesseract-ocr-deu &&
    mkdir ${TESSDATA_PREFIX} &&
    cd ${TESSDATA_PREFIX} &&
    wget https://github.com/tesseract-ocr/tessdata_best/raw/main/eng.traineddata &&
    wget https://github.com/tesseract-ocr/tessdata_best/raw/main/deu.traineddata &&
    tesseract --list-langs

# apt-get update && apt-get install -y fonts-liberation &&
#     wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - &&
#     sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' &&
#     apt update && apt install -y google-chrome-stable


# sudo apt-get update
# sudo apt install -y software-properties-common
# sudo add-apt-repository ppa:phd.re/chromium-browser
# sudo apt-get update
# sudo apt install -y chromium-browser

# apt-get update && apt-get install -y fonts-liberation
# wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
# sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
# apt update && apt install -y google-chrome-stable

# not really working
# wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb &&
#     apt-get install ./google-chrome-stable_current_amd64.deb
