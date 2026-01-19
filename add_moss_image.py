#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# コケ・カビの実際の写真を追加

with open('/home/user/webapp/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 画像をbase64エンコード
with open('/home/user/webapp/moss.b64', 'r') as f:
    moss_img = f.read().strip()

# コケ・カビのプレースホルダーを置き換え
moss_placeholder = '''                                <div class="bg-gray-100 p-4 rounded-lg mb-4">
                                    <div class="image-placeholder">
                                        <i class="fas fa-bacterium text-4xl mb-3 text-gray-400"></i>
                                        <p class="font-bold mb-2">コケ・カビの実例</p>
                                        <p class="text-sm">※実際の劣化写真を追加予定</p>
                                    </div>
                                </div>'''

moss_image = f'''                                <div class="bg-gray-100 p-4 rounded-lg mb-4">
                                    <div class="border-4 border-green-600 rounded-lg overflow-hidden">
                                        <img src="data:image/jpeg;base64,{moss_img}" alt="コケ・カビ - 屋根に繁殖した様子" class="w-full h-auto">
                                        <div class="p-3 bg-green-50">
                                            <p class="font-bold text-green-800">🦠 コケ・カビの実例（屋根）</p>
                                            <p class="text-sm text-gray-700">屋根に繁殖したコケ。湿気がこもり、防水機能が低下しています。室内に胞子が入り込むと、健康被害の原因になります。</p>
                                        </div>
                                    </div>
                                </div>'''

content = content.replace(moss_placeholder, moss_image)

with open('/home/user/webapp/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ コケ・カビの実際の写真を追加しました")
print("  - 屋根に繁殖したコケの様子")
print("  - 健康被害リスクを視覚化")
