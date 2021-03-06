class BinTreeNode(object):
 
    def __init__(self, value):
      
        self.value=value
        self.left=None
        self.right=None
 
       
def tree_insert(tree, item):
    if tree==None:
        tree=BinTreeNode(item)
    else:
        if(item < tree.value):
            if(tree.left==None):
                tree.left=BinTreeNode(item)
            else:
                tree_insert(tree.left,item)
        else:
            if(tree.right==None):
                tree.right=BinTreeNode(item)
            else:
                tree_insert(tree.right,item)
    return(tree)
 
def postorder(tree):
    if(tree.left!=None):
        postorder(tree.left)
    if(tree.right!=None):
        postorder(tree.right)
    print(tree.value)
 
 
def in_order(tree):
  inOrderStack = []
  inOrderList = []

  currentNode = tree

  complete = False #condition to end the while loop

  while complete == False:
    if currentNode is not None:
      inOrderStack.append(currentNode) #add node to stack
      currentNode = currentNode.left #follow left hand side of tree

    else:
      if len(inOrderStack) > 0: #if an element is in the stack
        currentNode = inOrderStack.pop() #pop off the top of stack and make the current node
        inOrderList.append(currentNode.value) #append the value of the current node to the final list
        currentNode = currentNode.right #and then go down the right hand side of the branch

      else:
        complete = True

  print("In Order List >> " + str(inOrderList))
  
  
 
if __name__ == '__main__':
   
  t=tree_insert(None,6);
  tree_insert(t,10)
  tree_insert(t,5)
  tree_insert(t,2)
  tree_insert(t,3)
  tree_insert(t,4)
  tree_insert(t,11)
  in_order(t)
