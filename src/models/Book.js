import { Schema, model } from 'mongoose';

const bookSchema = new Schema({
  title: {
    type: String,
    required: true
  },
  author: {
    type: String,
    required: true
  },
  category: {
    type: String,
    required: true
  },
  description: {
    type: String
  },
  publishedDate: {
    type: Date
  },
  isFeatured: {
    type: Boolean,
    default: false
  }
});

export default model('Book', bookSchema); 