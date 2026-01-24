#!/usr/bin/env python3
"""
雨漏り特化LP改修スクリプト
現在の外壁塗装LPを雨漏り専門サイトに変更
"""

# 新しいタイトルとメタ情報
new_title = "【緊急】雨漏りを今すぐ止めます｜オンライン診断24時間対応｜相模原・町田・横浜"
new_description = "雨漏り発生！今すぐ対応します。オンライン診断無料・緊急出動24時間・工事で出張費無料。訪問販売に騙されない、相見積もりサイトに頼らない、直接依頼で安心施工。"

# 新しいヘッダー（緊急対応バナー）
emergency_banner = '''    <!-- 🚨 緊急対応バナー（常時表示・最優先）-->
    <div class="bg-gradient-to-r from-red-700 via-red-600 to-red-700 text-white py-3 px-4 text-center sticky top-0 z-[100] shadow-2xl">
        <div class="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-center gap-3 md:gap-6">
            <div class="flex items-center gap-2">
                <span class="text-2xl animate-pulse">🚨</span>
                <span class="text-lg md:text-2xl font-black">雨漏り緊急対応24時間受付</span>
            </div>
            <a href="tel:0120773743" class="bg-yellow-400 text-red-900 px-6 py-3 rounded-full text-xl md:text-2xl font-black hover:bg-yellow-300 transition-all shadow-xl hover:scale-105">
                📞 0120-773-743
            </a>
            <span class="text-sm md:text-base text-yellow-200">最短1時間で駆けつけます</span>
        </div>
    </div>
'''

# 新しい屋号ヘッダー
new_header = '''    <!-- トップヘッダー（屋号）-->
    <header class="bg-gradient-to-r from-blue-700 to-blue-800 text-white py-4 md:py-6 px-4 shadow-lg">
        <div class="max-w-6xl mx-auto">
            <div class="text-center">
                <h1 class="text-2xl md:text-4xl font-black mb-2">
                    雨漏り修理オンライン診断センター
                </h1>
                <p class="text-lg md:text-2xl font-bold text-yellow-300">
                    ～24時間緊急対応・オンライン診断無料～
                </p>
                <p class="text-sm md:text-base mt-2 text-blue-100">
                    相模原・町田・横浜・川崎・八王子｜訪問なし・営業なし・毎日報告で安心
                </p>
            </div>
        </div>
    </header>
'''

# 新しいヒーローセクション
new_hero = '''    <!-- ヒーローセクション: 雨漏り特化 -->
    <section class="bg-gradient-to-b from-red-50 via-orange-50 to-white py-8 md:py-16 px-4">
        <div class="max-w-6xl mx-auto">
            
            <!-- メインコピー -->
            <div class="text-center mb-8">
                <div class="inline-block bg-red-600 text-white px-6 py-3 text-lg md:text-xl font-black mb-4 animate-pulse">
                    ⚠️ 雨漏りを放置すると家が崩れます
                </div>
                <h2 class="text-3xl md:text-6xl font-black mb-6 leading-tight text-gray-900">
                    その雨漏り、<br>
                    <span class="text-red-600">今すぐ止めます</span>
                </h2>
                <p class="text-xl md:text-3xl text-gray-800 mb-6 leading-relaxed font-bold">
                    オンライン診断なら<span class="text-blue-600">完全無料</span><br>
                    緊急対応なら<span class="text-red-600">最短1時間</span>で駆けつけます
                </p>
            </div>
            
            <!-- 2つのCTA -->
            <div class="grid md:grid-cols-2 gap-6 mb-12">
                <!-- 緊急対応CTA -->
                <div class="bg-gradient-to-br from-red-600 to-red-700 text-white rounded-2xl p-8 shadow-2xl border-4 border-red-400">
                    <div class="text-center mb-6">
                        <div class="text-6xl mb-3">🚨</div>
                        <h3 class="text-3xl font-black mb-3">緊急対応</h3>
                        <p class="text-lg mb-2">今すぐ雨漏りを止めたい！</p>
                        <p class="text-sm text-red-100">※応急処置のため出張費がかかります</p>
                        <p class="text-sm text-yellow-300 font-bold">工事契約時は出張費無料</p>
                    </div>
                    <a href="tel:0120773743" class="block bg-yellow-400 text-red-900 text-center text-2xl font-black px-8 py-6 rounded-full hover:bg-yellow-300 transition-all shadow-xl hover:scale-105">
                        📞 今すぐ電話する<br>
                        <span class="text-xl">0120-773-743</span>
                    </a>
                    <p class="text-center text-sm mt-4 text-red-100">24時間受付・最短1時間で到着</p>
                </div>
                
                <!-- オンライン診断CTA -->
                <div class="bg-gradient-to-br from-blue-600 to-blue-700 text-white rounded-2xl p-8 shadow-2xl border-4 border-blue-400">
                    <div class="text-center mb-6">
                        <div class="text-6xl mb-3">📱</div>
                        <h3 class="text-3xl font-black mb-3">オンライン診断</h3>
                        <p class="text-lg mb-2">写真を送るだけで診断！</p>
                        <p class="text-sm text-blue-100">※完全無料・営業一切なし</p>
                        <p class="text-sm text-yellow-300 font-bold">24時間以内に診断結果</p>
                    </div>
                    <a href="#diagnosis" class="block bg-yellow-400 text-blue-900 text-center text-2xl font-black px-8 py-6 rounded-full hover:bg-yellow-300 transition-all shadow-xl hover:scale-105">
                        📸 無料診断を受ける<br>
                        <span class="text-xl">30秒で完了</span>
                    </a>
                    <p class="text-center text-sm mt-4 text-blue-100">スマホで撮影→送信→診断完了</p>
                </div>
            </div>
            
            <!-- こんなお悩みありませんか？ -->
            <div class="bg-white rounded-2xl shadow-xl p-6 md:p-10 mb-8">
                <h3 class="text-2xl md:text-3xl font-black text-center mb-8 text-gray-800">
                    ⚠️ こんなお悩み、ありませんか？
                </h3>
                <div class="grid md:grid-cols-3 gap-6">
                    <div class="text-center p-6 bg-red-50 rounded-xl border-2 border-red-200">
                        <div class="text-5xl mb-3">😱</div>
                        <p class="font-black text-lg mb-2">天井から水が！</p>
                        <p class="text-sm text-gray-700">雨の日に天井から水が落ちてくる、シミができている</p>
                    </div>
                    <div class="text-center p-6 bg-orange-50 rounded-xl border-2 border-orange-200">
                        <div class="text-5xl mb-3">😰</div>
                        <p class="font-black text-lg mb-2">訪問販売に指摘</p>
                        <p class="text-sm text-gray-700">「雨漏りしますよ」と言われたけど、本当？嘘？</p>
                    </div>
                    <div class="text-center p-6 bg-yellow-50 rounded-xl border-2 border-yellow-200">
                        <div class="text-5xl mb-3">😓</div>
                        <p class="font-black text-lg mb-2">どこに頼めば…</p>
                        <p class="text-sm text-gray-700">相見積もりサイト？訪問販売？信頼できる業者がわからない</p>
                    </div>
                </div>
            </div>
        </div>
    </section>
'''

print("雨漏り特化LP改修スクリプト準備完了")
print("\n=== 変更内容 ===")
print("1. タイトル: 雨漏り緊急対応に変更")
print("2. 緊急対応バナー追加（常時表示）")
print("3. 屋号: 雨漏り修理オンライン診断センターに変更")
print("4. ヒーロー: 2つのCTA（緊急 / オンライン）")
print("5. 訴求: 失敗→共感→気付き→実行")
