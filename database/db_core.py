from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from .just_db import db


class Users(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    login = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(500), nullable=False)
    status = db.Column(db.String(25), default='padawan', nullable=False)  # admin, teacher

    def __repr__(self):
        return f'{self.user_id}: {self.name}'


class VKGroups(db.Model):
    __tablename__ = 'vk_groups'
    vk_group_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    vk_message = db.Column(db.String(255), nullable=False)
    last_update = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f'{self.title}'


class HomeWorks(db.Model):
    __tablename__ = 'hw'
    hw_id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False)
    max_exercises = db.Column(db.Integer, nullable=False)
    state = db.Column(db.String(15), default='test', nullable=False)  # write, variant

    def __repr__(self):
        return f'{self.state}'


class Students(db.Model):
    __tablename__ = 'students'
    student_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    vk_id = db.Column(db.Integer, nullable=False)
    vk_group = db.Column(db.Integer, db.ForeignKey('vk_groups.vk_group_id'))
    frozen = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    active = db.Column(db.Boolean, default=False, nullable=False)
    last_student_msg = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    last_teacher_msg = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    lives = db.Column(db.Integer, nullable=False)
    tags = db.Column(db.String(150), nullable=False)

    def __repr__(self):
        return f'{self.name}'