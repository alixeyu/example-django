FROM python:3
ENV PYTHONENVBUFFERED=1

COPY ./requirements.txt .

WORKDIR /web
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY ./ /web/

ENTRYPOINT ["python", "manage.py", "runserver"]