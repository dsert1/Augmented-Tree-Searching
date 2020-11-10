import random


#####################################
##### PLEASE DO NOT MODIFY THIS CODE
#####################################

class Node:

    # initialization
    def __init__(self, v=0, p=None, l=None, r=None):
        self.value = v
        self.parent = p
        self.left = l
        self.right = r
        self.size = 1
        if self.left != None:
            self.size += l.size
        if self.right != None:
            self.size += r.size

    # return the root of the tree
    def updateSize(self):
        nsize = 1
        if self.left != None:
            nsize += self.left.size
        if self.right != None:
            nsize += self.right.size
        if nsize != self.size:
            self.size = nsize
            if self.parent != None:
                return self.parent.updateSize()
            else:
                return self

    # set self as the left child of n
    def setLeft(self, n):
        assert (type(n) is Node)
        self.left = n
        n.parent = self
        self.updateSize()

    # set self as the right child of n
    def setRight(self, n):
        assert (type(n) is Node)
        self.right = n
        n.parent = self
        self.updateSize()

    # return true iff self is a root
    def isRoot(self):
        return (self.parent == None)

    # return true iff self is a leaf
    def isleaf(self):
        return (self.left == None and self.right == None)

    def subtreeMin(self):
        minNode = self
        while minNode.left != None:
            minNode = minNode.left
        return minNode

    def subtreeMax(self):
        maxNode = self
        while maxNode.right != None:
            maxNode = maxNode.right
        return maxNode

    # return the node immediately after self in the traversal order
    def successor(self):
        if self.right != None:  # return the first node of self.right subtree
            suc = self.right
            while (suc.left != None):
                suc = suc.left
            return suc
        if self.right == None:  # return an ancestor
            suc = self
            while (suc.parent != None and suc == suc.parent.right):
                suc = suc.parent
            return suc.parent

    # return the node immediately before self in the traversal order
    def predecessor(self):
        if self.left != None:  # return the first node of self.right subtree
            suc = self.left
            while (suc.right != None):
                suc = suc.right
            return suc
        if self.left == None:  # return an ancestor
            suc = self
            while (suc.parent != None and suc == suc.parent.left):
                suc = suc.parent
            return suc.parent

    # insert a value into the subtree of this node, return the node inserted
    # this function should only be called by the root of a tree!
    def insert(self, v):
        if v <= self.value:
            if self.left != None:
                return self.left.insert(v)
            else:
                n = Node(v)
                self.setLeft(n)
                return n
        else:
            if self.right != None:
                return self.right.insert(v)
            else:
                n = Node(v)
                self.setRight(n)
                return n

    # search for a value in the tree
    # return the node if found, else return last node we were on
    def search(self, v):
        if v == self.value:
            return self

        elif v < self.value and self.left != None:
            return self.left.search(v)

        elif v > self.value and self.right != None:
            return self.right.search(v)
        else:
            return self



    # delete self, return the root of the tree
    def delete(self):
        loop = 0
        while (True):
            numLeaves = (self.left != None) + (self.right != None)
            loop += 1
            assert (loop <= 2)
            if numLeaves == 0 and self.parent == None:
                return None
            if numLeaves == 0 and self.parent != None:
                if self.parent.left == self:
                    self.parent.left = None
                elif self.parent.right == self:
                    self.parent.right = None
                return self.parent.updateSize()
            elif numLeaves == 1 and self.parent == None:
                if self.left != None:
                    self.left.parent = None
                    return self.left
                if self.right != None:
                    self.right.parent = None
                    return self.right
            elif numLeaves == 1 and self.parent != None:
                if self.left != None:
                    self.left.parent = self.parent
                    if self.parent.left == self:
                        self.parent.left = self.left
                    elif self.parent.right == self:
                        self.parent.right = self.left
                    return self.parent.updateSize()
                if self.right != None:
                    self.right.parent = self.parent
                    if self.parent.left == self:
                        self.parent.left = self.right
                    elif self.parent.right == self:
                        self.parent.right = self.right
                    return self.parent.updateSize()
            else:
                suc = self.successor()
                assert (suc != None)
                # switch suc and self
                self.left.parent = suc
                self.right.parent = suc
                if suc.left != None:
                    suc.left.parent = self
                if suc.right != None:
                    suc.right.parent = self
                (s, p, l, r) = (self.size, self.parent, self.left, self.right)
                (self.size, self.parent, self.left, self.right) = (suc.size, suc.parent, suc.left, suc.right)
                (suc.size, suc.parent, suc.left, suc.right) = (s, p, l, r)

    # return the traversal order of self's subtree
    def traversalOrder(self):
        order = []
        if self.left != None:
            order += self.left.traversalOrder();
        order += [self.value]
        if self.right != None:
            order += self.right.traversalOrder();

        return order

    ###########################
    ##### YOUR CODE HERE ######
    ###########################

    def Rank(self, v):
        # return the number of nodes in self's subtree whose value is less than or equal to v

        # objective: find t. L, R, or at t?
        print('hi')
        old_v = v
        new_v = self.search(v)
        if new_v.value == self.value:
            if new_v.value > old_v:
                if self.left:
                    return 0 + self.left.size
                return 0
            if self.left:
                return 1 + self.left.size
            else:
                return 1

        if self.left:
            if new_v.value < self.value:
                return self.left.Rank(old_v)

        if self.right:
            if self.left:
                return 1 + self.left.size + self.right.Rank(old_v)
            else:
                return self.right.Rank(old_v) + 1



    def Find(self, i):
        # return the (i+1)^th node in the traversal order
        # Find(0) will return the smallest node, and Find(self.size - 1) will return the largest node
        assert (i < self.size and i >= 0)



        left_side = self.left.size if self.left else 0

        # BASE CASE

        if (i == left_side and i == 0) or i == left_side:
            return self.value


        if i < left_side:
            return self.left.Find(i)


        else:
            return self.right.Find(i-left_side-1)






