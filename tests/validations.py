def check_values(high, low, risk):
    if risk <= 0: 
        return "Risk must be greater than 0"
    if high <= 0: 
        return "High must be greater than 0"
    if low <= 0: 
        return "Low must be greater than 0"
    if low >= high:
        return "Low cant be bigger than High"
    return None