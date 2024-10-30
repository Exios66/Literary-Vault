const Book = require('../models/Book');

exports.getBookById = async (req, res) => {
  try {
    const book = await Book.findById(req.params.bookId);
    if (!book) {
      return res.status(404).json({ error: "Book not found" });
    }
    res.json(book);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

exports.searchBooks = async (req, res) => {
  try {
    const { searchTerm, category, limit = 10 } = req.query;
    let query = {};
    
    if (searchTerm) {
      const sanitizedTerm = searchTerm
        .replace(/[.*+?^${}()|[\]\\]/g, '\\$&')
        .slice(0, 100);
      
      query.$or = [
        { title: new RegExp(sanitizedTerm, 'i') },
        { author: new RegExp(sanitizedTerm, 'i') }
      ];
    }
    
    if (category) {
      query.category = category;
    }
    
    const books = await Book.find(query).limit(parseInt(limit));
    res.json(books);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

exports.getFeaturedBooks = async (req, res) => {
  try {
    const { limit = 5 } = req.query;
    const books = await Book.find({ isFeatured: true }).limit(parseInt(limit));
    res.json(books);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
}; 