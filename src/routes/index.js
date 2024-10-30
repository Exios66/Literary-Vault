import { Router } from 'express';
const router = Router();
import { getBookById, searchBooks, getFeaturedBooks } from '../controllers/bookController';
import { getAllCategories } from '../controllers/categoryController';

// Book routes
router.get('/books/:bookId', getBookById);
router.get('/search', searchBooks);
router.get('/featured', getFeaturedBooks);

// Category routes
router.get('/categories', getAllCategories);

export default router; 