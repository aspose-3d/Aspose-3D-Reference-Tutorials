---
date: 2026-05-24
description: Aspose.3D for Java を使用してスライスで 3D Extrusion を作成する方法を学びます。このステップバイステップ
  ガイドでは、linear extrusion、rounding radius の設定、OBJ のエクスポートについて説明します。
keywords:
- create 3d extrusion java
- Aspose 3D slices
- linear extrusion Java
linktitle: スライスを使用した3D Extrusionの作成 – Aspose.3D for Java
schemas:
- author: Aspose
  dateModified: '2026-05-24'
  description: Learn how to create 3d extrusion with slices using Aspose.3D for Java.
    This step‑by‑step guide covers linear extrusion, set rounding radius, and exporting
    OBJ.
  headline: Create 3D Extrusion with Slices – Aspose.3D for Java
  type: TechArticle
- description: Learn how to create 3d extrusion with slices using Aspose.3D for Java.
    This step‑by‑step guide covers linear extrusion, set rounding radius, and exporting
    OBJ.
  name: Create 3D Extrusion with Slices – Aspose.3D for Java
  steps:
  - name: Set up the scene and define the profile
    text: '`RectangleShape` is a class that defines a 2‑D rectangle profile. First
      we create a `RectangleShape` and give it a **rounding radius** so the corners
      are smooth. `Scene` is the root container for all nodes and geometry. Then we
      initialise a new `Scene` that will hold all geometry.'
  - name: Create child node objects for each extrusion
    text: '`Node` represents an element in the scene graph that can hold geometry
      and transformations. Every piece of geometry lives under a `Node`. Here we generate
      two sibling nodes – one for a low‑slice extrusion and another for a high‑slice
      extrusion – and move the left node a little to the side so the res'
  - name: Perform linear extrusion and set slices
    text: '`LinearExtrusion` is the class that creates a solid by sweeping a profile
      linearly. `LinearExtrusion` is Aspose.3D''s class that generates a solid by
      extruding a 2‑D profile along a straight line. Using an **anonymous inner class**
      we call `setSlices` to control the smoothness. The left node gets onl'
  - name: Export OBJ – save the scene
    text: Finally we write the scene to a Wavefront OBJ file, a format widely supported
      by 3‑D editors and game engines. This demonstrates the **export OBJ Java** capability
      of Aspose.3D.
  type: HowTo
