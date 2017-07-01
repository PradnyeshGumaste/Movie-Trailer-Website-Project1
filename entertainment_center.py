import media
import fresh_tomatoes
import json
import requests

MOVIE_URL = "https://api.themoviedb.org/3/movie/"
LANG = "&language=en-US"



def fetch_video_url(movie_id,api_key):
    """
    Takes in Movie Id and api key, and finds the video URL related to movie.
    """

    # Append youtube URL to the key
    TRAILER_URL = "https://www.youtube.com/watch?v="

    # Find the key from TMDB
    con = requests.get(MOVIE_URL + str(movie_id) +
                              "/videos?api_key=" + api_key + LANG)
    parsed_json_file = json.loads(con.text)
    con.close()

    # Return Result
    return TRAILER_URL + parsed_json_file['results'][0]['key']



def fetch_poster_image(movie_id,api_key):
    """
    This function takes the Movie id and api key as input and finds the poster image related to the movie
    """

    POSTER_URL = "https://image.tmdb.org/t/p/original/"

    con = requests.get(MOVIE_URL + str(movie_id) + "?api_key=" +
                                api_key + LANG)
    parsed_json_file = json.loads(con.text)
    con.close()
    return POSTER_URL + parsed_json_file['poster_path']



def get_movie_details(movie_id,api_key):
    """
    This function fetches all the data of the movie and returns the data in the form of
    media.Movie() so that it can be directly stored into the movie variable Name
    """


    con = requests.get(MOVIE_URL + str(movie_id) + "?api_key=" +
                                api_key + LANG)
    parsed_json_file = json.loads(con.text)
    con.close()

    title = parsed_json_file['title']
    story_line = parsed_json_file['overview']
    img_url = fetch_poster_image(parsed_json_file['id'],api_key)
    video_url = fetch_video_url(parsed_json_file['id'],api_key)

    return media.Movie(title,story_line,img_url,video_url)



Wonder_Woman =  get_movie_details("tt0451279","816d28a515c3309f8986ed251ad27336") #**Replace API key here

Transformer_The_Last_Knight = get_movie_details("tt3371366","816d28a515c3309f8986ed251ad27336")  #**Replace API key here

Spiderman_Homecoming = get_movie_details("tt2250912","816d28a515c3309f8986ed251ad27336")  #**Replace API key here

Justice_League = get_movie_details("tt0974015","816d28a515c3309f8986ed251ad27336")  #**Replace API key here

The_Dark_Tower = get_movie_details("tt1648190","816d28a515c3309f8986ed251ad27336")  #**Replace API key here

Star_Wars_The_Last_Jedi = get_movie_details("tt2527336","816d28a515c3309f8986ed251ad27336")  #**Replace API key here

The_Mummy = get_movie_details("tt2345759","816d28a515c3309f8986ed251ad27336")  #**Replace API key here

Cars3 = get_movie_details("tt3606752","816d28a515c3309f8986ed251ad27336")  #**Replace API key here


movies = [Wonder_Woman,Transformer_The_Last_Knight,Spiderman_Homecoming,Justice_League,The_Dark_Tower,Star_Wars_The_Last_Jedi,The_Mummy,Cars3]

fresh_tomatoes.open_movies_page(movies)
