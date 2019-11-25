def greet(first_name: str):
    """
    Simple function which can greet user by name.

    :param first_name: name of user
    :type first_name: str
    :raise ValueError
    """
    if not first_name:
        raise AttributeError

    value = f'Hello my dear {first_name}!'
    return value
