def greet(first_name):
    """
    Simple function which can greet user by name.
    :param first_name: name of user
    :type first_name: str
    """
    if not first_name:
        raise ValueError

    return f'Hello my dear {first_name}!'
