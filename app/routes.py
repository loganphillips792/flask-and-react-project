from app import app

@app.route('/')
def hello():
    app.logger.info('%s logged in successfully', 'logan564')
    return 'Hello, World!'