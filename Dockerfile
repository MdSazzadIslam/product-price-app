FROM python:3.12-slim

RUN adduser --system --home /app --no-create-home app

WORKDIR /app

COPY requirements.txt .
RUN python -m venv --system-site-packages --without-pip /venv \
    && /venv/bin/python -m pip install --no-cache-dir -r requirements.txt
ENV PATH=/venv/bin:$PATH

COPY . /app
ENV PYTHONPATH /app

USER app
EXPOSE 8080
CMD [ "uvicorn", "product_price_app.main:app", "--host=0.0.0.0", "--port=8080" ]
