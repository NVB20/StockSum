from flask import Flask, render_template, request, flash
import math
from tests.validations import check_values

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.secret_key = 'your_secret_key'
    

@app.route('/', methods=['GET', 'POST'])
def input_page():
    result = None
    
    if request.method == 'POST':
        # Get the two variables from the form
        high = float(request.form.get('high'))  
        low = float(request.form.get('low'))    
        risk = float(request.form.get('risk')) 

        
        # Calculate enter position and stop loss
        enter_position = high + 0.01
        stop_loss = low - 0.01
        
        # Calculate stock amount
        stock_amount = math.floor(risk / (enter_position - stop_loss))

        # Calculate deal cost
        deal_cost = stock_amount * enter_position


        error_message = check_values(high, low, risk)

        if error_message != None:
            return render_template('index.html', error_message=error_message)

        # Prepare result dictionary
        result = {
            'high': high,
            'low': low,
            'risk': risk,
            'enter_position': enter_position,
            'stop_loss': stop_loss,
            'stock_amount': round(stock_amount, 2), 
            'deal_cost': round(deal_cost, 2)  # Round to 2 decimal places

        }
   
      
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)