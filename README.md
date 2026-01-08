# Flask Chatbot

Chatbot simple desarrollado con **Flask** y **Python**, usando **PostgreSQL (Neon)** como base de datos, **Bulma CSS** para el diseño y desplegado en **Vercel**.

El proyecto guarda el historial de mensajes por sesión y responde según palabras clave (con detección básica de similitud).

---

## 🚀 Demo

👉 Deploy: [https://flask-chatbot-nine.vercel.app/](https://flask-chatbot-nine.vercel.app/)

👉 Repositorio: [https://github.com/Kenkyoo/flask-chatbot](https://github.com/Kenkyoo/flask-chatbot)

---

## 🧩 Tecnologías usadas

* Python
* Flask
* PostgreSQL (Neon)
* psycopg
* Bulma CSS
* JavaScript (fetch API)
* Vercel

---

## 📂 Estructura del proyecto

```
flask-chatbot/
├── flaskr/
│   ├── __init__.py
│   ├── chat.py
│   ├── db.py
│   ├── bot.py
│   ├── schema.sql
│   └── templates/
│       ├── hero.html
│       └── chat/
│           └── index.html
├── requirements.txt
├── vercel.json
└── README.md
```

---

## ⚙️ Configuración local

### 1. Clonar el repositorio

```bash
git clone https://github.com/Kenkyoo/flask-chatbot.git
cd flask-chatbot
```

### 2. Crear entorno virtual

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Variables de entorno

Configurar la URL de PostgreSQL (Neon):

```bash
export POSTGRES_URL="postgresql://usuario:password@host/dbname?sslmode=require"
```

---

## 🗄️ Base de datos

El esquema se define en `schema.sql`:

```sql
CREATE TABLE IF NOT EXISTS chat (
  id SERIAL PRIMARY KEY,
  session_id TEXT,
  message TEXT,
  response TEXT,
  date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

Inicializar la base de datos:

```bash
flask --app flaskr init-db
```

---

## 💬 Funcionamiento

* Cada usuario obtiene un `session_id` automático
* Los mensajes y respuestas se guardan en PostgreSQL
* Al recargar la página se muestra el historial
* Las respuestas del bot se generan en `bot.py`

---

## 📌 Objetivo del proyecto

Este proyecto forma parte de un **portfolio backend** y puede reutilizarse como base para:

* Chatbots simples
* Formularios con historial
* APIs con Flask + PostgreSQL
* Proyectos deployados en Vercel

---

## 📜 Licencia

Proyecto de uso libre con fines educativos y de portfolio.
