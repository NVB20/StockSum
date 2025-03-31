from flask import Flask, jsonify, render_template, request, session
from handle.validations import check_values
from handle.result import result_calc
import uuid
from mongo import insert_res, get_history, get_result_by_index

app = Flask(__name__, static_folder='static', static_url_path='/static')
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.secret_key = 'your_secret_key'

@app.route('/', methods=['GET', 'POST'])
def input_page():
    if 'username' not in session:
        session['username'] = str(uuid.uuid4())  # Generate a unique username per session
    
    username = session['username']  # Move inside function to ensure a request context exists

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

    return render_template('index.html', result=result, username=username)


@app.route('/navigate', methods=['GET'])
def navigate():
    if 'username' not in session:
        return jsonify({"error": "User session not found"}), 403
    
    username = session['username']  # Move inside function

    direction = request.args.get('direction')  # 'forward' or 'backward'
    current_index = int(request.args.get('current_index', 0))  # Default to 0 if no index
    
    history = get_history(username)
    max_index = len(history) - 1
    
    if direction == "backward":
        new_index = current_index - 1 if current_index > 0 else 0
    elif direction == "forward":
        new_index = current_index + 1 if current_index < max_index else max_index
    else:
        return jsonify({"error": "Invalid direction"}), 400

    result = get_result_by_index(username, new_index)
    
    if result:
        return jsonify({
            "new_index": new_index,
            "result": result['result'],  # Return the result to show in the frontend
            "date": result['date'].strftime('%Y-%m-%d %H:%M:%S')  # Format date
        })
    else:
        return jsonify({"error": "No result found"}), 404


@app.route('/total_results', methods=['GET'])
def total_results():
    if 'username' not in session:
        return jsonify({"error": "User session not found"}), 403

    username = session['username']  # Move inside function

    history = get_history(username)
    total_results = len(history)

    return jsonify({
        "totalResults": total_results,
        "currentIndex": total_results - 1  # Default to the latest result
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
