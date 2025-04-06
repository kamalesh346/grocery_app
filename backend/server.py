from flask import Flask, jsonify
import products_dao
from sql_connection import get_sql_connection
app = Flask(__name__)

connection=get_sql_connection()
@app.route('/getProducts',methods=['GET'])  # Define a route for the root URL
def get_products():
    products=products_dao.get_all_products(connection)
    response=jsonify(products)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/hello')
def hello():
    print("hello! how r u")  # Logs to the server console
    return "Hello! How are you?"  # Returns a response to the client

if __name__ == "__main__":
    print("Starting Python Flask Server For Grocery Store Management System")
    app.run(port=5000,debug=True)  # Starts the server on port 5000