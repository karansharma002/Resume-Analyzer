def generate_suggestions(text):
    suggestions = []
    if len(text) < 500:
        suggestions.append("Your resume is too short. Try adding more details.")
    if "Python" not in text:
        suggestions.append("Consider adding Python to your resume if applicable.")
    if "Experience" not in text:
        suggestions.append("Add a section for Experience to improve structure.")
    
    return suggestions if suggestions else ["Your resume looks well-structured!"]
