# Google広告コンバージョントラッキング設定完了

## ✅ 設定完了内容

Google広告のコンバージョントラッキングタグ（ID: AW-1788516127）を以下のファイルに追加しました：

- index.html
- blog-kasai-001.html
- blog-kasai-002.html
- blog-kasai-003.html

## 📋 追加したコード

```html
<!-- Google Ads Conversion Tracking -->
<script async src="https://www.googletagmanager.com/gtag/js?id=AW-1788516127"></script>
<script>
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', 'AW-1788516127');
</script>
<!-- End Google Ads Conversion Tracking -->
```

このコードは、すべてのページの `<head>` セクション内に設置されています。

## 🎯 これで何ができるようになったか

1. **コンバージョン測定**
   - 問い合わせフォーム送信
   - 電話ボタンクリック
   - LINE相談ボタンクリック

2. **広告効果の分析**
   - どの広告からコンバージョンが発生したか
   - コンバージョン単価（CPA）の計算
   - ROI（投資対効果）の測定

3. **自動入札の最適化**
   - コンバージョンデータを基に自動入札が最適化される

## 📊 次のステップ（Google広告管理画面で実施）

### ステップ1: コンバージョンアクションを作成

1. **Google広告管理画面にログイン**
   - https://ads.google.com/

2. **ツールと設定 > 測定 > コンバージョン**

3. **新しいコンバージョンアクションを作成**

#### **コンバージョン1: 電話問い合わせ**
- 種類: ウェブサイト
- カテゴリ: 電話での問い合わせ
- 値: 30,000円（見込み客1件あたりの価値）
- カウント方法: 1回のみ

#### **コンバージョン2: LINE問い合わせ**
- 種類: ウェブサイト
- カテゴリ: 問い合わせ
- 値: 25,000円
- カウント方法: 1回のみ

#### **コンバージョン3: フォーム送信**
- 種類: ウェブサイト
- カテゴリ: 問い合わせ
- 値: 20,000円
- カウント方法: 1回のみ

### ステップ2: イベントスニペットを追加（オプション）

より詳細な測定をしたい場合は、以下のコードを該当ページに追加：

#### **電話クリック測定**
```html
<script>
gtag('event', 'conversion', {
    'send_to': 'AW-1788516127/xxxxx', // xxxxx = コンバージョンラベル
    'value': 30000,
    'currency': 'JPY'
});
</script>
```

#### **LINE問い合わせ測定**
```html
<script>
gtag('event', 'conversion', {
    'send_to': 'AW-1788516127/yyyyy', // yyyyy = コンバージョンラベル
    'value': 25000,
    'currency': 'JPY'
});
</script>
```

## 🔍 動作確認方法

### 方法1: Google Tag Assistant（Chrome拡張機能）

1. **Google Tag Assistantをインストール**
   - https://chrome.google.com/webstore/detail/tag-assistant-legacy-by-g/kejbdjndbnbjgmefkgdddjlbokphdefk

2. **サイトを開いて「Record」をクリック**

3. **ページを更新**

4. **「Stop Recording」をクリック**

5. **Google Ads Conversion Trackingタグが検出されればOK**

### 方法2: ブラウザの開発者ツール

1. **サイトを開く**

2. **F12キーを押して開発者ツールを開く**

3. **「Network」タブを選択**

4. **ページを更新**

5. **「googletagmanager.com」への通信があればOK**

### 方法3: Google広告管理画面

1. **ツールと設定 > 測定 > コンバージョン**

2. **「ステータス」列を確認**

3. **「最近のコンバージョンなし」→「タグは正常に動作しています」に変わればOK**
   - 通常24時間以内に反映

## ⚠️ 注意事項

1. **テストコンバージョンは除外する**
   - 自分でクリックしたコンバージョンは除外設定をする

2. **プライバシーポリシーを更新**
   - Google広告のコンバージョントラッキングを使用していることを明記

3. **Cookieの同意バナー**
   - 必要に応じてCookie同意バナーを設置

## 📞 サポート

設定に問題がある場合は、Google広告サポートに問い合わせ：
- 電話: 0120-59-0331（平日9:00-18:00）
- チャット: Google広告管理画面右上のヘルプアイコンから

## 📅 作成日

2026年3月19日

## ✅ 完了確認

- [x] Google広告タグ（AW-1788516127）を追加
- [x] 主要HTMLファイルに設置
- [x] GitHubにプッシュ
- [x] Cloudflare Pagesにデプロイ
- [ ] Google広告管理画面でコンバージョンアクションを作成（次のステップ）
- [ ] 24時間後にタグの動作を確認
