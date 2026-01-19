import re

# Read the HTML file
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Read the base64 encoded image
with open('paint-comparison.b64', 'r', encoding='utf-8') as f:
    img_data = f.read().strip()

# Create the image tag with base64 data
img_tag = f'<img src="data:image/jpeg;base64,{img_data}" alt="各塗料の仕上がり比較 - 美しい外壁塗装の実例" class="w-full h-auto rounded-lg shadow-xl border-4 border-gray-200">'

# Find and replace the placeholder section
old_section = r'<div class="image-placeholder">.*?</div>'
new_section = f'''<div class="mb-4">
                    {img_tag}
                </div>
                <div class="text-center">
                    <p class="text-lg font-bold text-gray-800">✨ 適切な塗料で新築同様の美しさを実現</p>
                    <p class="text-sm text-gray-600 mt-2">無機塗料・ラジカル塗料・シリコン塗料など、お住まいに最適な塗料をご提案します</p>
                </div>'''

html = re.sub(old_section, new_section, html, flags=re.DOTALL)

# Write back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✅ 塗料比較画像を追加しました")
print("   - 美しい外壁塗装の実例写真")
print("   - 各塗料の仕上がりイメージを視覚化")
