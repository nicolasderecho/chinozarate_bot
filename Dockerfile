FROM python:3.11.1-buster as base

ENV APP_DIR /var/app
WORKDIR $APP_DIR
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
COPY . $APP_DIR

FROM base as development
COPY requirements.txt .
COPY requirements-dev.txt .
RUN pip install -r requirements-dev.txt
CMD ./bin/entrypoint_dev.sh


FROM base as production
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD ./bin/entrypoint.sh

# Run the application:
#COPY myapp.py .
#CMD ["python", "myapp.py"]