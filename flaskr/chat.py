import uuid

from flask import Blueprint, jsonify, render_template, request, session

from flaskr.db import get_db

bp = Blueprint("chat", __name__)


def bot_response(message):
    text = message.lower()

    # --- Saludo y Ayuda ---
    if "hola" in text or "buenos días" in text:
        return "¡Hola! Soy el asistente virtual de [Tu Nombre]. ¿Qué te gustaría saber sobre mi perfil profesional?"

    if "ayuda" in text or "que puedes hacer" in text:
        return "Puedes preguntarme sobre: tecnologías, experiencia, proyectos, educación, contacto o mi ubicación."

    # --- Perfil Técnico ---
    if "tecnologías" in text or "lenguajes" in text or "habilidades" in text:
        return "Mis habilidades principales son: Python, Flask, SQL y control de versiones con Git."

    if "proyectos" in text or "creado" in text:
        return "He desarrollado este Chatbot, una API REST con Flask y [menciona otro proyecto corto]."

    # --- Experiencia y Educación ---
    if "experiencia" in text or "trabajó" in text:
        return "He trabajado en proyectos de backend y automatización. Estoy enfocado en crear código limpio y eficiente."

    if "estudió" in text or "educación" in text or "formación" in text:
        return "Actualmente me formo de manera autodidacta en desarrollo backend y participo en comunidades de programación."

    # --- Información de Contacto ---
    if "contacto" in text or "email" in text or "correo" in text:
        return "Puedes contactarme en: tu-email@ejemplo.com"

    if "linkedin" in text:
        return "Mi perfil de LinkedIn es: linkedin.com/in/tu-usuario"

    if "github" in text:
        return "Puedes ver mi código en: github.com/tu-usuario"

    # --- Otros ---
    if "donde vives" in text or "ubicación" in text:
        return "Me encuentro en [Tu Ciudad/País], pero tengo disponibilidad para trabajo remoto."

    # --- Respuesta por defecto ---
    return "Aún estoy aprendiendo. Puedes intentar preguntando por 'experiencia', 'proyectos' o 'contacto'."


@bp.route("/chat", methods=["GET"])
def index():
    if "session_id" not in session:
        session["session_id"] = str(uuid.uuid4())

    db = get_db()
    messages = db.execute(
        "SELECT message, response FROM chat WHERE session_id = ?",
        (session["session_id"],),
    ).fetchall()

    return render_template("chat/index.html", messages=messages)


@bp.route("/chat", methods=["POST"])
def chat():
    if "session_id" not in session:
        session["session_id"] = str(uuid.uuid4())

    datos = request.get_json()
    msg = datos["texto"]
    reply = bot_response(msg)

    db = get_db()
    db.execute(
        "INSERT INTO chat (message, response, session_id) VALUES (?, ?, ?)",
        (msg, reply, session["session_id"]),
    )
    db.commit()

    return jsonify({"resultado": reply})
