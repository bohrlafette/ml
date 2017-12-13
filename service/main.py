import numpy as np
import scipy as sp
import tensorrec
import tensorflow as tf
import random
from sklearn import preprocessing

from testdaten import createMultipleTestdata

NO = 0
YES = 1

MALE = 0
FEMALE = 1


def user(name, gender, numChildren, ownsHouse, yearBorn, numCats, numDogs, numHorses):
    print "adding user " + name
    return [gender, numChildren, yearBorn, ownsHouse, numCats, numDogs, numHorses]

def item(name, secureFamily, secureProperty, retirement, health, animals):
    print "adding item " + name
    return [secureFamily, secureProperty, retirement, health, animals]

# Build the model with default parameters
#model = tensorrec.TensorRec()

model = tensorrec.TensorRec(user_repr_graph=tensorrec.representation_graphs.relu_representation_graph, item_repr_graph=tensorrec.representation_graphs.relu_representation_graph)

'''
users = [
    user("Hans", MALE, 1, NO, 1990, 0, 0, 0),
    user("Carla", FEMALE, 0, YES, 1985, 1, 0, 0),
    user("Franziska", FEMALE, 1, NO, 1981, 0, 1, 0),
    user("Susanne", FEMALE, 1, NO, 1971, 1, 1, 0),
    user("Carlotta", FEMALE, 0, NO, 1983, 0, 0, 1),
    user("Ralf", MALE, 0, NO, 1989, 0, 1, 0),
    user("Frank", MALE, 0, YES, 1988, 0, 1, 1),
    user("Manfreda", FEMALE, 1, NO, 1990, 0, 0, 0),
]

interaction = np.matrix([
        [0, 0, 0, -1, -1],
        [1, 0, 1, 0, 0],
        [1, 1, 0, 0, 0],
        [1, 0, 1, 0, 0],
        [1, 1, 1, 0, 0],
        [1, 1, 1, 0, 0],
        [1, 0, 0, 1, 1],
        [1, 0, 0, 0, 0]
    ])
'''

items = [
    item("haft", YES, YES, NO, NO, NO),
    item("foerder", YES, YES, YES, NO, NO),
    item("zahn", YES, NO, NO, YES, NO),
    item("pferd", NO, YES, NO, NO, YES),
    item("hund", NO, YES, NO, NO, YES),
    item("hausrat", YES, YES, NO, NO, NO),
    item("kfz", NO, YES, NO, NO, NO)
]

users, generatedInteractions = createMultipleTestdata(20)

# normalize
users = preprocessing.normalize(np.asarray(users, dtype=np.float), norm='l2')

user_features = sp.sparse.csr_matrix(users)
interactions = sp.sparse.csr_matrix(generatedInteractions)
item_features = sp.sparse.csr_matrix(np.matrix(items))


# Fit the model
model.fit(interactions, user_features, item_features, epochs=750, verbose=False)

# Predict scores for all users and all items
predictions = model.predict(user_features=user_features,
                            item_features=item_features)

print(predictions)


# Calculate and print the recall at 10
r_at_k = tensorrec.eval.recall_at_k(model, interactions,
                                    k=10,
                                    user_features=user_features,
                                    item_features=item_features)
print(np.mean(r_at_k))

def map(predictions):
    return {
        "haft": predictions[0].item(),
        "foerder": predictions[1].item(),
        "zahn": predictions[2].item(),
        "pferd": predictions[3].item(),
        "hund": predictions[4].item(),
        "hausrat": predictions[5].item(),
        "kfz": predictions[6].item()
    }

def predict(user):
    result = model.predict(sp.sparse.csr_matrix(np.matrix([user])), item_features)
    return map(result[0])
