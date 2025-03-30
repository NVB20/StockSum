from flask import Flask, render_template, request, session
from handle.validations import check_values
from handle.result import result_calc
import uuid
from mongo import insert_res

app = Flask(__name__, static_folder='css', static_url_path='/css')
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.secret_key = 'your_secret_key'


@app.route('/', methods=['GET', 'POST'])
def input_page():
    if 'username' not in session:
        session['username'] = str(uuid.uuid4())  # Generate a unique username per session
    
    username = session['username']  
    
    result = ()

    if request.method == 'POST':
        
        high = request.form.get('high')
        low = request.form.get('low')
        risk = request.form.get('risk') 


        error_message = check_values(high, low, risk)

        if error_message:
            return render_template('index.html', error_message=error_message), 400
        
        result = result_calc(float(high), float(low), float(risk))
        insert_res(result, username)  
      
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)