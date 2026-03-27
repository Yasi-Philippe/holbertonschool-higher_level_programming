#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json():
    try:
        with open('products.json', 'r') as f:
            return json.load(f)
    except Exception:
        return []

def read_csv():
    products = []
    try:
        with open('products.csv', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                })
    except Exception:
        return []
    return products


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ['json', 'csv']:
        return render_template('product_display.html',
                               error="Wrong source")

    if source == 'json':
        data = read_json()
    else:
        data = read_csv()

    if product_id:
        try:
            product_id = int(product_id)
            data = [p for p in data if p["id"] == product_id]

            if not data:
                return render_template('product_display.html',
                                       error="Product not found")
        except ValueError:
            return render_template('product_display.html',
                                   error="Invalid id")

    return render_template('product_display.html',
                           products=data,
                           error=None)


if __name__ == '__main__':
    app.run(debug=True)
