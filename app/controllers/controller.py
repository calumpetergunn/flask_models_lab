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
    order = orders_list[int(index) - 1]
    return render_template(
        'order.html',
        order = order
    )

# @app.route('/api/v1/resources/books', methods=['GET'])
# def api_id():
#     # Check if an ID was provided as part of the URL.
#     # If ID is provided, assign it to a variable.
#     # If no ID is provided, display an error in the browser.
#     if 'id' in request.args:
#         id = int(request.args['id'])
#     else:
#         return "Error: No id field provided. Please specify an id."

#     # Create an empty list for our results
#     results = []

#     # Loop through the data and match results that fit the requested ID.
#     # IDs are unique, but other fields might return many results
#     for book in books:
#         if book['id'] == id:
#             results.append(book)

#     # Use the jsonify function from Flask to convert our list of
#     # Python dictionaries to the JSON format.
#     return results