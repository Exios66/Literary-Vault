import { Router } from 'express';
import { rateLimit } from 'express-rate-limit';
import { body, param, query } from 'express-validator';
import { getBookById, searchBooks, getFeaturedBooks } from '../controllers/bookController';
import { getAllCategories } from '../controllers/categoryController';
import { authenticate } from '../middleware/auth';
import { validateRequest } from '../middleware/validation';

const router = Router();

// Rate limiting configuration
const apiLimiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // Limit each IP to 100 requests per window
  message: 'Too many requests from this IP, please try again later'
});

// Book routes
router.get('/books/:bookId', 
  apiLimiter,
  param('bookId').isMongoId(),
  validateRequest,
  getBookById
);

router.get('/search',
  apiLimiter,
  query('searchTerm').optional().trim().escape(),
  query('category').optional().trim().escape(),
  query('limit').optional().isInt({ min: 1, max: 100 }),
  validateRequest,
  searchBooks
);

router.get('/featured',
  apiLimiter,
  query('limit').optional().isInt({ min: 1, max: 20 }),
  validateRequest,
  getFeaturedBooks
);

router.post('/books',
  apiLimiter,
  authenticate,
  body('title').trim().notEmpty(),
  body('author').trim().notEmpty(),
  body('category').trim().notEmpty(),
  body('description').optional().trim(),
  body('publishedDate').optional().isISO8601(),
  validateRequest,
  createBook
);

router.put('/books/:bookId',
  apiLimiter,
  authenticate,
  param('bookId').isMongoId(),
  body('title').optional().trim().notEmpty(),
  body('author').optional().trim().notEmpty(),
  body('category').optional().trim().notEmpty(),
  body('description').optional().trim(),
  body('publishedDate').optional().isISO8601(),
  validateRequest,
  updateBook
);

router.delete('/books/:bookId',
  apiLimiter,
  authenticate,
  param('bookId').isMongoId(),
  validateRequest,
  deleteBook
);

// Category routes
router.get('/categories',
  apiLimiter,
  validateRequest,
  getAllCategories
);

router.post('/categories',
  apiLimiter,
  authenticate,
  body('name').trim().notEmpty(),
  body('description').optional().trim(),
  validateRequest,
  createCategory
);

router.put('/categories/:categoryId',
  apiLimiter,
  authenticate,
  param('categoryId').isMongoId(),
  body('name').optional().trim().notEmpty(),
  body('description').optional().trim(),
  validateRequest,
  updateCategory
);

router.delete('/categories/:categoryId',
  apiLimiter,
  authenticate,
  param('categoryId').isMongoId(),
  validateRequest,
  deleteCategory
);

// User routes
router.post('/users/register',
  apiLimiter,
  body('email').isEmail().normalizeEmail(),
  body('password').isLength({ min: 8 }),
  body('name').trim().notEmpty(),
  validateRequest,
  registerUser
);

router.post('/users/login',
  apiLimiter,
  body('email').isEmail().normalizeEmail(),
  body('password').notEmpty(),
  validateRequest,
  loginUser
);

router.get('/users/profile',
  apiLimiter,
  authenticate,
  validateRequest,
  getUserProfile
);

router.put('/users/profile',
  apiLimiter,
  authenticate,
  body('name').optional().trim().notEmpty(),
  body('email').optional().isEmail().normalizeEmail(),
  body('currentPassword').optional().notEmpty(),
  body('newPassword').optional().isLength({ min: 8 }),
  validateRequest,
  updateUserProfile
);

// Review routes
router.post('/books/:bookId/reviews',
  apiLimiter,
  authenticate,
  param('bookId').isMongoId(),
  body('rating').isInt({ min: 1, max: 5 }),
  body('comment').trim().notEmpty(),
  validateRequest,
  addReview
);

router.get('/books/:bookId/reviews',
  apiLimiter,
  param('bookId').isMongoId(),
  query('page').optional().isInt({ min: 1 }),
  query('limit').optional().isInt({ min: 1, max: 50 }),
  validateRequest,
  getBookReviews
);

router.put('/reviews/:reviewId',
  apiLimiter,
  authenticate,
  param('reviewId').isMongoId(),
  body('rating').optional().isInt({ min: 1, max: 5 }),
  body('comment').optional().trim().notEmpty(),
  validateRequest,
  updateReview
);

router.delete('/reviews/:reviewId',
  apiLimiter,
  authenticate,
  param('reviewId').isMongoId(),
  validateRequest,
  deleteReview
);

export default router;