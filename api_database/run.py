# run.py
from api_database import app, db
from api_database.config import Config

app.config.from_object(Config)
db.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0')