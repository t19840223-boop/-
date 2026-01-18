#!/usr/bin/env python3
# LINE機能を全て削除してフォーム診断のみにするスクリプト

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# LINE関連の置換・削除
replacements = [
    # ヒーローセクションのLINE削除
    ('''                <div class="mt-6">
                    <p class="text-xl font-bold mb-4">または、LINEで簡単診断</p>
                    <a href="https://line.me/R/ti/p/@example" target="_blank" class="inline-block px-8 py-4 text-xl font-black bg-gradient-to-r from-green-500 to-green-600 text-white rounded-full border-4 border-black shadow-lg hover:scale-105 transition">
                        <i class="fab fa-line mr-2"></i>LINE診断＋ガイドブックGET
                    </a>
                </div>''', ''),
    
    # 早期対応vsセクションのLINE CTA削除
    ('''            
            <!-- LINE CTA -->
            <div class="text-center mt-8">
                <div class="bg-gradient-to-r from-green-100 to-green-50 p-6 rounded-lg border-4 border-green-500">
                    <p class="text-xl font-black mb-3">今すぐLINE診断で現状をチェック</p>
                    <p class="text-sm text-gray-700 mb-4">✅ たった30秒 ✅ ガイドブック付き</p>
                    <a href="https://line.me/R/ti/p/@example" target="_blank" class="inline-block px-8 py-4 text-xl font-black bg-gradient-to-r from-green-500 to-green-600 text-white rounded-full border-4 border-black shadow-lg hover:scale-105 transition">
                        <i class="fab fa-line mr-2"></i>LINE診断を受ける
                    </a>
                </div>
            </div>''',
    '''            
            <!-- 診断CTA -->
            <div class="text-center mt-8">
                <div class="bg-gradient-to-r from-orange-100 to-red-50 p-6 rounded-lg border-4 border-red-500">
                    <p class="text-xl font-black mb-3">今すぐ無料診断で現状をチェック</p>
                    <p class="text-sm text-gray-700 mb-4">✅ たった30秒 ✅ ガイドブック付き ✅ 自動返信</p>
                    <a href="#diagnosis" class="inline-block px-8 py-4 text-xl font-black bg-gradient-to-r from-red-600 to-red-700 text-white rounded-full border-4 border-black shadow-lg hover:scale-105 transition">
                        <i class="fas fa-clipboard-list mr-2"></i>無料診断を受ける
                    </a>
                </div>
            </div>'''),
    
    # 塗料セクションのLINE CTA削除
    ('''            <!-- LINE CTA -->
            <div class="text-center mb-8">
                <div class="bg-gradient-to-r from-yellow-100 to-orange-50 p-6 rounded-lg border-4 border-orange-400">
                    <p class="text-xl font-black mb-3">💡 どの塗料が最適？LINEで診断</p>
                    <p class="text-sm text-gray-700 mb-4">✅ 無料 ✅ 予算に合わせて提案</p>
                    <a href="https://line.me/R/ti/p/@example" target="_blank" class="inline-block px-8 py-4 text-xl font-black bg-gradient-to-r from-green-500 to-green-600 text-white rounded-full border-4 border-black shadow-lg hover:scale-105 transition">
                        <i class="fab fa-line mr-2"></i>最適な塗料を診断
                    </a>
                </div>
            </div>''',
    '''            <!-- 診断CTA -->
            <div class="text-center mb-8">
                <div class="bg-gradient-to-r from-yellow-100 to-orange-50 p-6 rounded-lg border-4 border-orange-400">
                    <p class="text-xl font-black mb-3">💡 どの塗料が最適？無料診断</p>
                    <p class="text-sm text-gray-700 mb-4">✅ 無料 ✅ 予算に合わせて提案 ✅ ガイドブック付き</p>
                    <a href="#diagnosis" class="inline-block px-8 py-4 text-xl font-black bg-gradient-to-r from-red-600 to-red-700 text-white rounded-full border-4 border-black shadow-lg hover:scale-105 transition">
                        <i class="fas fa-clipboard-list mr-2"></i>最適な塗料を診断
                    </a>
                </div>
            </div>'''),
    
    # 強みセクションのタイトル変更
    ('毎日LINEで<br>現場写真報告', '毎日メールで<br>現場写真報告'),
    ('施工中の様子（LINE報告例）', '施工中の様子（メール報告例）'),
    ('※実際のLINE報告画面のスクリーンショットを追加予定', '※実際のメール報告画面のスクリーンショットを追加予定'),
    
    # 強みセクションLINE CTA削除
    ('''            
            <!-- LINE CTA -->
            <div class="text-center mb-12">
                <div class="bg-gradient-to-r from-blue-100 to-purple-50 p-6 rounded-lg border-4 border-blue-500">
                    <p class="text-xl font-black mb-3">📱 毎日LINE報告をあなたも体験</p>
                    <p class="text-sm text-gray-700 mb-4">✅ まずは無料診断から ✅ しつこい営業なし</p>
                    <a href="https://line.me/R/ti/p/@example" target="_blank" class="inline-block px-8 py-4 text-xl font-black bg-gradient-to-r from-green-500 to-green-600 text-white rounded-full border-4 border-black shadow-lg hover:scale-105 transition">
                        <i class="fab fa-line mr-2"></i>LINE診断を始める
                    </a>
                </div>
            </div>''',
    '''            
            <!-- 診断CTA -->
            <div class="text-center mb-12">
                <div class="bg-gradient-to-r from-blue-100 to-purple-50 p-6 rounded-lg border-4 border-blue-500">
                    <p class="text-xl font-black mb-3">📧 まずは無料診断から始めましょう</p>
                    <p class="text-sm text-gray-700 mb-4">✅ 診断後すぐにガイドブック送付 ✅ しつこい営業なし</p>
                    <a href="#diagnosis" class="inline-block px-8 py-4 text-xl font-black bg-gradient-to-r from-red-600 to-red-700 text-white rounded-full border-4 border-black shadow-lg hover:scale-105 transition">
                        <i class="fas fa-clipboard-list mr-2"></i>無料診断を始める
                    </a>
                </div>
            </div>'''),
    
    # お客様の声のLINE→メール
    ('「毎日LINEで写真が届くから安心。', '「毎日メールで写真が届くから安心。'),
    
    # 特典バナー
    ('※LINE・フォームどちらからでも受け取れます', '※診断フォーム送信後、自動でメール送信されます'),
    
    # フッター
    ('毎日LINE報告', '毎日メール報告'),
    
    # フォーム送信メッセージ
    ('''                alert('✅ 診断依頼を受け付けました！\\n\\n📱 24時間以内にご連絡いたします。\\n🎁「外壁塗装ガイドブック」もお送りします。\\n\\nしばらくお待ちください。');''',
    '''                alert('✅ 診断依頼を受け付けました！\\n\\n📧 ご入力いただいたメールアドレスに\\n「外壁塗装ガイドブック（PDF）」を自動送信しました。\\n\\n⚡ 24時間以内にプロから詳しい診断結果をお送りします。\\n\\nしばらくお待ちください。');'''),
    
    # 診断結果送信方法
    ('📱 診断結果はLINE・メール・お電話でお送りします', '📧 診断結果とガイドブックは自動でメール送付'),
]

