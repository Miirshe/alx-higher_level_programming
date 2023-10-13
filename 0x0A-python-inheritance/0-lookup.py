def lookup(obj):
    attributes = []
    methods = []

    for attr in dir(obj):
        if not attr.startswith('__'):
            if callable(getattr(obj, attr)):
                methods.append(attr)
            else:
                attributes.append(attr)

    return attributes + methods
