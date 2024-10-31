from flask import Blueprint

from src.core import questions

bp = Blueprint('questions', __name__)

from flask import jsonify, request
from src.models.database import db
from src.models.answer import Answer
from src.utils.auth import login_required

@bp.route('/questions', methods=['GET'])
def get_questions():
    questions = questions.query.all()
    return jsonify([q.to_dict() for q in questions])

@bp.route('/questions/<int:question_id>', methods=['GET']) 
def get_question(question_id):
    question = question.query.get_or_404(question_id)
    return jsonify(question.to_dict())

@bp.route('/questions', methods=['POST'])
@login_required
def create_question():
    data = request.get_json()
    
    if not data or 'title' not in data or 'content' not in data:
        return jsonify({'error': 'Missing required fields'}), 400
        
    question = question(
        title=data['title'],
        content=data['content'],
        user_id=request.user.id
    )
    
    db.session.add(question)
    db.session.commit()
    
    return jsonify(question.to_dict()), 201

@bp.route('/questions/<int:question_id>', methods=['PUT'])
@login_required
def update_question(question_id):
    question = question.query.get_or_404(question_id)
    
    if question.user_id != request.user.id:
        return jsonify({'error': 'Unauthorized'}), 403
        
    data = request.get_json()
    
    if 'title' in data:
        question.title = data['title']
    if 'content' in data:
        question.content = data['content']
        
    db.session.commit()
    
    return jsonify(question.to_dict())

@bp.route('/questions/<int:question_id>', methods=['DELETE'])
@login_required
def delete_question(question_id):
    question = question.query.get_or_404(question_id)
    
    if question.user_id != request.user.id:
        return jsonify({'error': 'Unauthorized'}), 403
        
    db.session.delete(question)
    db.session.commit()
    
    return '', 204

@bp.route('/questions/<int:question_id>/answers', methods=['GET'])
def get_question_answers(question_id):
    answers = Answer.query.filter_by(question_id=question_id).all()
    return jsonify([a.to_dict() for a in answers])

@bp.route('/questions/<int:question_id>/answers', methods=['POST'])
@login_required
def create_answer(question_id):
    questions.query.get_or_404(question_id)  # Verify question exists
    
    data = request.get_json()
    
    if not data or 'content' not in data:
        return jsonify({'error': 'Missing required fields'}), 400
        
    answer = Answer(
        content=data['content'],
        question_id=question_id,
        user_id=request.user.id
    )
    
    db.session.add(answer)
    db.session.commit()
    
    return jsonify(answer.to_dict()), 201