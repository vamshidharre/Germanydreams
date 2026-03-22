import os
import re

files_to_update = ['index.html', 'calculator.html', 'visa.html', 'estimator.html', 'wgmessage.html', 'jobtracker.html']

for file in files_to_update:
    filepath = os.path.join('d:\\GermanyDreams', file)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace Google Fonts link
    content = re.sub(
        r'<link\s+href="https://fonts\.googleapis\.com/css2\?family=[^>"]+"\s*rel="stylesheet">',
        '<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">',
        content,
        flags=re.DOTALL
    )
    # also handle the multiline case for index.html:
    content = re.sub(
        r'<link\s*\n\s*href="https://fonts\.googleapis\.com/css2\?family=[^>"]+"\s*\n\s*rel="stylesheet">',
        '<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">',
        content,
        flags=re.DOTALL
    )
    # and handle case with opsz
    content = re.sub(
        r'<link[^>]*href="https://fonts\.googleapis\.com/css2\?family=Bricolage[^>]+rel="stylesheet">',
        '<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">',
        content,
        flags=re.DOTALL
    )
    
    # Replace muted color
    content = content.replace('--muted: #7a90a8;', '--muted: #94a7bf;')
    
    # Replace Fonts
    content = content.replace("'Instrument Sans'", "'Plus Jakarta Sans'")
    content = content.replace("'Bricolage Grotesque'", "'Space Grotesk'")
    content = content.replace("'Syne'", "'Space Grotesk'")
    content = content.replace("'DM Sans'", "'Plus Jakarta Sans'")
    
    # Body font-size and styles
    content = content.replace('font-size: 17px;', 'font-size: 18px;')
    content = content.replace('line-height: 1.65;', 'line-height: 1.7;')
    content = content.replace('letter-spacing: -0.01em;', 'letter-spacing: 0.01em;')
    
    # Update various small sizes
    content = content.replace('font-size: 0.7rem;', 'font-size: 0.76rem;')
    content = content.replace('font-size: 0.72rem;', 'font-size: 0.78rem;')
    content = content.replace('font-size: 0.78rem;', 'font-size: 0.88rem;')
    content = content.replace('font-size: 0.8rem;', 'font-size: 0.88rem;')
    content = content.replace('font-size: 0.82rem;', 'font-size: 0.88rem;')
    content = content.replace('font-size: 0.85rem;', 'font-size: 0.9rem;')
    content = content.replace('font-size: 0.88rem;', 'font-size: 0.92rem;')
    
    # Tweak descriptions line height if tight (like 1.6)
    content = content.replace('line-height: 1.6;', 'line-height: 1.7;')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
print('Updated files')
