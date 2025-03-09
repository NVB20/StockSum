import math 


def result_calc(high, low, risk):
    result = {
        'high': high,
        'low': low,
        'risk': risk,
        'enter_position': high + 0.01,
        'stop_loss': low - 0.01,
        'stock_amount': round(math.floor(risk / ((high + 0.01) - (low - 0.01))), 2), 
        'deal_cost': round((math.floor(risk / ((high + 0.01) - (low - 0.01)))) * (high + 0.01), 2)  # Round to 2 decimal places

    }

    return result