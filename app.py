from flask import Flask, render_template, request
from tests.validations import check_values
from handle.result import result_calc

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
    

@app.route('/', methods=['GET', 'POST'])
def input_page():  

    result = ()

    if request.method == 'POST':
        
        high = request.form.get('high')
        low = request.form.get('low')
        risk = request.form.get('risk') 


        error_message = check_values(high, low, risk)

        if error_message:
            return render_template('index.html', error_message=error_message), 400

        result = result_calc(high, low, risk)
      
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)