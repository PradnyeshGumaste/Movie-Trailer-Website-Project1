import webbrowser

class Movie():
    """
    The Movie class initialized above allows the user to use the constructor
    and instantiate different movies( i.e objects) in the entertainment_center.py
    and cretes a website displaying the movies along with its trailers
    """

    def __init__(self,title,storyline,poster_image_url,trailer_youtube_url):

        """
        __init__ constructor allocates memory and initializes the new movie object
        The parameters passed inside are
        movie_title = Name of the movie
        movie_storyline = Brief one-line description of the movie
        poster_image = Poster art of the movie
        trailer_youtube = The Official trailer of movie
        """

        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_movie(self):

        """
        show_movie() plays the trailer of the movie
        """
        ffpath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'
        wb.register('chrome', None, wb.BackgroundBrowser(ffpath), 1)
        chrome = wb.get('chrome')
        chrome.open(self.trailer_youtube)
