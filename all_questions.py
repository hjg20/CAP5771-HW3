# Add import files
import pickle
import math



# -----------------------------------------------------------
def question1():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "K-means assumes that clusters will be globular. \
    Agglomerative hierarchical clustering's ability to accommodate various cluster \
    shapes and its detailed hierarchical output make it better suited for handling \
    outliers compared to K-means."

    # type: bool (True/False)
    answers["(b)"] = True

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "For Kmeans, randomized centroid selections can mean that your final clusters will \
    be different every time you run the algorithm. For agglomerative hierarchical \
    clustering, every point begins as a cluster and clusters merge due to proximity. \
    Therefore, different runs of this clustering method will always produce the same \
    clusters, given the same dataset is used. "

    # type: bool (True/False)
    answers["(c)"] = False

    # type: explanatory string (at least four words)
    answers["(c) explain"] = 'Kmeans is much faster and uses less memory than agglomerative hierarchical \
    clustering, but cannot be labeled as "the most efficient". DBSCAN can be more \
    efficient if used for non-globular shapes and when handeling outliers.'

    # type: bool (True/False)
    answers["(d)"] = False

    # type: explanatory string (at least four words)
    answers["(d) explain"] = "The standard kmeans algorithm does not involve splitting a cluster and picking \
    one of the points as a new centroid. The typical alogrithm involves randomly \
    picking centroids as intialization, computing new centroids as the mean \
    between all points chosen in the cluster, and repeating until convergence. \
    The SSE of the clustering, however, decreases little by little until it either \
    converges or is below a certian threshold."

    # type: bool (True/False)
    answers["(e)"] = True

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "Cohesion is the measure of how closely related points in a cluster are. Therefore, \
    as SSE decreases, points are closer together and cohesion increases."

    # type: bool (True/False)
    answers["(f)"] = True
    # type: explanatory string (at least four words)
    answers["(f) explain"] = "Separation is the measure of how distinct clusters are from on another, and is \
    measure by the SSB of clusters. Therefore, as SSB increases, separation increases."

    # type: bool (True/False)
    answers["(g)"] = False

    # type: explanatory string (at least four words)
    answers["(g) explain"] = "Cohesion measures the inner cluster relations, whereas separation measures how \
    separated a cluster is from other clusters. The K-means algorithm optimizes cluster assignments and by doing so \
    can increase both separation and cohesion simultaneously."

    # type: bool (True/False)
    answers["(h)"] = True

    # type: explanatory string (at least four words)
    answers["(h) explain"] = "As the kmeans alogrithm interates, cluster shapes change and can thus be smaller and \
    more concise, or be more separated from eachother. As they do so, the SSE and BSS are changed proportional to one \
    another and thus have the sum of a constant."

    # type: bool (True/False)
    answers["(i)"] = True

    # type: explanatory string (at least four words)
    answers["(i) explain"] = "Cohesion measures the inner cluster relations, whereas separation measures how \
    separated a cluster is from other clusters. If the cohesion in a cluster is \
    increased (i.e., the cluster is tightly formed around the centroid), the separation \
    (i.e., the SSB from other clusters) will increase due SSE and BSS increasing/decreasing proportional to one another."

    return answers




# -----------------------------------------------------------
def question2():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Since the distance from each cirlce is greater than the radii of each circle, \
    each cirlce will be a cluster and will have a centroid at its center."

    # type: bool (True/False)
    answers["(b)"] = False

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Since the kmeans algorithm uses euclidean distance as its metric for finding \
    clusters, the clusters will be globular and will contain points from both regions."

    # type: bool (True/False)
    answers["(c)"] = True

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "The cluster which is intialized with centroid of 12.5 will be empty due to there \
    being no points nearby to be assigned to it. 10 is closer to 7.75 than it is to \
    12.5 and 15 is closer to 17.25 than it is to 12.5."

    return answers




# -----------------------------------------------------------
def question3():
    answers = {}

    # type: a string that evaluates to a float
    answers["(a) SSE"] = "4*(R**2)"

    # type: a string that evaluates to a float
    answers["(b) SSE"] = "((a**2)+(b-R)**2)+(((a+R)**2)+(b**2))+((a**2)+(b+R)**2)+(((a-R)**2)+(b**2))"

    # type: a string that evaluates to a float
    answers["(c) SSE"] = "(2*(R/2)**2)+(2*(3*R/2)**2)+(4*(((R/2)**2)+(R**2)))"

    return answers




