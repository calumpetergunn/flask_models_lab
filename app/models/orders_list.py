from app.models.order import Order

order1 = Order("James", "21/02/21", 3)
order2 = Order("Lucy", "10/02/21", 1)
order3 = Order("Jade", "01/03/21", 5)

orders_list = [order1, order2, order3]
order_len = len(orders_list)
