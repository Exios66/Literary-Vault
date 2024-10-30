import csv from 'csv-parser';
import fs from 'fs';

class QuestionAPI {
  constructor() {
    this.questions = [];
    this.categories = new Set();
    this.loadQuestions();
  }

  async loadQuestions() {
    const csvFiles = [
      'docs/Questions/CSV/psychology.csv',
      'docs/Questions/CSV/american-history-questions.csv',
      'external-resources/questions/Refined_Astronomy_Questions.csv',
      'external-resources/questions/Refined_Literature_Questions.csv',
      'external-resources/questions/Refined_Mathematics_Questions.csv'
    ];

    for (const filePath of csvFiles) {
      await new Promise((resolve, reject) => {
        fs.createReadStream(filePath)
          .pipe(csv())
          .on('data', (data) => {
            this.questions.push(data);
            this.categories.add(data['Knowledge Category'].toLowerCase());
          })
          .on('end', resolve)
          .on('error', reject);
      });
    }
  }

  getCategories() {
    return Array.from(this.categories);
  }

  getRandomQuestion() {
    const randomIndex = Math.floor(Math.random() * this.questions.length);
    return this.formatQuestion(this.questions[randomIndex]);
  }

  getCategoryQuestions(category) {
    const categoryQuestions = this.questions.filter(
      q => q['Knowledge Category'].toLowerCase() === category.toLowerCase()
    );
    return categoryQuestions.map(q => this.formatQuestion(q));
  }

  getCategoryStats(category) {
    const categoryQuestions = this.questions.filter(
      q => q['Knowledge Category'].toLowerCase() === category.toLowerCase()
    );

    const difficultyCount = {
      easy: 0,
      medium: 0,
      hard: 0
    };

    categoryQuestions.forEach(q => {
      const difficulty = this.getDifficultyLabel(parseInt(q.difficulty));
      difficultyCount[difficulty]++;
    });

    return {
      total_questions: categoryQuestions.length,
      difficulty_breakdown: difficultyCount,
      average_difficulty: this.getAverageDifficulty(difficultyCount)
    };
  }

  formatQuestion(q) {
    return {
      id: q.id,
      question: q.question,
      correct_answer: q.correct_answer,
      choices: [
        q.choice_1,
        q.choice_2,
        q.choice_3,
        q.correct_answer
      ].sort(() => Math.random() - 0.5),
      difficulty: this.getDifficultyLabel(parseInt(q.difficulty)),
      category: q['Knowledge Category'].toLowerCase(),
      topic: q['Topic Focus']
    };
  }

  getDifficultyLabel(difficulty) {
    const labels = ['easy', 'medium', 'hard', 'expert'];
    return labels[difficulty] || 'unknown';
  }

  getAverageDifficulty(difficultyCount) {
    const total = Object.values(difficultyCount).reduce((a, b) => a + b, 0);
    const weightedSum = difficultyCount.easy * 1 + 
                       difficultyCount.medium * 2 + 
                       difficultyCount.hard * 3;
    const average = weightedSum / total;
    
    if (average <= 1.5) return 'easy';
    if (average <= 2.5) return 'medium';
    return 'hard';
  }
}

// Export for OpenAI function calling
export const openAiFunctions = [
  {
    name: "get_categories",
    description: "Get all available question categories",
    parameters: {
      type: "object",
      properties: {}
    }
  },
  {
    name: "get_random_question",
    description: "Get a random question from any category",
    parameters: {
      type: "object",
      properties: {}
    }
  },
  {
    name: "get_category_questions",
    description: "Get questions from a specific category",
    parameters: {
      type: "object",
      properties: {
        category: {
          type: "string",
          description: "The category name (e.g., astronomy, literature, mathematics)"
        }
      },
      required: ["category"]
    }
  },
  {
    name: "get_category_stats",
    description: "Get statistics about questions in a category",
    parameters: {
      type: "object",
      properties: {
        category: {
          type: "string",
          description: "The category name (e.g., astronomy, literature, mathematics)"
        }
      },
      required: ["category"]
    }
  }
];

export const questionAPI = new QuestionAPI(); 