# -----------------------------------------------------------
def question4():
    answers = {}

    # type: int
    answers["(a) Circle (a)"] = 1

    # type: int
    answers["(a) Circle (b)"] = 1

    # type: int
    answers["(a) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "The centroid on the left has the majority of its points in A and the centroid \
    on the right has the majority of its points in C. Therefore, as the algorithm \
    iterates, each circle will have its own centroid."

    # type: int
    answers["(b) Circle (a)"] = 1

    # type: int
    answers["(b) Circle (b)"] = 1

    # type: int
    answers["(b) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Centroid A will keep its original centroid. The right centroid will have a \
    majority of its points in circle C (because there are 100,000 points there) and \
    will become the centroid of C and the middle centroid will stay in B. "

    # type: int
    answers["(c) Circle (a)"] = 0

    # type: int
    answers["(c) Circle (b)"] = 0

    # type: int
    answers["(c) Circle (c)"] = 2

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "Since C has 100,000 points and A and B have 100, there aren't enough points \
    in B to pull one of C's original centroids away. Therefore, there will be a centroid in between A and B and 2 centroids in C."

    return answers




# -----------------------------------------------------------
def question5():
    answers = {}

    # type: set
    answers["(a)"] = set({"Group A", "Group B"})

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "The minimum distance between any point in A and B is much smaller than the \
    minimum distance between any other groups. Thus, A and B merge."

    # type: set
    answers["(b)"] = set({"Group A", "Group C"})

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "The maximum distance between any point in A and C is much smaller than the \
    maximum distance between any other groups. Thus, A and C merge."

    return answers




# -----------------------------------------------------------
def question6():
    answers = {}

    # type: set
    answers["(a) core"] = set({"B", "C", "E", "F", "I", "J", "L", "M"})

    # type: set
    answers["(a) boundary"] = set({"D", "G"})

    # type: set
    answers["(a) noise"] = set({"A", "H"})

    # type: set 
    answers["(b) cluster 1"] = set({"B", "C", "D", "E", "F", "G"})

    # type: set 
    answers["(b) cluster 2"] = set({"I", "J", "L", "M"})

    # type: set
    answers["(b) cluster 3"] = set({})

    # type: set
    answers["(b) cluster 4"] = set({})

    # type: set
    answers["(c)-a core"] = set({"B", "C", "D", "E", "F", "G", "I", "J", "L", "M"})

    # type: set
    answers["(c)-a boundary"] = set({"A", "H"})

    # type: set
    answers["(c)-a noise"] = set({})

    # type: set
    answers["(c)-b cluster 1"] = set({"A", "B", "C", "D", "E", "F", "G"})

    # type: set
    answers["(c)-b cluster 2"] = set({"H", "I", "J", "L", "M"})

    # type: set
    answers["(c)-b cluster 3"] = set({})

    # type: set
    answers["(c)-b cluster 4"] = set({})

    return answers




# -----------------------------------------------------------
def question7():

    def entropy(cluster_counts):
        total_points = sum(cluster_counts)
        entropy = -sum((count / total_points) * math.log2(count / total_points) for count in cluster_counts if count > 0)
        return entropy

    cluster1 = [10, 100, 20, 10, 30000]
    cluster2 = [3000,10,1000,10,0]
    cluster3 = [10,3000,500,150,200]
    cluster4 = [2000,2500,1500,3000,1400]

    #print(entropy(cluster1), entropy(cluster2), entropy(cluster3), entropy(cluster4))

    answers = {}

    # type: string
    answers["(a)"] = "Cluster 4"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Cluster 4 has an entropy of 2.262 which is higher than the entropies of the other clusters (0.049, 0.857, 1.090)"

    # type: string
    answers["(b)"] = "Cluster 1"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Cluster 1 has an entropy of 0.049 which is lower than the entropies of the other clusters (0.857, 1.09, 2.262)"

    return answers




# -----------------------------------------------------------
def question8():
    answers = {}

    # type: string
    answers["(a) Matrix 1"] = "Dataset Z"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 1"] = "The diagonal entries of Matrix 1 are very solid and dark blue, indicating very low \
    distances among points in each cluster (lots of cohesion, small SSE). Dataset Z has an equal looking SSE for each cluster, as shown in Matrix 1."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 1"] = "The colors of the non-diagonal entries of Matrix 1 seem to be consitently bright \
    colors for each cluster. Therefore, this implies that the clusters are separated from one another very consistently. Also, we see \
    that 2 clusters have the same distance from another 2 clusters, concluding that this matches Dataset Z."

    # type: string
    answers["(a) Matrix 2"] = "Dataset X"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 2"] = "For the diagonal entries of Matrix 2, the middle two cubes \
    look to have the most cohesion due to their solid blue color, with 2 clustters having a bit less cohesion. We see this in both \
    dataset X and Y."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 2"] = "For the non-diagonal entries of Matrix 2, we see that row 1 is closest to row 2, row 2 is closest \
    to row 1 and row 3, row 3 is closest to row 2 and row 4, and row 4 is closest to row 3. We see distance of clusters in a sequence only in dataset X."

    # type: string
    answers["(a) Matrix 3"] = "Dataset Y"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 3"] = "For the diagonal entries of Matrix 3, the middle two cubes \
    look to have the most cohesion due to their solid blue color, with 2 clustters having a bit less cohesion. We see this in both \
    dataset X and Y."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 3"] = "Similar to matrix 1, we see that 2 clusters have the same distance from another 2 \
    clusters. The dataset match both this description and the weakly cohesive diagonals is dataset Y."

    # type: string
    answers["(b) Row 1"] = "Cluster A"

    # type: string
    answers["(b) Row 2"] = "Cluster B"

    # type: string
    answers["(b) Row 3"] = "Cluster C"

    # type: string
    answers["(b) Row 4"] = "Cluster D"

    # type: explanatory string (at least four words)
    answers["(b) Row 1 explain"] = "Row 1 is cluster A due to its low cohesion and grainy non-diagonal columns. It's also closest to row 2."

    # type: explanatory string (at least four words)
    answers["(b) Row 2 explain"] = "Row 2 is cluster B due to its high cohesion and grainy non-diagonal columns only with row 1 and 4, but not row 3. \
    Also, it's equidistance from row 1 and row 3."

    # type: explanatory string (at least four words)
    answers["(b) Row 3 explain"] = "Row 3 is cluster C due to its high cohesion and grainy non-diagonal columns only with row 1 and 4, but not row 2. \
    Also, it's equidistance from row 2 and row 4. "

    # type: explanatory string (at least four words)
    answers["(b) Row 4 explain"] = "Row 4 is cluster D due to its low cohesion and grainy non-diagonal columns. It's also closest to row 3."

    return answers




