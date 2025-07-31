class Game:
    def guess(self, guessNumber):
        if guessNumber is None:
            raise  TypeError()

        if len(guessNumber) != 3:
            raise TypeError()

        for numbers in guessNumber:
            if not ord('0') <= ord(numbers) <= ord('9'):
                raise TypeError()