def validate_pin(pin):
    if len(pin) != 4 and len(pin) != 6:
        return False
    
    for i in pin:
        if not i.isdigit():
            return False
    return True