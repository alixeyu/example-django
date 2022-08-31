FROM python:3
ENV PYTHONENVBUFFERED=1

COPY ./requirements.txt /web/

WORKDIR /web
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY ./ /web/

RUN chmod +x entrypoint.sh

ENTRYPOINT ["/web/entrypoint.sh"]