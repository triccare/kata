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

class BowlingGame(object):
    pass