#####################################
##### PLEASE DO NOT MODIFY THIS CODE
#####################################

def testTree(opr):
    root = None
    output = []

    for i in range(len(opr)):
        if opr[i][0] == "Reserve":
            if root == None:
                root = Node(opr[i][1])
            else:
                root.insert(opr[i][1])
        # print(opr[i])
        # print(root.traversalOrder())
        elif opr[i][0] == "Land":
            assert (root != None)
            earliestPlane = root.subtreeMin()
            root = earliestPlane.delete()
        # print(opr[i])
        # print(root.traversalOrder())
        elif opr[i][0] == "Rank":
            if root == None:
                output.append(0)
            else:
                output.append(root.Rank(opr[i][1]))
        # print(opr[i])
        # print(root.traversalOrder())
        elif opr[i][0] == "Find":
            if root == None:
                output.append(-1)
            else:
                output.append(root.Find(opr[i][1]))
        # print(opr[i])
        # print(root.traversalOrder())
        else:
            assert (False)

    return output


def main():
    print("hi")
    # passed
    # print('ans: ', testTree([('Reserve', 8058), ('Rank', 7973), ('Find', 0)]))
    # print('exp: ', [0, 8058])
    #
    # # passed
    # print('ans: ', testTree([('Reserve', 1953), ('Rank', 1298), ('Find', 0), ('Land', 0), ('Reserve', 5937), ('Rank', 6592), ('Find', 0)]))
    # print('exp: ', [0, 1953, 1, 5937])


    # print('ans: ', testTree([('Reserve', 110), ('Rank', 6300), ('Find', 0), ('Reserve', 7810), ('Rank', 9793), ('Find', 1), ('Land', 0), ('Reserve', 7217), ('Rank', 5466), ('Find', 0)]))
    # print('exp: ', [1, 110, 2, 7810, 0, 7217])

    # print('ans: ', testTree([('Reserve', 834), ('Rank', 8794), ('Find', 0), ('Reserve', 3094), ('Rank', 9449), ('Find', 1), ('Land', 0), ('Reserve', 6641), ('Rank', 8531), ('Find', 0), ('Reserve', 9150), ('Rank', 4209), ('Find', 1), ('Reserve', 2601), ('Rank', 2719), ('Find', 0), ('Land', 0), ('Reserve', 5541), ('Rank', 2169), ('Find', 3), ('Reserve', 9350), ('Rank', 6311), ('Find', 4), ('Reserve', 6942), ('Rank', 3236), ('Find', 4), ('Land', 0), ('Reserve', 7445), ('Rank', 8518), ('Find', 1), ('Reserve', 5213), ('Rank', 4711), ('Find', 2)]))
    # print('exp: ', [1, 834, 2, 3094, 2, 3094, 1, 6641, 1, 2601, 0, 9150, 2, 9350, 1, 9150, 4, 6641, 0, 6641])


    print('ans: ', testTree([('Reserve', 9319), ('Rank', 3168), ('Find', 0), ('Land', 0), ('Reserve', 6787), ('Rank', 333), ('Find', 0), ('Reserve', 2387), ('Rank', 3927), ('Find', 1), ('Reserve', 2092), ('Rank', 5615), ('Find', 1), ('Land', 0), ('Reserve', 4517), ('Rank', 5434), ('Find', 0), ('Reserve', 5405), ('Rank', 4341), ('Find', 2), ('Reserve', 6638), ('Rank', 4539), ('Find', 3), ('Land', 0), ('Reserve', 8798), ('Rank', 5506), ('Find', 4), ('Reserve', 5646), ('Rank', 2643), ('Find', 0), ('Reserve', 5588), ('Rank', 1242), ('Find', 3), ('Land', 0), ('Reserve', 4359), ('Rank', 7221), ('Find', 2), ('Reserve', 3973), ('Rank', 390), ('Find', 2), ('Reserve', 6899), ('Rank', 1455), ('Find', 3), ('Land', 0), ('Reserve', 2078), ('Rank', 2315), ('Find', 1), ('Reserve', 4731), ('Rank', 4732), ('Find', 6), ('Reserve', 9629), ('Rank', 3708), ('Find', 7), ('Land', 0), ('Reserve', 7016), ('Rank', 3879), ('Find', 4), ('Reserve', 3564), ('Rank', 2555), ('Find', 2), ('Reserve', 2863), ('Rank', 4003), ('Find', 7), ('Land', 0), ('Reserve', 1990), ('Rank', 5107), ('Find', 3)]))
    print('exp: ', [0, 9319, 0, 6787, 1, 6787, 2, 2387, 2, 2387, 1, 5405, 2, 6638, 2, 8798, 0, 4517, 0, 5646, 6, 5588, 0, 5405, 0, 5588, 1, 4359, 3, 6638, 1, 6787, 0, 5646, 0, 4731, 2, 6638, 4, 4731])




if __name__ == "__main__":
    main()