# movielens-neo4j-jupyter
Ingesting 20m dataset to neo4j and displaying it to Jupyter

## How to start

1. Run `docker-compose up` and it would start downaload 20m movielens dataset, and ingesting it to `neo4j`
2. After that, check the logs of `jupyter` container which contains a URL. 
3. Connect to `./jupyter/data/Movielens - Storytelling.ipynb` and verify it works. 
