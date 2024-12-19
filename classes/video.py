class Video:
    def __init__(self, title: str, duration: int, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __str__(self):
        return f'{self.title}'

    def __eq__(self, other):
        if isinstance(other, Video):
            return self.title == other.title
        return self.title == other

