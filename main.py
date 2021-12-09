import sql
from pgsql import query
import requests
import json
from datetime import datetime

#def get_movie_data(title):
    #headers = {"Authorization": "9855f49b"}
    #request_url = f"https://www.omdbapi.com/?t={title}&apikey=686eed26"
    #return requests.get(request_url, headers=headers).json()

if __name__ == '__main__':

    # get some movie data from the API
    #print(get_movie_data('WarGames'))

    #list1_titles = []
    #remove_dupe_dict = {}

    #f_read = open("datasets/json/movies.json")

    #data = json.load(f_read)

    #for i in data:
        #if i["year"] >= 2018:
            #list1_titles.append(i["title"])
        #remove_dupe_dict = list(set(list1_titles))

    #filtered_data = {}

    #for movie in list1_titles:
        #filtered_data[movie] = get_movie_data(movie)

    #f_write = open("datasets/json/filteredmovies.json", "w")
    #json.dump(filtered_data, f_write, indent=4)

    #f_read.close()
    #f_write.close()
    #print(list1_titles)
    #print(list1_titles[235])

    fm = open('datasets/json/filteredmovies.json', 'r')
    fms = fm.read()
    fm.close()
    info = json.loads(fms)
    value = "English"
    english_movies = []
    for k, v in info.items():
        for k1, v1 in v.items():
            if k1 == "Language":
                if value in v1:
                    english_movies.append(v)
    #print(len(english_movies))

    required_columns = []
    names = ["Title", "Rated", "Released", "Runtime", "Genre", "Director", "Writer", "Actors", "Plot", "Awards", "Poster"]

    for i in english_movies:
        a_subset = {key: i[key] for key in names}
        required_columns.append(a_subset)
        #print(required_columns)

    no_NA = []
    for i in required_columns:
        if "N/A" not in i.values() and (datetime.strptime(i["Released"], "%d %b %Y").year >= 2018):
            no_NA.append(i)

    for item in no_NA:
        clean_table = []
        clean_table.append(item["Title"])
        clean_table.append(item["Rated"])
        date_obj = datetime.strptime(item["Released"], "%d %b %Y")
        clean_table.append(date_obj)
        clean_table.append((item["Runtime"]).strip(" min"))
        clean_table.append(item["Genre"].split(","))
        clean_table.append(item["Director"])
        clean_table.append(item["Writer"].split(","))
        clean_table.append(item["Actors"].split(","))
        clean_table.append(item["Plot"])
        clean_table.append(item["Awards"])
        clean_table.append(item["Poster"])

        query(sql.create_insert, clean_table)

        #print(clean_table)



