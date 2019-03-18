import webbrowser

class Video():
    #Essa classe construtora irá criar toda a base para ser adcionado os filmes mais tarde.
    def __init__(self , title, duration):
        self.title = title
        self.duration = duration

class Movie(Video):
    def __init__(self,title,duration,movie_storyline,poster_image,trailer_youtube):
        Video.__init__(self,title,duration)
        self.movie_storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open (self.trailer_youtube)



class Tvshow(Video):
    def __init__(self,title,duration,season,number_of_episodes,tv_station):
        Video.__init__(self, title, duration)
        self.season = season
        self.number_of_episodes = number_of_episodes
        self.tv_station = tv_station

