import requests_with_caching
import json

#The first function should interact with the TasteDive API to obtain all data for a list of 5 movies related to the input
def get_movies_from_tastedive(titleorName):
    baseURL = 'https://tastedive.com/api/similar'
    params_d = {}
    params_d['q'] = titleorName
    params_d['type'] = 'movies'
    params_d['limit'] = 5
    tastedive_response = requests_with_caching.get(baseURL, params = params_d)
    return json.loads(tastedive_response.text)

#The second function should extract only the titles related to the original input, without the other data from the TasteDive API
def extract_movie_titles(dictionary):   
    result = [r['Name'] for r in dictionary['Similar']['Results']]
    return result

#The third function allows the user to input a list of movies, returning 5 related movies for each input with no repeats
def get_related_titles(movie_list):
    related_titles = []
    for movie in movie_list:
        related_titles.extend(extract_movie_titles(get_movies_from_tastedive(movie)))
    return(list(set(related_titles)))

#The fourth function pivots to another REST API, OMDB, to retrieve metadata like release year, ratings, plot line, etc, for one movie input by the user 
def get_movie_data(title):
    url = 'http://www.omdbapi.com/'
    parameters = {}
    parameters['t'] = title
    parameters['r'] = 'json'
    omdb_response = requests_with_caching.get(url, params = parameters)
    print(json.loads(omdb_response.text))
    return json.loads(omdb_response.text)

#The fifth function retrieves only the Rotten Tomatoes rating from the result of the previous function if there is one; if not, the function returns a 0 value
def get_movie_rating(dic):
    for r in dic['Ratings']:
        if r['Source'] == 'Rotten Tomatoes':
            return int(r['Value'][:-1])
    return 0

#The sixth function allows the user to input a list of movie titles for which they wish to view related titles sorted by their Rotten Tomatoes ranking
#The function passes the input list to the previous five functions, sorting the results in descending order of ranking with ties broken by reverse alphabetical order
def get_sorted_recommendations(list_movie_titles):
    related = get_related_titles(list_movie_titles)
    related_scores = {}
    for mov in related:
        rating = get_movie_rating(get_movie_data(mov))
        related_scores[mov] = rating
    print(related_scores)
    return [i for i in sorted(related_scores, reverse = True, key = lambda x: (related_scores[x], x))]
