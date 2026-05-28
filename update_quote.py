import json
import random
import re

def update_readme():
    # Load quotes
    with open('quotes.json', 'r', encoding='utf-8') as f:
        quotes = json.load(f)
        
    # Select random quote
    selected = random.choice(quotes)
    quote_text = selected['quote']
    author = selected['author']
    
    # Format for README
    formatted_quote = f'"{quote_text}"<br>— <b>{author}</b>'
    
    # Read README
    with open('README.md', 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace the quote section using regex
    pattern = r'(<!-- QUOTE:START -->)(.*?)(<!-- QUOTE:END -->)'
    replacement = f'\\1\n<p align="center">\n  <em>{formatted_quote}</em>\n</p>\n\\3'
    
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    # Write updated README
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"Updated README with quote: {quote_text}")

if __name__ == "__main__":
    update_readme()
