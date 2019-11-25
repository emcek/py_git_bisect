def greet(first_name):
    if not first_name:
        raise AttributeError

    return f'Hello my dear {first_name}!'
