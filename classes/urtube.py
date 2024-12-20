import time

from user import User
from video import Video


class UrTube:
    def __init__(self):
        self.videos = []
        self.users = []
        self.current_user = None

    # def __str__(self):
    #     return self.videos

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname.lower() and user.password == hash(password):
                print(f'Login successfully \nCurrent user: {self.current_user}\n')
                self.current_user = user
                return
        else:
            print(f'User "{nickname}" not find')

    def register(self, nickname, password, age):
        new_user = User(nickname.lower(), password, age)
        if new_user not in self.users:
            self.users.append(new_user)
            self.current_user = new_user
        else:
            print(f'Пользователь {new_user} уже существует')
            return

    def log_out(self):
        if self.current_user:
            self.current_user = None

    def add(self, *videos):
        for i in videos:
            if self.videos:
                for z in self.videos:
                    if i == z:
                        return
                    else:
                        self.videos.append(i)
                        return
            else:
                self.videos.append(i)


    def get_videos(self, search_word):
        result = []
        for video in self.videos:
            if search_word.lower() in video.title.lower():
                result.append(video)

        return result

    def watch_video(self, film_name):
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return

        for video in self.videos:
            if video == film_name:
                found_video = video
                if found_video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return

                for second in range(found_video.time_now, found_video.duration):
                    print(second + 1, end=' ')
                    found_video.time_now = second + 1
                    time.sleep(0.5)
                print('Конец видео')


