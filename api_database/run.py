# run.py
from app import app
from app.models import db
from config import Config

app.config.from_object(Config)
db.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=False, host='0.0.0.0')