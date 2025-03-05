from flask import Flask, render_template, request
import math

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/', methods=['GET', 'POST'])
def input_page():
    result = None
    
    if request.method == 'POST':
        # Get the two variables from the form
        high = request.form.get('high')
        low = request.form.get('low')
        risk = request.form.get('risk')
        
        # Calculate enter position and stop loss
        enter_position = high + 0.01
        stop_lose = low - 0.01
        
        # Calculate stock amount
        stock_amount = math.floor(risk / (enter_position - stop_lose))

        # Calculate deal cost
        deal_cost = stock_amount * enter_position

        # Prepare result dictionary
        result = {
            'high': high,
            'low': low,
            'risk': risk,
            'enter_position': enter_position,
            'stop_lose': stop_lose,
            'stock_amount': round(stock_amount, 2),  # Round to 2 decimal places
            'deal_cost': round(deal_cost, 2)  # Round to 2 decimal places

        }
    print("Debug Result:", result)
      
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)