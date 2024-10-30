import { Schema, model } from 'mongoose';

const categorySchema = new Schema({
  name: {
    type: String,
    required: true,
    unique: true
  },
  description: {
    type: String
  },
  createdAt: {
    type: Date,
    default: Date.now
  }
});

export default model('Category', categorySchema); 