# -----------------------------------------------------------
def question9():
    answers = {}

    # type: list
    answers["(a)"] =  ['Hierarchical', 'overlapping', 'partial']

    # type: list
    answers["(b)"] = ['Partitional', 'exclusive', 'complete']

    # type: list
    answers["(c)"] = ['Partitional', 'fuzzy', 'complete']

    # type: list
    answers["(d)"] = ['Hierarchical', 'overlapping', 'partial']

    # type: list
    answers["(e)"] = ['Partitional', 'Exclusive', 'partial']

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "This clustering is partitional, as each cluster (letter grade) is individual of one another and don't overlap. This is exclusive \
    because each student is assigned to only one cluster, they can't have more than one grade in the course. Finally, the clustering is partial \
    because not all students in the Computer Science department have taken (or will take) CSci 5523."

    return answers




# -----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    answers["(a) Figure (a)"] = "No"

    # type: string
    answers["(a) Figure (b)"] = "Yes"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "DBSCAN looks for clusters of high densities. Therefore, DBSCAN would classsifiy the face in figure (a) as a cluster \
    but wouldn't classify the eyes, nose, and mouth as clusters. However, in figure (b) the eyes, nose, and mouth are of high density and \
    thus will be classifies as clusters."

    # type: string
    answers["(b) Figure (a)"] = "No"

    # type: string
    answers["(b) Figure (b)"] = "Yes"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "For K-means, if you started with centroids inside the eyes, mouth, and nose of the face in figure (a), you \
    still wouldn't be able to classify these facial features due to the high number of points around them. However, in figure (b), if you \
    intialized centroids in the eyes, mouth, and nose of the face, you could find patterns represented by these features due to the high \
    number of points in those regions."

    # type: string
    answers["(c)"] = "We could use DBSCAN, but alter the algorithm slightly. We could take the densities calculated but perform 1/density. \
    Therefore, areas with high density are represented as having low after the augmentation and low density areas appear higher."

    return answers

# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()
    print('end code')

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
