import random
import numpy as np

NO = 0
YES = 1

def user(name, gender, numChildren, ownsHouse, yearBorn, numCats, numDogs, numHorses):
    #print "adding user " + name
    return [gender, numChildren, ownsHouse, yearBorn, numCats, numDogs, numHorses]

def item(name, secureFamily, secureProperty, retirement, health, animals):
    #print "adding item " + name
    return [secureFamily, secureProperty, retirement, health, animals]

def interaction(haft, foerder, zahn, pferd, hunde, hausrat, kfz):
    return [haft, foerder, zahn, pferd, hunde, hausrat, kfz]

def createYoungAgedSingle():
    return (user('YoungAgedSingle', 
            random.randint(0,1), 
            int(round(random.uniform(0.0,0.65))), 
            int(round(random.uniform(0.0,0.65))), 
            random.randint(1997, 2001),
            int(round(random.uniform(0.0,0.65))), 
            random.randint(0,1), 
            int(round(random.uniform(0.0,0.60)))))

def createMidAgedFamilyMember():
    return (user('MidAgedFamilyMember', 
            random.randint(0,1), 
            random.randint(0,4),
            random.randint(0,1), 
            random.randint(1987, 1995),
            int(round(random.uniform(0.2,1.0))), 
            int(round(random.uniform(0.2,1.0))), 
            random.randint(0,1)))

def createMidAgedSingle():
    return (user('MidAgedSingle', 
            random.randint(0,1), 
            int(round(random.uniform(0.0,0.65))),
            int(round(random.uniform(0.0,0.65))),
            random.randint(1977, 1990),
            int(round(random.uniform(0.2,1.0))), 
            int(round(random.uniform(0.2,1.0))),
            int(round(random.uniform(0.0,0.65)))))

def generateInteraction(numChildren, ownsHouse, yearBorn, numCats, numDogs, numHorses):

    haft = int(round(random.uniform(0.2,1.0)))
    zahn = int(round(random.uniform(-0.6,1.0)))

    foerder = 0
    pferd = -1
    hunde = -1
    hausrat = 0
    kfz = 0

    if numDogs > 0:
        hunde = int(round(random.uniform(0.4,1.0)))

    if numHorses > 0:
        pferd = int(round(random.uniform(0.4,1.0)))

    if ownsHouse > 0:
        hausrat= int(round(random.uniform(0.4,1.0)))

    if yearBorn <= 1992:
        foerder = int(round(random.uniform(0.3,1.0)))
    else:
        foerder = int(round(random.uniform(-0.7,0.6)))

    if yearBorn <= 1997:
        kfz = int(round(random.uniform(-0.7,0.7)))
    else:
        kfz = int(round(random.uniform(0.3,1.0)))
    
    return interaction(haft, foerder, zahn, pferd, hunde, hausrat, kfz)

items = [
    item("haft", YES, YES, NO, NO, NO),
    item("foerder", YES, YES, YES, NO, NO),
    item("zahn", YES, NO, NO, YES, NO),
    item("pferd", NO, YES, NO, NO, YES),
    item("hunde", NO, YES, NO, NO, YES),
    item("hausrat", YES, YES, NO, NO, NO),
    item("kfz", NO, YES, NO, NO, NO)
]

def createSingleTestdata(typ):
    if typ == 0:
        testUser = createYoungAgedSingle()
    elif typ == 1:
        testUser = createMidAgedFamilyMember()
    else:
        testUser = createMidAgedSingle()

    generatedInteraction = generateInteraction(
                                        testUser[1],
                                        testUser[2],
                                        testUser[3],
                                        testUser[4],
                                        testUser[5],
                                        testUser[6])
                                        
    return testUser, generatedInteraction

def createMultipleTestdata(count):
    i = 1
    initialUser, initialInteraction = createSingleTestdata(random.randint(0,2),)
    users = [initialUser]
    interactions = [initialInteraction]

    while i < count:

        testUser, generatedInteraction = createSingleTestdata(random.randint(0,2),)

        users = np.append(users, [testUser], axis=0)
        interactions = np.append(interactions, [generatedInteraction], axis=0)

        i = i + 1

    print("[gender, numChildren, ownsHouse, yearBorn, numCats, numDogs, numHorses]")
    print(users)
    
    print("[haft, foerder, zahn, pferd, hunde, hausrat, kfz]")
    print(interactions)
    
    return users, interactions

createMultipleTestdata(10)