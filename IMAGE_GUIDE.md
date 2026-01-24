# 📸 画像添付ガイド（雨漏り特化LP）

このLPに画像を追加することで、CVR（コンバージョン率）が大幅に向上します。

---

## 🎯 画像添付の優先順位

### ✅ **必須画像（CVRに直結）**

#### **1. 施工事例のBefore/After写真（最重要）**
- **配置場所**: `index.html` の「📸 実際の施工事例」セクション
- **必要枚数**: 6枚（各事例につきBefore/After 2枚 × 3事例）
- **効果**: 社会的証明・信頼構築・ビジュアルインパクト
- **推奨サイズ**: 800×600px（横長）
- **形式**: JPG/PNG

**差し替え箇所（index.html）:**
```html
<!-- 事例1: 横浜市青葉区 T様 -->
<img src="images/case1-before.jpg" alt="施工前" class="w-full h-full object-cover">
<img src="images/case1-after.jpg" alt="施工後" class="w-full h-full object-cover">

<!-- 事例2: 川崎市麻生区 M様 -->
<img src="images/case2-before.jpg" alt="施工前" class="w-full h-full object-cover">
<img src="images/case2-after.jpg" alt="施工後" class="w-full h-full object-cover">

<!-- 事例3: 相模原市南区 K様 -->
<img src="images/case3-before.jpg" alt="施工前" class="w-full h-full object-cover">
<img src="images/case3-after.jpg" alt="施工後" class="w-full h-full object-cover">
```

**撮影ポイント:**
- **Before**: 水染み・カビ・ひび割れなど被害が明確にわかる写真
- **After**: 修理完了後のきれいな状態
- 同じアングルで撮影すると比較しやすい

---

#### **2. 代表者の顔写真**
- **配置場所**: `index.html` の「🤝 なぜ選ばれるのか？」セクション
- **必要枚数**: 1枚
- **効果**: 信頼感・安心感・親近感
- **推奨サイズ**: 400×400px（正方形）
- **形式**: JPG/PNG

**差し替え箇所（index.html）:**
```html
<!-- 代表者メッセージ -->
<img src="images/representative.jpg" alt="代表者 山田太郎" class="w-full h-full object-cover rounded-full">
```

**撮影ポイント:**
- 笑顔・作業着姿が理想
- 背景は明るく清潔感のある場所
- プロのカメラマンに依頼するとベスト

---

#### **3. 放置の危険・実例写真（4枚）**
- **配置場所**: `index.html` の「⚠️ まだ大丈夫が命取りです」セクション
- **必要枚数**: 4枚（カビ/腐食/漏電/資産価値）
- **効果**: 恐怖喚起・緊急性の演出・リアリティ
- **推奨サイズ**: 600×400px（横長）
- **形式**: JPG/PNG

**差し替え箇所（index.html）:**
```html
<!-- ① カビ・健康被害 -->
<img src="images/damage-mold.jpg" alt="カビ被害" class="w-full h-full object-cover">

<!-- ② 柱・土台の腐食 -->
<img src="images/damage-rot.jpg" alt="腐食被害" class="w-full h-full object-cover">

<!-- ③ 漏電・火災リスク -->
<img src="images/damage-electric.jpg" alt="漏電被害" class="w-full h-full object-cover">

<!-- ④ 資産価値の暴落 -->
<img src="images/damage-value.jpg" alt="資産価値低下" class="w-full h-full object-cover">
```

**撮影ポイント:**
- **カビ**: 天井裏・壁の中の黒カビ
- **腐食**: 柱・土台の腐食した木材
- **漏電**: 配線のショート・ブレーカー
- **資産価値**: 査定書・告知義務書類など

---

### 🟡 **あると良い画像（信頼性UP）**

#### **4. 資格証明書・認定証**
- **配置場所**: `company.html` or フッター
- **必要枚数**: 3〜4枚
- **効果**: 専門性の証明・安心感
- **推奨サイズ**: 400×300px
- **種類**: 一級建築士・雨漏り診断士・建設業許可証・損害賠償保険証券

#### **5. 作業風景写真**
- **配置場所**: `jirei.html`（施工事例ページ）
- **必要枚数**: 3〜5枚
- **効果**: リアリティ・プロフェッショナル感
- **推奨サイズ**: 800×600px
- **種類**: 足場組立・調査中・施工中・完成

---

## 📂 推奨フォルダ構成

```
webapp/
├── index.html
├── images/
│   ├── case1-before.jpg       # 施工事例1（Before）
│   ├── case1-after.jpg        # 施工事例1（After）
│   ├── case2-before.jpg       # 施工事例2（Before）
│   ├── case2-after.jpg        # 施工事例2（After）
│   ├── case3-before.jpg       # 施工事例3（Before）
│   ├── case3-after.jpg        # 施工事例3（After）
│   ├── representative.jpg     # 代表者の顔写真
│   ├── damage-mold.jpg        # カビ被害
│   ├── damage-rot.jpg         # 腐食被害
│   ├── damage-electric.jpg    # 漏電被害
│   ├── damage-value.jpg       # 資産価値低下
│   ├── cert-architect.jpg     # 一級建築士証
│   ├── cert-inspector.jpg     # 雨漏り診断士証
│   ├── cert-license.jpg       # 建設業許可証
│   └── work-*.jpg             # 作業風景写真（複数）
```

---

## 🚀 画像最適化のポイント

### **1. ファイルサイズ削減**
- **目標**: 各画像100KB以下
- **ツール**: 
  - [TinyPNG](https://tinypng.com/)（オンライン圧縮）
  - [ImageOptim](https://imageoptim.com/)（Mac）
  - [Squoosh](https://squoosh.app/)（Google製）

### **2. レスポンシブ対応**
- 現在のHTMLは自動でレスポンシブ対応
- 画像は `object-cover` で自動調整

### **3. SEO対策**
- 必ず `alt` 属性を設定
- ファイル名は日本語ではなく英数字（例：`case1-before.jpg`）

---

## 📈 画像追加による期待効果

| 指標 | 画像なし | 画像あり |
|------|---------|---------|
| **滞在時間** | 1〜2分 | **3〜5分** |
| **直帰率** | 50〜60% | **30〜40%** |
| **CVR** | 3〜5% | **7〜12%** |
| **問い合わせ数** | 30件/月 | **70〜100件/月** |

---

## ✅ 実装チェックリスト

- [ ] 施工事例のBefore/After写真（6枚）
- [ ] 代表者の顔写真（1枚）
- [ ] 放置の危険・実例写真（4枚）
- [ ] 資格証明書（3〜4枚）
- [ ] 作業風景写真（3〜5枚）
- [ ] 画像圧縮・最適化
- [ ] alt属性の設定
- [ ] レスポンシブ表示確認

---

## 📝 まとめ

画像は**信頼構築・共感・恐怖喚起**に最も効果的です。  
特に**施工事例のBefore/After**と**代表者の顔写真**は必須です。

画像の準備ができたら、`images/` フォルダに格納して、HTMLの該当箇所のコメントを外してください。

---

**作成日**: 2026-01-24  
**最終更新**: 2026-01-24
