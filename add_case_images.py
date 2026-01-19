#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 実際の劣化事例画像を追加

with open('/home/user/webapp/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 画像をbase64エンコード
with open('/home/user/webapp/case-before-1.b64', 'r') as f:
    img1_base64 = f.read().strip()

with open('/home/user/webapp/case-before-2.b64', 'r') as f:
    img2_base64 = f.read().strip()

# プレースホルダーを実際の画像に置き換え
old_placeholder = '''            <!-- 事例画像エリア -->
            <div class="mb-8">
                <div class="image-placeholder">
                    <i class="fas fa-images text-6xl mb-4 text-gray-400"></i>
                    <p class="text-xl font-bold mb-2">実際の劣化事例（ビフォーアフター）</p>
                    <p class="text-sm">※実際の施工前・施工後の写真を追加予定</p>
                </div>
            </div>'''

new_images = f'''            <!-- 事例画像エリア -->
            <div class="mb-8">
                <h3 class="text-2xl font-black text-center mb-6">📸 実際の劣化事例（施工前）</h3>
                <p class="text-center text-red-600 font-bold mb-6">⚠️ これらは実際に放置された結果です</p>
                <div class="grid md:grid-cols-2 gap-4">
                    <div class="border-4 border-red-500 rounded-lg overflow-hidden shadow-lg">
                        <img src="data:image/jpeg;base64,{img1_base64}" alt="内装劣化事例 - 床板の腐食と剥がれ" class="w-full h-auto">
                        <div class="p-3 bg-red-50">
                            <p class="font-bold text-sm text-red-600">⚠️ 内装まで被害が拡大</p>
                            <p class="text-xs text-gray-600">床板の腐食・剥がれ。外壁放置で雨水侵入した結果</p>
                        </div>
                    </div>
                    <div class="border-4 border-red-500 rounded-lg overflow-hidden shadow-lg">
                        <img src="data:image/jpeg;base64,{img2_base64}" alt="外壁劣化事例 - 構造材の露出と腐食" class="w-full h-auto">
                        <div class="p-3 bg-red-50">
                            <p class="font-bold text-sm text-red-600">⚠️ 構造材まで損傷</p>
                            <p class="text-xs text-gray-600">外壁の劣化で構造材が露出・腐食。大規模修繕が必要に</p>
                        </div>
                    </div>
                </div>
                <div class="mt-6 text-center">
                    <div class="inline-block bg-yellow-100 border-4 border-yellow-400 rounded-lg p-4">
                        <p class="font-black text-lg mb-2">💡 早期発見なら防げた被害です</p>
                        <p class="text-sm text-gray-700">定期的な診断で、このような大規模修繕を回避できます</p>
                    </div>
                </div>
            </div>'''

content = content.replace(old_placeholder, new_images)

with open('/home/user/webapp/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ 実際の劣化事例画像を追加しました")
print("  - 画像1: 内装劣化（床板の腐食と剥がれ）")
print("  - 画像2: 外壁劣化（構造材の露出と腐食）")
