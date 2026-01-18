/**
 * 外壁塗装診断フォーム - Google Apps Script
 * 
 * 【機能】
 * 1. フォームデータをスプレッドシートに保存
 * 2. 診断御礼メールを自動送信（ガイドブックPDF添付）
 * 3. 管理者に通知メール送信
 * 
 * 【設定手順】
 * 1. Google Driveに「guidebook.pdf」をアップロード
 * 2. PDFファイルのIDを取得（URLの「/d/ここの部分/view」）
 * 3. 下記の「PDF_FILE_ID」に設定
 * 4. スプレッドシートを作成し、URLをコピー
 * 5. 「SPREADSHEET_ID」に設定
 * 6. デプロイ → ウェブアプリとして実行 → URLをコピー
 * 7. index.htmlの「scriptUrl」に設定
 */

// ========================================
// 設定項目（ここを変更してください）
// ========================================

// PDFファイルのID（Google DriveにアップロードしたガイドブックPDF）
const PDF_FILE_ID = 'YOUR_PDF_FILE_ID_HERE';

// スプレッドシートのID（診断データを保存する）
const SPREADSHEET_ID = 'YOUR_SPREADSHEET_ID_HERE';

// 管理者メールアドレス（診断依頼の通知を受け取る）
const ADMIN_EMAIL = 'your-email@example.com';

// 会社情報
const COMPANY_NAME = '外壁塗装の真実';
const COMPANY_URL = 'https://your-domain.com';

// ========================================
// メイン処理
// ========================================

/**
 * POSTリクエストを受け取る
 */
function doPost(e) {
  try {
    // CORSヘッダー設定
    const output = ContentService.createTextOutput();
    output.setMimeType(ContentService.MimeType.JSON);
    
    // リクエストデータ取得
    const data = JSON.parse(e.postData.contents);
    
    // スプレッドシートに保存
    saveToSpreadsheet(data);
    
    // お客様に御礼メール送信（ガイドブック添付）
    sendThankYouEmail(data);
    
    // 管理者に通知メール送信
    sendNotificationToAdmin(data);
    
    // 成功レスポンス
    return output.setContent(JSON.stringify({
      status: 'success',
      message: '診断依頼を受け付けました'
    }));
    
  } catch (error) {
    // エラーレスポンス
    Logger.log('Error: ' + error.toString());
    return ContentService.createTextOutput(JSON.stringify({
      status: 'error',
      message: error.toString()
    })).setMimeType(ContentService.MimeType.JSON);
  }
}

/**
 * GETリクエスト（テスト用）
 */
function doGet() {
  return ContentService.createTextOutput('外壁塗装診断フォーム API is running');
}

// ========================================
// スプレッドシート保存
// ========================================

/**
 * スプレッドシートにデータ保存
 */
function saveToSpreadsheet(data) {
  const sheet = SpreadsheetApp.openById(SPREADSHEET_ID).getActiveSheet();
  
  // ヘッダー行がない場合は追加
  if (sheet.getLastRow() === 0) {
    sheet.appendRow(['受付日時', 'お名前', '地域', '築年数', '電話番号', 'メールアドレス', 'ステータス']);
  }
  
  // データ追加
  sheet.appendRow([
    new Date(),
    data.name,
    data.location,
    data.age,
    data.phone,
    data.email,
    '未対応'
  ]);
}

// ========================================
// メール送信
// ========================================

/**
 * お客様に御礼メール送信（ガイドブック添付）
 */
