import express from 'express';
import { rateLimit } from 'express-rate-limit';
import {
  getAllQuestions,
  getQuestionById,
  getQuestionsByCategory,
  getQuestionsByDifficulty,
  getRandomQuestions
} from '../controllers/questionController';

const router = express.Router();

const apiLimiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100,
  message: 'Too many requests from this IP, please try again later'
});

router.get('/questions', apiLimiter, getAllQuestions);
router.get('/questions/random', apiLimiter, getRandomQuestions);
router.get('/questions/category/:category', apiLimiter, getQuestionsByCategory);
router.get('/questions/difficulty/:difficulty', apiLimiter, getQuestionsByDifficulty);
router.get('/questions/:id', apiLimiter, getQuestionById);

export default router; 