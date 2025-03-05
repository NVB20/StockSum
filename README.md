# Stock Calculator Web App

This is a simple web application built with Flask that calculates position size, stop loss, and deal cost for stock trading. It allows users to input the high and low values of a candle along with the risk amount. The app then calculates the following:

- **Enter Position**: The price at which the trade will be entered.
- **Stop Loss**: The price at which the trade will be stopped to limit losses.
- **Stock Amount**: The number of stocks to buy based on the risk.
- **Total Deal Cost**: The total cost of the deal based on stock amount and enter position.

## Features

- User-friendly form to input candle high, low, and risk amount.
- Displays results dynamically after submitting the form:
  - Enter position
  - Stop loss
  - Stock amount to buy
  - Total deal cost

## Technologies Used

- **Flask**: Web framework for building the application.
- **HTML/CSS**: For structuring and styling the frontend.
- **Python**: Backend logic for calculations.

## Installation

### Prerequisites

- Python 3.x
- Flask

### Steps to Run the App Locally

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/your-username/stock-calculator.git
    ```

2. Navigate to the project folder:

    ```bash
    cd stock-calculator
    ```

3. Create a virtual environment (optional but recommended):

    ```bash
    python3 -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

      ```bash
      venv\Scripts\activate
      ```

    - On macOS/Linux:

      ```bash
      source venv/bin/activate
      ```

5. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Run the Flask app:

    ```bash
    python app.py
    ```

7. Open your browser and visit [http://127.0.0.1:5000/](http://127.0.0.
