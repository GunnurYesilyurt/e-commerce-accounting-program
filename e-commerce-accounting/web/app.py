"""
Serves the HTML pages and provides REST APIs for the JavaScript frontend.
"""
from flask import Flask, render_template, request, jsonify
from datetime import datetime
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.mock_data import COST_DB, generate_mock_orders
from core.calculator import FinancialEngine

app = Flask(__name__)
orders = generate_mock_orders()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/costs', methods=['GET', 'POST'])
def handle_costs():
    if request.method == 'POST':
        data = request.json
        barcode = data.get('barcode')
        if barcode in COST_DB:
            COST_DB[barcode].product_cost = float(data.get('product_cost', COST_DB[barcode].product_cost))
            COST_DB[barcode].packaging_cost = float(data.get('packaging_cost', COST_DB[barcode].packaging_cost))
            COST_DB[barcode].other_expenses = float(data.get('other_expenses', COST_DB[barcode].other_expenses))
            return jsonify({"status": "success"})
    
    return jsonify({bc: cost.__dict__ for bc, cost in COST_DB.items()})

@app.route('/api/calculate', methods=['POST'])
def calculate():
    data = request.json
    start_date = datetime.strptime(data['start_date'], '%Y-%m-%d')
    end_date = datetime.strptime(data['end_date'], '%Y-%m-%d')
    
    engine = FinancialEngine(COST_DB)
    summary = engine.calculate_summary(orders, start_date, end_date)
    return jsonify(summary)