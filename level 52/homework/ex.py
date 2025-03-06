def multi_table(number):
    lines = []
    for i in range(1, 11):
        line = f"{i} * {number} = {i * number}"
        lines.append(line)
    return "\n".join(lines)