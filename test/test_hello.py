from pytest import raises

from hello import greet


def test_greet_1():
    assert greet('Mike') == 'Hello my dear Mike!'


def test_greet_2():
    with raises(AttributeError):
        greet('')
