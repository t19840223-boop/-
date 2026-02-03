#!/usr/bin/env python3
import re

# Read the file
with open('jirei.html.backup', 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern to find each case
# 事例の開始パターン: <!-- 事例X: ... -->
case_pattern = r'(<!-- 事例(\d+):.*?-->)\s*(<div class="bg-white rounded-2xl shadow-2xl.*?">)'

def replace_case(match):
    comment = match.group(1)
    case_num = int(match.group(2))
    div_tag = match.group(3)
    
    # Determine page number
    # Page 1: Cases 1-3
    # Page 2: Cases 4-9 (6 items)
    # Page 3: Cases 10-11
    if case_num <= 3:
        page = 1
    elif case_num <= 9:
        page = 2
    else:
        page = 3
    
    return f'{comment}\n                <div class="case-item" data-page="{page}">\n                {div_tag}'

# Replace all cases
content = re.sub(case_pattern, replace_case, content)

# Add closing </div> for case-item before next case or before closing container
# Pattern: </div>\n            </div>\n\n            <!-- 事例
content = re.sub(
    r'(</div>\s*</div>)\s*(<!-- 事例)',
    r'\1\n                </div>\n\n                \2',
    content
)

# Add closing </div> before the CTA section
content = re.sub(
    r'(</div>\s*</div>)\s*(</div>\s*<!-- 心理的CTA)',
    r'\1\n                </div>\n            \2',
    content
)

# Write the modified content
with open('jirei.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Pagination markup added successfully!")
print("Page 1: Cases 1-3 (3 items)")
print("Page 2: Cases 4-9 (6 items)")
print("Page 3: Cases 10-11 (2 items)")
