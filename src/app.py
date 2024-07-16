from flask import Flask, jsonify, request
from datastructures import FamilyStructure

app = Flask(__name__)


jackson_family = FamilyStructure('Jackson')

@app.route('/members', methods=['GET'])
def get_all_members():
    try:
        members = jackson_family.get_all_members()
        return jsonify(members), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/member/<int:member_id>', methods=['GET'])
def get_member(member_id):
    try:
        member = jackson_family.get_member(member_id)
        if member:
            return jsonify(member), 200
        else:
            return jsonify({"error": "Member not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/member', methods=['POST'])
def add_member():
    try:
        member = request.get_json()
        if not member or not isinstance(member, dict) or 'first_name' not in member or 'age' not in member or 'lucky_numbers' not in member:
            return jsonify({"error": "Invalid member data"}), 400

        jackson_family.add_member(member)
        return jsonify({"message": "Member added successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    try:
        jackson_family.delete_member(member_id)
        return jsonify({"done": True}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
