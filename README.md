# Flask Full CRUD API Lab

This project implements a small RESTful API for events using Flask and in-memory storage.

## Endpoints

- `GET /` -> welcome message
- `GET /events` -> list all events
- `POST /events` -> create an event
- `PATCH /events/<id>` -> update an event title
- `DELETE /events/<id>` -> delete an event

## Run locally

1. Create and activate a virtual environment.
2. Install dependencies:
   `pip install -r requirements.txt`
3. Start server:
   `python app.py`

Server runs on `http://127.0.0.1:5000`.
