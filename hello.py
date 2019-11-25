def greet(first_name: str) -> str:
    """
    Simple function which can greet user by name.

    :param first_name: name of user
    :type first_name: str
    :raise ValueError
    :return: greeting string
    """
    if not first_name:
        raise ValueError
    return f'Hello my dear {first_name}!'
