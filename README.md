# movielens-neo4j-jupyter
Ingesting 20m dataset to neo4j and displaying it to Jupyter

## How to start

1. Run `docker-compose up` and it would start building two images, 

2. See the logs that downaloading 20m movielens dataset, and ingesting it to `neo4j`, 
   it would take around 2~3 minutes.
   See datils in  [download_and_import.sh](https://github.com/tomahawk28/movielens-neo4j-jupyter/blob/master/neo4j/download_and_import.sh)
   
```
IMPORT DONE in 59s 768ms.
Imported:
  165771 nodes
  20000263 relationships
  193049 properties
Peak memory usage: 1.03 GB
```
2. After that, check the docker-compose logs of `jupyter` container which contains a URL. it looks similiar to, 
```
jupyter_notebook |     Copy/paste this URL into your browser when you connect for the first time,
jupyter_notebook |     to login with a token:
jupyter_notebook |         http://localhost:8888/?token=26a9debd07cb3fa21757cad23e69fb41a85753f3f6bc59d9
```
3. Connect to [`./jupyter/data/Movielens - Storytelling.ipynb`](https://github.com/tomahawk28/movielens-neo4j-jupyter/blob/master/jupyter/data/Movielens%20-%20Storytelling.ipynb) and verify it works. 

4. Now you can use the list of method. 
```
MovieLens.find_movies_by_name
MovieLens.find_movie_by_id
MovieLens.recommendation
```

Please check jupyter notebook file about sample usage.
