def greet(first_name):
    """

    :type first_name: str
    """
    if not first_name:
        raise AttributeError

    return f'Hello my dear {first_name}!'
