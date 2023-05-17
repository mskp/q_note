from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user
from .models import Notes
from . import db

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@views.route('/home')
@login_required
def home():
    if request.method == "POST":
        title = request.form.get('title').strip()
        description = request.form.get('description').strip()

        if (title and description):
            db.session.add(Notes(
                user_id=current_user.id,
                title=title,
                description=description
            ))
            db.session.commit()

    if request.form.get('delete-btn'):
        id = request.form.get('delete-btn')
        Notes.query.filter_by(id=id).delete()
        db.session.commit()

    notes = Notes.query.filter_by(user_id=current_user.id).order_by(
        Notes.created_on.desc()).all()

    return render_template('index.html', notes=notes)


@views.route('/note')
@login_required
def delete_note():
    note_id = request.args.get('note_id')
    Notes.query.filter_by(id=note_id).delete()
    db.session.commit()
    return redirect(url_for('views.home'))
