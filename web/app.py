from flask import Flask, request, render_template, jsonify, redirect, session, url_for

import uuid, datetime

app = Flask(__name__)

app.config['SECRET_KEY'] = str(uuid.uuid4())
app.permanent_session_lifetime = datetime.timedelta(days=31)

@app.route('/')
@app.route('/main')
def main():
    if 'Login' not in session or not session['Login']:
        return redirect(url_for("authorization"))
    return render_template('index.html')

@app.route('/authorization')
def authorization():
    session.permanent = True
    if 'Login' not in session:
        session['Login'] = ''
        session['Password'] = ''
        session.modified = True
    return render_template('authorization.html')

@app.route('/log', methods=['POST'])
def log():
    if 'Login' not in session:
        return jsonify({'status_result': 0, 'message': 'Произошла ошибка'})
    
    print(request.json['password'])
    print(request.json['login'])
    
    return jsonify({'status_result': 200, 'message': 'Успешная авторизация'})
    # if request.method == 'POST':
    #     login = request.json['login']
    #     password = request.json['password']
    #     ed = db.EmployeesDatabase()
    #     if ed.authenticate_user(login, password):
    #         session.permanent = True
    #         session['Login'] = login
    #         session['Password'] = password
    #         session.modified = True
    #         return jsonify({'status_result': 200, 'message': 'Успешная авторизация'})
    #     return jsonify({'status_result': 0, 'message': 'Произошла ошибка'}) main_rectangle

if __name__ == '__main__':
    app.run(debug=True)