from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional, Dict
from pydantic import BaseModel
import random
import json
from pathlib import Path
import pandas as pd
from enum import Enum

app = FastAPI(
    title="Literary Vault API",
    description="API for managing educational questions and documentation",
    version="1.0.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QuestionCategory(str, Enum):
    astronomy = "astronomy"
    literature = "literature"
    mathematics = "mathematics"
    psychology = "psychology"
    american_history = "american-history"

class QuestionBase(BaseModel):
    id: str
    question: str
    options: List[str]
    correct_answer: str
    difficulty: int
    knowledge_category: str
    topic_focus: str

class QuestionManager:
    def __init__(self):
        self.questions_dir = Path(__file__).parent.parent / "data"
        self.category_cache: Dict[str, List[dict]] = {}

    def _load_markdown_table(self, file_path: Path) -> List[dict]:
        """Load and parse markdown table format"""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Skip header and split into lines
        lines = content.split('\n')
        table_start = next(i for i, line in enumerate(lines) if line.startswith('|--'))
        
        # Convert markdown table to DataFrame
        table_lines = [line for line in lines[table_start-1:] if line.strip() and line.startswith('|')]
        df = pd.read_csv(pd.StringIO('\n'.join(table_lines)), sep='|', skipinitialspace=True)
        df.columns = df.columns.str.strip()
        
        questions = []
        for _, row in df.iterrows():
            options = [
                row['Choice 1'].strip(),
                row['Choice 2'].strip(),
                row['Choice 3'].strip()
            ]
            
            # Add correct answer to options if not already present
            correct_answer = row['Correct Answer'].strip()
            if correct_answer not in options:
                options.append(correct_answer)
            
            question_dict = {
                "id": str(row['ID']).strip(),
                "question": row['Question'].strip(),
                "options": options,
                "correct_answer": correct_answer,
                "difficulty": int(row['Difficulty']),
                "knowledge_category": row['Knowledge Category'].strip(),
                "topic_focus": row['Topic Focus'].strip()
            }
            questions.append(question_dict)
        
        return questions

    def get_questions(self, category: str) -> List[dict]:
        """Get questions for a category with caching"""
        if category not in self.category_cache:
            file_path = self.questions_dir / f"{category}-questions.md"
            if not file_path.exists():
                raise FileNotFoundError(f"No questions found for category: {category}")
            
            self.category_cache[category] = self._load_markdown_table(file_path)
        
        return self.category_cache[category]

    def get_topics(self, category: str) -> List[str]:
        """Get unique topics for a category"""
        questions = self.get_questions(category)
        return sorted(set(q['topic_focus'] for q in questions))

# Initialize QuestionManager
question_manager = QuestionManager()

@app.get("/api/v1/questions/{category}/random", response_model=List[QuestionBase])
async def get_random_questions(
    category: QuestionCategory,
    count: int = Query(default=5, ge=1, le=20),
    seed: Optional[int] = None,
    topic: Optional[str] = None,
    difficulty: Optional[int] = Query(None, ge=0, le=3)
):
    """
    Get random questions from a specific category with optional filters.
    """
    try:
        if seed is not None:
            random.seed(seed)
            
        all_questions = question_manager.get_questions(category)
        filtered_questions = all_questions
        
        # Apply filters
        if topic:
            filtered_questions = [q for q in filtered_questions 
                                if q['topic_focus'].lower() == topic.lower()]
        if difficulty is not None:
            filtered_questions = [q for q in filtered_questions 
                                if q['difficulty'] == difficulty]
        
        if not filtered_questions:
            raise HTTPException(
                status_code=404,
                detail=f"No questions found for category '{category}' with the specified criteria"
            )
        
        # Adjust count if necessary
        count = min(count, len(filtered_questions))
        
        # Select and randomize questions
        selected_questions = random.sample(filtered_questions, count)
        for question in selected_questions:
            random.shuffle(question['options'])
                
        return selected_questions
        
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/questions/{category}/topics")
async def get_topics(category: QuestionCategory):
    """Get all available topics for a category"""
    try:
        topics = question_manager.get_topics(category)
        return {"topics": topics}
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.get("/api/v1/categories")
async def get_categories():
    """Get all available question categories"""
    return {"categories": [cat.value for cat in QuestionCategory]}

@app.get("/api/v1/questions/{category}/stats")
async def get_category_stats(category: QuestionCategory):
    """Get statistics about questions in a category"""
    try:
        questions = question_manager.get_questions(category)
        topics = {}
        difficulties = {0: 0, 1: 0, 2: 0, 3: 0}
        
        for q in questions:
            topic = q['topic_focus']
            difficulty = q['difficulty']
            
            topics[topic] = topics.get(topic, 0) + 1
            difficulties[difficulty] += 1
            
        return {
            "total_questions": len(questions),
            "topics": topics,
            "difficulties": difficulties
        }
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))