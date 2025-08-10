# でっかい回覧板

本作品は、地域コミュニケーションの活性化を目的とした回覧板システムです。  
都道府県ごとのユーザーがAI生成のお題に答え、月ごとにAIが内容を集計し、1枚の「まとめ回覧板」として可視化されます。

---

## 🔧 技術構成

- フロントエンド：HTML / CSS / JavaScript
- バックエンド：Python (Flask)
- データベース：MySQL
- 使用ライブラリ・ツール：
  - Geolonia 日本地図 SVG（ライセンス：GFDL）

---

## 🗺 日本地図データの使用について

本アプリケーションでは、日本地図のSVGデータとして以下を使用しています：

- 出典：[Geolonia - japanese-prefectures](https://github.com/geolonia/japanese-prefectures)
- 元データ：Wikipediaの「日本地図.svg」
- ライセンス：GNU Free Documentation License（GFDL）

このSVGデータはGFDLライセンスのもとで提供されており、本作品でも同ライセンスに従って利用・再配布しております。

### 🔄 加えた変更点：
- 地図のスタイル調整（カラー、ホバー演出など）
- 都道府県クリックによるデータ閲覧処理の追加

---

## 📝 ライセンスに関する記述（GFDL）

このプロジェクトに含まれる一部のファイル（日本地図SVG）は、GFDL（GNU Free Documentation License）のもとに提供されています。

- GFDL原文：[https://www.gnu.org/licenses/fdl.html](https://www.gnu.org/licenses/fdl.html)

再配布・改変にあたっては、このライセンスに従ってください。

---

