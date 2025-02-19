# suggestions.py - Generate AI-based recommendations
def generate_suggestions(text):
    suggestions = []
    if "teamwork" not in text.lower():
        suggestions.append("Consider adding 'teamwork' as a soft skill.")
    if "problem-solving" not in text.lower():
        suggestions.append("Mention 'problem-solving' experience in your resume.")
    return suggestions
