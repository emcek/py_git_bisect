def greet(nam):
    if not nam:
        raise AttributeError
    return f'Hello my dear {nam}!'
