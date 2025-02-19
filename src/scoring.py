# scoring.py - AI-based resume scoring system
def calculate_resume_score(text):
    score = 0
    if "Python" in text:
        score += 10
    if "Machine Learning" in text:
        score += 15
    if "Project" in text:
        score += 5
    return score