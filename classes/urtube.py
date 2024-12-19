import time

from user import User
from video import Video


class UrTube:
    def __init__(self):
        self.videos = []
        self.users = []
        self.current_user = None

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
            print(f'Successful registration! \nCurrent user: {self.current_user}\n')
        else:
            print(f'User {nickname} already exists')

    def log_out(self):
        if self.current_user:
            print(f'{self.current_user} log out\n')
            self.current_user = None

    def add(self, *videos):
        for i in videos:
            if self.videos:
                for z in self.videos:
                    if i == z:
                        print('Такой фильм есть в списке!')
                        return
                    else:
                        self.videos.append(i)
                        return
            else:
                print(f'Film {i} add')
                self.videos.append(i)


    def get_videos(self, search_word):
        result = []
        for video in self.videos:
            if search_word.lower() in video.title.lower():
                result.append(video)

        if result:
            for i in result:
                print(i)

    def watch_video(self, film_name):
        if self.current_user is None:
            print("Log in to watch the video")
            return

        found_video = None
        for video in self.videos:
            if video.title == film_name:
                found_video = video
                break

        if not found_video:
            return

        if found_video.adult_mode and self.current_user.age < 18:
            print("You are under 18 years old, please leave the page")
            return

        for second in range(found_video.time_now, found_video.duration):
            print(f"Просмотр на секунде: {second}")
            found_video.time_now = second + 1
            time.sleep(0.1)
        found_video.time_now = 0


