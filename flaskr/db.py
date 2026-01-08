import psycopg
import click
from flask import current_app, g

def get_db():
    if "db" not in g:
        g.db = psycopg.connect(current_app.config["DATABASE_URL"])
    return g.db

def init_db():
    db = get_db()
    with current_app.open_resource("schema.sql") as f:
        db.execute(f.read().decode("utf8"))
        db.commit()

@click.command("init-db")
def init_db_command():
    init_db()
    click.echo("Initialized the database.")

def close_db(e=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
