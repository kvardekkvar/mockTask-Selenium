FROM python:3.10

#install python requirements
COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt

# install chrome
RUN apt-get update && apt-get install -y wget && apt-get install -y zip
RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get install -y ./google-chrome-stable_current_amd64.deb

# install chromedriver
ENV CHROMEDRIVER_VERSION=120.0.6099.71
RUN wget https://storage.googleapis.com/chrome-for-testing-public/130.0.6723.93/linux64/chromedriver-linux64.zip \
  && unzip chromedriver-linux64.zip && rm -dfr chromedriver_linux64.zip \
  && mv /chromedriver-linux64/chromedriver /usr/bin/chromedriver \
  && chmod +x /usr/bin/chromedriver

#install allure
RUN apt-get update && apt-get install -y default-jre-headless
RUN wget https://github.com/allure-framework/allure2/releases/download/2.32.0/allure_2.32.0-1_all.deb
RUN dpkg -i allure_2.32.0-1_all.deb
RUN allure --version

RUN mkdir docker
WORKDIR /docker
COPY . .
