#!/bin/bash
# 事例1-3: page 1
# 事例4-9: page 2  
# 事例10-11: page 3

# 事例2を修正
sed -i 's|<!-- 事例2: 訪問販売と比較して220万円削減 -->|<!-- 事例2: 訪問販売と比較して220万円削減 -->\n                <div class="case-item" data-page="1">|' jirei.html
sed -i '0,/<div class="bg-white rounded-2xl shadow-2xl overflow-hidden hover:shadow-3xl transition-all border-4 border-yellow-400">/s|<div class="bg-white rounded-2xl shadow-2xl overflow-hidden hover:shadow-3xl transition-all border-4 border-yellow-400">|<div class="bg-white rounded-2xl shadow-2xl overflow-hidden hover:shadow-3xl transition-all border-4 border-yellow-400">\n                </div>|' jirei.html

echo "Script executed"
