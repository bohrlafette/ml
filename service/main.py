import numpy as np
import scipy as sp
import tensorrec
import tensorflow as tf
import random
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler

from testdaten import createMultipleTestdata

NO = 0
YES = 1

MALE = 0
FEMALE = 1

def user(name, gender, numChildren, ownsHouse, yearBorn, numCats, numDogs, numHorses):
    print "adding user " + name
    return [gender, numChildren, ownsHouse, yearBorn, numCats, numDogs, numHorses]

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

users, generatedInteractions = createMultipleTestdata(3000)

# train the normalization
scaler = MinMaxScaler(feature_range=(0, 1))
scaler = scaler.fit(users)
#print('Min: %f, Max: %f' % (scaler.data_min_, scaler.data_max_))
# normalize the dataset and print the first 5 rows
normalizedUsers = scaler.transform(users)
print("########### normalized ###########")
print(users)

# normalize
#users = preprocessing.normalize(np.asarray(users, dtype=np.float), norm='l2')

#print("normalized")
#print(users)

user_features = sp.sparse.csr_matrix(normalizedUsers)
interactions = sp.sparse.csr_matrix(generatedInteractions)
item_features = sp.sparse.csr_matrix(np.matrix(items))


# Fit the model
model.fit(interactions, user_features, item_features, epochs=1000, verbose=False)

#print(user_features)
#print(interactions)

# Predict scores for all users and all items
predictions = model.predict(user_features=user_features,
                            item_features=item_features)

print(predictions)

i = 0
for prediction in predictions:
    print('gender=%i, numChildren=%i, ownsHouse=%i, yearBorn=%i, numCats=%i, numDogs=%i, numHorses=%i' 
    % (users[i][0],users[i][1],users[i][2],users[i][3],users[i][4],users[i][5],users[i][6])) 
    print('haft=%f, foerder=%f, zahn=%f, pferd=%f, hund=%f, hausrat=%f, kfz=%f'
    % (generatedInteractions[i][0],generatedInteractions[i][1],generatedInteractions[i][2],generatedInteractions[i][3],generatedInteractions[i][4],generatedInteractions[i][5],generatedInteractions[i][6])) 
    print('haft=%2.2f, foerder=%2.2f, zahn=%2.2f, pferd=%2.2f, hund=%2.2f, hausrat=%2.2f, kfz=%2.2f' 
    % (prediction[0],prediction[1],prediction[2],prediction[3],prediction[4],prediction[5],prediction[6])) 
    print("#")
    i = i + 1


# Calculate and print the recall at 10
#r_at_k = tensorrec.eval.recall_at_k(model, interactions,
#                                    k=10,
#                                    user_features=user_features,
#                                    item_features=item_features)
#print(np.mean(r_at_k))

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
    print user

    print scaler.transform([user])
    result = model.predict(sp.sparse.csr_matrix(scaler.transform([user])), item_features)
    return map(result[0])

def interact(user, interaction):
    model.fit(interaction, scaler.transform(user), item_features)

predictUser = user("Anna", 1, 0, 0, 2000, 0, 0, 0)
print(predict(predictUser))