#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
フッターに特商法・プライバシーポリシーのリンクを追加し、対応エリアを神奈川全域に変更
"""

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 対応エリアを神奈川全域に変更
old_area = '''                <div class="text-center">
                    <h4 class="font-black text-lg mb-3">対応エリア</h4>
                    <p class="text-gray-400">東京都全域<br>町田・立川・調布<br>八王子・多摩</p>
                </div>'''

new_area = '''                <div class="text-center">
                    <h4 class="font-black text-lg mb-3">対応エリア</h4>
                    <p class="text-gray-400">神奈川県全域<br>横浜・川崎・相模原<br>その他全市町村</p>
                </div>'''

html = html.replace(old_area, new_area)

# フッターのコピーライト前に特商法・プライバシーポリシーのリンクを追加
old_copyright = '''            <p class="text-gray-500 text-center text-sm">© 2026 外壁塗装の真実 All rights reserved.</p>'''

new_copyright = '''            <!-- 法的リンク -->
            <div class="flex justify-center gap-6 mb-6">
                <a href="tokushohou.html" class="text-gray-400 hover:text-white underline transition">
                    特定商取引法に基づく表記
                </a>
                <span class="text-gray-600">|</span>
                <a href="privacy.html" class="text-gray-400 hover:text-white underline transition">
                    プライバシーポリシー
                </a>
            </div>
            <p class="text-gray-500 text-center text-sm">© 2026 外壁塗装の真実 All rights reserved.</p>'''

html = html.replace(old_copyright, new_copyright)

# 診断フォーム下部の個人情報保護の文言にもリンクを追加
old_privacy_note = '''            <div class="mt-8 bg-white p-6 rounded-lg border-4 border-green-500">
                <p class="text-center text-lg font-bold">
                    🔒 個人情報は厳重に管理します<br>
                    📧 診断結果とガイドブックは自動でメール送付<br>
                    ⚡ 24時間以内にプロから詳しい診断結果をお送りします
                </p>
            </div>'''

new_privacy_note = '''            <div class="mt-8 bg-white p-6 rounded-lg border-4 border-green-500">
                <p class="text-center text-lg font-bold">
                    🔒 個人情報は厳重に管理します<br>
                    📧 診断結果とガイドブックは自動でメール送付<br>
                    ⚡ 24時間以内にプロから詳しい診断結果をお送りします
                </p>
                <p class="text-center text-sm text-gray-600 mt-4">
                    詳しくは<a href="privacy.html" class="text-blue-600 underline hover:text-blue-800" target="_blank">プライバシーポリシー</a>をご覧ください
                </p>
            </div>'''

html = html.replace(old_privacy_note, new_privacy_note)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✅ フッターを更新しました")
print("  - 特商法・プライバシーポリシーのリンクを追加")
print("  - 対応エリアを「神奈川県全域」に変更")
print("  - 診断フォーム下部にプライバシーポリシーリンクを追加")
