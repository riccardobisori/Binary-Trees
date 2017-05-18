import pickle
import TestInsert
import matplotlib.pyplot as mp

elements = (10, 50, 1000, 10000, 50000)
rangeElements = (30, 1500, 1000000000)

testValues = (elements, rangeElements)

pickle.dump(testValues, open("testInsert.p", "wb"))

TestInsert.testInsert()

resultInsertABR = pickle.load(open("resultInsertABR.p", "rb"))
resultInsertRB = pickle.load(open("resultInsertRB.p", "rb"))


x = (30, 100, 500, 1000)

# Plot dei tempi di inserimento in un Binary Search Tree all'aumentare del range con cui vengono generati i numeri
# inseriti nell'albero in ordine crescente. Il numero inserito e' (max(range) + 1)

mp.plot(x, resultInsertABR[1])

mp.xlabel('Range elementi')
mp.ylabel('Tempo di inserimento di (max(range) + 1)')
mp.title("Tempi di inserimento in un Binary Search Tree\n con elementi precedentemente inseriti in ordine crescente")
mp.show()

# Plot dei tempi di inserimento in un Red-Black Tree all'aumentare del range con cui vengono generati i numeri
# inseriti nell'albero in ordine crescente. Il numero inserito e' (max(range) + 1)

x = (30, 100, 500, 1000, 1500)

mp.plot(x, resultInsertRB[1])

mp.xlabel('Range elementi')
mp.ylabel('Tempo di inserimento di (max(range) + 1)')
mp.title("Tempi di inserimento in un Red-Black Tree\n con elementi precedentemente inseriti in ordine crescente")
mp.show()