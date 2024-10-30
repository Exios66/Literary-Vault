import express from 'express';
import csv from 'csv-parser';
import fs from 'fs';

const router = express.Router();
const allQuestions = [];

// CSV files paths
const csvFiles = [
  'docs/Questions/CSV/psychology.csv',
  'docs/Questions/CSV/american-history-questions.csv',
  'external-resources/questions/Refined_Astronomy_Questions.csv',
  'external-resources/questions/Refined_Literature_Questions.csv',
  'external-resources/questions/Refined_Mathematics_Questions.csv'
];

// Load questions when server starts
const loadQuestions = async () => {
  for (const filePath of csvFiles) {
    await new Promise((resolve, reject) => {
      fs.createReadStream(filePath)
        .pipe(csv())
        .on('data', (data) => allQuestions.push(data))
        .on('end', resolve)
        .on('error', reject);
    });
  }
  console.log(`Loaded ${allQuestions.length} questions`);
};

loadQuestions();

// GET all questions
router.get('/', (req, res) => {
  res.json(allQuestions);
});

// GET questions by category
router.get('/category/:category', (req, res) => {
  const category = req.params.category;
  const filteredQuestions = allQuestions.filter(q => q['Knowledge Category'] === category);
  res.json(filteredQuestions);
}); 