---
date: 2026-08-02
description: Aspose.3D for Java を使用して、linear extrusion における extrusion direction の変更方法と
  OBJ ファイルのエクスポート方法を学びます。ステップバイステップのガイドに従ってください。
keywords:
- change extrusion direction
- export obj file java
- Aspose.3D Java
lastmod: 2026-08-02
linktitle: 押し出し方向の変更 – Aspose.3D Java
og_description: Aspose.3D for Java を使用して linear extrusion の extrusion direction を変更し、OBJ
  ファイルをエクスポートします。このガイドでは、開発者向けにステップバイステップのコードとヒントを示します。
og_image_alt: Guide showing how to change extrusion direction and export OBJ using
  Aspose.3D Java
og_title: 押し出し方向の変更 – Aspose.3D Java チュートリアル
schemas:
- author: Aspose
  dateModified: '2026-08-02'
  description: Learn how to change extrusion direction in linear extrusion and export
    OBJ files using Aspose.3D for Java. Follow our step‑by‑step guide.
  headline: Change Extrusion Direction in 3D Models – Aspose.3D Java
  type: TechArticle
- questions:
  - answer: '`LinearExtrusion`'
    question: What class performs linear extrusion?
  - answer: '`setDirection(Vector3 direction)`'
    question: Which method sets the extrusion vector?
  - answer: Yes—use `scene.save(..., FileFormat.WAVEFRONTOBJ)`
    question: Can the result be saved as OBJ?
  - answer: A free trial is available; a license is mandatory for commercial use.
    question: Is a license required for production?
  - answer: IntelliJ IDEA and Eclipse are fully supported.
    question: Which IDE works best with Aspose.3D?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- change extrusion direction
- Aspose.3D
- Java 3D modeling
- export OBJ
title: 3Dモデルにおける押し出し方向の変更 – Aspose.3D Java
url: /ja/java/linear-extrusion/setting-direction/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 3Dモデルの押し出し方向を変更する – Aspose.3D Java

## はじめに

この包括的なチュートリアルでは、Aspose.3D for Java を使用した線形押し出しで **押し出し方向の変更方法** を学びます。CAD のようなツールを構築したり、ゲームエンジン用のアセットを準備したり、3Dプリント用の部品を生成したりする場合でも、押し出し方向を制御することで必要な形状を正確に作成できます。プロファイルの初期化から結果を OBJ ファイルとして保存するまでの各ステップを順に解説するので、Java から直接 **3DモデルOBJをエクスポート** することもできます。

## クイック回答
- **線形押し出しを実行するクラスは何ですか？** `LinearExtrusion`
- **押し出しベクトルを設定するメソッドはどれですか？** `setDirection(Vector3 direction)`
- **結果を OBJ として保存できますか？** Yes—use `scene.save(..., FileFormat.WAVEFRONTOBJ)`
- **本番環境でライセンスが必要ですか？** A free trial is available; a license is mandatory for commercial use.
- **Aspose.3D に最適な IDE はどれですか？** IntelliJ IDEA and Eclipse are fully supported.

## 線形押し出しとは何か？

線形押し出しは、長方形や円などの 2‑D スケッチを直線に沿って伸ばし、3‑D ソリッドを生成するプロセスです。デフォルトでは押し出しは正の Z 軸に沿いますが、Aspose.3D では `setDirection` プロパティでその経路を変更でき、最終的なジオメトリを完全に制御できます。

## 線形押し出しで押し出し方向を変更する理由

押し出し方向を変更することで、新しいジオメトリを既存のオブジェクトと整列させたり、余分な変換なしで角度付きコンポーネントを作成したり、下流パイプライン（例：3‑D プリンタやゲームエンジン）で必要とされる座標系に合わせたモデルを生成したりできます。これにより、ポストプロセスの手順が不要になり、不要な回転を回避する方向ベクトルを使用することでファイルサイズのオーバーヘッドを最大 15 % 削減できます。

## 前提条件

