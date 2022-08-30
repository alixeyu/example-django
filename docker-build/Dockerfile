FROM python:3
ENV PYTHONENVBUFFERED=1

WORKDIR /web/
COPY requirements.txt /web/

RUN pip install --upgrade pip && pip install -r requirements.txt
COPY ./ /web/

ENTRYPOINT ["python", "manage.py", "runserver"]