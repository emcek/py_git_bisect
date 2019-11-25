def greet(na):
    if not na:
        raise AttributeError
    return f'Hello my dear {na}!'
