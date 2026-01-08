import os
from flask import Flask, render_template

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE_URL=os.environ.get('POSTGRES_URL', 'postgresql://localhost/flaskr')
    )
    
    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.update(test_config)

    @app.route("/")
    def index():
        return render_template("hero.html")        

    @app.route("/hello")
    def hello():
        return "Hello, World!"
        
    from . import db
    db.init_app(app)
    
    from . import chat
    app.register_blueprint(chat.bp)
    
    app.add_url_rule("/", endpoint="index")
    return app

app = create_app()