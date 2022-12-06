FROM ubuntu:22.04

ENV VIRTUAL_ENV=/root/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN groupadd -r nonroot && useradd --no-log-init -r -g nonroot nonroot

# install packages
RUN apt-get update && apt-get install -y virtualenv

RUN chown nonroot:nonroot -R /root
USER nonroot
WORKDIR /root
RUN virtualenv -ppython3 ${VIRTUAL_ENV}
COPY . .
RUN pip install -r requirements.txt

# set entrypoint
ENTRYPOINT ["python3", "wsgi.py"]