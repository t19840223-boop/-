#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ビフォーアフターセクションを施工後画像のみに変更

with open('/home/user/webapp/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 施工後画像
with open('/home/user/webapp/case-after.b64', 'r') as f:
    after_img = f.read().strip()

# 現在のビフォーアフターセクションを探して置換
import re

# パターン: ヒーロー画像エリア全体
pattern = r'            <!-- ヒーロー画像エリア -->.*?            <!-- 解決策：3つの安心 -->'

new_section = f'''            <!-- ヒーロー画像エリア -->
            <div class="mb-8">
                <h3 class="text-2xl font-black text-center mb-6">🏠 適切な塗装で新築同様に</h3>
                <p class="text-center text-gray-700 mb-6">定期的なメンテナンスで、家は美しさを保ち続けます</p>
                <div class="max-w-3xl mx-auto">
                    <div class="border-4 border-green-500 rounded-lg overflow-hidden shadow-xl">
                        <img src="data:image/jpeg;base64,{after_img}" alt="外壁塗装後の美しい住宅" class="w-full h-auto">
                        <div class="p-6 bg-gradient-to-r from-green-50 to-blue-50">
                            <p class="font-black text-2xl text-center text-green-600 mb-4">✨ 適切な塗装の効果</p>
                            <div class="grid md:grid-cols-3 gap-4 text-sm">
                                <div class="bg-white p-3 rounded-lg border-2 border-green-400">
                                    <p class="font-bold text-green-600 mb-1">✓ 新築同様の美観</p>
                                    <p class="text-gray-600 text-xs">外観が生まれ変わります</p>
                                </div>
                                <div class="bg-white p-3 rounded-lg border-2 border-blue-400">
                                    <p class="font-bold text-blue-600 mb-1">✓ 10年以上の耐久性</p>
                                    <p class="text-gray-600 text-xs">次の塗装まで安心</p>
                                </div>
                                <div class="bg-white p-3 rounded-lg border-2 border-purple-400">
                                    <p class="font-bold text-purple-600 mb-1">✓ 資産価値を維持</p>
                                    <p class="text-gray-600 text-xs">将来の売却も有利に</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="mt-6 text-center">
                    <div class="inline-block bg-gradient-to-r from-yellow-100 to-orange-100 border-4 border-yellow-400 rounded-lg p-4">
                        <p class="font-black text-xl mb-2">💡 早期診断で、この美しさを保てます</p>
                        <p class="text-sm text-gray-700">放置する前に、まず無料診断を。適切なタイミングで塗装すれば、大規模修繕を回避できます</p>
                    </div>
                </div>
            </div>
            
            <!-- 解決策：3つの安心 -->'''

content = re.sub(pattern, new_section, content, flags=re.DOTALL)

with open('/home/user/webapp/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ ヒーローセクションを更新しました")
print("  - ビフォー画像を削除")
print("  - 施工後の美しい家の写真のみ表示")
print("  - ポジティブな訴求に変更")
