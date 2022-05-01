"""
main:
    1. Intializes dataset paths, global variables and global logs
    2. Configures Logger
    3. Phase One : Data Preprocessing
    4. Phase Two : Data Filtering & Extraction
    5. Phase Three : Creating Graphs
"""

from dataset_processing import DatasetProcessing as DP
from nodes import CreateNodes as CN
from edges import CreateEdges as CE
from utility_functions import json_to_pydata as jpd
from utility_functions import filter_live_actors as fla
from utility_functions import save_json as sj
from utility_functions import filter_artists_by_profession as fa
from utility_functions import filter_titles_type as ft
from utility_functions import build_artists_titles_list as batl
from utility_functions import build_artists_titles_connections_list as batcl
from utility_functions import filter_titles_by_years as ftby
from utility_functions import make_output_directory as mod
import logging
import os


"""
Dataset Paths, Global Variables & Global Logs
"""
DATASET_BASE_DIR = "Data/IMDb datasets/"
NAMES_DATASET = "name_basics.tsv"
TITLES_BASIC_DATASET = "title_basics.tsv"
TITLES_CREW_DATASET = "title_crew.tsv"
TITLES_RATINGS_DATASET = "title_ratings.tsv"
SAVE_PATH = "Data/Constructed Datasets/"
CONSTRUCTED_DATA_PATH = "Data/Constructed Datasets/"
ARTISTS_DATASET_JSON = "artists_data.json"
TITLES_BASIC_DATASET_JSON = "titles_basic_data.json"
ACTORS_LIVE_DATASET_JSON = "actors_live_data.json"
ACTRESS_LIVE_DATASET_JSON = "actress_live_data.json"
ACTORS_DEAD_DATASET_JSON = "actors_dead_data.json"
ACTRESS_DEAD_DATASET_JSON = "actress_dead_data.json"
TITLES_BASIC_MOVIE_DATASET_JSON = "titles_basic_movie_data.json"
DIRECTORS_LIVE_DATASET_JSON = "director_live_data.json"
DIRECTORS_DEAD_DATASET_JSON = "director_dead_data.json"
WRITERS_LIVE_DATASET_JSON = "writer_live_data.json"
WRITERS_DEAD_DATASET_JSON = "writer_dead_data.json"
START_YEAR = "2021" # change according to need
END_YEAR = "2022"   # change according to need
SEPERATOR_LOG = "############################"
SEPERATOR_DASH = "----------------------------"

"""
configuring logger
"""
logging.basicConfig(format="%(message)s", level=logging.INFO)

