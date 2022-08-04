FROM python:3.6-slim

RUN apt-get update -y && \
    apt-get install -y python3-pip python-dev ffmpeg libsm6 libxext6 poppler-utils tesseract-ocr tesseract-ocr-rus unoconv abiword  && \
    pip3 install --upgrade pip
# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