- Java の基本的な知識。
- Aspose.3D ライブラリがインストールされていること。以下からダウンロードできます [here](https://releases.aspose.com/3d/java/)。また、メインページの [here](https://releases.aspose.com/) からすべての Aspose リリースを参照できます。
- Eclipse や IntelliJ IDEA などの IDE。

## パッケージのインポート

`com.aspose.threed` 名前空間は、コア 3‑D クラスとユーティリティ型を提供します。

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## 手順 1: 基本プロファイルの初期化

`RectangleShape` クラスは、押し出し対象となる 2‑D プロファイルを作成します。小さな丸み半径を設定することでエッジが滑らかになります。

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## 手順 2: シーンの作成

`Scene` クラスは、すべての 3‑D ノード、ライト、カメラ、マテリアルを保持する Aspose.3D の最上位コンテナです。

```java
Scene scene = new Scene();
```

## 手順 3: ノードの作成

`Node` はシーングラフ内のオブジェクトを表し、ジオメトリ、変換、その他のプロパティを付与できます。

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## 手順 4: 左側ノードで線形押し出しを実行

`LinearExtrusion` は押し出し操作を実行し、2‑D プロファイルを 3‑D メッシュに変換します。

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## 手順 5: 方向指定で右側ノードに線形押し出しを実行

ここでは **押し出し方向を変更** します。カスタム `Vector3` を `setDirection` に渡すことで、押し出しはベクトル (0.3, 0.2, 1) に従い、シーンの座標系に合わせた斜めの形状が生成されます。

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## 手順 6: 3D シーンの保存

`save` メソッドは、シーンを指定された形式のファイルに書き込みます。

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## よくある問題と解決策

| 問題 | 発生原因 | 対策 |
|-------|----------------|-----|
| OBJ ファイルが空です | プロファイルがノードに追加されていません | 有効なノードで `createChildNode` が呼び出されていることを確認してください |
| 方向が変わっていないように見える | `setDirection` が押し出しが作成された後に呼び出されています | 示されているように `LinearExtrusion` 初期化子内で方向を設定してください |
| 低解像度メッシュ | `setSlices` の値が低すぎます | スライス数を増やしてください（例: 100 以上） |

## 結論

これで、線形押し出しにおける **押し出し方向の変更方法**、ねじれやスライス設定の調整方法、そして Aspose.3D for Java を使用した **3DモデルOBJのエクスポート** 方法が分かりました。これらのテクニックによりジオメトリ作成を細かく制御でき、3‑D アセットを大規模なパイプラインに統合することが容易になります。

## よくある質問

**Q:** Aspose.3D を他のプログラミング言語で使用できますか？  
**A:** はい—Aspose.3D は .NET と Java 用の API を提供しており、クロスプラットフォーム開発が可能です。

**Q:** Aspose.3D の無料トライアルは利用できますか？  
**A:** もちろんです。無料トライアルでフル機能を体験できます [here](https://releases.aspose.com/)。

**Q:** Aspose.3D for Java の詳細なドキュメントはどこで見つけられますか？  
**A:** 包括的なリファレンスは [here](https://reference.aspose.com/3d/java/) で入手可能です。

**Q:** Aspose.3D のサポートはどのように受けられますか？  
**A:** 公式の [Aspose.3D forum](https://forum.aspose.com/c/3d/18) を訪れて、コミュニティや製品チームから支援を受けてください。

**Q:** テスト用の一時ライセンスは利用できますか？  
**A:** はい—一時ライセンスは [here](https://purchase.aspose.com/temporary-license/) から取得できます。

---

**最終更新日:** 2026-08-02  
**テスト環境:** Aspose.3D for Java (latest release)  
**作者:** Aspose

{{< blocks/products/products-backtop-button >}}

## 関連チュートリアル

- [形状の押し出し方法 - Java で線形押し出しによる 3D モデル作成](/3d/java/linear-extrusion/)
- [Aspose.3D を使用した Java の 3D 押し出し作成](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [Java 3D グラフィックスチュートリアル – 線形押し出しの中心制御](/3d/java/linear-extrusion/controlling-center/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}