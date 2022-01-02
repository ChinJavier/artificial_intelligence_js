import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

# data inicial dada por el problema
DATA = np.array([
    [8, 2],
    [9, 7],
    [2, 12],
    [9, 1],
    [10, 7],
    [3, 14],
    [8, 1],
    [1, 13],
])

# 1ra iteracion
# CENTROID = np.array([
#     [10,7],
# ])
# kmeans = KMeans(n_clusters=1, init=CENTROID, n_init=1)
# kmeans.fit(DATA)

# 2da iteracion
# CENTROID = np.array([
#     [10,7],
#     [6.25,7.125],
# ])
# kmeans = KMeans(n_clusters=2, init=CENTROID, n_init=1)
# kmeans.fit(DATA)

# 3ra iteracion
# CENTROID = np.array([
#     [6.25, 7.125],
#     [8.8, 3.6],
#     [2,  13]
# ])
# kmeans = KMeans(n_clusters=3, init=CENTROID, n_init=1)
# kmeans.fit(DATA)


# kMeans con clustering
kmeans = KMeans(n_clusters=3)
kmeans.fit(DATA)

# grafica los puntos de la data
plt.scatter(DATA[:, 0], DATA[:, 1], c=kmeans.labels_, cmap="rainbow")

# grafica los centroides del conjunto de datos
plt.scatter(kmeans.cluster_centers_[:, 0],
            kmeans.cluster_centers_[:, 1],
            color="black"
            )

# imprimimos los centroides
print(kmeans.cluster_centers_)

# imprimo las predicciones
predicts = kmeans.predict(DATA)
print(predicts)

print("-----------------------------")

# imprimo las clases 
for x,y in enumerate(kmeans.labels_):
    print(DATA[x])

plt.show()
