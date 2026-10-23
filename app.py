from flask import Flask, jsonify, request

app = Flask(__name__)

class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}


events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]


def find_event(event_id: int):
    return next((event for event in events if event.id == event_id), None)


@app.get("/")
def home():
    return jsonify({"message": "Welcome to the Event API"}), 200


@app.get("/events")
def get_events():
    return jsonify([event.to_dict() for event in events]), 200


@app.post("/events")
def create_event():
    data = request.get_json(silent=True)
    if not data or "title" not in data or not str(data["title"]).strip():
        return jsonify({"error": "'title' is required"}), 400

    next_id = (max((event.id for event in events), default=0) + 1)
    new_event = Event(next_id, str(data["title"]).strip())
    events.append(new_event)

    return jsonify(new_event.to_dict()), 201


@app.patch("/events/<int:event_id>")
def update_event(event_id: int):
    event = find_event(event_id)
    if event is None:
        return jsonify({"error": "Event not found"}), 404

    data = request.get_json(silent=True)
    if not data or "title" not in data or not str(data["title"]).strip():
        return jsonify({"error": "'title' is required"}), 400

    event.title = str(data["title"]).strip()
    return jsonify(event.to_dict()), 200


@app.delete("/events/<int:event_id>")
def delete_event(event_id: int):
    event = find_event(event_id)
    if event is None:
        return jsonify({"error": "Event not found"}), 404

    events.remove(event)
    return "", 204

if __name__ == "__main__":
    app.run(debug=True)
