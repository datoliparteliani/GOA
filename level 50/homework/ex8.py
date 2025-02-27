def printer_error(s):
    allowed_colors = set("abcdefghijklm")
    
    errors = sum(1 for i in s if i not in allowed_colors)
    
    return f"{errors}/{len(s)}"