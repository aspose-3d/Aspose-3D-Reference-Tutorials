---
date: 2026-02-22
description: Aspose.3D for Java を使用してスライス付きの 3D 押し出しを作成する方法を学びましょう。このステップバイステップ ガイドでは、線形押し出し、丸み半径の設定、OBJ
  へのエクスポートについて解説します。
linktitle: Create 3D Extrusion with Slices – Aspose.3D for Java
second_title: Aspose.3D Java API
title: スライスを使用した3D押し出しの作成 – Aspose.3D for Java
url: /ja/java/linear-extrusion/specifying-slices/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# スライスを使用した3D押し出しの作成 – Aspose.3D for Java

## はじめに

滑らかで精密に見える **create 3d extrusion** オブジェクトを作成する必要がある場合、スライス数の制御が重要です。このチュートリアルでは、Aspose.3D for Java を使用して線形押し出しを行う際にスライスを指定する方法を解説します。スライス数がなぜ重要か、丸み半径の設定方法、そして結果を任意の 3D パイプラインで使用できる OBJ ファイルとしてエクスポートする方法が分かります。

## クイック回答
- **“slices” は何を制御しますか？** 押し出し表面を近似するために使用される中間断面の数です。  
- **スライス数を設定するメソッドはどれですか？** `LinearExtrusion.setSlices(int)`  
- **プロファイルの丸み半径を変更できますか？** はい、`RectangleShape.setRoundingRadius(double)` を使用します。  
- **この例で使用されているファイル形式は何ですか？** Wavefront OBJ (`FileFormat.WAVEFRONTOBJ`)  
- **コードを実行するのにライセンスが必要ですか？** 評価には無料トライアルで動作しますが、製品環境では商用ライセンスが必要です。

## スライス付き線形押し出しとは？

線形押し出しは、2‑D プロファイル（例: 長方形）を直線に沿って伸ばし、3‑D ソリッドを形成します。**slices** を指定することで、Aspose.3D に生成する中間ステップ数を指示し、丸み長方形のような曲線エッジの滑らかさに直接影響します。

## なぜ Java 用 Aspose.3D を使用して 3d extrusion を作成するのか？

* **フルコントロール** – スライス数、丸み半径、エクスポート形式をプログラムで調整できます。  
* **クロスプラットフォーム** – ネイティブ依存なしで、Java が動作する環境ならどこでも使用できます。  
* **エクスポートの柔軟性** – OBJ、FBX、STL など多数の形式に直接保存できます。

## 前提条件

1. **Java Development Kit** – JDK 8 以上がインストールされていること。  
2. **Aspose.3D for Java** – 公式サイトからライブラリをダウンロードしてください [here](https://releases.aspose.com/3d/java/)。  
3. お好みの IDE またはテキストエディタ。

## パッケージのインポート

プロジェクトに Aspose.3D 名前空間を追加し、3‑D モデリングクラスにアクセスできるようにします。

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## ステップバイステップガイド

### ステップ 1: シーンの設定とプロファイルの定義

まず `RectangleShape` を作成し、角を滑らかにするために **rounding radius** を設定します。その後、すべてのジオメトリを保持する新しい `Scene` を初期化します。

```java
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
Scene scene = new Scene();
```

### ステップ 2: 各押し出し用の **Create child node** オブジェクト

すべてのジオメトリは `Node` の下に配置されます。ここでは、低スライス押し出し用と高スライス押し出し用の 2 つの兄弟ノードを生成し、左側のノードを少し横に移動させて結果を比較しやすくします。

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### ステップ 3: 線形押し出しを実行し **set slices** を設定

ここで実際に **create 3d extrusion** オブジェクトを作成します。`LinearExtrusion` コンストラクタはプロファイルと押し出し深さを受け取ります。**匿名内部クラス** を使用して `setSlices` を呼び出し、滑らかさを制御します。左側のノードは 2 スライス（粗い）だけ、右側のノードは 10 スライス（滑らか）を使用します。

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(2);}});
right.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(10);}});
```

### ステップ 4: **Export OBJ** – シーンの保存

最後にシーンを Wavefront OBJ ファイルに書き出します。この形式は 3‑D エディタやゲームエンジンで広くサポートされています。これにより Aspose.3D の **export obj java** 機能が実証されます。

```java
scene.save(MyDir + "SlicesInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## よくある問題と解決策

| 問題 | 発生原因 | 対策 |
|------|----------|------|
| **押し出しが平坦に見える** | スライス数が 1 または 0 に設定されている | `setSlices` が 2 以上の値で呼び出されていることを確認してください。 |
| **丸みのある角がギザギザに見える** | スライス数に対して丸み半径が小さすぎる | 滑らかな曲線にするため、半径またはスライス数のいずれかを増やしてください。 |
| **保存時にファイルが見つからない** | `MyDir` が存在しないフォルダーを指している | 事前にディレクトリを作成するか、絶対パスを使用してください。 |

## よくある質問

**Q: Aspose.3D for Java はどこからダウンロードできますか？**  
A: ライブラリは [here](https://releases.aspose.com/3d/java/) からダウンロードできます。

**Q: Aspose.3D のドキュメントはどこで確認できますか？**  
A: ドキュメントは [here](https://reference.aspose.com/3d/java/) を参照してください。

**Q: 無料トライアルは利用できますか？**  
A: はい、無料トライアルは [here](https://releases.aspose.com/) で試すことができます。

**Q: Aspose.3D のサポートはどこで受けられますか？**  
A: サポートフォーラムは [here](https://forum.aspose.com/c/3d/18) をご覧ください。

**Q: 一時ライセンスを購入できますか？**  
A: はい、一時ライセンスは [here](https://purchase.aspose.com/temporary-license/) で取得できます。

---

**最終更新日:** 2026-02-22  
**テスト環境:** Aspose.3D for Java 24.11 (執筆時点での最新バージョン)  
**作者:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}