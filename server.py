from flask import Flask
import hashlib
app = Flask(__name__)

@app.route('/')
def base():
    render_template('base')
    set_password('alan', 'test')
    return 'Hello, World!'

def set_password(username, password):
    with open('users/'+username, 'w') as f:
        f.write(_get_hash(password))

def check_password(username, password):
    hashed_pw = _get_hash(password)
    return hashed_pw == _read_password(username)

def _read_password(username):
    with open('users/'+username, 'r') as f:
        password = f.read()
    return password

def _get_hash(password):
    return hashlib.sha256(bytearray(password, 'utf8')).hexdigest()

if __name__ == '__main__':
    app.run()
