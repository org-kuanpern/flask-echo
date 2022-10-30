FROM ubuntu:22.04

# install packages
RUN apt-get update && apt-get install -y python3-pip
RUN pip3 install flask
WORKDIR /root
COPY . .

# set entrypoint
ENTRYPOINT ["python3", "wsgi.py"]
