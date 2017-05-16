# =====================================================================================================================
# Nodo di un albero binario di ricerca
# =====================================================================================================================

class Node:
    # Costruttore
    def __init__(self, k):
        self.k = k
        self.left = None
        self.right = None
        self.p = None

    # Restituisce la chiave k
    def getKey(self):
        return self.k

    # Cambia la chiave k
    def setKey(self, k):
        self.k = k

    # Resituisce i figli del nodo corrente
    def getChildren(self):
        children = []
        if self.left is not None:
            children.append(self.left)
        if self.right is not None:
            children.append(self.right)
        return children


# =====================================================================================================================
# Albero binario di ricerca
# =====================================================================================================================

class BinarySearchTree:
    # Costruttore
    def __init__(self):
        self.root = None

    # Cambia la radice
    def setRoot(self, k):
        self.root = Node(k)

    # Inserimento
    def insert(self, k):
        if self.root is None:
            self.setRoot(k)
        else:
            self.insertNode(self.root, k)

    # Funzione che effettua l'inserimento
    def insertNode(self, currentNode, k):
        if k <= currentNode.k:
            if currentNode.left is not None:
                self.insertNode(currentNode.left, k)
            else:
                currentNode.left = Node(k)
                currentNode.left.p = currentNode
        elif k > currentNode.k:
            if currentNode.right is not None:
                self.insertNode(currentNode.right, k)
            else:
                currentNode.right = Node(k)
                currentNode.right.p = currentNode

    # Ricerca
    def search(self, k):
        if self.searchNode(self.root, k):
            print "\nThe value is in the tree"
            print
        else:
            print "\nThe value is not in the tree"
            print

    # Funzione che effettua la ricerca
    def searchNode(self, currentNode, k):
        if currentNode is None:
            return False
        elif k == currentNode.k:
            return True
        elif k < currentNode.k:
            return self.searchNode(currentNode.left, k)
        else:
            return self.searchNode(currentNode.right, k)

    # Stampa tutti gli elementi dell'albero in ordine crescente
    def inorder(self):
        print "\nOrdered value in the Binary Tree: [",

        def _inorder(v):
            if v is None:
                return
            if v.left is not None:
                _inorder(v.left)
            print v.k,
            if v.right is not None:
                _inorder(v.right)

        _inorder(self.root)
        print "]\n"

    # Restituisce il valore minimo contenuto nel sottoalbero del nodo "node" (incluso) che gli viene passato
    def getTreeMinimum(self, node):
        while node.left is not None:
            node = node.left
        return node.k

    # Restituisce il valore massimo contenuto nel sottoalbero del nodo "node" (incluso) che gli viene passato
    def getTreeMaximum(self, node):
        while node.right is not None:
            node = node.right
        return node.k

    # Stampa il valore minimo contenuto nell'albero (tutto l'albero)
    def printMinimum(self):
        print "\nMinimum is: ", self.getTreeMinimum(self.root)
        print

    # Stampa il valore massimo contenuto nell'albero (tutto l'albero)
    def printMaximum(self):
        print "\nMaximum is: ", self.getTreeMaximum(self.root)
        print

    # Stampa l'albero
    def stampa(self):
        self.traverse(self.root)

    # Funzione che esegue la stampa del sottoalbero del nodo "node" (incluso) che gli viene passato
    def traverse(self, node):
        currentLevel = [node]
        while currentLevel:
            nextlevel = list()
            for n in currentLevel:
                if n.p is None:
                    print "\n\n", n.k
                else:
                    print "|| *", n.k, "* <- son of", n.p.k, "||     ",
                if n.left:
                    nextlevel.append(n.left)
                if n.right:
                    nextlevel.append(n.right)
            print
            currentLevel = nextlevel
        print

    # Restituisce l'altezza del sottoalbero del nodo "node" (incluso) che gli viene passato
    def getHeight(self, node):
        currentLevel = [node]
        count = 0
        while currentLevel:
            nextLevel = list()
            for n in currentLevel:
                if n.left:
                    nextLevel.append(n.left)
                if n.right:
                    nextLevel.append(n.right)
            count += 1
            currentLevel = nextLevel
        return count

    # Stampa l'altezza dell'albero
    def printHeight(self):
        print "\nHeight is:", self.getHeight(self.root)
        print
