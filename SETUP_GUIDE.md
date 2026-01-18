# 診断フォーム自動メール送信 - 設定手順書

## 📋 概要

診断フォーム送信後、自動で以下を実行します：
1. ✅ お客様に御礼メール送信（ガイドブックPDF添付）
2. ✅ 診断データをスプレッドシートに保存
3. ✅ 管理者に通知メール送信

---

## 🚀 設定手順

### ステップ1: Google Driveにガイドブックをアップロード

1. Google Driveにアクセス
2. 「guidebook.pdf」（塗装プレゼント.pdf）をアップロード
3. ファイルを右クリック → 「共有」
4. 「リンクを知っている全員」に変更して保存
5. URLをコピー（例: `https://drive.google.com/file/d/ABCD1234EFGH/view`）
6. URLから **ファイルID** を抽出（`ABCD1234EFGH` の部分）

---

### ステップ2: Googleスプレッドシート作成

1. Googleスプレッドシートを新規作成
2. シート名: 「外壁塗装診断_受付データ」
3. URLをコピー（例: `https://docs.google.com/spreadsheets/d/SPREADSHEET_ID_HERE/edit`）
4. URLから **スプレッドシートID** を抽出

---

### ステップ3: Google Apps Scriptの設定

#### 3-1. Apps Scriptエディタを開く

1. スプレッドシートを開く
2. メニュー → 「拡張機能」 → 「Apps Script」

#### 3-2. コードを貼り付け

1. `google-apps-script.js` の内容をコピー
2. Apps Scriptエディタに貼り付け
3. 以下の設定項目を変更：

```javascript
// PDFファイルのID（ステップ1で取得）
const PDF_FILE_ID = 'YOUR_PDF_FILE_ID_HERE';

// スプレッドシートのID（ステップ2で取得）
const SPREADSHEET_ID = 'YOUR_SPREADSHEET_ID_HERE';

// 管理者メールアドレス
const ADMIN_EMAIL = 'your-email@example.com';

// 会社情報
const COMPANY_NAME = '外壁塗装の真実';
const COMPANY_URL = 'https://your-domain.com';
```

#### 3-3. 保存

1. プロジェクト名: 「外壁塗装診断フォーム」
2. 「プロジェクトを保存」をクリック

---

### ステップ4: デプロイ

#### 4-1. ウェブアプリとして公開

1. 画面右上「デプロイ」 → 「新しいデプロイ」
2. 種類: 「ウェブアプリ」を選択
3. 説明: 「診断フォームAPI v1.0」
4. 次のユーザーとして実行: 「自分」
5. アクセスできるユーザー: 「全員」
6. 「デプロイ」をクリック
7. **ウェブアプリのURL** をコピー（例: `https://script.google.com/macros/s/ABCD1234/exec`）

#### 4-2. 権限の承認

1. 「アクセスを承認」をクリック
2. Googleアカウントを選択
3. 「詳細」 → 「外壁塗装診断フォーム（安全ではないページ）に移動」
4. 「許可」をクリック

---

### ステップ5: HTMLフォームの設定

#### 5-1. index.htmlを編集

`index.html` の JavaScript部分（約1150行目）を以下のように変更：

```javascript
// フォーム送信
const form = document.getElementById('diagnosisForm');
if (form) {
    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        // フォームデータ取得
        const formData = {
            name: form.name.value,
            location: form.location.value,
            age: form.age.value,
            phone: form.phone.value,
            email: form.email.value
        };
        
        // Google Apps Script URL（ステップ4で取得したURL）
        const scriptUrl = 'https://script.google.com/macros/s/YOUR_SCRIPT_ID/exec';
        
        try {
            // ローディング表示（オプション）
            const button = form.querySelector('button[type="submit"]');
            const originalText = button.innerHTML;
            button.innerHTML = '<i class="fas fa-spinner fa-spin mr-2"></i>送信中...';
            button.disabled = true;
            
            // Google Apps Scriptに送信
            await fetch(scriptUrl, {
                method: 'POST',
                mode: 'no-cors',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(formData)
            });
            
            alert('✅ 診断依頼を受け付けました！\n\n📧 ご入力いただいたメールアドレスに\n「外壁塗装ガイドブック（PDF）」を自動送信しました。\n\n⚡ 24時間以内にプロから詳しい診断結果をお送りします。\n\nしばらくお待ちください。');
            form.reset();
            
            // ボタンを元に戻す
            button.innerHTML = originalText;
            button.disabled = false;
            
        } catch (error) {
            alert('❌ 送信エラーが発生しました。\nお手数ですが、もう一度お試しください。');
            console.error('Error:', error);
            
            // ボタンを元に戻す
            button.innerHTML = originalText;
            button.disabled = false;
        }
    });
}
```

