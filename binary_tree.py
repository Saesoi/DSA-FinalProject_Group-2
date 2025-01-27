from flask import Flask, request, render_template

# Define TreeNode and BinaryTree classes
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinaryTree:
    def search(self, root, key):
        """
        Search for a key in the binary tree.
        """
        if root is None or root.val == key:
            return root

        if key < root.val:
            return self.search(root.left, key)
        return self.search(root.right, key)

    def delete_node(self, root, key):
        """
        Delete a node with the given key from the binary tree.
        """
        if root is None:
            return root

        if key < root.val:
            root.left = self.delete_node(root.left, key)
        elif key > root.val:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            min_larger_node = self.get_min(root.right)
            root.val = min_larger_node.val
            root.right = self.delete_node(root.right, min_larger_node.val)

        return root

    def get_min(self, node):
        """
        Get the node with the smallest value greater than the current node.
        """
        current = node
        while current.left is not None:
            current = current.left
        return current

    def add_node(self, root, key):
        """
        Add a new node with the given key to the binary tree.
        """
        if root is None:
            return TreeNode(key)

        if key < root.val:
            root.left = self.add_node(root.left, key)
        else:
            root.right = self.add_node(root.right, key)

        return root

    def in_order(self, root):
        """
        In-order traversal of the binary tree to get sorted keys.
        """
        if root is None:
            return []
        return self.in_order(root.left) + [root.val] + self.in_order(root.right)

# Initialize the binary tree and create the root node
app = Flask(__name__)
tree = BinaryTree()
root = TreeNode(50)
root.left = TreeNode(30)
root.right = TreeNode(70)

@app.route('/', methods=['GET', 'POST'])
def home():
    global root  # Declare 'root' as global before accessing or modifying it
    message = None
    if request.method == 'POST':
        key = request.form['key']
        
        # Validate the input
        try:
            key = int(key)  # Convert to integer
        except ValueError:
            message = "Please enter a valid number."
        
        if message is None:
            # Check which form was submitted: search, delete, or add
            action = request.form['action']
            if action == 'search':
                result = tree.search(root, key)
                if result:
                    message = f"Key {key} found in the binary tree."
                else:
                    message = f"Key {key} not found in the binary tree."
            elif action == 'delete':
                root = tree.delete_node(root, key)  # Modify the root node
                message = f"Key {key} deleted from the binary tree."
            elif action == 'add':
                root = tree.add_node(root, key)  # Add the new node
                message = f"Key {key} added to the binary tree."
    
    # Get the sorted nodes for display (in-order traversal)
    nodes = tree.in_order(root)
    
    # Render the template and pass the message and tree nodes
    return render_template('binary-tree.html', message=message, nodes=nodes)

if __name__ == "__main__":
    app.run(debug=True, port=5004)