for old, new in replacements:
    content = content.replace(old, new)

# LINE診断カード全体を削除（grid md:grid-cols-2を削除して、フォームのみにする）
# LINE診断カード部分を探して削除
line_diagnosis_start = content.find('            <div class="grid md:grid-cols-2 gap-8">')
if line_diagnosis_start != -1:
    # LINE診断カードの終わりを探す（フォーム診断の開始まで）
    form_start = content.find('                <!-- フォーム診断 -->', line_diagnosis_start)
    if form_start != -1:
        # gridの開始からLINE診断カードまでを削除して、フォームを中央配置にする
        before = content[:line_diagnosis_start]
        after_form_start = content[form_start:]
        
        # フォームを中央配置にする
        new_section = '''            <!-- フォーム診断 -->
            <div class="max-w-2xl mx-auto">
                <div class="impact-box">
                    <div class="text-center mb-6">
                        <div class="inline-block bg-red-600 text-white px-6 py-2 rounded-full font-black text-lg">
                            最速30秒！今すぐ診断
                        </div>
                    </div>
                    <h3 class="text-2xl md:text-3xl font-black text-center mb-6">📧 無料診断フォーム</h3>
                    
                    <!-- 特典強調 -->
                    <div class="bg-yellow-100 border-4 border-yellow-400 rounded-lg p-4 mb-6 text-center">
                        <p class="font-black text-lg text-red-600 mb-2">
                            👇 送信後すぐにガイドブックをメール送付！ 👇
                        </p>
                        <p class="text-sm font-bold">
                            診断結果とガイドブックが自動で届きます
                        </p>
                    </div>'''
        
        # フォーム診断の<h3>タグ以降を取得
        form_h3_start = after_form_start.find('<h3 class="text-2xl md:text-3xl font-black text-center mb-8">📧 フォーム診断</h3>')
        if form_h3_start != -1:
            # <h3>以降を取得
            after_h3 = after_form_start[form_h3_start + len('<h3 class="text-2xl md:text-3xl font-black text-center mb-8">📧 フォーム診断</h3>'):]
            content = before + new_section + after_h3

# </div>を1つ追加（grid削除の代わり）
content = content.replace('                </div>\n            </div>\n            \n            <!-- 最終警告 -->', '                </div>\n            </div>\n            \n            <!-- 最終警告 -->')

# ボタンテキスト変更
content = content.replace('<i class="fas fa-paper-plane mr-2"></i>診断を依頼する', '<i class="fas fa-paper-plane mr-2"></i>診断を依頼する（ガイドブック自動送付）')

# 24時間以内に返信
content = content.replace('⚡ 24時間以内に必ず返信します', '⚡ 24時間以内にプロから詳しい診断結果をお送りします')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ LINE機能を全て削除しました")
print("✅ フォーム診断のみに変更しました")
print("✅ 自動メール送信の仕組みに変更しました")
