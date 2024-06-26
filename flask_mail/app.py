from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER'] = ''
app.config['MAIL_PORT'] = 0
app.config['MAIL_USERNAME'] = ''
app.config['MAIL_PASSWORD'] = ''
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_DEFAULT_SENDER'] = ''

mail = Mail()
mail.init_app(app)


@app.route('/')
def index():
    msg = Message('Hello from Flask!', recipients=['veroyem494@trackden.com'])
    mail.send(msg)
    
    return '<h1>Sent!</h1>'

if __name__ == '__main__':
    app.run(debug=True)