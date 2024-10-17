FROM python:3.12.5

WORKDIR /omie_app
COPY . .


ARG host
ARG port

ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV PYTHON_ENV="production"


##EXPOSE ${port}
EXPOSE 5050

RUN pip install poetry
RUN poetry install

CMD ["poetry", "run", "python3", "-m", "gunicorn", "--workers", "4", "--bind", "0.0.0.0:5050", "main"]



 