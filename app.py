from flask import Flask, request, redirect, flash, render_template
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'your_secret_key'

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'yourgmail@gmail.com'
app.config['MAIL_PASSWORD'] = 'yourpassword'
app.config['MAIL_DEFAULT_SENDER'] = 'yourgmail@gmail.com'

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send-email', methods=['POST'])
def send_email():
    name = request.form.get('name')
    sender_email = request.form.get('email')
    message_body = request.form.get('message')
    
    msg = Message(subject=f"New message from {name}",
                  recipients=["anasnasim1@gmail.com"],
                  body=message_body,
                  sender=sender_email)
    mail.send(msg)
    flash("Message sent successfully!")
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)