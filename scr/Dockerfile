FROM ubuntu:18.04

RUN apt-get update && apt-get install -y python3-tk
RUN apt-get install -y python3
RUN apt-get install -y python3-pip

COPY . /app
WORKDIR /app

RUN pip3 install --upgrade pip
RUN pip3 install pyinstaller
RUN pyinstaller --noconfirm --onefile --windowed Renamer.py

CMD [ "./output/Renamer " ]