from random import Random
from model.centroid import Centroid

MIN_COLOR_VALUE = 0
MAX_COLOR_VALUE = 256


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
            for r in range(MAX_COLOR_VALUE):
                for g in range(MAX_COLOR_VALUE):
                    for b in range(MAX_COLOR_VALUE):
                        value = value_space[r][g][b]
                        if value != 0:
                            self.fight_for_point([r, g, b], value)

            changed = False
            for centroid in self._centroids:
                print "Prev Value: %s" % (centroid)
                centroid.calculate_new_pos()
                print "Current Value: %s" % (centroid)
                changed = changed or centroid.pos_changed

            if not changed:
                count += 1
            else:
                count = 0

    def fight_for_point(self, point, point_value):
        closest_centroid = None
        closest_centroid_dist = None

        print "Fighting for point. Point %s, Value: %s" % (point, point_value)

        for centroid in self._centroids:
            dist = self.euclidean_distance(centroid.pos, point)
            if closest_centroid_dist is None or dist < closest_centroid_dist:
                closest_centroid_dist = dist
                closest_centroid = centroid

        for i in range(point_value):
            closest_centroid.add_item(point)

    def euclidean_distance(self, p1, p2):
        if len(p1) != len(p2):
            raise ArithmeticError("p1 and p2 lengths must be equal")

        length = len(p1)
        total = 0
        for i in range(length):
            total += (p1[i] - p2[i]) ** 2

        return total // 2

    def generate_centroid(self):
        random = Random()
        centroids = []
        for i in range(self.k):
            r = random.randint(MIN_COLOR_VALUE, MAX_COLOR_VALUE)
            g = random.randint(MIN_COLOR_VALUE, MAX_COLOR_VALUE)
            b = random.randint(MIN_COLOR_VALUE, MAX_COLOR_VALUE)
            centroids.append(Centroid([r, g, b]))
        return centroids
