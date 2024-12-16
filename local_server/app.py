import random
import time

from flask import Flask, request, jsonify

from db_base import SQLiteActions

app = Flask(__name__)



@app.route('/students/', methods=['GET'])
def get_students():
    data = db.get_students()
    return jsonify(data), 200

@app.route('/students/<student_id>', methods=['GET'])
def get_student(student_id: str):

    if not student_id.isnumeric():
        return jsonify({'error': 'student_id should be int'}), 400

    data = db.get_student(student_id)
    if not data:
        return jsonify({'error': 'Student with this id does not exist'}), 404

    return jsonify(data), 200


@app.route('/students/', methods=['POST'])
def create_students():
    request_data = request.get_json()
    time.sleep(random.random() + 1.5) # sleep 1.5-2.5 sec
    error_msgs = []
    name = request_data.get('name')
    score = request_data.get('score', 0)

    if not name:
        error_msgs.append("You have to input name")
    if not 0 < score <= 100:
        error_msgs.append("Score must be between 1 and 100")

    if error_msgs:
        return jsonify(error_msgs), 400

    student = db.add_student(name=name, score=score)
    return jsonify(student), 200


@app.route('/students/<student_id>', methods=['PUT'])
def update_students(student_id):
    request_data = request.get_json()

    name = request_data.get('name')
    score = request_data.get('score')

    student = db.get_student(student_id)

    if not name and not score:
        return jsonify({'message': 'You have to put name and/or score of the student'}), 400

    name = name if name is not None else student['name']
    score = score if score is not None else student['score']
    student = db.update_student(student_id=student_id, name=name, score=score)
    return jsonify(student), 200


@app.route('/students/<student_id>', methods=['DELETE'])
def delete_student(student_id):

    db.delete_student(student_id)
    return jsonify({'message': f'Student {student_id} deleted'}), 204


if __name__ == '__main__':
    db = SQLiteActions('ololo.db')
    host = '127.0.0.1'
    port = 8080
    app.run(host=host, port=port, debug=True)