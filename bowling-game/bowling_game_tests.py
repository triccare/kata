# Tests
import pytest


from bowling_game import *

game_scores = [
    (10, 10),
    (3, 13),
    (7, 30),
    (6, 36),
    (1, 43),
    (10, 53),
    (10, 73),
    (10, 103),
    (2, 107),
    (8, 125),
    (9, 134),
    (0, 143),
    (7, 150),
    (3, 153),
    (10, 173),
    (10, 183),
    (10, 193)
]


@pytest.fixture(scope='module')
def game():
    return BowlingGame()

def test_init():
    assert isinstance(Frame(5), Frame)
    assert isinstance(Frame(5, 5), Frame)
    with pytest.raises(FrameError):
        Frame(20)
    with pytest.raises(FrameError):
        Frame(1, 1, 1)
    with pytest.raises(FrameError):
        Frame(8, 8)


def test_roll():
    import pytest
    frame = Frame()
    with pytest.raises(FrameError):
        frame.roll(-1)
    with pytest.raises(FrameError):
        frame.roll(11)
    frame.roll(4)
    with pytest.raises(FrameError):
        frame.roll(10)
    frame.roll(4)
    with pytest.raises(FrameError):
        frame.roll(4)


def test_spare():
    assert Frame(3, 7).is_spare
    assert Frame(3, 3).is_spare is False


def test_strike():
    assert Frame(10).is_strike
    assert Frame(0).is_strike is False


@pytest.mark.parametrize("roll, score", game_scores)
def test_game(roll, score, game):
    game.roll(roll)
    assert game.score == score
