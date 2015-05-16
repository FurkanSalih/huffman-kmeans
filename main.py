from kmeans import KMeans

import kmeans


def main():
    histogram = [[[0 for r in range(kmeans.MAX_COLOR_VALUE)]
                  for g in range(kmeans.MAX_COLOR_VALUE)]
                 for b in range(kmeans.MAX_COLOR_VALUE)]

    histogram[0][0][1] = 1
    histogram[0][255][0] = 1
    histogram[1][0][0] = 1

    km = KMeans()
    km.calculate(histogram)

    print km._centroids[0]
    print km._centroids[1]

if __name__ == '__main__':
    main()