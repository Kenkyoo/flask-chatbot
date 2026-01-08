import uuid
from flask import Blueprint, jsonify, render_template, request, session
from flaskr.bot import bot_response
from flaskr.db import get_db

bp = Blueprint("chat", __name__)

@bp.route("/chat", methods=["GET"])
def index():
    if "session_id" not in session:
        session["session_id"] = str(uuid.uuid4())
    
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "SELECT message, response FROM chat WHERE session_id = %s",
        (session["session_id"],)
    )
    messages = cursor.fetchall()
    
    return render_template("chat/index.html", messages=messages)

@bp.route("/chat", methods=["POST"])
def chat():
    if "session_id" not in session:
        session["session_id"] = str(uuid.uuid4())
    
    datos = request.get_json()
    msg = datos["texto"]
    reply = bot_response(msg)
    
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO chat (message, response, session_id) VALUES (%s, %s, %s)",
        (msg, reply, session["session_id"])
    )
    db.commit()
    
    return jsonify({"resultado": reply})