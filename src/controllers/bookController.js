import { findById, find, create } from '../models/Book';

export async function getBookById(req, res) {
  try {
    const book = await findById(req.params.bookId);
    if (!book) {
      return res.status(404).json({ message: 'Book not found' });
    }
    res.json(book);
  } catch (error) {
    res.status(500).json({ message: 'Server error' });
  }
}

export async function searchBooks(req, res) {
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
    
    const books = await find(query).limit(Number(limit));
    res.json(books);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
}

export async function getFeaturedBooks(req, res) {
  try {
    const { limit = 5 } = req.query;
    const books = await find({ isFeatured: true }).limit(parseInt(limit));
    res.json(books);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
}

export async function createBook(req, res) {
  try {
    const { title, author, category, description, publishedDate, isFeatured } = req.body;
    
    const book = await create({
      title,
      author,
      category,
      description,
      publishedDate: publishedDate ? new Date(publishedDate) : undefined,
      isFeatured
    });
    
    res.status(201).json(book);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
} 