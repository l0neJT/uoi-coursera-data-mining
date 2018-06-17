"""
Evaluate clusters using entropy-based (Normalized Mutual Information) and
pairwise (Jaccard coefficient) validation methods.
"""

import glob
import numpy as np
from math import log, sqrt
from scipy.special import binom
# from sklearn.metrics.cluster import normalized_mutual_info_score
# from sklearn.metrics import jaccard_similarity_score, confusion_matrix

def getEntropy(clustering):
    """Calcuate the entropy for a clustering/paritioning.
        
        Args:
            clustering(:obj:`ndarry`): Cluster labels.
        
        Returns:
            float: Entropy of the clustering.
    """
    clusters, counts = np.unique(clustering, return_counts=True)
    probs = np.divide(counts.astype(float), clustering.size)
    h = np.vectorize(lambda p: -1 * p * log(p))
    return sum(h(probs))
    
def getMI(c1, c2):
    """Calculate Mutual Information between two clusterings.
    
        Args:
            c1(:obj:`ndarry`): Cluster labels.
            c2(:obj:`ndarry`): Cluster labels.
        
        Returns:
            float: Mutual Information
    """
    # Get number of points and label intersections/counts
    inter = np.vstack((c1, c2)).T
    interLabels, interCounts = np.unique(inter, axis=0, return_counts=True)
    
    # Store label counts for each clusting as defaultdict for quick lookup and
    # to automatically return zero for missing key
    c1Counts = dict(zip(*np.unique(c1, return_counts=True)))
    c2Counts = dict(zip(*np.unique(c2, return_counts=True)))
    
    # Sum NMI over label intersections and return
    n = float(c1.size) # Typed `float` to assure non-integer math in final sum
    mi = 0.0
    for i, c in enumerate(interCounts):
        c1Count = c1Counts[interLabels[i, 0]]
        c2Count = c2Counts[interLabels[i, 1]]
        mi += (c / n) * log(n * c / (c1Count * c2Count))
    return mi

def getNMI(c1, c2):
    """Calculate Normalized Mutual Information between two clusterings.
    
        Args:
            c1(:obj:`ndarry`): Cluster labels.
            c2(:obj:`ndarry`): Cluster labels.

        Returns:
            float: Normalized Mutual Information
    """
    return getMI(c1, c2) / sqrt(getEntropy(c1) * getEntropy(c2))


def getPairwiseTruths(p, c):
    """Count pairwise truths (i.e., TP, FP, FN, and TN) between a partitioning
        (ground truth) and clustering (predicted).
    
        Args:
            p(:obj:`ndarry`): Partition labels.
            c(:obj:`ndarry`): Cluster labels.

        Returns:
            :obj:`tuple` of int: (TP, FP, FN, TN)
    """    
    # Calcuate true-postives
    inter = np.vstack((p, c)).T
    interLabels, interCounts = np.unique(inter, axis=0, return_counts=True)
    tp = sum(binom(interCounts, 2))

     # Calculate false-positives
    cLabels, cCounts = np.unique(c, return_counts=True)
    fp = sum(binom(cCounts, 2)) - tp
    
    # Calcuate false-negatives
    pLabels, pCounts = np.unique(p, return_counts=True)
    fn = sum(binom(pCounts, 2)) - tp
    
    # Return with true-negatives
    return (tp, fp, fn, binom(p.size, 2) - tp - fp - fn)

def getJaccardCoefficient(p, c):
    """Calcuate Jaccard coefficient between a partitioning (ground truth) and
        clustering (predicted).
    
        Args:
            p(:obj:`ndarry`): Partition labels.
            c(:obj:`ndarry`): Cluster labels.

        Returns:
            float: Jaccard Coefficient
    """ 
    tp, fp, fn, tn = getPairwiseTruths(p, c)
    return float(tp) / (tp + fn + fp)


# Read ground truth partitioning from text; ignores first column of item indices
partitioning = np.loadtxt(fname="./source/partitions.txt", usecols=1)
# print("partitioning has shape {}".format(partitioning.shape))
# print("First five rows:")
# print(partitioning[:5,])


# Iterate through clustering attempts calculating NMI and Jaccard coefficient
validations = []
for f in glob.iglob('./source/clustering_*.txt'):
    clustering = np.loadtxt(fname=f, usecols=1)
    validations.append([getNMI(partitioning, clustering), \
                        getJaccardCoefficient(partitioning, clustering)])

# Output validations to text
np.savetxt(fname="./output/validations.txt", X=validations, fmt="%1.7f")