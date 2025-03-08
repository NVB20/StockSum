from app import high, low, risk

def check_values_zero(high, low, risk):
    if risk <= 0: 
        return "Risk must be greater than 0", 400
    if high <= 0: 
        return "High must be greater than 0", 400
    if low <= 0: 
        return "Low must be greater than 0", 400

def high_low(high, low):
    if low >= high:
        return "High cant be bigger than Low", 400
    
    
