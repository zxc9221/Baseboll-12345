from math import gamma
class GameResult:
    def __init__(self, solved, strikes, balls):
        self._solved = solved
        self._strikes = strikes
        self._balls = balls

    @property
    def solved(self):
        return self._solved

    @property
    def strikes(self):
        return self._strikes

    @property
    def balls(self):
        return self._balls

class Game:
    def __init__(self):
        self._question = ""

    @property
    def question(self):
        raise AttributeError("읽을 수 없는 속성")

    @question.setter
    def question(self, value):
        self._question = value

    def guess(self, guess_number):
        self._assert_illegal_value(guess_number)
        if guess_number == self._question:
            return  GameResult(True, 3, 0)
        else:
            return GameResult(False, 0, 0)

    def _assert_illegal_value(self, guess_number):
        if guess_number is None:
            raise TypeError("입력이 None 입니다.")
        if len(guess_number) != 3:
            raise TypeError("입력은 3 자리 문자열이여야 합니다.")
        if not guess_number.isdigit():
                raise TypeError("모든 문자는 숫자로 구성되어야 합니다.")
        if self._isDuplicatedNumber(guess_number):
            raise TypeError("중복된 숫자가 존재합니다.")

    def _isDuplicatedNumber(self, guessNumber):
        return len(set(guessNumber)) != 3