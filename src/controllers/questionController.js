import Question from '../models/Question';

export const getAllQuestions = async (req, res) => {
  try {
    const questions = await Question.find();
    res.json(questions);
  } catch (error) {
    res.status(500).json({ message: 'Server error' });
  }
};

export const getQuestionById = async (req, res) => {
  try {
    const question = await Question.findById(req.params.id);
    if (!question) {
      return res.status(404).json({ message: 'Question not found' });
    }
    res.json(question);
  } catch (error) {
    res.status(500).json({ message: 'Server error' });
  }
};

export const getQuestionsByCategory = async (req, res) => {
  try {
    const { category } = req.params;
    const questions = await Question.find({ knowledgeCategory: category });
    res.json(questions);
  } catch (error) {
    res.status(500).json({ message: 'Server error' });
  }
};

export const getQuestionsByDifficulty = async (req, res) => {
  try {
    const { difficulty } = req.params;
    const questions = await Question.find({ difficulty: Number(difficulty) });
    res.json(questions);
  } catch (error) {
    res.status(500).json({ message: 'Server error' });
  }
};

export const getRandomQuestions = async (req, res) => {
  try {
    const { limit = 10 } = req.query;
    const questions = await Question.aggregate([
      { $sample: { size: Number(limit) } }
    ]);
    res.json(questions);
  } catch (error) {
    res.status(500).json({ message: 'Server error' });
  }
}; 