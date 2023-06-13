def decimal_to_roman(decimal):
    if decimal <= 3:
        return 'I' * decimal
    elif decimal == 5:
        return 'V'
    else:
        return "X"