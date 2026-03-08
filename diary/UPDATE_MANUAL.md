# 📝 上原社長の日記 - 更新マニュアル

## 🎯 目的
週3〜4回、5分で記事を投稿できるようにする

---

## 📂 ファイル構成

```
/home/user/webapp/
├── diary/
│   ├── index.html          ← 日記一覧ページ
│   ├── diary-001.html      ← 記事1（自己紹介）
│   ├── diary-002.html      ← 記事2（現場レポート）
│   ├── diary-003.html      ← 記事3（子育て）
│   ├── template.html       ← コピペ用テンプレート ★これを使う
│   └── (次回: diary-004.html を作成)
│
└── images/diary/
    ├── profile.jpg         ← 上原社長の写真
    └── (今後の写真はここに保存)
```

---

## 🚀 記事の書き方（5ステップ）

### 【ステップ1】テンプレートをコピー

```bash
cd /home/user/webapp/diary
cp template.html diary-004.html
```

↓

### 【ステップ2】エディタで開いて編集

```bash
# VSCodeやテキストエディタで開く
code diary-004.html
```

または

```bash
# Vimで開く
vim diary-004.html
```

↓

### 【ステップ3】以下の部分を書き換える

#### 📅 日付を変更（2箇所）
```html
<!-- ① メタタグ -->
<title>【タイトルを書く】｜上原社長の日記</title>

<!-- ② 本文内の日付 -->
<div class="text-sm text-gray-500 mb-4">
    📅 2024年3月XX日（X）☀️
</div>
```

#### 📝 タイトルを変更
```html
<h1 class="text-3xl md:text-4xl font-black text-gray-800 mb-6">
    【ここにタイトルを書く】
</h1>
```

#### ✍️ 本文を書く（3〜10行くらい）
```html
<p class="text-lg leading-relaxed text-gray-700 mb-6">
    【ここに文章を書く】
</p>
```

#### 🏷️ タグを変更（3つまで）
```html
<span class="bg-blue-100 text-blue-800 px-3 py-1 rounded-full text-sm">#タグ1</span>
<span class="bg-blue-100 text-blue-800 px-3 py-1 rounded-full text-sm">#タグ2</span>
```

**人気のタグ例：**
- #お客様の声
- #子育てと仕事
- #女性社長
- #町田市 / #横浜市 / #相模原市
- #社員に感謝
- #現場レポート

↓

### 【ステップ4】写真を追加（任意）

写真がある場合：

1. 写真を `/home/user/webapp/images/diary/` に保存
   - ファイル名例：`diary-004-1.jpg`

2. HTMLで写真パスを変更
```html
<div class="my-8">
    <img src="../images/diary/diary-004-1.jpg" alt="写真の説明" class="w-full rounded-xl shadow-lg">
</div>
```

写真がない場合：
- アイコンのままでOK（削除不要）

↓

### 【ステップ5】一覧ページに追加

`diary/index.html` を開いて、**一番上に**新しい記事カードを追加：

```html
<!-- 記事4（NEW!） -->
<article class="diary-entry bg-white rounded-2xl shadow-lg overflow-hidden hover:shadow-xl transition"
         data-keywords="【検索用キーワードをスペース区切りで】">
    <a href="diary-004.html" class="block md:flex">
        <div class="md:w-1/3 bg-gray-200 flex items-center justify-center p-8">
            <i class="fas fa-【アイコン名】 text-6xl text-gray-400"></i>
        </div>
        <div class="md:w-2/3 p-6 md:p-8">
            <div class="text-sm text-gray-500 mb-2">
                📅 2024年3月XX日（X）
            </div>
            <h2 class="text-2xl font-black text-gray-800 mb-3 hover:text-blue-600 transition">
                【タイトル】
            </h2>
            <p class="text-gray-600 mb-4">
                【記事の要約（2〜3行）】
            </p>
            <div class="flex flex-wrap gap-2">
                <span class="bg-blue-100 text-blue-800 px-3 py-1 rounded-full text-sm">#タグ1</span>
                <span class="bg-blue-100 text-blue-800 px-3 py-1 rounded-full text-sm">#タグ2</span>
            </div>
        </div>
    </a>
</article>
```

**アイコン例：**
- `fa-child` → 子供
- `fa-comments` → 会話
- `fa-home` → 家
- `fa-tools` → 工事
- `fa-heart` → 感謝

↓

### 【ステップ6】トップページも更新（任意）

`index.html` の社長日記セクションの最新3件を更新：

```html
<!-- 最新記事3件のカードを差し替える -->
```

---

## 📤 アップロード手順

### ローカルで確認
```bash
cd /home/user/webapp
# ブラウザで確認（任意）
```

### Git コミット
```bash
cd /home/user/webapp
git add diary/diary-004.html diary/index.html index.html images/diary/*
git commit -m "Add diary post 4: タイトル"
```

### Cloudflare Pages にデプロイ
```bash
cd /home/user/webapp
npx wrangler pages deploy . --project-name=amamoritokka0623 --branch=main
```

**完了！🎉**

数分で本番サイトに反映されます。

---

## 💡 記事ネタ例

### 【仕事系】
- 今日の現場レポート
- お客様から嬉しい言葉をいただいた
- 訪問販売トラブルの相談
- 火災保険適用のケース
- 工事完了の写真

### 【子育て系】
- 子供が熱を出して…
- 保育園の運動会
- 仕事と子育ての両立
- 長男・次男のエピソード

### 【社員・会社系】
- 社員さんに助けられた話
- 事務所の掃除
- チームミーティング
- 会社のこれから

### 【プライベート】
- 週末の過ごし方
- 家族でお出かけ
- 今週の振り返り

---

## ⏱️ 所要時間目安

- 記事作成：3〜5分
- 写真追加：1〜2分
- 一覧ページ更新：2分
- コミット・デプロイ：2分

**合計：8〜11分**

---

## 🆘 困った時は

1. **テンプレートを間違えて編集した**
   → `git checkout template.html` で元に戻す

2. **デプロイがエラーになる**
   → `git status` でファイル確認
   → エラーメッセージを確認

3. **写真が表示されない**
   → パスが正しいか確認（`../images/diary/ファイル名`）
   → ファイル名に日本語・スペースがないか確認

---

## 📞 サポート

わからないことがあれば、いつでも聞いてください！
