import random
import ABR
import RB
import sys
import pickle

sys.setrecursionlimit(4400)


def testHeights():
    testHeightsStart = pickle.load(open("tests.p", "rb"))
    resultABR = testHeightABR(testHeightsStart)
    resultRB = testHeightRB(testHeightsStart)

    pickle.dump(resultABR, open("resultHeightABR.p", "wb"))
    pickle.dump(resultRB, open("resultHeightRB.p", "wb"))


def testHeightABR(testHeightsStart):
    elements = testHeightsStart[0]
    rangeElements = testHeightsStart[1]

    arrayHeightABR = []
    resultRandomHeightABR = []
    averageArrayHeightABR = []

    print "\n", "=" * 100
    print "Average heights of Binary Search Trees for random elements. 3 executions. "
    print "Columns: ranges [20, 200, 1000, 10000000]. "
    print "Lines: elements [10, 50, 500, 1000, 10000, 50000]"
    print "=" * 100, "\n"

    for p in elements:
        for i in rangeElements:
            for j in range(3):
                ABRtree = ABR.BinarySearchTree()
                for k in range(p):
                    ABRtree.insert(random.randint(0, i))
                heightABR = ABRtree.getHeight(ABRtree.root)
                arrayHeightABR.append(heightABR)
            averageArrayHeightABR.append(sum(arrayHeightABR)/len(arrayHeightABR))
            arrayHeightABR = []

        resultRandomHeightABR.append(averageArrayHeightABR)
        print averageArrayHeightABR
        averageArrayHeightABR = []

    return resultRandomHeightABR


def testHeightRB(testHeightsStart):
    elements = testHeightsStart[0]
    rangeElements = testHeightsStart[1]

    arrayHeightRB = []
    resultRandomHeightRB = []
    resultOrderedHeightRB = []
    averageArrayHeightRB = []

    print "\n", "=" * 100
    print "Average heights of Red-Black Trees for random elements. 10 executions. "
    print "Columns: ranges [20, 200, 1000, 10000000]. "
    print "Lines: elements [10, 50, 500, 1000, 10000, 50000]"
    print "=" * 100, "\n"

    for p in elements:
        for i in rangeElements:
            for j in range(10):
                RBtree = RB.RedBlackTree()
                for k in range(p):
                    RBtree.insert(random.randint(0, i))
                heightRB = RBtree.getHeight(RBtree.root)
                arrayHeightRB.append(heightRB)
            averageArrayHeightRB.append(sum(arrayHeightRB)/len(arrayHeightRB))
            arrayHeightRB = []

        resultRandomHeightRB.append(averageArrayHeightRB)
        print averageArrayHeightRB
        averageArrayHeightRB = []

    print

    print "\n", "=" * 100
    print "Average heights of Red-Black Trees for ordered elements. 5 executions. "
    print "Columns: ranges [20, 200, 1000, 10000000]. "
    print "Lines: elements [10, 50, 500, 1000, 10000, 50000]"
    print "=" * 100, "\n"

    for p in elements:
        for i in range(len(rangeElements)):
            for j in range(5):
                RBtree = RB.RedBlackTree()
                for k in range(p):
                    RBtree.insert(k)
                heightRB = RBtree.getHeight(RBtree.root)
                arrayHeightRB.append(heightRB)
            averageArrayHeightRB.append(sum(arrayHeightRB)/len(arrayHeightRB))
            arrayHeightRB = []

        resultOrderedHeightRB.append(averageArrayHeightRB)
        print averageArrayHeightRB
        averageArrayHeightRB = []

    return resultRandomHeightRB, resultOrderedHeightRB


