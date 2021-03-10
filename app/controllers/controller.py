from flask import render_template

from app import app

from app.models.orders_list import orders_list

@app.route('/orders')
def index():
    return render_template(
        'index.html', 
        title='Orders', 
        orders = orders_list
    )
