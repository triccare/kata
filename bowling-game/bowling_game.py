FRAME_MARK_SCORE = 10
FRAME_INITIAL_REQUIRED_ROLLS = 2

class FrameError(Exception):
    """Frame error."""


class Frame(object):
    """Bowling frame."""
    def __init__(self, *rolls):
        self.rolls = []
        self.required_rolls = FRAME_INITIAL_REQUIRED_ROLLS
        for roll in rolls:
            self.roll(roll)

    @property
    def score(self):
        if self.completed:
            return sum(self.rolls)
        else:
            return None

    @property
    def completed(self):
        return len(self.rolls) == self.required_rolls

    @property
    def is_strike(self):
        try:
            return self.rolls[0] == FRAME_MARK_SCORE
        except IndexError:
            return False

    @property
    def is_spare(self):
        try:
            return self.rolls[0] + self.rolls[1] == FRAME_MARK_SCORE
        except IndexError:
            return False

    def roll(self, roll):
        if self.completed:
            raise FrameError('Frame completed.')
        if roll not in range(0, 11):
            raise FrameError('Invalid roll {}. Must be between 0 and 10.'.format(roll))
        if not self.is_strike and len(self.rolls) == 1 and self.rolls[0] + roll > 10:
            raise FrameError('Invalid roll {}. First two rolls cannot be greater than 10.')
        self.rolls.append(roll)
        if self.is_spare or self.is_strike:
            self.required_rolls = 3


class BowlingGame(object):
    pass
