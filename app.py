import os
from datetime import datetime
from flask import Flask, render_template, request, url_for, session, redirect
from werkzeug.security import generate_password_hash

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


# обработка заморозки
@app.route('/frozen')
def frozen():
    return render_template('frozen.html')


@app.route('/login', methods=('POST', 'GET'))
def login():
    if request.method == 'POST':
        try:
            hash = generate_password_hash(request.form['password'])
            login = request.form['username']
            # u = Users(user_id=1, name='Тиличеев Михаил', login='ArchAL',
            #           password=generate_password_hash(''),
            #           status='teacher')
            # db.session.add(u)
            # db.session.commit()
        except:
            pass
    return render_template('login.html')


if __name__ == '__main__':
    # with app.app_context():
    #     db.create_all()
    app.run()
