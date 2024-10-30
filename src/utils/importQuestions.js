import csv from 'csv-parser';
import fs from 'fs';

const csvFiles = [
  'docs/Questions/CSV/psychology.csv',
  'docs/Questions/CSV/american-history-questions.csv',
  'external-resources/questions/Refined_Astronomy_Questions.csv',
  'external-resources/questions/Refined_Literature_Questions.csv',
  'external-resources/questions/Refined_Mathematics_Questions.csv'
];

const allResults = [];

// Process each CSV file
csvFiles.forEach(filePath => {
  fs.createReadStream(filePath)
    .pipe(csv())
    .on('data', (data) => allResults.push(data))
    .on('end', () => {
      console.log(`Finished reading ${filePath}`);
      console.log(`Total questions loaded: ${allResults.length}`);
    })
    .on('error', (error) => {
      console.error(`Error reading ${filePath}:`, error);
    });
}); 