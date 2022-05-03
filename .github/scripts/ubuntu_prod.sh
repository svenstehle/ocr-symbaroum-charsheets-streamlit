sudo apt-get install -y tesseract-ocr tesseract-ocr-eng tesseract-ocr-deu

# Install Chrome.
sudo curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add
sudo echo "deb https://dl.google.com/linux/chrome/deb/ stable main" >>/etc/apt/sources.list.d/google-chrome.list
sudo apt-get -y update
sudo apt-get -y install google-chrome-stable
