from flask import Flask, render_template, request

app = Flask(__name__)

class LinkedList:
    def __init__(self):
        self.head = None

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def insert_at_beginning(self, data):
        new_node = self.Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = self.Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def remove_beginning(self):
        if not self.head:
            return "List is empty. Nothing to remove."
        removed_data = self.head.data
        self.head = self.head.next
        return f"Removed {removed_data} from the beginning of the list."

    def remove_at_end(self):
        if not self.head:
            return "List is empty. Nothing to remove."
        if not self.head.next:
            removed_data = self.head.data
            self.head = None
            return f"Removed {removed_data} from the end of the list."
        current = self.head
        while current.next and current.next.next:
            current = current.next
        removed_data = current.next.data
        current.next = None
        return f"Removed {removed_data} from the end of the list."

    def remove_at(self, data):
        if not self.head:
            return "List is empty. Nothing to remove."
        if self.head.data == data:
            self.head = self.head.next
            return f"Removed {data} from the list."
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        if not current.next:
            return f"{data} not found in the list."
        current.next = current.next.next
        return f"Removed {data} from the list."

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def print_list(self):
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        return "\n".join(result) if result else "List is empty."


linked_list = LinkedList()

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        operation = request.form['operation']
        data = request.form.get('data', '').strip()

        if operation == "remove_beginning":
            result = linked_list.remove_beginning()
        elif operation == "remove_at_end":
            result = linked_list.remove_at_end()
        elif operation == "remove_at":
            result = linked_list.remove_at(data)
        elif operation == "insert_at_beginning":
            linked_list.insert_at_beginning(data)
            result = f"Inserted {data} at the beginning of the list."
        elif operation == "insert_at_end":
            linked_list.insert_at_end(data)
            result = f"Inserted {data} at the end of the list."
        elif operation == "search":
            result = f"Found {data} in the list." if linked_list.search(data) else f"{data} not found in the list."

    return render_template('work.html', result=result, linked_list=linked_list.print_list())

if __name__ == '__main__':
    app.run(debug=True, port=5000)
