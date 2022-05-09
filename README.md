# IMDb-Dataset-Visualization-PFCH
Network Graph Visualization created from the IMDb datasets

**Contents**
- About
- Datasets
- Classes
- Scripts
- Executables
- Outputs
  1. Actors-Movies-2021-2022
  2. Actresses-Movie-2021-2022
  3. Directors-Movie-2021-2022
  4. Writers-Movie-2021-2022

**About**</br>
I have constructed network graph of different professions and movies during the
year 2021-2022. The professions include Actor, Actresses, Directors and Writers.
Once the graphs were constructed I dumped them to the csv files and used Gephi
to create network graph visualizations from the csv files.
The constructed data and the created visualizations are stored in the Data
directory

*To execute the program run the main.py script*

**Datasets**</br>
I used the datasets from the IMDb Api. The documentation and download links for
the datasets are as follows:
- [Documentation URL](https://www.imdb.com/interfaces/)
- [Download URL](https://datasets.imdbws.com)

**Classes**
- **nodes**: Contains Class CreateNodes to create the nodes csv output to be used in Gephi for graph visualization
- **edges**: Contains Class CreateEdges to create the edges csv output to be used in Gephi for graph visualization
- **dataset_processing**: Contains Class DatasetProcessing to construct custom datastructures from the IMDb datasets  

**Scripts**
- **utility_functions**: Contains several utility functions including fucntions to be used for data sorting, filtering, munging and dumping. 

**Executables**
- **main**: Initializaes the the global variables and data paths, prcesses datasets using the datasetProcessing class, Filters and extracts data and constructs custom datastructures using utility fucntions, Creates the Nodes and Edges csv files to be used as input for Gephi to create dataset Visualizations

**Outputs**
- Actor-Movies-2021-2022
  1. [High-Def PDF](https://github.com/gauravpatil123/IMDb-Dataset-Visualization-PFCH/blob/main/Data/Visualizations/Actor_Movies_2021_2022_D_Labels.pdf)
  2. 4K Image:
  <img src="Data/Visualizations/Actor_Movies_2021_2022_D_Labels_4K.png" width=1000>
- Actresses-Movies-2021-2022
  1. [High-Def PDF](https://github.com/gauravpatil123/IMDb-Dataset-Visualization-PFCH/blob/main/Data/Visualizations/Actress_Movies_2021_2022_C_Labels.pdf)
  2. 11K Image:
  <img src="Data/Visualizations/Actress_Movies_2021_2022_C_Labels_11K.png" width=1000>
- Directors-Movies-2021-2022
  1. [High-Def PDF](https://github.com/gauravpatil123/IMDb-Dataset-Visualization-PFCH/blob/main/Data/Visualizations/Directors_movies_2021_2022_D_Labels.pdf)
  2. 12K Image:
  <img src="Data/Visualizations/Directors_movies_2021_2022_D_Labels_12K.png" width=1000>
- Writers-Movies-2021-2022
  1. [High-Def PDF](https://github.com/gauravpatil123/IMDb-Dataset-Visualization-PFCH/blob/main/Data/Visualizations/Writers_movies_2021_2022_B_Labels.pdf)
  2. 12K Image:
  <img src="Data/Visualizations/Writers_movies_2021_2022_B_Labels_12K.png" width=1000>
