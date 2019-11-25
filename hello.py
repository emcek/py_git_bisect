def greet(name):
    if not name:
        raise AttributeError
    return f'Hello my dear {name}!'
