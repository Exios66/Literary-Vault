import express from 'express';
import questionsRouter from './routes/questions.js';

const app = express();

app.use(express.json());
app.use('/api/questions', questionsRouter);

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
}); 