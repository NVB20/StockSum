import math 


def result_calc(high, low, risk):
    result = {
        'high': high,
        'low': low,
        'risk': risk,
        'enter_position': round((high + 0.01), 4),
        'stop_loss': round((low - 0.01), 4),
        'stock_amount': round(math.floor(risk / ((high + 0.01) - (low - 0.01))), 2), 
        'deal_cost': round((math.floor(risk / ((high + 0.01) - (low - 0.01)))) * (high + 0.01), 2)  # Round to 2 decimal places

    }

    return result