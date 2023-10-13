def lookup(obj):
    result = []
    for attr in dir(obj):
        if not attr.startswith('__'):
            result.append(attr)
    return result
