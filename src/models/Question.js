import { Schema, model } from 'mongoose';

const questionSchema = new Schema({
  id: {
    type: Number,
    required: true,
    unique: true
  },
  question: {
    type: String,
    required: true
  },
  correct_answer: {
    type: String,
    required: true
  },
  choice_1: {
    type: String,
    required: true
  },
  choice_2: {
    type: String,
    required: true
  },
  choice_3: {
    type: String,
    required: true
  },
  difficulty: {
    type: Number,
    required: true,
    min: 1,
    max: 3
  },
  knowledgeCategory: {
    type: String,
    required: true
  },
  topicFocus: {
    type: String,
    required: true
  }
});

const Question = model('Question', questionSchema);

export const find = Question.find.bind(Question);
export const findById = Question.findById.bind(Question);
export const create = Question.create.bind(Question);

export default Question; 