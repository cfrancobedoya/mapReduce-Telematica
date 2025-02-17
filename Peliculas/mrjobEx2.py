from mrjob.job import MRJob
from mrjob.step import MRStep

class procesar(MRJob):
# B -> Dia en que mas peliculas se han visto

    def mapper1(self, _, line):
        user_id,movie_id,rating,genre,date = line.split(',')
        yield date, 1

    def reducer1(self, date, values):
        moviesCont = 0

        for value in values:
            moviesCont += 1

        yield 1, (moviesCont, date)

    def reducer2(self, date, values):
        max_day = max(values)
        print max_day



    def steps(self):
        return [
           MRStep(mapper=self.mapper1, reducer=self.reducer1), MRStep(reducer=self.reducer2)]

if __name__ == '__main__':
    procesar.run()
