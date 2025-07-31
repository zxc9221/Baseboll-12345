import pytest
from game import Game

@pytest.fixture
def game():
    return Game()

def test_exception_when_input_is_none(game):
    game = Game()
    with pytest.raises(TypeError):
        game.guess(None)