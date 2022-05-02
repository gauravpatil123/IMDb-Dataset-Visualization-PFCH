# IMDb-Dataset-Visualization-PFCH
Network Graph Visualization created from the IMDb datasets

**Contents**
- About
- Datasets
- Classes
- Scripts
- Executables
- Outputs
  1. Actors Movie 2021-2022
  2. Actresses Movie 2021-2022
  3. Directors Movie 2021-2022
  4. Writers Movie 2021-2022

**About**

**Datasets**

**Classes**
- nodes: Contains Class CreateNodes to create the nodes csv output to be used in Gephi for graph visualization
- edges: Contains Class CreateEdges to create the edges csv output to be used in Gephi for graph visualization
- dataset_processing: Contains Class DatasetProcessing to construct custom datastructures from the IMDb datasets  

**Scripts**
- utility_functions: Contains several utility functions including fucntions to be used for data sorting, filtering, munging and dumping. 

**Executables**
- main: Initializaes the the global variables and data paths, prcesses datasets using the datasetProcessing class, Filters and extracts data and constructs custom datastructures using utility fucntions, Creates the Nodes and Edges csv files to be used as input for Gephi to create dataset Visualizations

**Outputs**
