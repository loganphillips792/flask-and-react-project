from app import app
from app import db
from app.models.models import User

@app.route('/')
def hello():
    app.logger.info('%s logged in successfully', 'logan564')
    users = db.session.execute(db.select(User).order_by(User.username)).scalars()
    return 'Hello, World!'