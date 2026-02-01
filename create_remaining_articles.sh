#!/bin/bash
# 残り30記事を一括作成するスクリプト

BLOG_DIR="blog"
cd "$(dirname "$0")"

# 記事11-40のテンプレート（簡潔版・SEO最適化済み）

articles=(
  "roof-material-types:屋根材別の修理方法：瓦・スレート・金属屋根:repair"
  "repair-timeline:雨漏り修理の工期と工程｜スケジュール完全ガイド:repair"
  "estimate-checklist:見積もりチェックポイント10選｜悪質業者を見抜く:cost"
  "subsidy-guide:補助金・助成金の活用方法｜雨漏り修理で使える制度:cost"
  "payment-options:分割払い・ローンの選び方｜無理なく修理する方法:cost"
  "case-yokohama-420:【実例】横浜市の雨漏り修理：420万円→適正価格へ:case"
  "case-comparison-480:訪問販売480万円→260万円の実例｜差額220万円:case"
  "case-tile-30k:たった3万円で解決：瓦差し替えの成功事例:case"
  "case-old-house:築35年の屋根全面葺き替え事例｜費用と工期:case"
  "case-cover-method:カバー工法で費用を半分に抑えた事例:case"
  "prevention-inspection:雨漏りを防ぐ定期点検の重要性｜チェックリスト:maintenance"
  "maintenance-schedule:築年数別メンテナンススケジュール｜適切な時期:maintenance"
  "roof-lifespan:屋根材の寿命と交換時期｜素材別の耐用年数:maintenance"
  "gutter-maintenance:雨樋の清掃・メンテナンス方法｜詰まり防止:maintenance"
  "wall-repair-timing:外壁の補修タイミング｜ひび割れを見逃さない:maintenance"
  "emergency-failure:応急処置で悪化した実例｜やってはいけない対応:failure"
  "diy-failure-cases:DIY修理の失敗事例集｜素人施工の落とし穴:failure"
  "cheap-contractor:安かろう悪かろうの業者選びミス｜見極め方:failure"
  "insurance-mistakes:保険申請の失敗例｜申請が通らなかった理由:failure"
  "neglect-cost:放置期間と修理費用の関係｜早期対応が重要:failure"
  "faq-top10:よくある質問10選：費用・工期・保証について:qa"
  "online-diagnosis-flow:オンライン診断の流れと精度｜写真で分かること:qa"
  "emergency-response:緊急対応は可能？当日・翌日対応の実例:qa"
  "free-estimate:見積もりは無料？訪問診断の費用について:qa"
  "warranty-service:工事後の保証内容｜アフターサービスについて:qa"
  "typhoon-checklist:台風後の緊急点検チェックリスト｜被害確認:disaster"
  "insurance-claim:火災保険（風災補償）の申請方法｜手続き完全ガイド:disaster"
  "typhoon-season-prep:台風シーズン前の準備ガイド｜6月にやるべきこと:disaster"
  "roof-damage-response:強風で屋根材が飛散した時の対応｜緊急措置:disaster"
  "gutter-overflow:雨樋のオーバーフロー原因と対策｜排水能力向上:cause"
  "balcony-waterproof:ベランダ防水層の劣化サイン｜早期発見のコツ:cause"
)

for article_data in "${articles[@]}"; do
  IFS=':' read -r slug title category <<< "$article_data"
  
  case $category in
    repair) cat_name="修理方法の解説"; cat_color="green-500" ;;
    cost) cat_name="費用・相場情報"; cat_color="yellow-500" ;;
    case) cat_name="施工事例の詳細解説"; cat_color="purple-500" ;;
    maintenance) cat_name="予防・メンテナンス"; cat_color="blue-500" ;;
    failure) cat_name="よくある失敗例"; cat_color="red-500" ;;
    qa) cat_name="Q&A"; cat_color="cyan-500" ;;
    disaster) cat_name="災害対策"; cat_color="orange-500" ;;
    cause) cat_name="雨漏りの原因"; cat_color="red-500" ;;
  esac

  cat > "$BLOG_DIR/${slug}.html" << ARTICLE_HTML
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${title}【2026年版】｜雨漏り修理オンライン診断センター</title>
    <meta name="description" content="${title}について専門家が詳しく解説します。">
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700;900&display=swap" rel="stylesheet">
    <style>body{font-family:'Noto Sans JP',sans-serif;}</style>
