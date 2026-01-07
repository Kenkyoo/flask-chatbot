# bot.py
from difflib import SequenceMatcher


def bot_response(message: str) -> str:
    text = message.strip().lower()

    def es_parecida(text, response, umbral=0.7):
        ratio = SequenceMatcher(None, text, response).ratio()
        return ratio >= umbral

    responses = {
        # Saludos y ayuda
        "saludo": ("hola", "buenos días", "buenas tardes", "hey", "hi"),
        "ayuda": ("ayuda", "qué puedes hacer", "comandos", "qué sabes"),
        # Perfil técnico
        "tecnologias": (
            "tecnologías",
            "lenguajes",
            "habilidades",
            "stack",
            "herramientas",
        ),
        "proyectos": ("proyectos", "has creado", "has hecho", "portfolio", "trabajos"),
        # Experiencia y educación
        "experiencia": ("experiencia", "trabajo", "trabajaste", "empleo"),
        "educacion": (
            "estudiaste",
            "educación",
            "formación",
            "estudios",
            "universidad",
        ),
        # Contacto
        "contacto": ("contacto", "email", "correo", "mail"),
        "linkedin": ("linkedin", "linked in"),
        "github": ("github", "git hub", "repo", "código"),
        # Otros
        "ubicacion": ("dónde vives", "ubicación", "ciudad", "país"),
    }

    # Respuestas personalizadas
    if any(es_parecida(text, word) for word in responses["saludo"]):
        return "¡Hola! Soy el asistente virtual de [Tu Nombre]. ¿En qué puedo ayudarte hoy? 😊"

    if any(es_parecida(text, word) for word in responses["ayuda"]):
        return (
            "Puedes preguntarme sobre:\n"
            "- Tecnologías y habilidades\n"
            "- Proyectos que he desarrollado\n"
            "- Mi experiencia profesional\n"
            "- Educación y formación\n"
            "- Cómo contactarme (email, LinkedIn, GitHub)\n"
            "- Dónde estoy ubicado"
        )

    if any(es_parecida(text, word) for word in responses["tecnologias"]):
        return (
            "Domino las siguientes tecnologías:\n"
            "• Python (avanzado)\n"
            "• Flask y FastAPI\n"
            "• SQL y bases de datos (PostgreSQL, SQLite)\n"
            "• Git y GitHub\n"
            "• HTML/CSS básico y JavaScript"
        )

    if any(es_parecida(text, word) for word in responses["proyectos"]):
        return (
            "Algunos proyectos destacados:\n"
            "• Este mismo Chatbot inteligente con Flask 🎯\n"
            "• API REST para gestión de tareas\n"
            "• Script de automatización de backups\n"
            "¡Puedes ver más en mi GitHub!"
        )

    if any(es_parecida(text, word) for word in responses["experiencia"]):
        return "Tengo experiencia desarrollando aplicaciones backend, automatizaciones y APIs. Me apasiona escribir código limpio, testable y bien documentado."

    if any(es_parecida(text, word) for word in responses["educacion"]):
        return "Soy autodidacta apasionado por la programación. He completado cursos en Platzi, freeCodeCamp y Udemy, y sigo aprendiendo todos los días."

    if any(es_parecida(text, word) for word in responses["contacto"]):
        return "¡Contáctame sin problema! Mi email es: tu-email@ejemplo.com"

    if any(es_parecida(text, word) for word in responses["linkedin"]):
        return "Mi LinkedIn: https://linkedin.com/in/tu-usuario"

    if any(es_parecida(text, word) for word in responses["github"]):
        return "Mi GitHub: https://github.com/tu-usuario"

    if any(es_parecida(text, word) for word in responses["ubicacion"]):
        return "Vivo en [Ciudad, País], pero estoy totalmente disponible para trabajo remoto 🌍"

    # Respuesta por defecto divertida
    return (
        "Mmm... aún no entiendo esa pregunta 🤔\n"
        "Prueba preguntándome sobre mis proyectos, tecnologías, experiencia o cómo contactarme.\n"
        "¡O escribe 'ayuda' para ver lo que puedo hacer!"
    )
