from flask import render_template

from app import app

@app.route('/orders')
def index():
    return render_template(
        'index.html', 
        title='Orders', 
    )
