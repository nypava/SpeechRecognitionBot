From python:3.10
RUN apt-get update && apt-get -y install \
    python3 python3-dev python3-dev python3-pip python3-venv 
RUN apt-get install -y ffmpeg
COPY requirements.txt app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
ADD . /app
EXPOSE 5000
CMD python main.py
