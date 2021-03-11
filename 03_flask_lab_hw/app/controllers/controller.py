from flask import render_template

from app import app
from app.models.order_list import orders

# Basic route, no logic in the controller, HTML handles presentation etc
@app.route('/order/')
def index():
    return render_template(
        'base.html', 
        title = "Dildos 'r' us", 
        orders = orders
    )

# Route for by index, logic is here in controller but commented out as we couldn't get it to search by index number properly.
# Missing something... Very close. I can feel it. Instead index was linked to HTML
@app.route('/order/find-by-index/<index>')
def find_by_index(index):
    
#     for order in orders:
#         if orders[0] == index:
#             return f"{str(order.customer_name)} ordered {str(order.quantity)} of{str(order.item_name)} for personal reasons, on {str(order.order_date)}"

#     return "User not found (try 0 or 1)"

    return render_template(
        'order_list.html',
        title = "Dildos 'r' us",
        orders = orders
    )

# Route for search by name, we could get this to work by giving individual response based on name parameter.
# Almost all logic in controller, basic presentation is even dictated from here via a formatted string.
@app.route('/order/find-by-name/<name>')
def find_by_name(name):
    for order in orders:
        if order.customer_name == name:
            return f"{str(order.customer_name)} ordered {str(order.quantity)} of {str(order.item_name)} for personal reasons, on {str(order.order_date)}"

    return "User not found (try Robert or Bob)"

    return render_template(
        'order.html',
        title = "Dildos 'r' us",
        orders = orders
    )