- questions:
  - answer: You can download the library [here](https://releases.aspose.com/3d/java/).
    question: How can I download Aspose.3D for Java?
  - answer: Refer to the documentation [here](https://reference.aspose.com/3d/java/).
    question: Where can I find the documentation for Aspose.3D?
  - answer: Yes, you can explore a free trial [here](https://releases.aspose.com/).
    question: Is there a free trial available?
  - answer: Visit the support forum [here](https://forum.aspose.com/c/3d/18).
    question: How can I get support for Aspose.3D?
  - answer: Yes, a temporary license can be obtained [here](https://purchase.aspose.com/temporary-license/).
    question: Can I purchase a temporary license?
  type: FAQPage
second_title: Aspose.3D Java API
title: スライスを使用した3D Extrusionの作成 – Aspose.3D for Java
url: /ja/java/linear-extrusion/specifying-slices/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# スライス付き 3D 押し出しの作成 – Aspose.3D for Java

## はじめに

滑らかで精密に見える **3D 押し出し** オブジェクトを作成する必要がある場合、スライス数の制御が重要です。このチュートリアルでは、Aspose.3D for Java を使用した線形押し出しでスライスを指定する方法を解説します。スライス数がなぜ重要か、丸め半径の設定方法、そして結果を任意の 3‑D パイプラインで使用できる OBJ ファイルとしてエクスポートする方法が分かります。

## クイック回答
- **「スライス」は何を制御しますか？** 押し出し表面を近似するために使用される中間断面の数です。  
- **どのメソッドがスライス数を設定しますか？** `LinearExtrusion.setSlices(int)`  
- **プロファイルの丸め半径を変更できますか？** はい、`RectangleShape.setRoundingRadius(double)` を使用します。  
- **この例で使用されているファイル形式は何ですか？** Wavefront OBJ (`FileFormat.WAVEFRONTOBJ`)  
- **コードを実行するのにライセンスが必要ですか？** 評価には無料トライアルで動作しますが、本番環境では商用ライセンスが必要です。

`LinearExtrusion.setSlices(int)` は、押し出しが生成する中間スライスの数を設定します。  
`RectangleShape.setRoundingRadius(double)` は、矩形プロファイルの角の半径を定義します。

## スライス付き 3D 押し出し（Java）の作成方法

2‑D プロファイルを読み込み、スライス数を選択し、丸め半径を設定して `save` を呼び出すだけで、ワークフローは数行で完結します。Aspose.3D for Java はジオメトリの作成、スライスの補間、OBJ エクスポートを自動的に処理するため、低レベルのメッシュ計算に煩わされることなく、ビジュアル品質に集中できます。

## スライス付き線形押し出しとは？

スライス付き線形押し出しは、平面の 2‑D 形状を直線に沿って掃引し、設定可能な数の中間断面を生成することで 3‑D ソリッドに変換します。スライス数は、丸め角などの曲線エッジがどれだけ滑らかに描画されるかに直接影響します。

## なぜ Aspose.3D for Java を使って 3D 押し出しを作成するのか？

Aspose.3D は、すべての押し出しパラメータに対して **完全なプログラム制御** を提供し、**50 以上の入出力フォーマット**（OBJ、FBX、STL、GLTF など）をサポートし、ファイル全体をメモリに読み込むことなく **数百ページ規模のモデル** を処理できます。Java が動作する任意のプラットフォームで実行でき、ネイティブ DLL は不要で、Windows、Linux、macOS 間で決定的な結果を保証します。

## 前提条件

1. **Java Development Kit** – JDK 8 以上がインストールされていること。  
2. **Aspose.3D for Java** – 公式サイトからライブラリをダウンロードしてください [here](https://releases.aspose.com/3d/java/)。  
3. お好みの IDE またはテキストエディタ。

## パッケージのインポート

プロジェクトに Aspose.3D 名前空間を追加し、3‑D モデリングクラスにアクセスできるようにします。

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## ステップバイステップ ガイド

### ステップ 1: シーンの設定とプロファイルの定義

`RectangleShape` は 2‑D 四角形プロファイルを定義するクラスです。  
まず `RectangleShape` を作成し、角を滑らかにするために **丸め半径** を設定します。  
`Scene` はすべてのノードとジオメトリのルートコンテナです。  
次に、すべてのジオメトリを保持する新しい `Scene` を初期化します。

```java
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
Scene scene = new Scene();
```

### ステップ 2: 各押し出しの子ノードオブジェクトを作成

`Node` はジオメトリと変換を保持できるシーングラフの要素を表します。  
すべてのジオメトリは `Node` の下に配置されます。ここでは、低スライス押し出し用と高スライス押し出し用の 2 つの兄弟ノードを生成し、左側のノードを少し横に移動させて結果を比較しやすくします。

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### ステップ 3: 線形押し出しを実行しスライスを設定

`LinearExtrusion` はプロファイルを直線的に掃引してソリッドを作成するクラスです。  
`LinearExtrusion` は Aspose.3D のクラスで、2‑D プロファイルを直線に沿って押し出しソリッドを生成します。**匿名内部クラス** を使用して `setSlices` を呼び出し、滑らかさを制御します。左側のノードは 2 スライス（粗い）だけ、右側のノードは 10 スライス（滑らか）を使用します。

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(2);}});
right.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(10);}});
```

### ステップ 4: OBJ をエクスポート – シーンを保存

最後に、シーンを Wavefront OBJ ファイルに書き出します。このフォーマットは 3‑D エディタやゲームエンジンで広くサポートされています。これは Aspose.3D の **OBJ エクスポート（Java）** 機能を示す例です。

```java
scene.save(MyDir + "SlicesInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## 一般的な問題と解決策

| 問題 | 発生理由 | 対処法 |
|------|----------|--------|
| **押し出しが平坦に見える** | スライス数が 1 または 0 に設定されている | `setSlices` を 2 以上の値で呼び出すことを確認してください。 |
| **丸め角がギザギザになる** | スライス数に対して丸め半径が小さすぎる | 半径またはスライス数のいずれかを増やして曲線を滑らかにしてください。 |
| **保存時にファイルが見つからない** | `MyDir` が存在しないフォルダーを指している | 事前にディレクトリを作成するか、絶対パスを使用してください。 |

## よくある質問

**Q: Aspose.3D for Java はどこからダウンロードできますか？**  
A: ライブラリは [here](https://releases.aspose.com/3d/java/) からダウンロードできます。

**Q: Aspose.3D のドキュメントはどこで確認できますか？**  
A: ドキュメントは [here](https://reference.aspose.com/3d/java/) を参照してください。

**Q: 無料トライアルは利用可能ですか？**  
A: はい、無料トライアルは [here](https://releases.aspose.com/) でお試しできます。

**Q: Aspose.3D のサポートはどこで受けられますか？**  
A: サポートフォーラムは [here](https://forum.aspose.com/c/3d/18) です。

**Q: 一時ライセンスを購入できますか？**  
A: はい、一時ライセンスは [here](https://purchase.aspose.com/temporary-license/) で取得できます。

**最終更新日:** 2026-05-24  
**テスト環境:** Aspose.3D for Java 24.11 (latest at time of writing)  
**作者:** Aspose

## 関連チュートリアル

- [Aspose.3D を使用した Java での 3D 押し出しの作成](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [Aspose.3D for Java で線形押し出しの方向を設定する方法](/3d/java/linear-extrusion/setting-direction/)
- [線形押し出しでツイストを加えた 3D シーンの作成 – Aspose.3D for Java](/3d/java/linear-extrusion/applying-twist/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}