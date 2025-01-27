from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if not self.rear:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if not self.front:
            return "Queue is empty"
        temp = self.front
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return temp.data

    def get_queue(self):
        queue_elements = []
        current = self.front
        while current:
            queue_elements.append(current.data)
            current = current.next
        return queue_elements

class Deque:
    def __init__(self):
        self.front = None
        self.rear = None

    def append_left(self, data):
        new_node = Node(data)
        if not self.front:
            self.front = self.rear = new_node
            return
        new_node.next = self.front
        self.front = new_node

    def append_right(self, data):
        new_node = Node(data)
        if not self.rear:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def pop_left(self):
        if not self.front:
            return "Deque is empty"
        temp = self.front
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return temp.data

    def pop_right(self):
        if not self.rear:
            return "Deque is empty"
        current = self.front
        while current.next != self.rear:
            current = current.next
        temp = self.rear
        self.rear = current
        current.next = None
        return temp.data

    def get_deque(self):
        deque_elements = []
        current = self.front
        while current:
            deque_elements.append(current.data)
            current = current.next
        return deque_elements

queue = Queue()
deque = Deque()

@app.route('/')
def home():
    return render_template('queue.html')

@app.route('/enqueue', methods=['POST'])
def enqueue():
    data = request.form.get('data')
    queue.enqueue(data)
    return jsonify(queue.get_queue())

@app.route('/dequeue', methods=['POST'])
def dequeue():
    return jsonify(queue.dequeue())

@app.route('/append_left', methods=['POST'])
def append_left():
    data = request.form.get('data')
    deque.append_left(data)
    return jsonify(deque.get_deque())

@app.route('/append_right', methods=['POST'])
def append_right():
    data = request.form.get('data')
    deque.append_right(data)
    return jsonify(deque.get_deque())

@app.route('/pop_left', methods=['POST'])
def pop_left():
    return jsonify(deque.pop_left())

@app.route('/pop_right', methods=['POST'])
def pop_right():
    return jsonify(deque.pop_right())

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5003)
