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

def createJohnDoeYoungAgedSingle():
    return user('JohnDoeYoungAgedSingle', 
            1, 
            0, 
            0, 
            2000,
            1, 
            0, 
            0)

def createJohnDoeMidAgedFamilyMember():
    return user('JohnDoeMidAgedFamilyMember', 
            1, 
            2, 
            1, 
            1980,
            0, 
            1, 
            0)

def createJohnDoeMidAgedSingle():
    return user('JohnDoeMidAgedSingle', 
            1, 
            0, 
            1, 
            1990,
            2, 
            0, 
            1)

def generateInteraction(name, numChildren, ownsHouse, yearBorn, numCats, numDogs, numHorses):

    haft = int(round(random.uniform(0.2,1.0)))
    zahn = int(round(random.uniform(-0.6,1.0)))

    foerder = 0
    pferd = -1
    hunde = -1
    hausrat = 0
    kfz = 0

    if numDogs > 0:
        hunde = 1

    if numHorses > 0:
        pferd = 1

    if ownsHouse > 0:
        hausrat= 1

    if yearBorn <= 1992:
        foerder = int(round(random.uniform(0.3,1.0)))
    else:
        foerder = int(round(random.uniform(-0.7,0.6)))

    if yearBorn <= 1995:
        kfz = int(round(random.uniform(-0.7,0.9)))
    else:
        kfz = 1
    
    return interaction(haft, foerder, zahn, pferd, hunde, hausrat, kfz)

def generateJohnDoeYoungAgedSingleInteraction():

    return interaction(-1, -1, -1, -1, -1, -1, 1)

def generateJohnDoeMidAgedFamilyMemberInteraction():

    return interaction(1, 1, 1, -1, 1, 1, -1)

def generateJohnDoeMidAgedSingle():

    return interaction(1, 1, 1, 1, -1, 1, 1)

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
                                        testUser[0],
                                        testUser[1],
                                        testUser[2],
                                        testUser[3],
                                        testUser[4],
                                        testUser[5],
                                        testUser[6])
                                        
    return testUser, generatedInteraction

def createJohnDoeSingleTestdata(typ):
    if typ == 0:
        testUser = createJohnDoeYoungAgedSingle()
        generatedInteraction = generateJohnDoeYoungAgedSingleInteraction()
    elif typ == 1:
        testUser = createJohnDoeMidAgedFamilyMember()
        generatedInteraction = generateJohnDoeMidAgedFamilyMemberInteraction()
    else:
        testUser = createJohnDoeMidAgedSingle()
        generatedInteraction = generateJohnDoeMidAgedSingle()

    return testUser, generatedInteraction

def createMultipleTestdata(count):
    i = 1
    initialUser, initialInteraction = createJohnDoeSingleTestdata(random.randint(0,2),)
    users = [initialUser]
    interactions = [initialInteraction]

    while i < count:

        #if (i%2)==0:
        testUser, generatedInteraction = createJohnDoeSingleTestdata(random.randint(0,2),)
        #else:
        #    testUser, generatedInteraction = createSingleTestdata(random.randint(0,2),)

        users = np.append(users, [testUser], axis=0)
        interactions = np.append(interactions, [generatedInteraction], axis=0)

        i = i + 1

    print("[gender, numChildren, ownsHouse, yearBorn, numCats, numDogs, numHorses]")
    print(users)
    
    print("[haft, foerder, zahn, pferd, hunde, hausrat, kfz]")
    print(interactions)
    
    return users, interactions

createMultipleTestdata(20)