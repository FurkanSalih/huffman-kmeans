from random import Random
from model.centroid import Centroid

MIN_COLOR_VALUE = 0
MAX_COLOR_VALUE = 255


class KMeans(object):

    """docstring for KMeans"""

    def __init__(self, k=2, done_count=2):
        self.k = k
        self.done_count = done_count
        self._result = None
        self._centroids = None

    def calculate(self, value_space):
        count = 0
        self._centroids = self.generate_centroid()

        while count < self.done_count:
            print "Calculating"
            count += 1
        print "Done"

    def generate_centroid(self):
        random = Random()
        centroids = []
        for i in range(self.k):
            r = random.randint(MIN_COLOR_VALUE, MAX_COLOR_VALUE)
            g = random.randint(MIN_COLOR_VALUE, MAX_COLOR_VALUE)
            b = random.randint(MIN_COLOR_VALUE, MAX_COLOR_VALUE)
            centroids.append(Centroid([r, g, b]))
        return centroids


if __name__ == '__main__':
    km = KMeans()
    centroids = km.generate_centroid()
    km.calculate([])
    print centroids[0]
