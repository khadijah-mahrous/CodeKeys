# utils/text_normalizer.py

def normalize_code(code):
    """Normalize code for comparison"""
    if not code:
        return ""
    
    # Normalize newlines
    code = code.replace('\r\n', '\n').replace('\r', '\n')
    
    # Normalize quotes
    code = code.replace('"', '"').replace('"', '"')
    code = code.replace("'", "'").replace("'", "'")
    
    # Split into lines
    lines = code.split('\n')
    
    # Remove trailing spaces from each line (preserve indentation spaces)
    lines = [line.rstrip() for line in lines]
    
    # Remove trailing empty lines
    while lines and lines[-1] == '':
        lines.pop()
    
    return '\n'.join(lines)


def calculate_accuracy(user_text, target_text):
    """Calculate exact accuracy character by character"""
    user_text = normalize_code(user_text)
    target_text = normalize_code(target_text)
    
    correct = 0
    mistakes = 0
    
    max_len = max(len(user_text), len(target_text))
    
    for i in range(max_len):
        user_char = user_text[i] if i < len(user_text) else ''
        target_char = target_text[i] if i < len(target_text) else ''
        
        if user_char == target_char:
            correct += 1
        elif user_char != '' and target_char != '':
            mistakes += 1
        else:
            mistakes += 1
    
    if len(target_text) == 0:
        return 100, 0, 0
    
    accuracy = int((correct / len(target_text)) * 100)
    return min(100, max(0, accuracy)), mistakes, correct