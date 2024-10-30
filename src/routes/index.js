import { Router } from 'express';
const router = Router();
import { getBookById, searchBooks, getFeaturedBooks } from '../controllers/bookController';
import { getAllCategories } from '../controllers/categoryController';

// Book routes
router.get('/books/:bookId', getBookById);
router.get('/search', searchBooks);
router.get('/featured', getFeaturedBooks);
router.post('/books', createBook);
router.put('/books/:bookId', updateBook);
router.delete('/books/:bookId', deleteBook);

// Category routes
router.get('/categories', getAllCategories);
router.post('/categories', createCategory);
router.put('/categories/:categoryId', updateCategory);
router.delete('/categories/:categoryId', deleteCategory);

// User routes
router.post('/users/register', registerUser);
router.post('/users/login', loginUser);
router.get('/users/profile', getUserProfile);
router.put('/users/profile', updateUserProfile);

// Review routes
router.post('/books/:bookId/reviews', addReview);
router.get('/books/:bookId/reviews', getBookReviews);
router.put('/reviews/:reviewId', updateReview);
router.delete('/reviews/:reviewId', deleteReview);

export default router;