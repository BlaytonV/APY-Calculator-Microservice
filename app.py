from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

def calculate_apy(initial_deposit, monthly_deposit, apy, years):
    total_savings = initial_deposit
    monthly_rate = apy / 100 / 12
    total_months = years * 12
    for _ in range(total_months):
        total_savings += monthly_deposit
        total_savings += total_savings * monthly_rate
    interest_earned = total_savings - (initial_deposit + monthly_deposit * total_months)
    return total_savings, interest_earned

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        initial_deposit = float(data.get('initial_deposit', 0))
        monthly_deposit = float(data.get('monthly_deposit', 0))
        apy = float(data.get('apy', 0))
        years = int(data.get('time_period', 0))

        print(f"Received JSON payload - Initial Deposit: {initial_deposit}, Monthly Deposit: {monthly_deposit}, APY: {apy}, Time Period (Years): {years}")

        total_savings, interest_earned = calculate_apy(initial_deposit, monthly_deposit, apy, years)

        response = {
            'initial_deposit': initial_deposit,
            'monthly_deposit': monthly_deposit,
            'apy': apy,
            'time_period': years,
            'total_savings': round(total_savings, 2),
            'interest_earned': round(interest_earned, 2)
        }
        
        return jsonify(response)
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({
            'error': 'An error occurred while processing the request.',
            'details': str(e)
        })

@app.route('/')
def index():
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)), 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
