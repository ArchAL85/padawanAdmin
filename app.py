import os
from datetime import datetime
from flask import Flask, render_template, request, url_for, session, redirect
from flask_login import LoginManager, login_required, login_user, current_user, logout_user

from database.just_db import db
from database.db_core import Users, VKGroups, Students, HomeWorks

SECRET_KEY = 'turbo_padawan_is_the_best'

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config.from_object(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'project.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return db.session.query(Users).get(user_id)


# обработка заморозки
@app.route('/frozen')
@login_required
def frozen():
    return render_template('frozen.html')


@app.route('/login', methods=('POST', 'GET'))
def login():
    if request.method == 'POST':
        try:
            user_password = request.form['password']
            user_login = request.form['username']
            user = db.session.query(Users).filter(Users.login.ilike(user_login)).first()
            if user and user.check_password(user_password):
                login_user(user, remember=True)
                return redirect(url_for('frozen'))
            return redirect(url_for('login'))
        except:
            pass
    return render_template('login.html')



@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    # with app.app_context():
    #     db.create_all()
    app.run()
