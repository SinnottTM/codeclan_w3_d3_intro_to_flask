class Order():

    def __init__(self,customer_name, item_name, order_date, quantity):
        self.customer_name = customer_name
        self.item_name = item_name
        self.order_date = order_date
        self.quantity = quantity
        
    # def return_by_index(self, orders, name):
    #     for order in orders:
    #         if order[0] == name:
    #             return order
    #         else:
    #             return "User not found (try Malcolm)"
