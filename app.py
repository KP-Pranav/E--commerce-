# backend/app.py
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS

# Dummy orders database
orders = [
    {"order_id": "1001", "status": "Shipped", "item": "Laptop", "price": 50000},
    {"order_id": "1002", "status": "Processing", "item": "Mobile", "price": 20000},
    {"order_id": "1003", "status": "Delivered", "item": "Headphones", "price": 3000},
]

# Endpoint to get all orders
@app.route('/api/orders', methods=['GET'])
def get_orders():
    return jsonify(orders)

# Endpoint to get order by ID
@app.route('/api/order/<order_id>', methods=['GET'])
def get_order_by_id(order_id):
    for order in orders:
        if order["order_id"] == order_id:
            return jsonify(order)
    return jsonify({"error": "Order not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