function sendThankYouEmail(data) {
  // PDFファイル取得
  const pdfFile = DriveApp.getFileById(PDF_FILE_ID);
  const pdfBlob = pdfFile.getBlob();
  
  // メール件名
  const subject = '【' + COMPANY_NAME + '】診断依頼ありがとうございます＋ガイドブックプレゼント🎁';
  
  // メール本文（HTML）
  const htmlBody = `
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <style>
    body { font-family: 'Hiragino Sans', 'Meiryo', sans-serif; line-height: 1.8; color: #333; }
    .container { max-width: 600px; margin: 0 auto; padding: 20px; }
    .header { background: linear-gradient(135deg, #ff0000 0%, #cc0000 100%); color: white; padding: 30px; text-align: center; border-radius: 10px 10px 0 0; }
    .content { background: #f9f9f9; padding: 30px; border-radius: 0 0 10px 10px; }
    .highlight { background: #fff3cd; padding: 15px; border-left: 4px solid #ffc107; margin: 20px 0; }
    .gift-box { background: linear-gradient(135deg, #ffd700 0%, #ffed4e 100%); padding: 20px; border-radius: 10px; text-align: center; margin: 20px 0; }
    .button { display: inline-block; background: #ff0000; color: white; padding: 15px 30px; text-decoration: none; border-radius: 50px; font-weight: bold; margin: 20px 0; }
    .footer { text-align: center; color: #666; font-size: 12px; margin-top: 30px; padding-top: 20px; border-top: 1px solid #ddd; }
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <h1 style="margin: 0; font-size: 24px;">診断依頼ありがとうございます！</h1>
    </div>
    
    <div class="content">
      <p><strong>${data.name}</strong> 様</p>
      
      <p>この度は「${COMPANY_NAME}」の無料診断をご依頼いただき、誠にありがとうございます。</p>
      
      <div class="gift-box">
        <h2 style="margin: 0 0 10px 0; font-size: 20px;">🎁 ガイドブックをプレゼント</h2>
        <p style="margin: 0; font-size: 16px; font-weight: bold;">
          「戸建の屋根・外壁塗装ガイドブック」<br>
          （2026年度・保存版）
        </p>
        <p style="margin: 10px 0 0 0; font-size: 14px;">
          ※添付ファイルをご確認ください
        </p>
      </div>
      
      <div class="highlight">
        <h3 style="margin-top: 0;">📖 ガイドブックの内容（全12ポイント）</h3>
        <ul style="margin: 10px 0;">
          <li>💰 外壁塗装の相場と見積書の読み方</li>
          <li>🏠 塗装時期の見極め方</li>
          <li>🎨 塗料の種類と特徴比較</li>
          <li>⚠️ 悪徳業者の見分け方</li>
          <li>📋 施工品質チェックポイント</li>
          <li>その他、助成金・保証・工事の流れなど</li>
        </ul>
      </div>
      
      <h3>⚡ 次のステップ</h3>
      <p>
        <strong>24時間以内に</strong>、プロの診断士から詳しい診断結果をお送りいたします。<br>
        以下の内容を含む診断レポートをご提供いたします：
      </p>
      <ul>
        <li>✅ お住まいの劣化状況の分析</li>
        <li>✅ 最適な塗装時期のご提案</li>
        <li>✅ おすすめの塗料と工事プラン</li>
        <li>✅ 概算費用の目安</li>
      </ul>
      
      <h3>📝 ご依頼内容の確認</h3>
      <table style="width: 100%; border-collapse: collapse; margin: 10px 0;">
        <tr style="background: #f0f0f0;">
          <td style="padding: 10px; border: 1px solid #ddd; width: 30%;">お名前</td>
          <td style="padding: 10px; border: 1px solid #ddd;">${data.name}</td>
        </tr>
        <tr>
          <td style="padding: 10px; border: 1px solid #ddd;">地域</td>
          <td style="padding: 10px; border: 1px solid #ddd;">${data.location}</td>
        </tr>
        <tr style="background: #f0f0f0;">
          <td style="padding: 10px; border: 1px solid #ddd;">築年数</td>
          <td style="padding: 10px; border: 1px solid #ddd;">${data.age}</td>
        </tr>
        <tr>
          <td style="padding: 10px; border: 1px solid #ddd;">電話番号</td>
          <td style="padding: 10px; border: 1px solid #ddd;">${data.phone}</td>
        </tr>
        <tr style="background: #f0f0f0;">
          <td style="padding: 10px; border: 1px solid #ddd;">メールアドレス</td>
          <td style="padding: 10px; border: 1px solid #ddd;">${data.email}</td>
        </tr>
      </table>
      
      <p style="margin-top: 30px; text-align: center;">
        <a href="${COMPANY_URL}" class="button">公式サイトはこちら</a>
      </p>
      
      <div style="background: #e3f2fd; padding: 15px; border-radius: 5px; margin-top: 20px;">
        <p style="margin: 0; font-size: 14px;">
          <strong>💡 安心ポイント</strong><br>
          ✅ しつこい営業は一切ありません<br>
          ✅ 正直な診断を心がけています<br>
          ✅ 毎日メールで施工報告<br>
          ✅ お客様のペースで進められます
        </p>
      </div>
    </div>
    
    <div class="footer">
      <p>
        <strong>${COMPANY_NAME}</strong><br>
        対応エリア: 東京都全域（町田・立川・調布・八王子・多摩）<br>
        Web: <a href="${COMPANY_URL}">${COMPANY_URL}</a>
      </p>
      <p style="font-size: 11px; color: #999; margin-top: 15px;">
        ※このメールは自動送信されています。<br>
        ご不明な点がございましたら、お気軽にお問い合わせください。
      </p>
    </div>
  </div>
</body>
</html>
  `;
  
  // テキスト版メール本文
  const textBody = `
${data.name} 様

この度は「${COMPANY_NAME}」の無料診断をご依頼いただき、誠にありがとうございます。

━━━━━━━━━━━━━━━━━━━━
🎁 ガイドブックをプレゼント
━━━━━━━━━━━━━━━━━━━━

「戸建の屋根・外壁塗装ガイドブック」（2026年度・保存版）
※添付ファイルをご確認ください

【ガイドブックの内容（全12ポイント）】
・外壁塗装の相場と見積書の読み方
・塗装時期の見極め方
・塗料の種類と特徴比較
・悪徳業者の見分け方
・施工品質チェックポイント
・その他、助成金・保証・工事の流れなど

━━━━━━━━━━━━━━━━━━━━
⚡ 次のステップ
━━━━━━━━━━━━━━━━━━━━

24時間以内に、プロの診断士から詳しい診断結果をお送りいたします。

【診断レポートの内容】
✅ お住まいの劣化状況の分析
✅ 最適な塗装時期のご提案
✅ おすすめの塗料と工事プラン
✅ 概算費用の目安

━━━━━━━━━━━━━━━━━━━━
📝 ご依頼内容の確認
━━━━━━━━━━━━━━━━━━━━

お名前: ${data.name}
地域: ${data.location}
築年数: ${data.age}
電話番号: ${data.phone}
メールアドレス: ${data.email}

━━━━━━━━━━━━━━━━━━━━
💡 安心ポイント
━━━━━━━━━━━━━━━━━━━━

✅ しつこい営業は一切ありません
✅ 正直な診断を心がけています
✅ 毎日メールで施工報告
✅ お客様のペースで進められます

━━━━━━━━━━━━━━━━━━━━

${COMPANY_NAME}
対応エリア: 東京都全域（町田・立川・調布・八王子・多摩）
Web: ${COMPANY_URL}

※このメールは自動送信されています。
ご不明な点がございましたら、お気軽にお問い合わせください。
  `;
  
  // メール送信
  GmailApp.sendEmail(
    data.email,
    subject,
    textBody,
    {
      htmlBody: htmlBody,
      attachments: [pdfBlob],
      name: COMPANY_NAME
    }
  );
  
  Logger.log('御礼メール送信完了: ' + data.email);
}

/**
 * 管理者に通知メール送信
 */
function sendNotificationToAdmin(data) {
  const subject = '【新規診断依頼】' + data.name + ' 様から診断依頼がありました';
  
  const body = `
新しい診断依頼が届きました。

━━━━━━━━━━━━━━━━━━━━
お客様情報
━━━━━━━━━━━━━━━━━━━━

お名前: ${data.name}
地域: ${data.location}
築年数: ${data.age}
電話番号: ${data.phone}
メールアドレス: ${data.email}

受付日時: ${new Date().toLocaleString('ja-JP')}

━━━━━━━━━━━━━━━━━━━━
対応事項
━━━━━━━━━━━━━━━━━━━━

✅ お客様に御礼メール＋ガイドブック送信済み
⏰ 24時間以内に診断結果を送信してください

スプレッドシートで詳細を確認:
https://docs.google.com/spreadsheets/d/${SPREADSHEET_ID}

━━━━━━━━━━━━━━━━━━━━

${COMPANY_NAME}
  `;
  
  GmailApp.sendEmail(ADMIN_EMAIL, subject, body);
  
  Logger.log('管理者通知メール送信完了: ' + ADMIN_EMAIL);
}
