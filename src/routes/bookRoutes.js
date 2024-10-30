import { rateLimit } from 'express-rate-limit';

// Define rate limiter
const apiLimiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // Limit each IP to 100 requests per window
  message: 'Too many requests from this IP, please try again later'
});
import express from 'express';
import { getBookById, searchBooks, getFeaturedBooks } from '../controllers/bookController';

const router = express.Router();

// Apply rate limiting to routes
router.get('/books/:bookId', apiLimiter, getBookById);
router.get('/search', apiLimiter, searchBooks);
router.get('/featured', apiLimiter, getFeaturedBooks);
router.post('/books', apiLimiter, createBook); 