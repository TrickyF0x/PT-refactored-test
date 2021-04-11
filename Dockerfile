FROM python:3

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
ADD tests ./tests
ADD funcs ./funcs

ENV PYTHONPATH "${PYTHONPATH}:/app"

CMD [ "pytest","--tb=native", "-r","tests"]