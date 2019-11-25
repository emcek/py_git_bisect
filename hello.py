def greet(first_name):
    """
    Simnple finction which can greet user by name.
    :param first_name: name of user
    :type first_name: str
    """
    if not first_name:
        raise AttributeError

    return f'Hello my dear {first_name}!'
