class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def add_child(self,data):
        if self.data == data:
            return #node is already exists and we know similar node not contained in BST
        # insertion in left Zone
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:    
                self.left = Node(data) #iska matlab agar left None mtlab left me kuch nhi toh left node ke liye Node class 
                #call hogi jise left node me data pass ho jayga aur left node as root node work krega aur uske left aur right me none hoga
        # insetrion in right zone
        if data > self.data:
            if self.right:
                self.right.add_child(data)
            else:    
                self.right = Node(data)  
              
    def in_order_traversal(self):
        elements = []
        if self.left:
            elements = elements + self.left.in_order_traversal() 

        elements.append(self.data)

        if self.right:
            elements = elements + self.right.in_order_traversal() 

        return elements 
       
    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum 
    
    def search(self,val):
        if val == self.data:
            return True
        if val < self.data:
            if self.left:
                 return self.left.search(val)
            else:
                return False
        if val > self.data:
            if self.right:
                 return self.right.search(val)
            else:
                return False
             
            
            
                
def build_tree(elements):
    print("Building tree with these elements:",elements)
    root = Node(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root  
                    

       
       
       
if __name__ == "__main__":   
    numbers_tree = build_tree(list(map(int,input("Enter No >").split())))
    # we also perform bST with strings.
    while(True):   
       ch = int(input("Enter Your Choice ->>>>>>> 1.Traversal 2.Search 3.Min Max Sum 4.Deletion"))
       if ch == 1:
           print("In order traversal gives this sorted list:",numbers_tree.in_order_traversal())
           print("Post Order traversal:",numbers_tree.post_order_traversal())
           print("Pre Order traversal:",numbers_tree.pre_order_traversal())
       if ch == 2:
               print("Search ---->",numbers_tree.search(int(input("Enter Value You weant to seacrh ->"))))
       if ch == 3:
              print("Min -->",numbers_tree.find_min())        
              print("Max -->",numbers_tree.find_max())        
              print("Total -->",numbers_tree.calculate_sum())
       if ch == 4:
           pass               
    
     
    
    
             