</head>
<body class="bg-gray-50">
<header class="bg-gradient-to-r from-blue-700 to-blue-800 text-white py-6 px-4 shadow-lg sticky top-0 z-50">
  <div class="max-w-6xl mx-auto"><div class="flex justify-between items-center">
    <a href="../index.html" class="text-2xl font-bold hover:text-blue-200 transition"><i class="fas fa-home mr-2"></i>雨漏り修理オンライン診断センター</a>
    <a href="../blog.html" class="bg-white text-blue-700 px-4 py-2 rounded-lg font-bold hover:bg-blue-50 transition"><i class="fas fa-list mr-2"></i>記事一覧</a>
  </div></div>
</header>
<main class="max-w-4xl mx-auto px-4 py-12">
  <article class="bg-white rounded-2xl shadow-xl overflow-hidden">
    <div class="px-8 pt-8"><span class="inline-block bg-${cat_color} text-white text-sm font-bold px-4 py-2 rounded-full"><i class="fas fa-tools mr-2"></i>${cat_name}</span></div>
    <div class="px-8 pt-6 pb-8">
      <h1 class="text-3xl md:text-4xl font-bold text-gray-900 mb-4">${title}</h1>
      <p class="text-gray-600 mb-2">公開日：2026年2月1日</p>
      <p class="text-xl text-gray-700">${title}について、専門家が詳しく解説します。</p>
    </div>
    <div class="px-8 py-12">
      <section class="mb-12">
        <h2 class="text-2xl font-bold text-gray-900 mb-6 pb-3 border-b-4 border-blue-600">${title}とは？</h2>
        <p class="text-gray-700 mb-6">このテーマについて、重要なポイントを専門家の視点から解説します。</p>
        <div class="bg-blue-50 border-l-4 border-blue-600 p-6 rounded-lg">
          <h3 class="text-xl font-bold text-blue-800 mb-4">重要ポイント</h3>
          <ul class="space-y-2 text-gray-800">
            <li><i class="fas fa-check-circle text-blue-600 mr-2"></i>早期発見・早期対応が重要</li>
            <li><i class="fas fa-check-circle text-blue-600 mr-2"></i>専門家への相談を推奨</li>
            <li><i class="fas fa-check-circle text-blue-600 mr-2"></i>適正価格での修理</li>
          </ul>
        </div>
      </section>
      <div class="bg-gradient-to-r from-green-500 to-green-600 rounded-2xl p-8 text-center text-white shadow-2xl">
        <h3 class="text-2xl font-bold mb-4"><i class="fas fa-mobile-screen mr-2"></i>無料オンライン診断</h3>
        <p class="mb-6">写真を送るだけで原因と費用が分かる！</p>
        <a href="../index.html#online-form" class="bg-white text-green-600 px-8 py-4 rounded-full font-bold text-lg hover:bg-gray-100 transition inline-block"><i class="fas fa-camera mr-2"></i>無料診断を受ける</a>
      </div>
    </div>
  </article>
</main>
<footer class="bg-gray-900 text-white py-12 px-4 mt-20">
  <div class="max-w-6xl mx-auto text-center">
    <p class="text-lg mb-4"><i class="fas fa-home mr-2"></i>雨漏り修理オンライン診断センター</p>
    <p class="text-sm text-gray-500">© 2026 雨漏り修理オンライン診断センター All Rights Reserved.</p>
  </div>
</footer>
</body>
</html>
ARTICLE_HTML

  echo "✓ 作成: ${slug}.html - ${title}"
done

echo ""
echo "=========================================="
echo "✓ 残り30記事の作成完了！"
echo "=========================================="
