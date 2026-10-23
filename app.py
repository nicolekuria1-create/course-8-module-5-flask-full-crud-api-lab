from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory store to simulate a database.
events = [
    {"id": 1, "title": "Team Meeting"},
    {"id": 2, "title": "Tech Conference"},
]
next_id = 3


def find_event(event_id: int):
    """Return the matching event dict or None."""
    return next((event for event in events if event["id"] == event_id), None)


@app.get("/")
def home():
    return jsonify({"message": "Welcome to the Event API"}), 200


@app.get("/events")
def get_events():
    return jsonify(events), 200


@app.post("/events")
def create_event():
    global next_id

    data = request.get_json(silent=True)
    if not data or "title" not in data or not str(data["title"]).strip():
        return jsonify({"error": "'title' is required"}), 400

    new_event = {
        "id": next_id,
        "title": str(data["title"]).strip(),
    }
    events.append(new_event)
    next_id += 1

    return jsonify(new_event), 201


@app.patch("/events/<int:event_id>")
def update_event(event_id: int):
    event = find_event(event_id)
    if event is None:
        return jsonify({"error": "Event not found"}), 404

    data = request.get_json(silent=True)
    if not data or "title" not in data or not str(data["title"]).strip():
        return jsonify({"error": "'title' is required"}), 400

    event["title"] = str(data["title"]).strip()
    return jsonify(event), 200


@app.delete("/events/<int:event_id>")
def delete_event(event_id: int):
    event = find_event(event_id)
    if event is None:
        return jsonify({"error": "Event not found"}), 404

    events.remove(event)
    return jsonify({"message": "Event deleted successfully"}), 200


if __name__ == "__main__":
    app.run(debug=True)
