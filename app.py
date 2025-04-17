from flask import Flask, render_template, request, redirect, url_for
import database

app = Flask(__name__)
database.create_table()

@app.route('/')
def index():
    items = database.get_all_items()
    return render_template('index.html', items=items)
@app.route('/add', methods=['POST'])
def add_item():
    name = request.form['name']
    quantity = int(request.form['quantity'])
    price = float(request.form['price'])
    database.insert_item(name, quantity, price)
    return redirect(url_for('index'))
@app.route('/update/<int:item_id>', methods=['POST'])
def update_item(item_id):
    quantity = int(request.form['quantity'])
    price = float(request.form['price'])
    database.update_item(item_id, quantity, price)
    return redirect(url_for('index'))
@app.route('/delete/<int:item_id>')
def delete_item(item_id):
    database.delete_item(item_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
