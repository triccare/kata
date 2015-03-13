class FrameError(Exception):
    """Frame error."""


class Frame(object):
    """Bowling frame."""
    def __init__(self, *rolls):
        self.score = 0
        self.completed = False
        self.rolls = []
        for roll in rolls:
            self.roll(roll)

    @property
    def is_strike(self):
        try:
            return self.rolls[0] == 10
        except KeyError:
            return False

    @property
    def is_spare(self):
        try:
            return self.rolls[0] + self.rolls[1] == 10
        except KeyError:
            return False

    def roll(self, roll):
        if roll not in range(0, 11):
            raise FrameError('Invalid roll {}. Must be between 0 and 10.'.format(roll))
        try:
            if self.completed or len(self.rolls) >= 2 or self.rolls[0] == 10:
                raise FrameError('Frame completed.')
        except (KeyError, IndexError):
            pass
        try:
            if self.rolls[0] + roll > 10:
                raise FrameError('Total roll count greater than 10.')
        except IndexError:
            pass
        self.rolls.append(roll)
        self.completed = (len(self.rolls) == 2 and self.rolls[0] + self.rolls[1] < 10)


class Tests(object):
    game = [
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

    def test_init(self):
        import pytest
        assert isinstance(Frame(5), Frame)
        assert isinstance(Frame(5, 5), Frame)
        with pytest.raises(FrameError):
            Frame(20)
        with pytest.raises(FrameError):
            Frame(1, 1, 1)
        with pytest.raises(FrameError):
            Frame(8, 8)

    def test_roll(self):
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

    def test_spare(self):
        assert Frame(3, 7).is_spare
        assert Frame(3, 3).is_spare is False

    def test_strick(self):
        assert Frame(10).is_strike
        assert Frame(0).is_strike is False
