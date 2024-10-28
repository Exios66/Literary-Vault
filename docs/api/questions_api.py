from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from pydantic import BaseModel, Field
from typing import List, Optional
import pandas as pd
import random
from enum import Enum
from pathlib import Path
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Questions API",
    description="API for retrieving and randomizing questions from various categories",
    version="1.0.0"
)

# Get the root directory path
ROOT_DIR = Path(__file__).parent.parent  # This gets us to the docs directory

# Enums and Models
class Category(str, Enum):
    astronomy = "astronomy"
    literature = "literature"
    mathematics = "mathematics"

class QuestionBase(BaseModel):
    id: str
    question: str
    correct_answer: str
    options: Optional[List[str]] = None

class GetQuestionsParams(BaseModel):
    category: Category
    limit: int = Field(default=10, ge=1, le=50)
    random: bool = True

class RandomizeQuestionsParams(BaseModel):
    category: Category
    count: int = Field(default=5, ge=1, le=20)
    seed: Optional[int] = None

# Service Class
class QuestionService:
    def __init__(self):
        self.base_path = ROOT_DIR / "Questions" / "CSV"
        logger.info(f"Base path for questions: {self.base_path}")
        
        self.question_files = {
            Category.astronomy: self.base_path / "astronomy-questions.csv",
            Category.literature: self.base_path / "literature-questions.csv",
            Category.mathematics: self.base_path / "math-questions.csv"
        }
        self._cache = {}
        
        # Log file paths and existence
        for category, path in self.question_files.items():
            logger.info(f"Question file for {category}: {path} (exists: {path.exists()})")

    def _load_questions(self, category: Category) -> pd.DataFrame:
        if category not in self._cache:
            file_path = self.question_files[category]
            logger.info(f"Attempting to load questions for {category} from {file_path}")
            
            if not file_path.exists():
                error_msg = f"Question file for category {category} not found at {file_path}"
                logger.error(error_msg)
                raise HTTPException(status_code=404, detail=error_msg)
            
            try:
                df = pd.read_csv(file_path)
                logger.info(f"Successfully loaded CSV file for {category}")
                logger.info(f"Columns found: {df.columns.tolist()}")
                
                required_columns = ['id', 'question', 'correct_answer']
                missing_cols = [col for col in required_columns if col not in df.columns]
                if missing_cols:
                    error_msg = f"Missing required columns for {category}: {missing_cols}"
                    logger.error(error_msg)
                    raise HTTPException(status_code=500, detail=error_msg)
                
                # Convert options to list if present
                if 'options' in df.columns:
                    df['options'] = df['options'].apply(
                        lambda x: eval(x) if isinstance(x, str) and x.strip() else None
                    )
                
                self._cache[category] = df
                logger.info(f"Successfully processed and cached questions for {category}")
            except Exception as e:
                error_msg = f"Error loading questions for {category}: {str(e)}"
                logger.error(error_msg)
                raise HTTPException(status_code=500, detail=error_msg)
            
        return self._cache[category]

    def get_questions(self, params: GetQuestionsParams) -> List[QuestionBase]:
        logger.info(f"Getting {params.limit} questions for category {params.category}")
        df = self._load_questions(params.category)
        
        if params.random:
            selected_df = df.sample(n=min(params.limit, len(df)))
        else:
            selected_df = df.head(params.limit)
        
        questions = []
        for _, row in selected_df.iterrows():
            question_dict = row.to_dict()
            questions.append(QuestionBase(**question_dict))
        
        logger.info(f"Successfully retrieved {len(questions)} questions")
        return questions

    def randomize_questions(self, params: RandomizeQuestionsParams) -> List[QuestionBase]:
        logger.info(f"Randomizing {params.count} questions for category {params.category}")
        if params.seed is not None:
            random.seed(params.seed)
            logger.info(f"Using random seed: {params.seed}")
            
        get_params = GetQuestionsParams(
            category=params.category,
            limit=params.count,
            random=True
        )
        questions = self.get_questions(get_params)
        
        # Randomize options for each question if they exist
        for question in questions:
            if question.options:
                options = list(question.options)
                random.shuffle(options)
                question.options = options
        
        logger.info(f"Successfully randomized {len(questions)} questions")
        return questions

# Initialize service
question_service = QuestionService()

# Root route
@app.get("/", response_class=HTMLResponse)
async def root():
    """
    Root endpoint that provides API documentation and links
    """
    html_content = """
    <html>
        <head>
            <title>Questions API</title>
            <style>
                body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
                h1 { color: #2c3e50; }
                h2 { color: #34495e; }
                code { background-color: #f7f9fa; padding: 2px 5px; border-radius: 3px; }
                pre { background-color: #f7f9fa; padding: 15px; border-radius: 5px; overflow-x: auto; }
                a { color: #3498db; text-decoration: none; }
                a:hover { text-decoration: underline; }
            </style>
        </head>
        <body>
            <h1>Questions API</h1>
            <p>Welcome to the Questions API. This API provides endpoints for retrieving and randomizing questions from various categories.</p>
            
            <h2>Documentation</h2>
            <ul>
                <li><a href="/docs">Interactive API Documentation (Swagger UI)</a></li>
                <li><a href="/redoc">Alternative Documentation (ReDoc)</a></li>
            </ul>
            
            <h2>Available Endpoints</h2>
            <ul>
                <li><code>GET /api/v1/questions/{category}</code> - Get questions from a category</li>
                <li><code>GET /api/v1/questions/{category}/random</code> - Get randomly selected and ordered questions</li>
                <li><code>GET /api/v1/health</code> - Check API health and file locations</li>
            </ul>
            
            <h2>Example Usage</h2>
            <pre>
# Get 5 random astronomy questions
GET /api/v1/questions/astronomy?limit=5&random=true

# Get 10 random mathematics questions with a specific seed
GET /api/v1/questions/mathematics/random?count=10&seed=42
            </pre>
            
            <h2>Categories</h2>
            <ul>
                <li>astronomy</li>
                <li>literature</li>
                <li>mathematics</li>
            </ul>
        </body>
    </html>
    """
    return html_content

# API Routes
@app.get("/api/v1/questions/{category}", response_model=List[QuestionBase])
async def get_questions(
    category: Category,
    limit: int = 10,
    random: bool = True
):
    """
    Get questions from a specific category.
    
    Parameters:
    - category: The category of questions (astronomy, literature, or mathematics)
    - limit: Maximum number of questions to return (1-50)
    - random: Whether to return random questions or sequential ones
    """
    params = GetQuestionsParams(category=category, limit=limit, random=random)
    try:
        return question_service.get_questions(params)
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Unexpected error in get_questions: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/questions/{category}/random", response_model=List[QuestionBase])
async def randomize_questions(
    category: Category,
    count: int = 5,
    seed: Optional[int] = None
):
    """
    Get randomly selected and ordered questions from a specific category.
    
    Parameters:
    - category: The category of questions (astronomy, literature, or mathematics)
    - count: Number of questions to randomly select (1-20)
    - seed: Optional random seed for reproducible randomization
    """
    params = RandomizeQuestionsParams(category=category, count=count, seed=seed)
    try:
        return question_service.randomize_questions(params)
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Unexpected error in randomize_questions: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/v1/health")
async def health_check():
    """
    Health check endpoint to verify API is running and show CSV file locations.
    """
    file_status = {}
    for category, path in question_service.question_files.items():
        file_status[category.value] = {
            "path": str(path.absolute()),
            "exists": path.exists()
        }
    
    return {
        "status": "healthy",
        "base_path": str(question_service.base_path),
        "question_files": file_status
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