if __name__ == '__main__':   

    ##############################
    """
    Phase One : Data Preprocessing
    """
    logging.info(SEPERATOR_LOG)
    phase_one_start = "Starting Phase One: Data Preprocessing"
    logging.info(phase_one_start)
    logging.info(SEPERATOR_LOG)

    # checking if data set directories exist using os module
    creating_directories_message = "Creating Driectory for datasets"
    logging.info(creating_directories_message)
    mod(CONSTRUCTED_DATA_PATH)
    logging.info(SEPERATOR_LOG)

    # Processing IMDb tsv Datasets into JSON files
    log  = "Processing the names_basic.tsv --> artists_data.json"
    logging.info(log)
    names_data = DP(DATASET_BASE_DIR, NAMES_DATASET)
    names_data()
    names_data.save_data(SAVE_PATH, "artists_data.json")
    log = f"artists_data.json created and saved in {CONSTRUCTED_DATA_PATH}"
    logging.info(log)

    log = "Processing the titles_basic.tsv --> titles_basic_data.json"
    logging.info(log)
    titles_basic_data = DP(DATASET_BASE_DIR, TITLES_BASIC_DATASET)
    titles_basic_data()
    titles_basic_data.save_data(SAVE_PATH, "titles_basic_data.json")
    log = f"titles_basic_data.json created and saved in {CONSTRUCTED_DATA_PATH}"
    logging.info(log)

    log = "Processing the titles_crew.tsv --> titless_crew_data.json"
    logging.info(log)
    titles_crew_data = DP(DATASET_BASE_DIR, TITLES_CREW_DATASET)
    titles_crew_data()
    titles_crew_data.save_data(SAVE_PATH, "titles_crew_data.json")
    log = f"titles_crew_data.json created and saved in {CONSTRUCTED_DATA_PATH}"
    logging.info(log)

    log = f"Processing the title_ratings.tsv --> titless_ratings_data.json"
    logging.info(log)
    titles_ratings_data = DP(DATASET_BASE_DIR, TITLES_RATINGS_DATASET)
    titles_ratings_data()
    titles_ratings_data.save_data(SAVE_PATH, "titles_ratings_data.json")
    log = f"titles_ratings_data.json created and saved in {CONSTRUCTED_DATA_PATH}"
    logging.info(log)
    logging.info(SEPERATOR_LOG)

    #########################################
    """
    Phase Two : Data Filtering and Extarction
    """

    phase_two_start = "Starting phase two: Data filtering and extraction"
    logging.info(phase_two_start)
    logging.info(SEPERATOR_LOG)

    log = "filtering live and dead artists datasets from artists_data.json"
    logging.info(log)
    artists_data_path = CONSTRUCTED_DATA_PATH + ARTISTS_DATASET_JSON
    artist_py_data = jpd(artists_data_path)
    live_artists, dead_artists = fla(artist_py_data)
    sj(live_artists, SAVE_PATH, 'artists_live_data.json')
    sj(dead_artists, SAVE_PATH, 'artists_dead_data.json')
    log = f"filtered artists datasets are created and saved in {CONSTRUCTED_DATA_PATH}"
    logging.info(log)
    logging.info(SEPERATOR_DASH)

    log = "filtering 'actors' from artists datasets"
    logging.info(log)
    live_actors = fa(live_artists, "actor")
    dead_actors = fa(dead_artists, "actor")
    logging.info(SEPERATOR_DASH)
    
    log = "filtering 'actresses' from artists datasets"
    logging.info(log)
    live_actress = fa(live_artists, "actress")
    dead_actress = fa(dead_artists, "actress")
    logging.info(SEPERATOR_DASH)

    log = "filtering 'directors' from artists datasets"
    logging.info(log)
    live_directors = fa(live_artists, "director")
    dead_directors = fa(dead_artists, "director")
    logging.info(SEPERATOR_DASH)
    
    log = "filtering 'writers' from artists datasets"
    logging.info(log)
    live_writers = fa(live_artists, "writer")
    dead_writers = fa(dead_artists, "writer")
    logging.info(SEPERATOR_DASH)
    
    log = "Saving filtered datasets to json files"
    logging.info(log)
    sj(live_actors, SAVE_PATH, 'actors_live_data.json')
    sj(dead_actors, SAVE_PATH, 'actors_dead_data.json')
    sj(live_actress, SAVE_PATH, 'actress_live_data.json')
    sj(dead_actress, SAVE_PATH, 'actress_dead_data.json')
    sj(live_directors, SAVE_PATH, 'director_live_data.json')
    sj(dead_directors, SAVE_PATH, 'director_dead_data.json')
    sj(live_writers, SAVE_PATH, 'writer_live_data.json')
    sj(dead_writers, SAVE_PATH, 'writer_dead_data.json')
    logging.info(SEPERATOR_DASH)
    
    log = "filtering movies from all titles dataset"
    logging.info(log)
    titles_data_path = CONSTRUCTED_DATA_PATH + TITLES_BASIC_DATASET_JSON
    titles_py_data = jpd(titles_data_path)
    titles_movies = ft(titles_py_data, "movie")
    sj(titles_movies, SAVE_PATH, 'titles_basic_movie_data.json')
    log = f"movies filtered and saved as titles_basic_movie_data.json in {CONSTRUCTED_DATA_PATH}"
    logging.info(log)
    logging.info(SEPERATOR_DASH)

    """
    Movie filter by years json
    """
    titles_movies_2012_2022 = ftby(titles_movies, 2012, 2022) # deprecated
    sj(titles_movies_2012_2022, SAVE_PATH, 'titles_basic_movie_data_2012_2022.json') # deprecated

    log = "filtering movies released during 2021 - 2022"
    logging.info(log)
    titles_movies_2021_2022 = ftby(titles_movies, 2021, 2022)
    sj(titles_movies_2021_2022, SAVE_PATH, 'titles_basic_movie_data_2021_2022.json')
    log = f"filtered movies data saved in {CONSTRUCTED_DATA_PATH}"
    logging.info(log)
    logging.info(SEPERATOR_LOG)

    ################################################
    """
    Phase Three : Creating graphs for 2021 - 2022 Movies
    """

    phase_three_start = "Starting phase three: Graph creation for 2021 - 2022 Movies"
    logging.info(phase_three_start)
    logging.info(SEPERATOR_LOG)
    
    """
    Actors - live
    """
    #NODES
    START_YEAR = "2021"
    END_YEAR = "2022"
    log = f"Starting to create Nodes for actors in years {START_YEAR} to {END_YEAR}"
    logging.info(log)
    TITLES_BASIC_MOVIE_DATASET_DECADE_JSON = f"titles_basic_movie_data_{START_YEAR}_{END_YEAR}.json"
    titles_movie_data_decade_path = CONSTRUCTED_DATA_PATH + TITLES_BASIC_MOVIE_DATASET_DECADE_JSON
    field_names_nodes = ['Id', 'Label', 'NodeType']
    profession = "actor"
    artist_age_filter = "live"
    save_filename_decade = f"{profession}_{artist_age_filter}_titles_{START_YEAR}_{END_YEAR}_nodes.csv"
    
    actors_live_data_path = CONSTRUCTED_DATA_PATH + ACTORS_LIVE_DATASET_JSON
    actors_live_title_decade_nodes, actors_live_title_decade_nodes_id_references = batl(actors_live_data_path, titles_movie_data_decade_path, "actor", "movie", True)
    actors_id_reference_filename = "actors_id.json"
    sj(actors_live_title_decade_nodes_id_references, SAVE_PATH, actors_id_reference_filename)
    create_actors_live_title_decade_nodes = CN(field_names_nodes, actors_live_title_decade_nodes)
    create_actors_live_title_decade_nodes(SAVE_PATH, save_filename_decade)
    log = f"Actor nodes created and saved in {CONSTRUCTED_DATA_PATH}"
    logging.info(log)
    logging.info(SEPERATOR_DASH)

    #EDGES
    log = "Starting to create Edges for the Actor Nodes"
    logging.info(log)
    field_names_edges = ['Source', 'Target', 'Type', 'Weight', 'TitleType']
    save_filename_decade_edges = f"{profession}_{artist_age_filter}_titles_edges_movies_{START_YEAR}_{END_YEAR}.csv"
    actors_live_titles_movie_decade_edges = batcl(actors_live_data_path, titles_movie_data_decade_path, actors_live_title_decade_nodes_id_references,title_type_filter="movie", title_type_sort=True)
    create_actors_live_title_decade_edges = CE(field_names_edges, actors_live_titles_movie_decade_edges)
    create_actors_live_title_decade_edges(SAVE_PATH, save_filename_decade_edges)
    log = f"Actor edges created and saved in {CONSTRUCTED_DATA_PATH}"
    logging.info(log)
    logging.info(SEPERATOR_DASH)

    """
    actress - live
    """
    #Nodes
    START_YEAR = "2021"
    END_YEAR = "2022"
    log = f"Starting to create Nodes for actress in years {START_YEAR} to {END_YEAR}"
    logging.info(log)
    profession = "actress"
    artist_age_filter = "live"
    save_filename_decade = f"{profession}_{artist_age_filter}_titles_{START_YEAR}_{END_YEAR}_nodes.csv"

    actress_live_data_path = CONSTRUCTED_DATA_PATH + ACTRESS_LIVE_DATASET_JSON
    actress_live_title_decade_nodes, actress_live_title_decade_nodes_id_references = batl(actress_live_data_path, titles_movie_data_decade_path, "actress", "Movie", True)
    actress_id_reference_filename = "actress_id.json"
    sj(actress_live_title_decade_nodes_id_references, SAVE_PATH, actress_id_reference_filename)
    create_actress_live_title_decade_nodes = CN(field_names_nodes, actress_live_title_decade_nodes)
    create_actress_live_title_decade_nodes(SAVE_PATH, save_filename_decade)
    log = f"Actress nodes created and saved in {CONSTRUCTED_DATA_PATH}"
    logging.info(log)
    logging.info(SEPERATOR_DASH)

    #Edges
    log = "Starting to create Edges for the Actress Nodes"
    logging.info(log)
    save_filename_decade_edges = f"{profession}_{artist_age_filter}_titles_edges_movies_{START_YEAR}_{END_YEAR}.csv"
    actress_live_titles_movie_decade_edges = batcl(actress_live_data_path, titles_movie_data_decade_path, actress_live_title_decade_nodes_id_references,title_type_filter="movie", title_type_sort=True)
    create_actress_live_title_decade_edges = CE(field_names_edges, actress_live_titles_movie_decade_edges)
    create_actress_live_title_decade_edges(SAVE_PATH, save_filename_decade_edges)
    log = f"Actress edges created and saved in {CONSTRUCTED_DATA_PATH}"
    logging.info(log)
    logging.info(SEPERATOR_DASH)

    """
    Directors - live
    """
    #Nodes
    START_YEAR = "2021"
    END_YEAR = "2022"
    log = f"Starting to create Nodes for directors in years {START_YEAR} to {END_YEAR}"
    logging.info(log) 
    TITLES_BASIC_MOVIE_DATASET_DECADE_JSON = f"titles_basic_movie_data_{START_YEAR}_{END_YEAR}.json"
    titles_movie_data_decade_path = CONSTRUCTED_DATA_PATH + TITLES_BASIC_MOVIE_DATASET_DECADE_JSON
    field_names_nodes = ['Id', 'Label', 'NodeType']
    profession = "director"
    artist_age_filter = "live"
    save_filename_decade = f"{profession}_{artist_age_filter}_titles_{START_YEAR}_{END_YEAR}_nodes.csv"

    directors_live_data_path = CONSTRUCTED_DATA_PATH + DIRECTORS_LIVE_DATASET_JSON
    directors_live_title_decade_nodes, directors_live_title_decade_nodes_id_references = batl(directors_live_data_path, titles_movie_data_decade_path, "director", "movie", True)
    directors_id_reference_filename = "directors_id.json"
    sj(directors_live_title_decade_nodes_id_references, SAVE_PATH, directors_id_reference_filename)
    create_directors_live_title_decade_nodes = CN(field_names_nodes, directors_live_title_decade_nodes)
    create_directors_live_title_decade_nodes(SAVE_PATH, save_filename_decade)
    log = f"Directors nodes created and saved in {CONSTRUCTED_DATA_PATH}"
    logging.info(log)
    logging.info(SEPERATOR_DASH)

    #Edges
    log = "Starting to create Edges for the directors Nodes"
    logging.info(log)
    field_names_edges = ['Source', 'Target', 'Type', 'Weight', 'TitleType']
    save_filename_decade_edges = f"{profession}_{artist_age_filter}_titles_edges_movies_{START_YEAR}_{END_YEAR}.csv"
    directors_live_titles_movie_decade_edges = batcl(directors_live_data_path, titles_movie_data_decade_path, directors_live_title_decade_nodes_id_references,title_type_filter="movie", title_type_sort=True)
    create_directors_live_title_decade_edges = CE(field_names_edges, directors_live_titles_movie_decade_edges)
    create_directors_live_title_decade_edges(SAVE_PATH, save_filename_decade_edges)
    log = f"Directors edges created and saved in {CONSTRUCTED_DATA_PATH}"
    logging.info(log)
    logging.info(SEPERATOR_DASH)

    """
    Writers - live
    """
    #Nodes
    START_YEAR = "2021"
    END_YEAR = "2022"
    log = f"Starting to create Nodes for writers in years {START_YEAR} to {END_YEAR}"
    logging.info(log) 
    TITLES_BASIC_MOVIE_DATASET_DECADE_JSON = f"titles_basic_movie_data_{START_YEAR}_{END_YEAR}.json"
    titles_movie_data_decade_path = CONSTRUCTED_DATA_PATH + TITLES_BASIC_MOVIE_DATASET_DECADE_JSON
    field_names_nodes = ['Id', 'Label', 'NodeType']
    profession = "writer"
    artist_age_filter = "live"
    save_filename_decade = f"{profession}_{artist_age_filter}_titles_{START_YEAR}_{END_YEAR}_nodes.csv"

    writers_live_data_path = CONSTRUCTED_DATA_PATH + WRITERS_LIVE_DATASET_JSON
    writers_live_title_decade_nodes, writers_live_title_decade_nodes_id_references = batl(writers_live_data_path, titles_movie_data_decade_path, "writer", "movie", True)
    writers_id_reference_filename = "writers_id.json"
    sj(writers_live_title_decade_nodes_id_references, SAVE_PATH, writers_id_reference_filename)
    create_writers_live_title_decade_nodes = CN(field_names_nodes, writers_live_title_decade_nodes)
    create_writers_live_title_decade_nodes(SAVE_PATH, save_filename_decade)
    log = f"Writers nodes created and saved in {CONSTRUCTED_DATA_PATH}"
    logging.info(log)
    logging.info(SEPERATOR_DASH)

    #Edges
    log = "Starting to create Edges for the writers Nodes"
    logging.info(log)
    field_names_edges = ['Source', 'Target', 'Type', 'Weight', 'TitleType']
    save_filename_decade_edges = f"{profession}_{artist_age_filter}_titles_edges_movies_{START_YEAR}_{END_YEAR}.csv"
    writer_live_titles_movie_decade_edges = batcl(writers_live_data_path, titles_movie_data_decade_path, writers_live_title_decade_nodes_id_references, title_type_filter="movie", title_type_sort=True)
    create_writers_live_title_decade_edges = CE(field_names_edges, writer_live_titles_movie_decade_edges)
    create_writers_live_title_decade_edges(SAVE_PATH, save_filename_decade_edges)
    log = f"Writers edges created and saved in {CONSTRUCTED_DATA_PATH}"
    logging.info(log)
    logging.info(SEPERATOR_LOG)
