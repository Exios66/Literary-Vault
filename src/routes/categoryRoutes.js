import express from 'express';
import { getAllCategories } from '../controllers/categoryController';
import { rateLimit } from 'express-rate-limit';

const router = express.Router();

const apiLimiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100,
  message: 'Too many requests from this IP, please try again later'
});

router.get('/categories', apiLimiter, getAllCategories);

export default router; 