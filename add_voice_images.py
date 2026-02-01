import re

# voice.htmlを読み込み
with open('voice.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 各お客様の声カードに画像を追加
voice_cards = [
    ('<!-- 声1 -->', 'voice-01.jpg', '大前雅裕様のアンケート'),
    ('<!-- 声2 -->', 'voice-02.jpg', 'いすみや醸造店様のアンケート'),
    ('<!-- 声3 -->', 'voice-03.jpg', '川上美智江様のアンケート'),
    ('<!-- 声4 -->', 'voice-04.jpg', 'M.D様のアンケート'),
    ('<!-- 声5 -->', 'voice-05.jpg', '匿名希望様のアンケート'),
    ('<!-- 声6 -->', 'voice-06.jpg', '野口友幸様のアンケート'),
    ('<!-- 声7 -->', 'voice-07.jpg', '芝本茶雄様のアンケート'),
    ('<!-- 声8 -->', 'voice-08.jpg', '青木太12様のアンケート'),
    ('<!-- 声9 -->', 'voice-09.jpg', '九津博一様のアンケート'),
    ('<!-- 声10 -->', 'voice-10.jpg', '宮本真武陸様のアンケート'),
    ('<!-- 声11 -->', 'voice-11.jpg', '山本靖文様のアンケート'),
    ('<!-- 声12 -->', 'voice-12.jpg', '港脇健三様のアンケート'),
    ('<!-- 声13 -->', 'voice-13.jpg', '三村文雄様のアンケート'),
    ('<!-- 声14 -->', 'voice-14.jpg', '鹿木様のアンケート'),
    ('<!-- 声15 -->', 'voice-15.jpg', '高名勝美様のアンケート'),
]

for marker, image_file, alt_text in voice_cards:
    # 各カードの </div> の後に画像を追加
    pattern = f'({re.escape(marker)}.*?</div>\\n                </div>\\n)(                <div class="bg-gray-50 p-4 rounded-lg mb-4">)'
    
    replacement = f'\\1                <!-- 実際のアンケート画像 -->\\n                <div class="mb-4">\\n                    <img src="images/voice/{image_file}" alt="{alt_text}" class="w-full rounded-lg shadow-md border border-gray-200">\\n                </div>\\n\\2'
    
    content = re.sub(pattern, replacement, content, flags=re.DOTALL, count=1)

# 保存
with open('voice.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ 画像を15箇所すべてに追加しました")
