# Task 1



def unpack_order(order_list):
    for item in order_list:
        print(f"{item[0]} has ordered {item[2]} {item[1]}(s).")



orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    # More orders...
]

unpack_order(orders)