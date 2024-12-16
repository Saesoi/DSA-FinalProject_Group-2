from flask import Flask, request, render_template

app = Flask(__name__)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        return self.top.data if self.top else None

    def is_empty(self):
        return self.top is None

def infix_to_postfix(infix):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = Stack()
    postfix = ""
    steps = []

    for char in infix.replace(" ", ""):
        if char.isalnum():  # Operand
            postfix += char
            steps.append(postfix)
        elif char in precedence:  # Operator
            while (not stack.is_empty() and
                   precedence.get(stack.peek(), 0) >= precedence[char]):
                postfix += stack.pop()
                steps.append(postfix)
            stack.push(char)
        elif char == '(':
            stack.push(char)
        elif char == ')':
            while stack.peek() != '(':
                postfix += stack.pop()
                steps.append(postfix)
            stack.pop()  # Pop '('

    while not stack.is_empty():
        postfix += stack.pop()
        steps.append(postfix)

    return steps

@app.route('/', methods=['GET'])
def home():
    return render_template('stack.html', steps=None)

@app.route('/convert', methods=['POST'])
def convert():
    infix = request.form['infix']
    steps = infix_to_postfix(infix)
    return render_template('stack.html', steps=steps)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
