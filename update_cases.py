#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 失敗事例セクションを訪問販売関連の内容に変更

with open('/home/user/webapp/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 事例1: Aさん - 訪問販売を無視
content = content.replace(
    '''チョーキング放置で<br>壁の中まで浸水</span>
                </h3>
                <div class="bg-gray-50 p-5 rounded-lg mb-4 border-l-4 border-red-500">
                    <p class="font-bold mb-3">「まだ大丈夫だろう」と放置した結果...</p>
                    <ul class="space-y-2">
                        <li class="flex items-start">
                            <span class="text-red-600 mr-2">→</span>
                            <span>気づいたら壁の中まで雨水侵入</span>
                        </li>
                        <li class="flex items-start">
                            <span class="text-red-600 mr-2">→</span>
                            <span>クロス・ボードの交換が必要に</span>
                        </li>
                        <li class="flex items-start">
                            <span class="text-red-600 mr-2">→</span>
                            <span>家具の移動・仮住まいの費用も...</span>
                        </li>
                    </ul>
                </div>
                <div class="danger-stripe">
                    <div class="bg-white p-5 text-center">
                        <p class="font-black text-red-600 text-2xl">早期発見していれば...</p>
                        <p class="text-lg mt-2">一般的な塗装で済んだケースです</p>''',
    '''「訪販は断れば良い」<br>と思っていたら...</span>
                </h3>
                <div class="bg-gray-50 p-5 rounded-lg mb-4 border-l-4 border-red-500">
                    <p class="font-bold mb-3">訪問販売員の指摘を「営業だろう」と無視した結果...</p>
                    <ul class="space-y-2">
                        <li class="flex items-start">
                            <span class="text-red-600 mr-2">→</span>
                            <span>半年後、壁の中まで雨水が侵入していた</span>
                        </li>
                        <li class="flex items-start">
                            <span class="text-red-600 mr-2">→</span>
                            <span>クロス・ボード・柱の交換に300万円</span>
                        </li>
                        <li class="flex items-start">
                            <span class="text-red-600 mr-2">→</span>
                            <span>「あの時ちゃんと見てもらえば...」と後悔</span>
                        </li>
                    </ul>
                </div>
                <div class="danger-stripe">
                    <div class="bg-white p-5 text-center">
                        <p class="font-black text-red-600 text-2xl">無料診断を受けていれば...</p>
                        <p class="text-lg mt-2">塗装だけで100万円台で済んだケース</p>'''
)

# 事例2: Bさん - 業者選びで迷って放置
content = content.replace(
    '''台風で屋根が飛散<br>隣家の車を破損</span>
                </h3>
                <div class="bg-gray-50 p-5 rounded-lg mb-4 border-l-4 border-red-500">
                    <p class="font-bold mb-3">屋根の釘抜けに気づかず放置...</p>
                    <ul class="space-y-2">
                        <li class="flex items-start">
                            <span class="text-red-600 mr-2">→</span>
                            <span>台風で屋根が飛んだ</span>
                        </li>
                        <li class="flex items-start">
                            <span class="text-red-600 mr-2">→</span>
                            <span>隣の家の新車に直撃</span>
                        </li>
                        <li class="flex items-start">
                            <span class="text-red-600 mr-2">→</span>
                            <span>近所付き合いが最悪に...</span>
                        </li>
                    </ul>
                </div>
                <div class="danger-stripe">
                    <div class="bg-white p-5 text-center">
                        <p class="font-black text-red-600 text-2xl">定期点検していれば...</p>
                        <p class="text-lg mt-2">損害賠償も自宅修理も不要でした</p>''',
    '''「どこに頼めば...」<br>と迷っている間に</span>
                </h3>
                <div class="bg-gray-50 p-5 rounded-lg mb-4 border-l-4 border-red-500">
                    <p class="font-bold mb-3">業者選びに迷い、3年放置した結果...</p>
                    <ul class="space-y-2">
                        <li class="flex items-start">
                            <span class="text-red-600 mr-2">→</span>
                            <span>台風で屋根が飛び、隣家の車を破損</span>
                        </li>
                        <li class="flex items-start">
                            <span class="text-red-600 mr-2">→</span>
                            <span>損害賠償＋自宅修理で500万円超え</span>
                        </li>
                        <li class="flex items-start">
                            <span class="text-red-600 mr-2">→</span>
                            <span>近所との関係も最悪に...</span>
                        </li>
                    </ul>
                </div>
                <div class="danger-stripe">
                    <div class="bg-white p-5 text-center">
                        <p class="font-black text-red-600 text-2xl">無料診断で相談していれば...</p>
                        <p class="text-lg mt-2">信頼できる業者を紹介できたケース</p>'''
)

# 事例3: Cさん - ネットで悪徳業者に騙された
content = content.replace(
    '''クラック放置で<br>柱が腐食・交換</span>
                </h3>
                <div class="bg-gray-50 p-5 rounded-lg mb-4 border-l-4 border-red-500">
                    <p class="font-bold mb-3">「小さいヒビだから平気」と放置...</p>
                    <ul class="space-y-2">
                        <li class="flex items-start">
                            <span class="text-red-600 mr-2">→</span>
                            <span>雨水が柱まで到達</span>
                        </li>
                        <li class="flex items-start">
                            <span class="text-red-600 mr-2">→</span>
                            <span>柱の交換が必要に</span>
                        </li>
                        <li class="flex items-start">
                            <span class="text-red-600 mr-2">→</span>
                            <span>外壁＋内装工事に拡大</span>
                        </li>
                    </ul>
                </div>
                <div class="danger-stripe">
                    <div class="bg-white p-5 text-center">
                        <p class="font-black text-red-600 text-2xl">早期対応していれば...</p>
                        <p class="text-lg mt-2">一般的な塗装で済んだケースです</p>''',
    '''「訪販は嫌」でネット検索<br>悪徳業者に当たった</span>
                </h3>
                <div class="bg-gray-50 p-5 rounded-lg mb-4 border-l-4 border-red-500">
                    <p class="font-bold mb-3">「訪販より安心」と思ってネットで依頼したが...</p>
                    <ul class="space-y-2">
                        <li class="flex items-start">
                            <span class="text-red-600 mr-2">→</span>
                            <span>高額見積もり＋手抜き工事で大失敗</span>
                        </li>
                        <li class="flex items-start">
                            <span class="text-red-600 mr-2">→</span>
                            <span>2年で再塗装が必要に（通常10年持つ）</span>
                        </li>
                        <li class="flex items-start">
                            <span class="text-red-600 mr-2">→</span>
                            <span>結局、倍以上の費用がかかった</span>
                        </li>
                    </ul>
                </div>
                <div class="danger-stripe">
                    <div class="bg-white p-5 text-center">
                        <p class="font-black text-red-600 text-2xl">無料診断で相見積もりしていれば...</p>
                        <p class="text-lg mt-2">悪徳業者を見抜けたケース</p>'''
)

with open('/home/user/webapp/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ 失敗事例セクションを訪問販売関連に更新しました")
print("  - 事例1: 訪販を無視して後悔")
print("  - 事例2: 業者選びに迷って大損")  
print("  - 事例3: ネットで悪徳業者に騙された")
