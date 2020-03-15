from flask import Blueprint, render_template, url_for, request, redirect
from flask_login import login_required, current_user
from flask_sqlalchemy import SQLAlchemy 
from . import db
from .models import tasks


main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/board')
@login_required
def board():
    todo = tasks.query.filter_by(user_id = current_user.id, status="todo").all()
    doing = tasks.query.filter_by(user_id = current_user.id, status="doing").all()
    done = tasks.query.filter_by(user_id = current_user.id, status="done").all()
    return render_template('board.html',name=current_user.first_name + " " + current_user.last_name,
    todo=todo,doing=doing,done=done)

@main.route('/add_task', methods=['POST'])
@login_required
def add_task():
    title = request.form.get('title')
    descripition = request.form.get('descripition')
    status = request.form.get('status')
    task = tasks(title=title, descripition=descripition, status=status, user_id=current_user.id )
    db.session.add(task)
    db.session.commit()
    return redirect(url_for('main.board'))

@main.route('/delete_task/<id>', methods=['POST'])
@login_required
def delete_task(id):
    task = tasks.query.filter_by(task_id=int(id)).first()
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('main.board'))


@main.route('/switch/<status>/<id>', methods=['POST'])
@login_required
def switch(status, id):
    task = tasks.query.filter_by(task_id=int(id)).first()
    task.status = str (status)
    db.session.commit()
    return redirect(url_for('main.board'))