#### 5-2. scriptUrlの設定

`YOUR_SCRIPT_ID` の部分を、ステップ4で取得したウェブアプリURLに置き換えてください。

---

## 🧪 テスト手順

### テスト1: フォーム送信テスト

1. ブラウザで `index.html` を開く
2. 診断フォームに以下のテストデータを入力：
   - お名前: テスト太郎
   - 地域: 東京都町田市テスト町1-2-3
   - 築年数: 10〜15年
   - 電話番号: 090-1234-5678
   - メールアドレス: **自分のメールアドレス**
3. 「診断を依頼する」ボタンをクリック
4. 成功メッセージが表示されることを確認

### テスト2: メール受信テスト

1. 自分のメールボックスを確認
2. 以下のメールが届いているか確認：
   - 件名: 「【外壁塗装の真実】診断依頼ありがとうございます＋ガイドブックプレゼント🎁」
   - 添付ファイル: guidebook.pdf（7.5MB）
   - メール本文: HTML形式で綺麗に表示される

### テスト3: スプレッドシート保存テスト

1. Googleスプレッドシートを開く
2. テストデータが追加されているか確認
3. 列構成：
   - A列: 受付日時
   - B列: お名前
   - C列: 地域
   - D列: 築年数
   - E列: 電話番号
   - F列: メールアドレス
   - G列: ステータス

### テスト4: 管理者通知テスト

1. 管理者メールボックスを確認
2. 通知メールが届いているか確認
3. 件名: 「【新規診断依頼】テスト太郎 様から診断依頼がありました」

---

## 📧 メールのカスタマイズ

### 会社情報の変更

`google-apps-script.js` の以下の部分を変更：

```javascript
const COMPANY_NAME = '外壁塗装の真実';  // 会社名
const COMPANY_URL = 'https://your-domain.com';  // サイトURL
```

### メール本文の変更

`sendThankYouEmail()` 関数内の `htmlBody` と `textBody` を編集してください。

---

## 🔧 トラブルシューティング

### 問題1: メールが届かない

**原因と対処法：**
- PDF_FILE_IDが正しく設定されているか確認
- PDFファイルの共有設定が「リンクを知っている全員」になっているか確認
- メールアドレスが正しいか確認
- Gmailのスパムフォルダを確認

### 問題2: スプレッドシートに保存されない

**原因と対処法：**
- SPREADSHEET_IDが正しく設定されているか確認
- Apps Scriptの実行権限が承認されているか確認
- スプレッドシートの共有設定を確認

### 問題3: フォーム送信後エラーが出る

**原因と対処法：**
- scriptUrlが正しく設定されているか確認
- ブラウザのコンソール（F12）でエラーを確認
- Apps ScriptのログでエラーをTROUBLE確認（Apps Script エディタ → 実行ログ）

### 問題4: 「no-cors」でレスポンスが取得できない

**対処法：**
`no-cors` モードでは成功/失敗の判定ができません。これは仕様です。
代わりに、以下の方法で確認：
1. スプレッドシートにデータが保存されているか
2. メールが届いているか

---

## 📊 運用フロー

```
1. お客様がフォーム送信
    ↓
2. Google Apps Script実行
    ├─ スプレッドシートに保存
    ├─ お客様に御礼メール＋ガイドブック
    └─ 管理者に通知メール
    ↓
3. 管理者がスプレッドシート確認
    ↓
4. 24時間以内に診断結果を返信
    ↓
5. スプレッドシートのステータスを「対応済み」に変更
```

---

## 🔐 セキュリティ

- ✅ PDFファイルは「リンクを知っている全員」で共有（アクセス制限）
- ✅ スプレッドシートは管理者のみアクセス可能
- ✅ Apps Scriptは「自分」として実行（管理者権限）
- ✅ 個人情報は暗号化通信（HTTPS）で送信

---

## 📝 メンテナンス

### 定期的な確認事項

- 週1回: スプレッドシートのデータ件数確認
- 月1回: メール送信エラーの確認（Apps Script実行ログ）
- 月1回: ガイドブックPDFの更新確認

### データのバックアップ

- スプレッドシート: 自動でGoogle Driveに保存
- 手動バックアップ: ファイル → ダウンロード → CSV

---

## 🎉 完成！

これで、診断フォーム送信後に自動でガイドブックPDFが送信されます！

### 次のステップ

1. ✅ 本番環境にデプロイ
2. ✅ 実際のお客様でテスト
3. ✅ メール開封率・コンバージョン率を計測
4. ✅ 必要に応じてメール文面を改善

---

**お疲れ様でした！** 🎊

何か質問があれば、お気軽にお問い合わせください。
