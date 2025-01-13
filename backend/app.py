from flask import Flask, jsonify, request
from flask_cors import CORS
from dsalogic.LinkedList import LinkedList
from dsalogic.DoublyLinkedList import DblLinkedList
from dsalogic.Queue import Queue

app = Flask(__name__)
CORS(app, origins='*')

@app.route('/', methods=['GET'])
def get_data():
    return jsonify({"message": "Hello world!"})

@app.route('/linkedlist', methods=['POST'])
def create_linked_list():
    data = request.get_json()
    values = data.get('values', [])
    if not values:
        return jsonify({'error': "List is empty"}, 400)
    linked_list = LinkedList()
    for val in values:
        linked_list.append(val)
    return jsonify(linked_list.export())

@app.route('/doublylinkedlist', methods=['POST'])
def create_doubly_linked_list():
    data = request.get_json()
    values = data.get('values', [])
    if not values:
        return jsonify({'error': "List is empty"}, 400)
    doubly_linked_list = DblLinkedList()
    for val in values:
        doubly_linked_list.append(val)
    return jsonify(doubly_linked_list.export())

@app.route('/queue', methods=['POST'])
def create_queue():
    data = request.get_json()
    values = data.get('values', [])
    if not values:
        return jsonify({'error': 'Queue is empty'}, 400)
    queue = Queue()
    for val in vals:
        Queue.enqueue(val)
    return jsonify(queue)


if __name__ == '__main__':
    app.run(port=8000, debug=True)