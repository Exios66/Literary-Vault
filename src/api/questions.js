import Papa from 'papaparse';

class QuestionAPI {
  constructor() {
    this.questions = [];
    this.categories = new Set();
    this.basePath = 'https://raw.githubusercontent.com/Exios66/Literary-Vault/main/';
    this.loadQuestions();
  }

  async loadQuestions() {
    const csvFiles = [
      `${this.basePath}docs/Questions/CSV/psychology.csv`,
      `${this.basePath}docs/Questions/CSV/american-history-questions.csv`,
      `${this.basePath}external-resources/questions/Refined_Astronomy_Questions.csv`,
      `${this.basePath}external-resources/questions/Refined_Literature_Questions.csv`,
      `${this.basePath}external-resources/questions/Refined_Mathematics_Questions.csv`
    ];

    try {
      for (const file of csvFiles) {
        const response = await fetch(file);
        if (!response.ok) {
          console.error(`Failed to load ${file}: ${response.statusText}`);
          continue;
        }
        
        const csvText = await response.text();
        const results = Papa.parse(csvText, { 
          header: true,
          skipEmptyLines: true
        });
        
        if (results.errors.length > 0) {
          console.warn(`Parsing warnings for ${file}:`, results.errors);
        }

        results.data.forEach(question => {
          if (question.question && question.correct_answer) {
            this.questions.push(question);
            const category = question['Knowledge Category']?.toLowerCase() || 
                           this.getCategoryFromFilename(file);
            this.categories.add(category);
          }
        });
      }
      
      console.log(`Loaded ${this.questions.length} questions from ${csvFiles.length} files`);
      console.log('Available categories:', Array.from(this.categories));
      
    } catch (error) {
      console.error('Error loading questions:', error);
    }
  }

  getCategoryFromFilename(filepath) {
    const filename = filepath.split('/').pop().toLowerCase();
    if (filename.includes('psychology')) return 'psychology';
    if (filename.includes('history')) return 'american-history';
    if (filename.includes('astronomy')) return 'astronomy';
    if (filename.includes('literature')) return 'literature';
    if (filename.includes('mathematics')) return 'mathematics';
    return 'unknown';
  }

  getCategories() {
    return Array.from(this.categories);
  }

  getRandomQuestion() {
    const randomIndex = Math.floor(Math.random() * this.questions.length);
    return this.formatQuestion(this.questions[randomIndex]);
  }

  getCategoryQuestions(category) {
    return this.questions.filter(q => 
      q['Knowledge Category']?.toLowerCase() === category.toLowerCase()
    ).map(this.formatQuestion);
  }

  getCategoryStats(category) {
    const categoryQuestions = this.getCategoryQuestions(category);
    return {
      total_questions: categoryQuestions.length,
      difficulty_breakdown: this.getDifficultyBreakdown(categoryQuestions),
      average_difficulty: this.calculateAverageDifficulty(categoryQuestions)
    };
  }

  formatQuestion(question) {
    return {
      id: question.id || `Q${Math.random().toString(36).substr(2, 9)}`,
      question: question.question,
      category: question['Knowledge Category']?.toLowerCase() || 'unknown',
      difficulty: question.difficulty || 'medium',
      correct_answer: question.correct_answer,
      options: question.options?.split('|') || []
    };
  }
}

export const questionAPI = new QuestionAPI();
export const openAiFunctions = [
  {
    name: "get_categories",
    description: "Get all available question categories",
    parameters: { type: "object", properties: {} }
  },
  {
    name: "get_random_question",
    description: "Get a random question from any category",
    parameters: { type: "object", properties: {} }
  },
  {
    name: "get_category_questions",
    description: "Get questions from a specific category",
    parameters: {
      type: "object",
      properties: {
        category: {
          type: "string",
          description: "The category name (e.g., astronomy, literature)"
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
          description: "The category name (e.g., astronomy, literature)"
        }
      },
      required: ["category"]
    }
  }
]; 