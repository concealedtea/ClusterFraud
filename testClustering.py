import pandas as pd
import numpy as np

class testClustering(): 
    def kmeans(self):
        # import data with date on top
        fileInput = r"\Users\thatq\Desktop\ML\Work\test"
        data = pd.read_csv(fileInput, sep="|", header=None, 
                         names=["UserID", "Monday", "Tuesday", "Wednesday",
                                "Thursday", "Friday", "Saturday", "Sunday"],
                                index_col=0).loc[:].values         
        centroids = []
        # creates random centroids with data lss_np, puts into centroids
        numClusters = 5
        centroids = self.randomize_centroids(data, centroids, numClusters)
        print("The total number of data instances is: " + str(len(data)))
        print("There are a total of " + str(numClusters) + " clusters")
        print("The original centroids are: " + str(centroids))   
        old_centroids = [[] for i in range(numClusters)] 
        iterations = 0
        while not (self.has_converged(centroids, old_centroids, iterations)):
            iterations += 1
            clusters = [[] for i in range(numClusters)]
            # assign data points to clusters
            clusters = self.choose_cluster(data, centroids, clusters)
            # recalculate centroids
            index = 0
            for cluster in clusters:
                old_centroids[index] = centroids[index]
                centroids[index] = np.mean(cluster, axis=0).tolist()
                index += 1
        print("The total number of iterations necessary is: " + str(iterations - 1))
        print("The clusters are as follows: \n")
        new_index = 0
        for cluster in clusters:
            print("Cluster with a size of " + str(len(cluster)) 
            + " has its center at " + str(centroids[new_index]))
            print ("Euclidean Distance for Cluster is: " + str(self.find_euclidean(cluster, centroids[new_index])) + "\n")
            new_index +=1
        print ("Total Euclidean is: " + str(self.find_total_euclid(clusters, len(data))))
        return
    
    def find_total_euclid(self, clusters, length):
        euclid = 0
        total = 0
        for cluster in clusters:
            for item in cluster:
                total += item
        totalAvg = total/ length
        for cluster in clusters:
            for item in cluster:
                euclid += totalAvg - item
        print ("Center of data is: " + str(totalAvg))
        euclidsum = 0
        for item in euclid:
            euclidsum += item
        return euclidsum
    
    def find_euclidean(self, cluster, center):
        euclidean = 0
        for item in cluster:
            euclidean += np.linalg.norm(item - center)
        return euclidean
        
    def randomize_centroids(self, data, centroids, numClusters):
        for cluster in range(0, numClusters):
            passed = False
            while not passed:
                new_clus = data[np.random.randint(0, len(data), size=1)].flatten()
                if new_clus.tolist() not in centroids:
                    passed = True
                    centroids.append(new_clus.tolist())
        return centroids
    
    def choose_cluster(self, data, centroids, clusters):
        for item in data: 
            mu_index = min([(i[0], np.linalg.norm(item - centroids[i[0]])) \
                                for i in enumerate(centroids)], key=lambda t:t[1])[0]
            clusters[mu_index].append(item)
        for cluster in clusters:
            if not cluster:
                cluster.append(data[np.random.randint(0, len(data), size=1)].flatten().tolist())
        return clusters
    
    # check if clusters have converged    
    def has_converged(self, centroids, old_centroids, iterations):
        MAX_ITERATIONS = 10
        if iterations > MAX_ITERATIONS:
            return True
        return old_centroids == centroids
    
s = testClustering()
s.kmeans()