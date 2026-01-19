#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# HTMLに画像をbase64で埋め込む

with open('/home/user/webapp/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 画像1をbase64エンコード
with open('/home/user/webapp/line-report-1.b64', 'r') as f:
    img1_base64 = f.read().strip()

# 画像2をbase64エンコード
with open('/home/user/webapp/line-report-2.b64', 'r') as f:
    img2_base64 = f.read().strip()

# 画像3をbase64エンコード
with open('/home/user/webapp/line-report-3.b64', 'r') as f:
    img3_base64 = f.read().strip()

# 画像パスをbase64に置換
content = content.replace(
    'src="line-report-1.jpg"',
    f'src="data:image/jpeg;base64,{img1_base64}"'
)

content = content.replace(
    'src="line-report-2.jpg"',
    f'src="data:image/jpeg;base64,{img2_base64}"'
)

content = content.replace(
    'src="line-report-3.jpg"',
    f'src="data:image/jpeg;base64,{img3_base64}"'
)

with open('/home/user/webapp/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ 画像をbase64エンコードしてHTMLに埋め込みました")
print("  - line-report-1.jpg → base64埋め込み")
print("  - line-report-2.jpg → base64埋め込み")
print("  - line-report-3.jpg → base64埋め込み")
