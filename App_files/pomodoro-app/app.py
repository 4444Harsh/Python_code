from flask import Flask, render_template, request, redirect, session, jsonify
from flask_session import Session

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecretkey"
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/", methods=["GET", "POST"])
def index():
    if "tasks" not in session:
        session["tasks"] = []

    return render_template("index.html", tasks=session["tasks"])

@app.route("/add_task", methods=["POST"])
def add_task():
    data = request.get_json()
    task = data.get("task")

    if "tasks" not in session:
        session["tasks"] = []

    if task:
        session["tasks"].append({"name": task, "done": False})
        session.modified = True
        return jsonify(success=True, index=len(session["tasks"]) - 1)

    return jsonify(success=False)

@app.route("/complete_task", methods=["POST"])
def complete_task():
    data = request.get_json()
    index = data.get("index")
    
    if "tasks" not in session:
        session["tasks"] = []
    
    if index is not None and 0 <= int(index) < len(session["tasks"]):
        session["tasks"][int(index)]["done"] = True
        session.modified = True
        return jsonify(success=True)
    
    return jsonify(success=False)

@app.route("/delete_task", methods=["POST"])
def delete_task():
    data = request.get_json()
    index = data.get("index")
    
    if "tasks" not in session:
        session["tasks"] = []
    
    if index is not None and 0 <= int(index) < len(session["tasks"]):
        session["tasks"].pop(int(index))
        session.modified = True
        return jsonify(success=True)
    
    return jsonify(success=False)

if __name__ == "__main__":
    app.run(debug=True)