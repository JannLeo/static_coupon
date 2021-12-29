from flask import (
    flash, redirect, render_template, request, session, url_for
)
from MyExp4 import app
from MyExp4.database import db_session


# login处有问题
@app.route('/admin/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        name = request.form['username']
        email = request.form['email']
        db = db_session()
        error = None

        if not name:
            error = 'Username is required.'
        elif not email:
            error = 'Email address is required.'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO customer_form (name, email) VALUES (?, ?)",
                    (name, email),
                )
                db.commit()
            except db.IntegrityError:
                error = f"User {name} is already registered."
            else:
                return redirect(url_for("admin.login"))

        flash(error)

    return render_template('admin/register.html')


@app.route('/admin/login')
def login():
    if request.method == 'POST':
        name = request.form['username']
        email = request.form['email']
        db = db_session()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE name = ?', (name,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not user['email'] == email:
            error = 'Incorrect email.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('admin/login.html')
