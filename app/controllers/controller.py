from flask import render_template

from app import app

from app.models.orders_list import orders_list, order_len

@app.route('/orders')
def index():
    return render_template(
        'index.html', 
        title='Orders', 
        orders = orders_list,
        order_len = order_len
    )

@app.route('/orders/<index>', methods=['GET'])
def show_order(index):
    try:
        order = orders_list[int(index) - 1]
        return render_template(
        'order.html',
        order = order
        )
    except:
        return page_not_found(404)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
