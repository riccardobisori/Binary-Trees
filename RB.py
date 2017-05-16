# =====================================================================================================================
# Nodo di un albero rosso-nero
# =====================================================================================================================

class RBNode:
    # Costruttore
    def __init__(self, k, nil):
        self.k = k
        self.left = nil
        self.right = nil
        self.p = nil
        self.color = "Black"


    # Restituisce la chiave
    def get(self):
        return self.k

    # Cambia la chiave
    def set(self, k):
        self.k = k

    # Restituisce i figli
    def getChildren(self, nil):
        children = []
        if self.left != nil:
            children.append(self.left)
        if self.right != nil:
            children.append(self.right)
        return children

    # Restituisce il colore
    def getColor(self):
        return self.color

    # Cambia il colore
    def setColor(self, color):
        self.color = color


# =====================================================================================================================
# Albero rosso-nero
# =====================================================================================================================

class RedBlackTree:
    # Costruttore
    def __init__(self):
        self.nil = RBNode(None, None)
        self.root = self.nil

    # Cambia la radice
    def setRoot(self, k):
        self.root = RBNode(k, self.nil)

    # Inserimento
    def insert(self, k):
        if self.root is self.nil:
            self.setRoot(k)
            self.root.color = "Red"
            self.insertFixup(self.root)
        else:
            self.insertNode(self.root, k)

    # Funzione che realizza l'inserimento
    def insertNode(self, currentNode, k):
        if k <= currentNode.k:
            if currentNode.left is not self.nil:
                self.insertNode(currentNode.left, k)
            else:
                currentNode.left = RBNode(k, self.nil)
                currentNode.left.p = currentNode
                currentNode.left.color = "Red"
                self.insertFixup(currentNode.left)
        elif k > currentNode.k:
            if currentNode.right is not self.nil:
                self.insertNode(currentNode.right, k)
            else:
                currentNode.right = RBNode(k, self.nil)
                currentNode.right.p = currentNode
                currentNode.right.color = "Red"
                self.insertFixup(currentNode.right)

    # Funzione che "rimette le cose a posto" (ovvero fa in modo che le proprieta' dell'albero rosso-nero vengano
    # nuovamente rispettate dopo l'inserimento)
    def insertFixup(self, node):
        while node.p.color is "Red":
            if node.p is node.p.p.left:
                y = node.p.p.right
                if y.color is "Red":
                    node.p.color = "Black"
                    y.color = "Black"
                    node.p.p.color = "Red"
                    node = node.p.p
                else:
                    if node is node.p.right:
                        node = node.p
                        self.leftRotate(node)
                    node.p.color = "Black"
                    node.p.p.color = "Red"
                    self.rightRotate(node.p.p)
            else:
                y = node.p.p.left
                if y.color is "Red":
                    node.p.color = "Black"
                    y.color = "Black"
                    node.p.p.color = "Red"
                    node = node.p.p
                else:
                    if node is node.p.left:
                        node = node.p
                        self.rightRotate(node)
                    node.p.color = "Black"
                    node.p.p.color = "Red"
                    self.leftRotate(node.p.p)
        self.root.color = "Black"

    # Rotazione a sinistra: l'obiettivo, data una condizione iniziale in cui c'e' un nodo 'x' e un suo figlio destro
    # 'y', e' fare in modo che alla fine 'y' occupi la posizione di 'x' e che 'x' diventi il figlio sinistro di 'y'.
    # 'x' diventando figlio sinistro di 'y' dovra' mantenere il suo sottoalbero sinistro e ottenere come
    # sottoalbero destro quello che era il sottoalbero sinistro di 'y', che mantiene il sottoalbero destro
    def leftRotate(self, node):
        y = node.right  # -> Definisce il nodo "y", figlio destro di "node"
        node.right = y.left  # -> Il sottoalbero sinistro di "y" diventa il sottoalbero destro di "node"
        if y.left is not self.nil:
            y.left.p = node
        y.p = node.p  # -> Ora il padre di "node" e' il padre di "y"
        if node.p is self.nil:  # -> Mette "y" nella posizione di "node", con 2 'if' e un 'else'
            self.root = y
        elif node is node.p.left:
            node.p.left = y
        else:
            node.p.right = y
        y.left = node  # -> "node" diventa il figlio sinistro di "y"
        node.p = y

    # Rotazione a destra: l'obiettivo, data una condizione iniziale in cui c'e' un nodo 'x' e un su figlio sinistro
    # 'y', e' fare in modo che alla fine 'y' occupi la posizione di 'x' e che 'x' diventi il figlio destro di 'y'.
    # 'x' diventando figlio destro di 'y' dovra' mantenere il suo sottoalbero destro e ottenere come
    # sottoalbero sinistro quello che era il sottoalbero destro di 'y', che mantiene il suo sottoalbero sinistro
    def rightRotate(self, node):
        y = node.left
        node.left = y.right
        if y.right is not self.nil:
            y.right.p = node
        y.p = node.p
        if node.p is self.nil:
            self.root = y
        elif node is node.p.right:
            node.p.right = y
        else:
            node.p.left = y
        y.right = node
        node.p = y

    # Ricerca
    def search(self, k):
        if self.searchNode(self.root, k):
            print "\nThe value is in the tree"
            print
        else:
            print "\nThe value is not in the tree"
            print

    # Funzione che realizza la ricerca
    def searchNode(self, currentNode, k):
        if currentNode is self.nil:
            return False
        elif k is currentNode.k:
            return True
        elif k < currentNode.k:
            return self.searchNode(currentNode.left, k)
        else:
            return self.searchNode(currentNode.right, k)

    # Stampa tutti gli elementi dell'albero in ordine crescente
    def inorder(self):
        print "\nOrdered value in the Red-Black Tree: [",

        def _inorder(v):
            if v.k is None:
                return
            if v.left.k is not None:
                _inorder(v.left)
            print v.k, "->", v.color, "|",
            if v.right.k is not None:
                _inorder(v.right)

        _inorder(self.root)
        print "]\n"

    # Restituisce il valore minimo contenuto nel sottoalbero del nodo "node" (incluso) che gli viene passato
    def getTreeMinimum(self, node):
        while node.left is not self.nil:
            node = node.left
        return node.k

    # Restituisce il valore massimo contenuto nel sottoalbero del nodo "node" (incluso) che gli viene passato
    def getTreeMaximum(self, node):
        while node.right is not self.nil:
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
                if n.p is self.nil:
                    print "\n", "*", n.k, "-", n.color, "*"
                else:
                    print "|| *", n.k, "-", n.color, "* <- son of", n.p.k, "||     ",
                if n.left is not self.nil:
                    nextlevel.append(n.left)
                if n.right is not self.nil:
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
                if n.left is not self.nil:
                    nextLevel.append(n.left)
                if n.right is not self.nil:
                    nextLevel.append(n.right)
            count += 1
            currentLevel = nextLevel
        return count

    # Stampa l'altezza dell'albero
    def printHeight(self):
        print "\nHeight is:", self.getHeight(self.root)
        print

    # Restituisce l'altezza NERA dell'albero
    def getBlackHeight(self, node):
        count = 0
        while node is not self.nil:
            if node.color is "Black":
                count += 1
            if node.left is not self.nil:
                node = node.left
            else:
                node = node.right
        return count

    # Stampa l'altezza NERA
    def printBlackHeight(self):
        print "\nBlack height is:", self.getBlackHeight(self.root)
        print
