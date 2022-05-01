"""
utility_functions: Contains several utility functions that can be called in the main scripts
    1. build_artists_titles_list: Builds and returns Node data for the NODES class to create nodes csv files
    2. build_artists_titles_connections_list: Builds and returns EDGE data for the EDGES class to create the edges csv file
    3. filter_live_actors: filters live artists from the python data dictionary and returns two dictionaries of live and dead artists
    4. filter_srtists_by_profession: returns data dictionary using the filter argument
    5. filter_titles_type: filters titles using the filter argument
    6. save_json: saves the python dictionary into a json file
    7. json_to_pydata: return a python datstructure from the json file
    8. filter_titles_by_years: returns filtered titles data if titles were released in the input interval
    9. make_output_directory: creates an outpur directory using inputs
"""

import json
import os
import logging


"""
configuring logger
"""
logging.basicConfig(format="%(message)s", level=logging.INFO)

def build_artists_titles_list(artists_data_path, titles_data_path, artist_profession = "", title_genre = "", add_profession_or_genre = False):
    """
    Builds and returns node dataset to be input to nodes class to create nodes
    Uses the json dataset files files created during the data preprocessing stage
    """
    data = []
    #id = 1 # deprecated algorithm 
    titles = None
    id_references = {}

    with open(titles_data_path, "r") as f:
        titles = json.load(f)

    with open(artists_data_path, 'r') as f:
        artists_data = json.load(f)
        for item in artists_data:
            artist_name = artists_data[item]['primaryName']
            if isinstance(artist_name, list):
                artist_name = "".join(artist_name)
            #print(artist_name)
            id = item
            id_references[artist_name] = id
            id_node = [id] + [artist_name]
            if add_profession_or_genre == True:
                id_node = id_node + [artist_profession]
            data.append(id_node)
            #id += 1 # deprecated algorithm
            #updated algorithms below
            known_titles = artists_data[item]['knownForTitles']
            if isinstance(known_titles, list):
                pass
            else:
                known_titles = [known_titles]
            title_added = False
            for t in known_titles:
                if t != "\\N":
                    try:
                        title_add = titles[t]
                        title_name = title_add['primaryTitle']
                        if isinstance(title_name, list):
                            title_name = "".join(title_name)
                        id = t
                        id_node = [id] + [title_name]
                        if add_profession_or_genre == True:
                            id_node = id_node + [title_genre]
                        #id += 1 # deprecated algorithm
                        title_added = True
                        data.append(id_node)
                        id_references[title_name] = id
                    except:
                        continue
            if title_added == False:
                data.pop(-1)
                #id -= 1 # deprecated algorithm
            
    """
    # deprecated algorithm
    with open(titles_data_path, 'r') as f:
        titles_basic_data = json.load(f)
        for item in titles_basic_data:
            title_primary_name = titles_basic_data[item]['primaryTitle']
            id_node = [id] + [title_primary_name]
            if add_profession_or_genre == True:
                id_node = id_node + [title_genre] # need to filter the title first by genre
            data.append(id_node)
            id += 1
    """

    return data, id_references

def build_artists_titles_connections_list(artists_data_path, titles_data_path, id_references, title_type_filter="", Type = "Undirected", weight = 1, title_type_sort = False, artist_live_sort = False):
    """
    Builds and returns data (list of lists) to be input in Edges class to create edges
    Using the json datset files created in the data preprocessing phase
    """
    data = [] #field_names = [Source, Target, Type, Weight, TitleType]
    titles_basic_data = None
    with open(titles_data_path, 'r') as titles:
        titles_basic_data = json.load(titles)

    with open(artists_data_path, "r") as artists:
        artists_data = json.load(artists)
        for item in artists_data:
            source = artists_data[item]['primaryName']
            if isinstance(source, list):
                source = "".join(source)
            live = artists_data[item]['deathYear']
            source_id = id_references[source]
            if artist_live_sort:
                if live != "\\N":
                    continue
            #targets = list(artists_data[item]['knownForTitles']) # deprecated
            targets = artists_data[item]['knownForTitles']
            if isinstance(targets, list):
                pass
            else:
                targets = [targets]
            for t in targets:
                if t != "\\N":
                    try:
                        t_data = titles_basic_data[t]
                    except:
                        continue
                    target = t_data['primaryTitle']
                    title_type = t_data['titleType']
                    if isinstance(target, list):
                        target = "".join(target)
                    target_id = id_references[target]
                    if title_type_sort:
                        if title_type_filter == title_type:
                            #row = [source] + [target] + [Type] + [weight] + [title_type] # deprecated
                            row = [source_id] + [target_id] + [Type] + [weight] + [title_type]
                            data.append(row)
                        else:
                            continue
                    else:
                        #row = [source] + [target] + [Type] + [weight] + [title_type] # deprecated
                        row = [source_id] + [target_id] + [Type] + [weight] + [title_type]
                        data.append(row)
                else:
                    continue
    return data

def filter_live_actors(artists_pydata_dict):
    """
    filters live artists from the python data dictionary
    returns live artists dict and dead actors dict
    """
    del_artists = []
    artists_pydata = artists_pydata_dict
    dead_actors_dict = {}

    for item in artists_pydata:
        artist_death_year = artists_pydata[item]['deathYear']
        if artist_death_year != "\\N":
            del_artists.append(item)
            continue

    for item in del_artists:
        dead_actors_dict[item] = artists_pydata[item]
        del artists_pydata[item]

    return artists_pydata, dead_actors_dict

def filter_artists_by_profession(data_dict, filter_profession_arg):
    """
    returns filtered data using filter profession argument
    """
    data = data_dict
    filtered_data = {}
    
    for item in data:
        professions = data[item]['primaryProfession']
        if isinstance(professions, list):
            if filter_profession_arg in professions:
                filtered_data[item] = data[item]
            else:
                continue
        else:
            if filter_profession_arg == professions:
                filtered_data[item] = data[item]
    
    return filtered_data               

def filter_titles_type(data_dict, filter_type_arg):
    """
    returns filtered data using filter titleType argument
    """
    data = data_dict
    filtered_data = {}

    for item in data:
        title_type = data[item]['titleType']
        if filter_type_arg == title_type:
            filtered_data[item] = data[item]
        else:
            continue

    return filtered_data

def save_json(data, save_path, file_name):
    """
    Saves data in a json file_name in save path
    """
    file_path = save_path + file_name
    json.dump(data, open(file_path, 'w'), indent = 4)

def json_to_pydata(json_data_path):
    """
    returns python data structure from the json file
    """
    data = None
    with open(json_data_path, "r") as f:
        data = json.load(f)
    return data

def filter_titles_by_years(data_dict, lower_limit, higher_limit):
    """
    returns filtered titles data if titles were made in the input intervals
    """
    data = data_dict
    filtered_data = {}

    for item in data:
        start_year = data[item]['startYear']
        if start_year == "\\N":
            continue
        start_year = int(start_year)
        # end_year = data[item]['endYear']
        if (start_year >= lower_limit) and (start_year < higher_limit):
            filtered_data[item] = data[item]
        else:
            continue
    return filtered_data

def make_output_directory(dir_name):
    """
    makes an output directory 'dir_name' in the currect working directory
    """
    cwd = os.getcwd()
    dir = str(dir_name)
    path = os.path.join(cwd, dir)
    output_directory_path = path
    try:
        os.mkdir(path)
    except FileExistsError:
        log = "directory already exists"
        logging.info(log) 
    logging.info(output_directory_path)