import random
import ABR
import RB
import sys
import pickle
from timeit import default_timer as timer

sys.setrecursionlimit(4400)


def testInsert():
    testInsertStart = pickle.load(open("testInsert.p", "rb"))

    resultABR = testInsertABR(testInsertStart)
    resultRB = testInsertRB(testInsertStart)

    pickle.dump(resultRB, open("resultInsertRB.p", "wb"))
    pickle.dump(resultABR, open("resultInsertABR.p", "wb"))


def testInsertABR(testInsertStart):
    elements = testInsertStart[0]
    rangeElements = testInsertStart[1]

    heightABR = []
    timerABR = []
    resultTimerRandomABR = []

    elementsOrderedABR = (10, 50, 1000, 3000)
    resultTimerOrderedABR = []

    print "\n", "=" * 100
    print "First array: heights of Binary Search Trees for random elements."
    print "Second array: time to insert a larger element than any other already in the tree."
    print "Columns: ranges [30, 1500, 1000000000]. "
    print "Lines: elements [10, 50, 1000, 10000, 50000]"
    print "=" * 100, "\n"

    for p in elements:
        for i in rangeElements:
            ABRtree = ABR.BinarySearchTree()
            for j in range(p):
                ABRtree.insert(random.randint(0, i))

            heightABR.append(ABRtree.getHeight(ABRtree.root))

            start = timer()
            ABRtree.insert(i + 1)
            end = timer()
            timerABR.append(end - start)

        resultTimerRandomABR.append(timerABR)
        print heightABR
        print timerABR
        print
        heightABR = []

    print "\n", "=" * 100
    print "First array: heights of Binary Search Tree for ordered elements."
    print "Second array: time to insert a larger element than any other already in the tree."
    print "Elements: [10, 50, 1000, 3000]"
    print "=" * 100, "\n"

    for p in elementsOrderedABR:
        ABRtree = ABR.BinarySearchTree()
        for j in range(p):
            ABRtree.insert(j)

        heightABR.append(ABRtree.getHeight(ABRtree.root))

        start = timer()
        ABRtree.insert(p + 1)
        end = timer()

        resultTimerOrderedABR.append(end - start)

    print heightABR
    print resultTimerOrderedABR
    print

    return resultTimerRandomABR, resultTimerOrderedABR


def testInsertRB(testInsertStart):
    elements = testInsertStart[0]
    rangeElements = testInsertStart[1]

    heightRB = []
    timerRB = []
    resultTimerRandomRB = []

    resultTimerOrderedRB = []

    print "\n", "=" * 100
    print "First array: heights of Red-Black Tree for random elements."
    print "Second array: time to insert a larger element than any other already in the tree."
    print "Columns: ranges [30, 1500, 1000000000]. "
    print "Lines: elements [10, 50, 1000, 10000, 50000]"
    print "=" * 100, "\n"

    for p in elements:
        for i in rangeElements:
            RBtree = RB.RedBlackTree()
            for j in range(p):
                RBtree.insert(random.randint(0, i))

            heightRB.append(RBtree.getHeight(RBtree.root))

            start = timer()
            RBtree.insert(i + 1)
            end = timer()
            timerRB.append(end - start)

        resultTimerRandomRB.append(timerRB)
        print heightRB
        print timerRB
        print
        heightRB = []

    print "\n", "=" * 100
    print "First array: heights of Red-Black Tree for ordered elements."
    print "Second array: time to insert a larger element than any other already in the tree."
    print "Elements: [10, 50, 1000, 10000, 50000]"
    print "=" * 100, "\n"

    for p in elements:
        RBtree = RB.RedBlackTree()
        for j in range(p):
            RBtree.insert(j)

        heightRB.append(RBtree.getHeight(RBtree.root))

        start = timer()
        RBtree.insert(p + 1)
        end = timer()

        resultTimerOrderedRB.append(end - start)

    print heightRB
    print resultTimerOrderedRB
    print

    return resultTimerRandomRB, resultTimerOrderedRB
