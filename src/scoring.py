import re

def evaluate_resume(text):
    length_score = min(len(text) / 1000 * 20, 20)  

    structure_keywords = ['Experience', 'Skills', 'Projects', 'Education']
    structure_score = 20 if any(re.search(rf'\b{kw}\b', text, re.IGNORECASE) for kw in structure_keywords) else 0

    # Keyword-based scoring
    important_keywords = ['Python', 'Java', 'SQL', 'Machine Learning', 'Django', 'Flask']
    keyword_score = sum(5 for kw in important_keywords if re.search(rf'\b{kw}\b', text, re.IGNORECASE))
    keyword_score = min(keyword_score, 30)  # Max keyword score capped at 30

    ats_score = min((length_score + keyword_score + structure_score) / 1.5, 100)
    total_score = min(length_score + keyword_score + structure_score, 100)

    return total_score, ats_score
