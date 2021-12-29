from flask import render_template

from MyExp4 import app
from MyExp4.database import db_session, engine
from MyExp4.models import CouponsForm, CustomerForm, Sign


@app.route('/functions/AllSearch')
def show_all():
    return render_template('functions/AllSearch.html', Coupons=db_session.query(CouponsForm).all())
