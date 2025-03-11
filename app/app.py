from flask import Flask
import mysql.connector

app = Flask(__name__)

# Database configuration
db_config = {
    'host': 'db',
    'user': 'root',
    'password': 'example',
    'database': 'mydatabase'
}

@app.route('/')
def hello():
    try:
        # Connect to the database
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Fetch data from the items table
        cursor.execute("SELECT name FROM items")
        items = cursor.fetchall()

        # Close the connection
        cursor.close()
        connection.close()

        # Display the items
        return f"Hello from Docker! Items in the database: {[item[0] for item in items]}"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
