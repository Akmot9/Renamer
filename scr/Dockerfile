FROM ubuntu:22.04

RUN apt-get update && apt-get install -y python3-tk
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get install -y x11-apps

COPY . /app
WORKDIR /app

RUN pip3 install --upgrade pip
RUN apt-get install -y tcl-dev tk-dev
RUN pip3 install pyinstaller
RUN pyinstaller --noconfirm --onefile --windowed Renamer.py

CMD [ "xhost +local:docker" ]
CMD [ "export DISPLAY=unix$DISPLAY" ]
CMD [ "./dist/Renamer" ]