def check_values(high, low, risk):
    try:
        high, low, risk = float(high), float(low), float(risk)
    except ValueError:
        return "All inputs must be numbers"
    
    if high <= 0:
        return "High must be greater than 0"
    if low <= 0:
        return "Low must be greater than 0"
    if risk <= 0:
        return "Risk must be greater than 0"
    if low >= high:
        return "Low can't be bigger than High"
    
    return None
