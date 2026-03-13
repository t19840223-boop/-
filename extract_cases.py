import re

# Read jirei.html
with open('jirei.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract case items
case_pattern = r'<div class="case-item".*?(?=<div class="case-item"|<!-- ページネーション -->)'
cases = re.findall(case_pattern, content, re.DOTALL)

print(f"Found {len(cases)} cases")

# Extract details for first 10 cases
for i, case in enumerate(cases[:10], 1):
    # Extract title
    title_match = re.search(r'事例\d+:\s*([^<\n]+)', case)
    title = title_match.group(1).strip() if title_match else f"事例{i}"
    
    # Extract area
    area_match = re.search(r'data-area="([^"]+)"', case)
    area = area_match.group(1) if area_match else "不明"
    
    print(f"\n事例{i}: {title}")
    print(f"  地域: {area}")
