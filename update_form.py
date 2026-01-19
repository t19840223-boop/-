#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
診断フォームを更新：
- 郵便番号必須フィールド追加
- 郵便番号から住所自動検索機能
- 住所を任意に変更
- オンライン相談を任意に変更
- 対応エリア「神奈川全域」の明記
"""

# index.htmlを読み込み
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 古いフォームセクションを探して置換
old_form = '''                    <form id="diagnosisForm" class="space-y-6">
                        <div>
                            <label class="block font-black text-lg mb-3">
                                👤 お名前 <span class="text-red-600 text-xl">（必須）</span>
                            </label>
                            <input type="text" name="name" placeholder="例: 山田 太郎" 
                                   class="w-full px-4 py-4 text-lg border-4 border-gray-300 rounded-lg focus:border-red-600 focus:outline-none" 
                                   required>
                            <p class="text-sm text-gray-600 mt-2">※診断結果のご連絡時に使用します</p>
                        </div>
                        
                        <div>
                            <label class="block font-black text-lg mb-3">
                                📍 お住まいの地域 <span class="text-red-600 text-xl">（必須）</span>
                            </label>
                            <input type="text" name="location" placeholder="例: 東京都町田市〇〇町1-2-3" 
                                   class="w-full px-4 py-4 text-lg border-4 border-gray-300 rounded-lg focus:border-red-600 focus:outline-none" 
                                   required>
                            <p class="text-sm text-gray-600 mt-2">※詳しいほど正確な診断ができます</p>
                        </div>'''

new_form = '''                    <!-- 対応エリア告知 -->
                    <div class="bg-gradient-to-r from-blue-50 to-green-50 border-4 border-blue-400 rounded-lg p-6 mb-6 text-center">
                        <p class="text-xl font-black text-blue-700 mb-2">
                            🏠 対応エリア: 神奈川全域
                        </p>
                        <p class="text-sm text-gray-700">
                            横浜市・川崎市・相模原市・横須賀市・平塚市・鎌倉市・藤沢市・小田原市・茅ヶ崎市・逗子市・三浦市・秦野市・厚木市・大和市・伊勢原市・海老名市・座間市・南足柄市・綾瀬市 ほか神奈川県全域
                        </p>
                    </div>
                    
                    <form id="diagnosisForm" class="space-y-6">
                        <div>
                            <label class="block font-black text-lg mb-3">
                                👤 お名前 <span class="text-red-600 text-xl">（必須）</span>
                            </label>
                            <input type="text" name="name" placeholder="例: 山田 太郎" 
                                   class="w-full px-4 py-4 text-lg border-4 border-gray-300 rounded-lg focus:border-red-600 focus:outline-none" 
                                   required>
                            <p class="text-sm text-gray-600 mt-2">※診断結果のご連絡時に使用します</p>
                        </div>
                        
                        <!-- 郵便番号（必須） -->
                        <div>
                            <label class="block font-black text-lg mb-3">
                                📮 郵便番号 <span class="text-red-600 text-xl">（必須）</span>
                            </label>
                            <div class="flex gap-2">
                                <input type="text" name="postalCode" id="postalCode" 
                                       placeholder="例: 123-4567" 
                                       maxlength="8"
                                       pattern="\d{3}-?\d{4}"
                                       class="flex-1 px-4 py-4 text-lg border-4 border-gray-300 rounded-lg focus:border-red-600 focus:outline-none" 
                                       required>
                                <button type="button" id="searchAddressBtn" 
                                        class="px-6 py-4 bg-blue-600 text-white font-black rounded-lg hover:bg-blue-700 transition whitespace-nowrap">
                                    🔍 住所検索
                                </button>
                            </div>
                            <p class="text-sm text-gray-600 mt-2">※郵便番号を入力して「住所検索」ボタンを押すと自動で住所が入力されます</p>
                        </div>
                        
                        <!-- 住所（任意） -->
                        <div>
                            <label class="block font-black text-lg mb-3">
                                📍 お住まいの住所 <span class="text-gray-500 text-base">（任意）</span>
                            </label>
                            <input type="text" name="address" id="address" 
                                   placeholder="例: 神奈川県横浜市〇〇区△△町1-2-3" 
                                   class="w-full px-4 py-4 text-lg border-4 border-gray-300 rounded-lg focus:border-red-600 focus:outline-none">
                            <p class="text-sm text-gray-600 mt-2">※詳しいほど正確な診断ができます（自動入力されます）</p>
                        </div>'''

html = html.replace(old_form, new_form)

# オンライン診断希望日時を任意に変更
old_online = '''                        <!-- オンライン診断希望日時 -->
                        <div>
                            <label class="block font-black text-lg mb-3">
                                📹 オンライン診断希望日時 <span class="text-red-600 text-xl">（必須）</span>
                            </label>'''

new_online = '''                        <!-- オンライン診断希望日時（任意） -->
                        <div>
                            <label class="block font-black text-lg mb-3">
                                📹 オンライン相談希望日時 <span class="text-gray-500 text-base">（任意）</span>
                            </label>'''

html = html.replace(old_online, new_online)

# 第1希望日のrequired属性を削除
html = html.replace(
    '<input type="date" name="preferredDate1" id="preferredDate1"\n                                           class="w-full px-4 py-4 text-lg border-4 border-gray-300 rounded-lg focus:border-red-600 focus:outline-none" \n                                           required>',
    '<input type="date" name="preferredDate1" id="preferredDate1"\n                                           class="w-full px-4 py-4 text-lg border-4 border-gray-300 rounded-lg focus:border-red-600 focus:outline-none">'
)

html = html.replace(
    '<select name="preferredTime1" class="w-full px-4 py-3 text-lg border-4 border-gray-300 rounded-lg focus:border-red-600 focus:outline-none mt-2" required>',
    '<select name="preferredTime1" class="w-full px-4 py-3 text-lg border-4 border-gray-300 rounded-lg focus:border-red-600 focus:outline-none mt-2">'
)

# 郵便番号検索のJavaScriptを追加（</body>の直前）
postal_search_script = '''
    <!-- 郵便番号検索機能 -->
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const searchBtn = document.getElementById('searchAddressBtn');
            const postalCodeInput = document.getElementById('postalCode');
            const addressInput = document.getElementById('address');
            
            if (searchBtn) {
                searchBtn.addEventListener('click', async function() {
                    let postalCode = postalCodeInput.value.replace(/[^0-9]/g, '');
                    
                    if (postalCode.length !== 7) {
                        alert('郵便番号を正しく入力してください（例: 123-4567）');
                        return;
                    }
                    
                    // ボタンをローディング状態に
                    searchBtn.disabled = true;
                    searchBtn.textContent = '検索中...';
                    
                    try {
                        // 郵便番号APIを使用（無料・認証不要）
                        const response = await fetch(`https://zipcloud.ibsnet.co.jp/api/search?zipcode=${postalCode}`);
                        const data = await response.json();
                        
                        if (data.status === 200 && data.results) {
                            const result = data.results[0];
                            const fullAddress = result.address1 + result.address2 + result.address3;
                            addressInput.value = fullAddress;
                            
                            // 神奈川県かチェック
                            if (result.address1 === '神奈川県') {
                                alert('✅ 対応エリアです！住所が自動入力されました。');
                            } else {
                                alert('⚠️ 申し訳ございません。現在の対応エリアは神奈川県全域となっております。\\n住所は自動入力されましたが、対応エリア外の可能性がございます。');
                            }
                        } else {
                            alert('郵便番号が見つかりませんでした。もう一度確認してください。');
                        }
                    } catch (error) {
                        console.error('住所検索エラー:', error);
                        alert('住所の検索に失敗しました。手動で入力してください。');
                    } finally {
                        // ボタンを元に戻す
                        searchBtn.disabled = false;
                        searchBtn.textContent = '🔍 住所検索';
                    }
                });
            }
            
            // 郵便番号の自動フォーマット（ハイフン追加）
            if (postalCodeInput) {
                postalCodeInput.addEventListener('input', function(e) {
                    let value = e.target.value.replace(/[^0-9]/g, '');
                    if (value.length > 3) {
                        value = value.slice(0, 3) + '-' + value.slice(3, 7);
                    }
                    e.target.value = value;
                });
            }
        });
    </script>

    </body>'''

html = html.replace('</body>', postal_search_script)

# 保存
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✅ 診断フォームを更新しました")
print("  - 郵便番号必須フィールド追加")
print("  - 郵便番号→住所自動検索機能追加")
print("  - 住所フィールドを任意に変更")
print("  - オンライン相談を任意に変更")
print("  - 対応エリア「神奈川全域」を明記")
