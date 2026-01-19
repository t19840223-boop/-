#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
屋号とサブタイトルを全ページに適用：
屋号：外壁塗装オンライン診断センター
サブタイトル：～雨漏り・外壁修理110番～
"""

# index.htmlを読み込み
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# タイトルタグを変更
html = html.replace(
    '<title>外壁塗装の真実 | 訪問販売に騙されない！無料オンライン診断で家を守る</title>',
    '<title>外壁塗装オンライン診断センター ～雨漏り・外壁修理110番～ | 神奈川・東京全域対応</title>'
)

# メタディスクリプションを変更
old_meta = '<meta name="description" content="外壁のチョーキング、ひび割れ、カビを放置していませんか？訪問販売に騙される前に、プロの無料オンライン診断で家を守りましょう。東京都・神奈川県対応。">'
new_meta = '<meta name="description" content="外壁塗装オンライン診断センター。雨漏り・外壁修理110番として神奈川・東京全域に対応。訪問なし・営業なしの無料オンライン診断で安心。毎日メール報告・正直見積もり。">'
html = html.replace(old_meta, new_meta)

# ヒーローセクションのタイトルを変更
old_hero = '''            <h1 class="text-4xl md:text-6xl lg:text-7xl font-black mb-6 leading-tight">
                外壁塗装の真実<br>
                <span class="text-yellow-400">家族を守る、家を守る</span>
            </h1>'''

new_hero = '''            <h1 class="text-4xl md:text-6xl lg:text-7xl font-black mb-6 leading-tight">
                外壁塗装オンライン診断センター<br>
                <span class="text-yellow-400">～雨漏り・外壁修理110番～</span>
            </h1>'''

html = html.replace(old_hero, new_hero)

# フッターのタイトルを変更
old_footer_title = '''            <h3 class="text-3xl font-black text-center mb-4">外壁塗装の真実</h3>
            <p class="text-xl text-center mb-8">家族を守る、家を守る</p>'''

new_footer_title = '''            <h3 class="text-3xl font-black text-center mb-4">外壁塗装オンライン診断センター</h3>
            <p class="text-xl text-center mb-8">～雨漏り・外壁修理110番～</p>'''

html = html.replace(old_footer_title, new_footer_title)

# コピーライトを変更
html = html.replace(
    '<p class="text-gray-500 text-center text-sm">© 2026 外壁塗装の真実 All rights reserved.</p>',
    '<p class="text-gray-500 text-center text-sm">© 2026 外壁塗装オンライン診断センター All rights reserved.</p>'
)

# 保存
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✅ index.html を更新しました")
print("  屋号: 外壁塗装オンライン診断センター")
print("  サブタイトル: ～雨漏り・外壁修理110番～")

# thankyou.htmlも更新
with open('thankyou.html', 'r', encoding='utf-8') as f:
    thankyou = f.read()

thankyou = thankyou.replace(
    '<title>診断お申し込みありがとうございます | 外壁塗装の真実</title>',
    '<title>診断お申し込みありがとうございます | 外壁塗装オンライン診断センター</title>'
)

thankyou = thankyou.replace(
    '<h1 class="text-3xl md:text-5xl font-black mb-6">外壁塗装の真実</h1>',
    '<h1 class="text-3xl md:text-5xl font-black mb-6">外壁塗装オンライン診断センター<br><span class="text-2xl">～雨漏り・外壁修理110番～</span></h1>'
)

with open('thankyou.html', 'w', encoding='utf-8') as f:
    f.write(thankyou)

print("✅ thankyou.html を更新しました")

# tokushohou.htmlも更新
with open('tokushohou.html', 'r', encoding='utf-8') as f:
    tokushohou = f.read()

tokushohou = tokushohou.replace(
    '<title>特定商取引法に基づく表記 | 外壁塗装診断</title>',
    '<title>特定商取引法に基づく表記 | 外壁塗装オンライン診断センター</title>'
)

with open('tokushohou.html', 'w', encoding='utf-8') as f:
    f.write(tokushohou)

print("✅ tokushohou.html を更新しました")

# privacy.htmlも更新
with open('privacy.html', 'r', encoding='utf-8') as f:
    privacy = f.read()

privacy = privacy.replace(
    '<title>プライバシーポリシー | 外壁塗装診断</title>',
    '<title>プライバシーポリシー | 外壁塗装オンライン診断センター</title>'
)

with open('privacy.html', 'w', encoding='utf-8') as f:
    f.write(privacy)

print("✅ privacy.html を更新しました")
print("\n🎉 すべてのページに屋号・サブタイトルを適用しました！")
