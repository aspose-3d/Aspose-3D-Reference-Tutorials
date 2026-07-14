---
date: 2026-05-24
description: Aspose.3D for Java を使用して形状を押し出す方法を学びます。この Java 3D モデリングチュートリアルでは、linear
  extrusion、center control、direction、slices、twist などをカバーしています！
keywords:
- how to extrude shape
- java 3d geometry
- create 3d model java
- create solid from 2d
linktitle: JavaでLinear Extrusionを使用した3Dモデル作成
schemas:
- author: Aspose
  dateModified: '2026-05-24'
  description: Learn how to extrude shape using Aspose.3D for Java. This java 3d modeling
    tutorial covers linear extrusion, center control, direction, slices, twist and
    more!
  headline: How to Extrude Shape - Creating 3D Models with Linear Extrusion in Java
  type: TechArticle
- description: Learn how to extrude shape using Aspose.3D for Java. This java 3d modeling
    tutorial covers linear extrusion, center control, direction, slices, twist and
    more!
  name: How to Extrude Shape - Creating 3D Models with Linear Extrusion in Java
  steps:
  - name: Define the 2‑D profile
    text: Create a `Polygon` or `Polyline` that represents the shape you want to extrude.
      *A `Polygon` represents a closed shape defined by vertices, while a `Polyline`
      is an open series of line segments.* Ready to get started? [Perform Linear Extrusion
      Now](./performing-linear-extrusion/) For a detailed tuto
  - name: Configure extrusion options
    text: 'Set the center, direction, slices, twist, and twist offset on an `Extrusion`
      object. *The `Extrusion` class encapsulates all parameters needed to generate
      a 3‑D mesh from a 2‑D profile.* Get hands‑on with center control: [Control Center
      in Linear Extrusion](./controlling-center/) Read more about cen'
  - name: Add the extrusion to the scene
    text: 'Instantiate a `Scene`, attach the extrusion mesh, and export to your desired
      format. *`Scene` is the container that holds all 3‑D objects and handles exporting
      to various file formats.* Ready to set the direction? [Explore Now](./setting-direction/)
      Learn more about direction: [Setting Direction in '
  - name: Export or render
    text: 'Use `Scene.save()` to write the model to OBJ, STL, or any supported format.
      *`Scene.save()` writes the entire scene to the specified file format, applying
      any necessary post‑processing.* Start specifying slices: [Learn More](./specifying-slices/)
      Detailed guide: [Specifying Slices in Linear Extrusio'
  type: HowTo
- questions:
  - answer: Yes, a valid Aspose license is required for production use, but a free
      trial is available for evaluation.
    question: Can I use Aspose.3D for Java in a commercial project?
  - answer: The library works with Java 8 and newer runtimes, including Java 11, 17,
      and 21.
    question: Which Java versions are supported?
  - answer: Aspose.3D handles mesh generation efficiently, but you can call `scene.dispose()`
      when you’re done with large scenes to free native resources.
    question: Do I need to manage memory for large extrusions?
  - answer: Absolutely – you can create several extrusion objects, position them independently,
      and add them to the same scene.
    question: Can I combine multiple extrusion operations in one model?
  - answer: Yes, the “Applying Twist” and “Using Twist Offset” tutorials demonstrate
      how to set both properties on the same extrusion object.
    question: Is there sample code for applying twist and twist offset together?
  type: FAQPage
second_title: Aspose.3D Java API
title: 形状の押し出し方法 - JavaでLinear Extrusionを使用した3Dモデル作成
url: /ja/java/linear-extrusion/
weight: 23
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 形状を押し出す方法 – Javaで線形押し出しによる3Dモデルの作成

Java アプリケーションで **形状を押し出す方法** に興味があるなら、ここが適切な場所です。このチュートリアルでは Aspose.3D for Java の線形押し出し機能を順に解説し、シンプルな 2‑D プロファイルを完全な 3‑D モデルに変換する方法を示します。CAD スタイルのビューアやゲームアセットパイプラインの構築、あるいはジオメトリの実験であれ、線形押し出しをマスターすれば、数行のコードで複雑な形状を作成する自信が得られます。

## クイック回答
- **線形押し出しとは何ですか？** 方向に沿って 2‑D スケッチを伸ばし、3‑D ソリッドに変換することです。  
- **どのライブラリが役立ちますか？** Aspose.3D for Java は押し出しタスク用のフルエント API を提供します。  
- **ライセンスは必要ですか？** 学習には無料トライアルで十分です。商用利用には商用ライセンスが必要です。  
- **必要な Java バージョンは？** Java 8 以上です。  
- **ねじれやオフセットを適用できますか？** はい、API はツイスト角度とツイストオフセットを標準でサポートしています。  

## Java における「形状を押し出す方法」とは？
`Extrusion` 操作は、Aspose.3D のコア機能で、平坦な輪郭を体積メッシュに変換します。簡単に言えば、2‑D プロファイル（例: 長方形やカスタムポリゴン）を提供し、どれだけ引き伸ばすかをエンジンに指示すると、ライブラリが 3‑D ジオメトリを構築してくれます。

## なぜ Aspose.3D for Java を使用するのか？
Aspose.3D は **50 以上の入出力フォーマット**（OBJ、STL、FBX、GLTF など）をサポートし、シーン全体をメモリにロードせずに **1 回の押し出しで最大 10 000 頂点** のメッシュを生成できます。そのクロスプラットフォームエンジンは Windows、Linux、macOS 上で動作し、デスクトップワークステーションでもヘッドレス CI サーバでも一貫した結果を提供します。

## 前提条件
- 開発マシンに Java 8 以上がインストールされていること。  
- 依存関係管理に Maven または Gradle を使用すること。  
- Aspose.3D for Java のライセンスファイル（トライアルの場合は任意）。  

## 線形押し出しはどのように機能しますか？
線形押し出しは、2‑D プロファイルを直線に沿って掃引することで 3‑D ソリッドを作成します。エンジンはまずプロファイルを三角形化し、押し出し軸に沿った各スライスでそれを複製し、最後にスライスをつなぎ合わせて watertight なメッシュを形成します。このプロセスは法線と UV 座標を自動的に計算するため、追加のジオメトリ処理なしで結果をレンダリングできます。

## 線形押し出しの主要パラメータは何ですか？
線形押し出しは複数のパラメータでカスタマイズできます。**center** は押し出し前のプロファイルのピボット点を定義します。**direction** ベクトルは押し出し軸を設定し、デフォルトは正の Z 軸です。**slices** は生成される中間断面の数を制御し、ねじれやテーパー形状の滑らかさに影響します。**twist angle** は開始から終了までプロファイルを段階的に回転させ、**twist offset** は軸に沿った直線的な変位を加えて螺旋形状を実現します。

- **Center** – 押し出し前にプロファイルが配置されるピボット点。  
- **Direction** – 押し出し軸を定義するベクトル。デフォルトは正の Z 軸。  
- **Slices** – 中間断面の数。スライス数が多いほど、ねじれやテーパー押し出しの遷移が滑らかになります。  
- **Twist Angle** – プロファイルに開始から終了まで適用される総回転角度（度単位）。  
- **Twist Offset** – ねじれながら押し出し軸に沿ってプロファイルを直線的に移動させるオフセットで、螺旋形状を可能にします。

## Aspose.3D for Java での線形押し出しの実行

プロファイルを読み込み、パラメータを設定し、API にメッシュ生成を任せます。以下の手順で一般的なワークフローを示します。

### Step 1: Define the 2‑D profile
押し出したい形状を表す `Polygon` または `Polyline` を作成します。  
*`Polygon` は頂点で定義された閉じた形状を表し、`Polyline` は開いた線分の系列です。*  
開始する準備はできましたか？ [今すぐ線形押し出しを実行](./performing-linear-extrusion/)  
詳細なチュートリアルは [Aspose.3D for Java での線形押し出しの実行](./performing-linear-extrusion/) を参照してください。

### Step 2: Configure extrusion options
`Extrusion` オブジェクトに center、direction、slices、twist、twist offset を設定します。  
*`Extrusion` クラスは 2‑D プロファイルから 3‑D メッシュを生成するために必要なすべてのパラメータをカプセル化します。*  
center 制御を体験する: [線形押し出しでのセンター制御](./controlling-center/)  
center 制御の詳細: [Aspose.3D for Java での線形押し出しにおけるセンター制御](./controlling-center/)

### Step 3: Add the extrusion to the scene
`Scene` をインスタンス化し、押し出しメッシュを添付して、希望のフォーマットにエクスポートします。  
*`Scene` はすべての 3‑D オブジェクトを保持し、さまざまなファイル形式へのエクスポートを処理するコンテナです。*  
方向を設定する準備はできましたか？ [今すぐ確認](./setting-direction/)  
方向設定の詳細: [Aspose.3D for Java での線形押し出しにおける方向設定](./setting-direction/)

### Step 4: Export or render
`Scene.save()` を使用してモデルを OBJ、STL、またはサポートされている任意のフォーマットに書き出します。  
*`Scene.save()` はシーン全体を指定されたファイル形式に書き込み、必要な後処理を適用します。*  
スライス指定を開始: [詳細を見る](./specifying-slices/)  
詳細ガイド: [Aspose.3D for Java での線形押し出しにおけるスライス指定](./specifying-slices/)

## 押し出しにねじれを適用する方法は？
`twistAngle` プロパティを押し出しオプションに設定してねじれを適用します。エンジンは各スライスを比例的に回転させ、螺旋効果を作り出します。角度を調整することで、微細なねじれから 360° の完全なスパイラルまで、装飾要素や機能的なスプリングに役立つ形状を作成できます。  
ねじれを加える準備はできましたか？ [ねじれを適用する](./applying-twist/)  
完全な例: [Aspose.3D for Java での線形押し出しにおけるねじれの適用](./applying-twist/)

## 螺旋形状にツイストオフセットを使用する方法は？
ツイストオフセットは、回転しながら各スライスを押し出し軸に沿って移動させ、螺旋階段やコルクねじの形状を形成します。ツイスト角度に正のオフセットを組み合わせると滑らかな螺旋ランプになり、負のオフセットは下降スパイラルを作ります。この手法はねじ山、スプリング、アーティスティックなリボンのモデリングに最適です。  
スキルを向上させる: [ツイストオフセットを学ぶ](./using-twist-offset/)  
包括的ガイド: [Aspose.3D for Java での線形押し出しにおけるツイストオフセットの使用](./using-twist-offset/)

## 線形押し出しの一般的な使用例
- **機械部品** – シンプルなスケッチからボルト、シャフト、ブラケットを迅速に生成。  
- **建築要素** – 平面図を壁や柱に押し出し、BIM プロトタイプを作成。  
- **ゲームアセット** – フェンス、パイプ、装飾レールなどのローポリプロップを 2‑D アートから直接作成。  
- **教育ツール** – パラメトリック曲線を押し出して数学的曲面を可視化。  

## 一般的な問題のトラブルシューティング
- **面が欠落** – プロファイルが閉じたループであることを確認してください。開いた輪郭は隙間を生じます。  
- **メモリ使用量が過剰** – `slices` の数を減らすか、`scene.setMemoryOptimization(true)` を有効にしてください。  
- **ねじれ方向が間違っている** – 正の角度は押し出し方向に沿って見ると時計回りに回転します。逆にしたい場合は負の値を使用してください。  

## よくある質問

**Q: Aspose.3D for Java を商用プロジェクトで使用できますか？**  
A: はい、製品版の使用には有効な Aspose ライセンスが必要ですが、評価用に無料トライアルが利用可能です。

**Q: 対応している Java バージョンは？**  
A: ライブラリは Java 8 以上のランタイムで動作し、Java 11、17、21 もサポートしています。

**Q: 大規模な押し出しでメモリ管理が必要ですか？**  
A: Aspose.3D はメッシュ生成を効率的に処理しますが、大規模シーンの使用後に `scene.dispose()` を呼び出してネイティブリソースを解放できます。

**Q: 1 つのモデルに複数の押し出し操作を組み合わせられますか？**  
A: もちろんです。複数の Extrusion オブジェクトを作成し、個別に配置して同じシーンに追加できます。

**Q: ねじれとねじれオフセットを同時に適用するサンプルコードはありますか？**  
A: はい、「ねじれの適用」と「ツイストオフセットの使用」チュートリアルで、同一の Extrusion オブジェクトに両方のプロパティを設定する方法を示しています。

**最終更新日:** 2026-05-24  
**テスト環境:** Aspose.3D for Java 24.11  
**作者:** Aspose  

{{< blocks/products/products-backtop-button >}}

## 関連チュートリアル

- [Java 3D グラフィックチュートリアル – 線形押し出しのセンター](/3d/java/linear-extrusion/controlling-center/)
- [Aspose.3D for Java での線形押し出しにおける方向設定方法](/3d/java/linear-extrusion/setting-direction/)
- [スライスで 3D 押し出しを作成 – Aspose.3D for Java](/3d/java/linear-extrusion/specifying-slices/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}