"""
Course CS2301 MW 1:30-2:50pm
Instructor:Fuentes, Olac
Tovar, Brianna
Date of last modification: 3/4/2019
4th Lab
This lab is over creating Binary Search Trees, printing them, and computing their
largest/smallest elements. Also, returning certain values contained in the tree.
"""
class BTree(object):
    # Constructor
    def __init__(self,item=[],child=[],isLeaf=True,max_items=5):  
        self.item = item
        self.child = child 
        self.isLeaf = isLeaf
        if max_items <3: #max_items must be odd and greater or equal to 3
            max_items = 3
        if max_items%2 == 0: #max_items must be odd and greater or equal to 3
            max_items +=1
        self.max_items = max_items

def FindChild(T,k):
    # Determines value of c, such that k must be in subtree T.child[c], if k is in the BTree
    c=0
    for i in T.item:
        if i>k:
            return c
        c +=1
    return len(T.item)
             
def InsertInternal(T,i):
    # T cannot be Full
    if T.isLeaf:
        InsertLeaf(T,i)
    else:
        k = FindChild(T,i)   
        if IsFull(T.child[k]):
            m, l, r = Split(T.child[k])
            T.item.insert(k,m) 
            T.child[k] = l
            T.child.insert(k+1,r) 
            k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
            
def Split(T):
    #print('Splitting')
    #PrintNode(T)
    mid = T.max_items//2
    if T.isLeaf:
        leftChild = BTree(T.item[:mid]) 
        rightChild = BTree(T.item[mid+1:]) 
    else:
        leftChild = BTree(T.item[:mid],T.child[:mid+1],T.isLeaf) 
        rightChild = BTree(T.item[mid+1:],T.child[mid+1:],T.isLeaf) 
    return T.item[mid], leftChild,  rightChild   
      
def InsertLeaf(T,i):
    T.item.append(i)  
    T.item.sort()

def IsFull(T):
    return len(T.item) >= T.max_items

def Insert(T,i):
    if not IsFull(T):
        InsertInternal(T,i)
    else:
        m, l, r = Split(T)
        T.item =[m]
        T.child = [l,r]
        T.isLeaf = False
        k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
        
def Search(T,k):
    # Returns node where k is, or None if k is not in the tree
    if k in T.item:
        return T
    if T.isLeaf:
        return None
    return Search(T.child[FindChild(T,k)],k)
                  
def Print(T):
    # Prints items in tree in ascending order
    if T.isLeaf:
        for t in T.item:
            print(t,end=' ')
    else:
        for i in range(len(T.item)):
            Print(T.child[i])
            print(T.item[i],end=' ')
        Print(T.child[len(T.item)])    
 
def PrintD(T,space):
    # Prints items and structure of B-tree
    if T.isLeaf:
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
    else:
        PrintD(T.child[len(T.item)],space+'   ')  
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
            PrintD(T.child[i],space+'   ')
    
def SearchAndPrint(T,k):
    node = Search(T,k)
    if node is None:
        print(k,'not found')
    else:
        print(k,'found',end=' ')
        print('node contents:',node.item)
        
        
def Height(T):
    if T.isLeaf:
        return 0
    return 1 + Height(T.child[0]) #child's height, added by 1 for root

def Extraction(T): #doesn't return correctly, only 0
    if T is None:
        return []
    if T.isLeaf:
        return T.item
    for i in range(len(T.child)):
        Extraction(T.child[i])
        return [i]
def Mini(T):
    return T.child[0].child[0].item[0] #basically leaf's smallest
        
def Max(T):
    return T.child[len(T.item)].child[len(T.item)+1].item[len(T.item)+1] #leaf's largest
        
def NumAtDepth(T,s): #returns right only for root
    count=0
    if s==0:
        return 1
    else:
        for i in range(len(T.child)):
            count+=NumAtDepth(T.child[i],s-1)
            return count
        
def PrintDepth(T,d):
    if d==0:
        return T.item
    if T.isLeaf:
        return T.item
    return  T.child[d-1].item, T.child[d].item #prints both children at depth
        
def NumNodeFull(T):#returns None, tree doesn't have any full
    if T.isLeaf:
        return 0
    if len(T.item)==T.max_items: #checks if the item is full, then will return method if is to check the rest
        return 1+NumNodeFull(T.child)
        
def NumLeavesFull(T):
    count=0
    if T.isLeaf:
        if len(T.item)==T.max_items:
            return 1
        else:
            return 0
        count+=NumLeavesFull(T.child[len(T.item)]) #goes through rest of tree's items
        return count
        
def SearchDepth(T,k): #doesn't return if k is None
    if k==T.item[0]:
        return 0
    return 1
        
L = [30, 50, 10, 20, 60, 70, 100, 40, 90, 80, 110, 120, 1, 11 , 3, 4, 5,105, 115, 200, 2, 45, 6]
T = BTree()    
for i in L:
    print('Inserting',i)
    Insert(T,i)
    PrintD(T,'') 
    #Print(T)
    print('\n####################################')
    
#SearchAndPrint(T,60)

print('1: Height:',Height(T))
print("2: Extract:",Extraction(T)) #wrong output
print('3: Smallest:',Mini(T))
print('4: Largest:',Max(T))
print('5: Amount at Depth:',NumAtDepth(T,0)) #only root correct
print('6: Printing Nodes in Depth:',PrintDepth(T,1))
print('7: Number of Nodes Full:',NumNodeFull(T))
print('8: Leaves full in tree:',NumLeavesFull(T))
print('9: Searching depth of k:', SearchDepth(T,10)) #forgot a return for k is None
