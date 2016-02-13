from app import app
from app import models
from app import views


if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'


app.run(debug=True)