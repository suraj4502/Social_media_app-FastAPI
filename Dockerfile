FROM python:3.11

WORKDIR /usr/src/code

COPY Social_media/requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# RUN alembic upgrade head
CMD ["uvicorn", "Social_media.main:app", "--host", "0.0.0.0", "--port", "8000"]