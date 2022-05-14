FROM python:3

ADD . /KluskaAdamski
WORKDIR /KluskaAdamski

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

COPY . .

CMD [ "python", "./main.py" ]