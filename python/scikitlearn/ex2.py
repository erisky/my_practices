from sklearn.datasets import load_iris
import numpy as np

iris = load_iris()
print iris.feature_names
print iris.target_names

for x in xrange(0,10):
    print iris.data[x]

print iris.target[0]

for i in range(len(iris.target)):
    print "example %d: label %s, feature: %s " % (i, iris.target[i], iris.data[i])


# train the classfiler

test_idx = [0, 50, 100]

#training data
train_target = np.delete(iris.target, test_idx)
train_data = np.delete(iris.data, test_idx, axis=0)

# testing data
test_target = iris.target[test_idx]
#test
print test_target
test_data = iris.data[test_idx]

