#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# チョーキングとクラックの実際の写真を追加

with open('/home/user/webapp/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 画像をbase64エンコード
with open('/home/user/webapp/chalking.b64', 'r') as f:
    chalking_img = f.read().strip()

with open('/home/user/webapp/crack.b64', 'r') as f:
    crack_img = f.read().strip()

# チョーキングのプレースホルダーを置き換え
chalking_placeholder = '''                                <div class="bg-gray-100 p-4 rounded-lg mb-4">
                                    <div class="image-placeholder">
                                        <i class="fas fa-hand-sparkles text-4xl mb-3 text-gray-400"></i>
                                        <p class="font-bold mb-2">チョーキング現象の実例</p>
                                        <p class="text-sm">※実際の劣化写真を追加予定</p>
                                    </div>
                                </div>'''

chalking_image = f'''                                <div class="bg-gray-100 p-4 rounded-lg mb-4">
                                    <div class="border-4 border-red-500 rounded-lg overflow-hidden">
                                        <img src="data:image/jpeg;base64,{chalking_img}" alt="チョーキング現象 - 壁を触ると白い粉が付く" class="w-full h-auto">
                                        <div class="p-3 bg-red-50">
                                            <p class="font-bold text-red-600">⚠️ チョーキング現象の実例</p>
                                            <p class="text-sm text-gray-700">壁を触ると白い粉（チョーク状の塗料）が付着。塗膜が劣化し、防水機能が完全に失われた状態です。</p>
                                        </div>
                                    </div>
                                </div>'''

content = content.replace(chalking_placeholder, chalking_image)

# クラックのプレースホルダーを置き換え
crack_placeholder = '''                                <div class="bg-gray-100 p-4 rounded-lg mb-4">
                                    <div class="image-placeholder">
                                        <i class="fas fa-exclamation-triangle text-4xl mb-3 text-gray-400"></i>
                                        <p class="font-bold mb-2">クラック（ヒビ割れ）の実例</p>
                                        <p class="text-sm">※実際の劣化写真を追加予定</p>
                                    </div>
                                </div>'''

crack_image = f'''                                <div class="bg-gray-100 p-4 rounded-lg mb-4">
                                    <div class="border-4 border-red-500 rounded-lg overflow-hidden">
                                        <img src="data:image/jpeg;base64,{crack_img}" alt="クラック - 外壁のひび割れ" class="w-full h-auto">
                                        <div class="p-3 bg-red-50">
                                            <p class="font-bold text-red-600">⚠️ クラック（ひび割れ）の実例</p>
                                            <p class="text-sm text-gray-700">外壁に発生したひび割れ。0.3mm以上のクラックは雨水が浸入し、構造材の腐食につながります。</p>
                                        </div>
                                    </div>
                                </div>'''

content = content.replace(crack_placeholder, crack_image)

with open('/home/user/webapp/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ チョーキングとクラックの実際の写真を追加しました")
print("  - チョーキング: 白い粉が手に付着する様子")
print("  - クラック: 外壁のひび割れの実例")
