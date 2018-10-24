from py2neo import Graph
class MovieLens():
    def __init__(self, host):
        self.graph = Graph(f"bolt://{host}")

    def find_movies_by_name(self, name, case_insensitive=True, limit=10):
        return self.graph.run(f"""MATCH (movie:Movie)
            WHERE movie.title =~ '{"(?i)" if case_insensitive else ""}.*{name}.*'
            RETURN movie.title as title, movie.movieId as movieId
            LIMIT {limit}""").data()

    def find_movie_by_id(self, movieId):
        return self.graph.run(f"""PROFILE MATCH (m:Movie)-[r]-()
            WHERE m.movieId = '{movieId}'
            RETURN m.movieId as movieId, m.title as title, 
            avg(r.rating) as average_rate, count(r) as count""").data()

    def recommendation(self, movieIds, rating=3.5, count=4, limit=5):
        return self.graph.run(f"""MATCH (m:Movie)-[r1]-(u)-[r]-(m2)
            WHERE m.movieId IN {movieIds} AND r1.rating > {rating}
            WITH count(*) as cnt, avg(r.rating) as rate, m2
            WHERE rate > {rating} AND cnt > {count}
            RETURN DISTINCT m2.movieId as movieId,
            m2.title as title, cnt as count, rate as average_rate
            ORDER BY cnt DESC, rate DESC LIMIT 10""").data()


