import webbrowser

#   Classes construtoras que recebem os dados.
#   são chamadas no arquivo content.py


class Video():
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration


class Movie(Video):
    def __init__(self, title, duration,
                 movie_storyline, poster_image, trailer_youtube):
        Video.__init__(self, title, duration)
        self.movie_storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube)


#   Para adcionar todos as séries mais tarde.
class Tvshow(Video):
    def __init__(self, title, duration,
                 season, number_of_episodes, tv_station):
        Video.__init__(self, title, duration)
        self.season = season
        self.number_of_episodes = number_of_episodes
        self.tv_station = tv_station
