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

const Book = model('Book', bookSchema);

export const find = Book.find.bind(Book);
export const findById = Book.findById.bind(Book);
export const create = Book.create.bind(Book);

export default Book; 