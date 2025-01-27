from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def remove_beginning(self):
        if self.head is None:
            return None
        removed_data = self.head.data
        self.head = self.head.next
        return removed_data

    def remove_at_end(self):
        if self.head is None:
            return None
        if self.head.next is None:
            removed_data = self.head.data
            self.head = None
            return removed_data
        last_node = self.head
        while last_node.next and last_node.next.next:
            last_node = last_node.next
        removed_data = last_node.next.data
        last_node.next = None
        return removed_data

    def remove_at(self, data):
        if self.head is None:
            return None
        if self.head.data == data:
            removed_data = self.head.data
            self.head = self.head.next
            return removed_data
        current_node = self.head
        while current_node.next:
            if current_node.next.data == data:
                removed_data = current_node.next.data
                current_node.next = current_node.next.next
                return removed_data
            current_node = current_node.next
        return None

    def display(self):
        elements = []
        current_node = self.head
        while current_node:
            elements.append(current_node.data)
            current_node = current_node.next
        return elements

linked_list = LinkedList()

@app.route('/')
def home():
    return render_template('work.html')

@app.route('/append', methods=['POST'])
def append():
    data = request.form['data']
    linked_list.append(data)
    return jsonify({"message": f"Added {data} to the list", "list": linked_list.display()})

@app.route('/remove_beginning', methods=['POST'])
def remove_beginning():
    removed_data = linked_list.remove_beginning()
    if removed_data:
        return jsonify({"message": f"Removed {removed_data} from the beginning", "list": linked_list.display()})
    else:
        return jsonify({"message": "The list is empty", "list": linked_list.display()})

@app.route('/remove_at_end', methods=['POST'])
def remove_at_end():
    removed_data = linked_list.remove_at_end()
    if removed_data:
        return jsonify({"message": f"Removed {removed_data} from the end", "list": linked_list.display()})
    else:
        return jsonify({"message": "The list is empty", "list": linked_list.display()})

@app.route('/remove_at', methods=['POST'])
def remove_at():
    data = request.form['data']
    removed_data = linked_list.remove_at(data)
    if removed_data:
        return jsonify({"message": f"Removed {removed_data} from the list", "list": linked_list.display()})
    else:
        return jsonify({"message": f"{data} not found in the list", "list": linked_list.display()})

if __name__ == "__main__":
    app.run(debug=True)
