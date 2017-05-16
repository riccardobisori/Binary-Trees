import pickle
import TestHeights
import matplotlib.pyplot as mp

elements = (10, 50, 500, 1000, 10000, 50000)
rangeElements = (20, 200, 1000, 10000000)

testValues = (elements, rangeElements)

pickle.dump(testValues, open("tests.p", "wb"))

TestHeights.testHeights()

resultHeightABR = pickle.load(open("resultHeightABR.p", "rb"))
resultHeightRB = pickle.load(open("resultHeightRB.p", "rb"))

randomHeightRB = resultHeightRB[0]
orderedHeightRB = resultHeightRB[1]

x = (50, 300, 900, 1800)

# Plot altezze dei Binary Search Trees all'aumentare del range con cui vengono generati i numeri casuali da inserire

mp.plot(x, resultHeightABR[5])
mp.plot(x, resultHeightABR[4])
mp.plot(x, resultHeightABR[3])

mp.xlabel('Range elementi')
mp.ylabel('Altezza albero')
mp.legend(['50000 elementi', '10000 elementi', '1000 elementi'], loc=2)
mp.title("Altezza Binary Search Tree al crescere del range\n degli elementi inseriti in ordine casuale")
mp.show()

# Plot altezze dei Red-Black Trees all'aumentare del range con cui vengono generati i numeri casuali da inserire

mp.plot(x, randomHeightRB[5])
mp.plot(x, randomHeightRB[4])
mp.plot(x, randomHeightRB[3])

mp.xlabel('Range elementi')
mp.ylabel('Altezza albero')
mp.legend(['50000 elementi', '10000 elementi', '1000 elementi'], loc=2)
mp.title("Altezza Red-Black Tree al crescere del range\n degli elementi inseriti in ordine casuale")
mp.show()



