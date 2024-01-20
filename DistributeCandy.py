#User function Template for python3



'''

class Node:

    def __init__(self, val):

        self.right = None

        self.data = val

        self.left = None

'''



class Solution:

    def __init__(self):

        self.total_moves = 0

    def distributeCandy(self, root):

        def distribute_helper(node):

            # Base case: If the node is None, return 0

            if not node:

                return 0

           

            # Recursive calls for left and right subtrees

            left_count = distribute_helper(node.left)

            right_count = distribute_helper(node.right)

           

            # Calculate moves for the current node

            self.total_moves += abs(left_count) + abs(right_count)

           

            # Return the total candy count for the current node

            return left_count + node.data + right_count - 1



        # Start the candy distribution process

        distribute_helper(root)

       

        # Return the total moves required

        return self.total_moves
