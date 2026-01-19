#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 画像1を新しいバージョンに置き換える

with open('/home/user/webapp/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 新しい画像をbase64エンコード
with open('/home/user/webapp/line-report-1-new.b64', 'r') as f:
    img_new_base64 = f.read().strip()

# 古い画像のbase64を探す
import re

# data:image/jpeg;base64,で始まる最初の画像を置換
pattern = r'(src="data:image/jpeg;base64,)([^"]+)(")'

def replace_first_image(match):
    global first_replaced
    if not hasattr(replace_first_image, 'called'):
        replace_first_image.called = True
        return f'{match.group(1)}{img_new_base64}{match.group(3)}'
    return match.group(0)

content = re.sub(pattern, replace_first_image, content, count=1)

with open('/home/user/webapp/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ 画像1を新しいバージョンに置き換えました")
print("  - 緑の説明文（防水工事 アルバムを作成しました）付きの画像に変更")
