#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
株式会社NEXTONEの正式な会社情報を反映
"""

# 特商法ページを更新
with open('tokushohou.html', 'r', encoding='utf-8') as f:
    tokushohou = f.read()

# 事業者情報テーブルを更新
old_table = '''                    <table class="w-full">
                        <tr class="border-b">
                            <th class="text-left py-3 px-4 bg-gray-100 font-bold w-1/3">サービス名</th>
                            <td class="py-3 px-4">外壁塗装オンライン診断センター ～雨漏り・外壁修理110番～</td>
                        </tr>
                        <tr class="border-b">
                            <th class="text-left py-3 px-4 bg-gray-100 font-bold">運営会社</th>
                            <td class="py-3 px-4">ネクストワン</td>
                        </tr>
                        <tr class="border-b">
                            <th class="text-left py-3 px-4 bg-gray-100 font-bold">代表者</th>
                            <td class="py-3 px-4">[代表者名を記入]</td>
                        </tr>
                        <tr class="border-b">
                            <th class="text-left py-3 px-4 bg-gray-100 font-bold">所在地</th>
                            <td class="py-3 px-4">[住所を記入]</td>
                        </tr>
                        <tr class="border-b">
                            <th class="text-left py-3 px-4 bg-gray-100 font-bold">電話番号</th>
                            <td class="py-3 px-4">[電話番号を記入]</td>
                        </tr>
                        <tr class="border-b">
                            <th class="text-left py-3 px-4 bg-gray-100 font-bold">メールアドレス</th>
                            <td class="py-3 px-4">[メールアドレスを記入]</td>
                        </tr>
                        <tr class="border-b">
                            <th class="text-left py-3 px-4 bg-gray-100 font-bold">営業時間</th>
                            <td class="py-3 px-4">月～金 9:00-18:00（土日祝日除く）</td>
                        </tr>
                    </table>'''

new_table = '''                    <table class="w-full">
                        <tr class="border-b">
                            <th class="text-left py-3 px-4 bg-gray-100 font-bold w-1/3">サービス名</th>
                            <td class="py-3 px-4">外壁塗装オンライン診断センター ～雨漏り・外壁修理110番～</td>
                        </tr>
                        <tr class="border-b">
                            <th class="text-left py-3 px-4 bg-gray-100 font-bold">運営会社</th>
                            <td class="py-3 px-4">株式会社NEXTONE</td>
                        </tr>
                        <tr class="border-b">
                            <th class="text-left py-3 px-4 bg-gray-100 font-bold">代表者</th>
                            <td class="py-3 px-4">上原 恵美</td>
                        </tr>
                        <tr class="border-b">
                            <th class="text-left py-3 px-4 bg-gray-100 font-bold">設立日</th>
                            <td class="py-3 px-4">2023年5月</td>
                        </tr>
                        <tr class="border-b">
                            <th class="text-left py-3 px-4 bg-gray-100 font-bold">所在地</th>
                            <td class="py-3 px-4">〒194-0045<br>東京都町田市南成瀬5丁目1-10 サンプラザ西之久保2-B号</td>
                        </tr>
                        <tr class="border-b">
                            <th class="text-left py-3 px-4 bg-gray-100 font-bold">電話番号</th>
                            <td class="py-3 px-4">0120-773-743（フリーダイヤル）</td>
                        </tr>
                        <tr class="border-b">
                            <th class="text-left py-3 px-4 bg-gray-100 font-bold">メールアドレス</th>
                            <td class="py-3 px-4">[メールアドレスを記入]</td>
                        </tr>
                        <tr class="border-b">
                            <th class="text-left py-3 px-4 bg-gray-100 font-bold">営業時間</th>
                            <td class="py-3 px-4">月～金 9:00-18:00（土日祝日除く）</td>
                        </tr>
                    </table>'''

tokushohou = tokushohou.replace(old_table, new_table)

with open('tokushohou.html', 'w', encoding='utf-8') as f:
    f.write(tokushohou)

print("✅ tokushohou.html を更新しました")

# プライバシーポリシーを更新
with open('privacy.html', 'r', encoding='utf-8') as f:
    privacy = f.read()

# 基本方針の会社名を更新
privacy = privacy.replace(
    'ネクストワン（運営サービス：外壁塗装オンライン診断センター）（以下「当社」といいます）',
    '株式会社NEXTONE（運営サービス：外壁塗装オンライン診断センター）（以下「当社」といいます）'
)

# お問い合わせ窓口のテーブルを更新
old_contact = '''                        <table class="w-full">
                            <tr class="border-b">
                                <th class="text-left py-2 font-bold w-1/3">サービス名</th>
                                <td class="py-2">外壁塗装オンライン診断センター</td>
                            </tr>
                            <tr class="border-b">
                                <th class="text-left py-2 font-bold">運営会社</th>
                                <td class="py-2">ネクストワン</td>
                            </tr>
                            <tr class="border-b">
                                <th class="text-left py-2 font-bold">住所</th>
                                <td class="py-2">[住所を記入]</td>
                            </tr>
                            <tr class="border-b">
                                <th class="text-left py-2 font-bold">電話番号</th>
                                <td class="py-2">[電話番号を記入]</td>
                            </tr>'''

new_contact = '''                        <table class="w-full">
                            <tr class="border-b">
                                <th class="text-left py-2 font-bold w-1/3">サービス名</th>
                                <td class="py-2">外壁塗装オンライン診断センター</td>
                            </tr>
                            <tr class="border-b">
                                <th class="text-left py-2 font-bold">運営会社</th>
                                <td class="py-2">株式会社NEXTONE</td>
                            </tr>
                            <tr class="border-b">
                                <th class="text-left py-2 font-bold">代表者</th>
                                <td class="py-2">上原 恵美</td>
                            </tr>
                            <tr class="border-b">
                                <th class="text-left py-2 font-bold">住所</th>
                                <td class="py-2">〒194-0045 東京都町田市南成瀬5丁目1-10 サンプラザ西之久保2-B号</td>
                            </tr>
                            <tr class="border-b">
                                <th class="text-left py-2 font-bold">電話番号</th>
                                <td class="py-2">0120-773-743（フリーダイヤル）</td>
                            </tr>'''

privacy = privacy.replace(old_contact, new_contact)

with open('privacy.html', 'w', encoding='utf-8') as f:
    f.write(privacy)

print("✅ privacy.html を更新しました")

# index.htmlのフッターにも電話番号を追加
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# フッターの対応エリアに電話番号を追加
old_footer_area = '''                <div class="text-center">
                    <h4 class="font-black text-lg mb-3">対応エリア</h4>
                    <p class="text-gray-400">神奈川県全域・東京都全域<br>横浜・川崎・町田・八王子<br>その他全市町村</p>
                </div>'''

new_footer_area = '''                <div class="text-center">
                    <h4 class="font-black text-lg mb-3">お問い合わせ</h4>
                    <p class="text-yellow-300 text-2xl font-black mb-2">0120-773-743</p>
                    <p class="text-gray-400 text-sm">フリーダイヤル<br>月～金 9:00-18:00</p>
                </div>
                <div class="text-center">
                    <h4 class="font-black text-lg mb-3">対応エリア</h4>
                    <p class="text-gray-400">神奈川県全域・東京都全域<br>横浜・川崎・町田・八王子<br>その他全市町村</p>
                </div>'''

# フッターは3列から4列に変更
html = html.replace(
    '<div class="grid md:grid-cols-3 gap-8 mb-8">',
    '<div class="grid md:grid-cols-4 gap-6 mb-8">'
)
html = html.replace(old_footer_area, new_footer_area)

# ヘッダーにも電話番号を追加
old_header = '''                <p class="text-sm md:text-base mt-2 text-blue-100">
                    神奈川・東京全域対応｜訪問なし・営業なし・毎日報告で安心
                </p>'''

new_header = '''                <p class="text-sm md:text-base mt-2 text-blue-100">
                    神奈川・東京全域対応｜訪問なし・営業なし・毎日報告で安心
                </p>
                <p class="text-xl md:text-2xl font-black mt-3 text-yellow-300">
                    📞 0120-773-743（フリーダイヤル）
                </p>'''

html = html.replace(old_header, new_header)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✅ index.html を更新しました")
print("\n🎉 株式会社NEXTONEの会社情報をすべてのページに反映しました！")
print("   - 会社名: 株式会社NEXTONE")
print("   - 代表者: 上原 恵美")
print("   - 設立日: 2023年5月")
print("   - 所在地: 〒194-0045 東京都町田市南成瀬5丁目1-10 サンプラザ西之久保2-B号")
print("   - 電話番号: 0120-773-743（フリーダイヤル）")
