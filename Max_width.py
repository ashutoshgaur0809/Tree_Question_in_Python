from queue import Queue

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def width_of_binary_tree(root):
    if not root:
        return 0
    
    ans = 0
    q = Queue()
    # initialize root node in 0 index of queue
    q.put((root, 0))
    
    while not q.empty():
        size = q.qsize()
        cur_min = q.queue[0][1]
        left_most, right_most = 0, 0
        
        for i in range(size):
            cur_node, cur_id = q.get()
            cur_id = cur_id - cur_min  # subtracted to prevent integer overflow
            
            if i == 0:
                left_most = cur_id
            if i == size - 1:
                right_most = cur_id
            
            if cur_node.left:
                q.put((cur_node.left, cur_id * 2 + 1))
            if cur_node.right:
                q.put((cur_node.right, cur_id * 2 + 2))
        
        ans = max(ans, right_most - left_most + 1)
    
    return ans



if __name__ == "__main__":
    root = Node(1)
    root.left = Node(3)
    root.left.left = Node(5)
    root.left.left.left = Node(7)
    root.right = Node(2)
    root.right.right = Node(4)
    root.right.right.right = Node(6)

    max_width = width_of_binary_tree(root)
    print(f"The maximum width of the Binary Tree is {max_width}")
