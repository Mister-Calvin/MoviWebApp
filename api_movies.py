import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
API_KEY = "63475212"



def search_movie_and_get_movies(search_movie):
    """
    :param search_movie: user-input search movie name
    :return: returns a list of dictionaries containing movie details
    """
    try:
        url = f"http://www.omdbapi.com/?apikey={API_KEY}&t={search_movie}"
        response = requests.get(url)
        movies_as_json = response.json()
        return movies_as_json
    except KeyError:
        print("Key not found.")
    except requests.exceptions.ConnectionError:
        print("No connection to the API (ConnectionError).")
    except requests.exceptions.Timeout:
        print("API request took too long (Timeout).")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP-Error: {e.response.status_code}")

print(search_movie_and_get_movies("Avatar"))

movie = search_movie_and_get_movies("Avatar")
print(movie["Title"])

