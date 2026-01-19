#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ビフォーアフター画像を追加

with open('/home/user/webapp/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 施工前画像（既存）
with open('/home/user/webapp/case-before-1.b64', 'r') as f:
    before_img = f.read().strip()

# 施工後画像（新規）
with open('/home/user/webapp/case-after.b64', 'r') as f:
    after_img = f.read().strip()

# プレースホルダーを実際の画像に置き換え
old_placeholder = '''            <!-- ヒーロー画像エリア -->
            <div class="mb-8">
                <div class="image-placeholder">
                    <i class="fas fa-home text-6xl mb-4 text-gray-400"></i>
                    <p class="text-xl font-bold mb-2">外壁劣化のビフォーアフター</p>
                    <p class="text-sm">※実際の施工事例写真を追加予定</p>
                </div>
            </div>'''

new_images = f'''            <!-- ヒーロー画像エリア -->
            <div class="mb-8">
                <h3 class="text-2xl font-black text-center mb-6">🏠 外壁塗装のビフォーアフター</h3>
                <p class="text-center text-gray-700 mb-6">適切な時期に塗装すれば、家は新築同様に生まれ変わります</p>
                <div class="grid md:grid-cols-2 gap-6">
                    <!-- Before -->
                    <div class="border-4 border-red-500 rounded-lg overflow-hidden shadow-lg">
                        <div class="bg-red-600 text-white text-center py-2 font-bold">
                            ❌ Before（施工前）
                        </div>
                        <img src="data:image/jpeg;base64,{before_img}" alt="施工前 - 内装劣化の様子" class="w-full h-auto">
                        <div class="p-4 bg-red-50">
                            <p class="font-bold text-red-600 mb-2">⚠️ 放置した結果...</p>
                            <ul class="text-sm text-gray-700 space-y-1">
                                <li>✗ 床板が腐食・剥がれ</li>
                                <li>✗ 内装工事が必要に</li>
                                <li>✗ 修繕費用が高額化</li>
                            </ul>
                        </div>
                    </div>
                    
                    <!-- After -->
                    <div class="border-4 border-green-500 rounded-lg overflow-hidden shadow-lg">
                        <div class="bg-green-600 text-white text-center py-2 font-bold">
                            ✅ After（施工後）
                        </div>
                        <img src="data:image/jpeg;base64,{after_img}" alt="施工後 - 新築同様の美しい外壁" class="w-full h-auto">
                        <div class="p-4 bg-green-50">
                            <p class="font-bold text-green-600 mb-2">✨ 適切な塗装で...</p>
                            <ul class="text-sm text-gray-700 space-y-1">
                                <li>✓ 新築同様の美しさ</li>
                                <li>✓ 10年以上の耐久性</li>
                                <li>✓ 資産価値を維持</li>
                            </ul>
                        </div>
                    </div>
                </div>
                <div class="mt-6 text-center">
                    <div class="inline-block bg-gradient-to-r from-yellow-100 to-orange-100 border-4 border-yellow-400 rounded-lg p-4">
                        <p class="font-black text-xl mb-2">💡 早期発見・早期対応が鍵</p>
                        <p class="text-sm text-gray-700">定期診断で大規模修繕を回避し、美しい家を保ちましょう</p>
                    </div>
                </div>
            </div>'''

content = content.replace(old_placeholder, new_images)

with open('/home/user/webapp/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ ビフォーアフター画像を追加しました")
print("  - Before: 内装劣化（床板の腐食）")
print("  - After: 施工後の美しい外壁（新築同様）")
