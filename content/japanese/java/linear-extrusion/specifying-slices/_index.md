---
title: Aspose.3D for Java を使用した線形押し出しでのスライスの指定
linktitle: Aspose.3D for Java を使用した線形押し出しでのスライスの指定
second_title: Aspose.3D Java API
description: Aspose.3D for Java を使用して線形押し出しでスライスを指定する方法を学びます。このステップバイステップのガイドで 3D モデリングのスキルを向上させましょう。
type: docs
weight: 13
url: /ja/java/linear-extrusion/specifying-slices/
---
## 導入

複雑な 3D モデルの作成には、多くの場合、創造性以上のものが必要です。自由に使えるツールを完全に理解することが必要です。 Aspose.3D for Java は、この点で大きな変革をもたらします。このチュートリアルでは、線形押し出しでのスライスの指定という特定の側面に焦点を当てます。

## 前提条件

チュートリアルに入る前に、次の前提条件が満たされていることを確認してください。

1. Java 環境: システムに Java 開発環境がセットアップされていることを確認します。
2.  Java 用 Aspose.3D: Aspose.3D ライブラリをダウンロードしてインストールします。必要なパッケージを見つけることができます[ここ](https://releases.aspose.com/3d/java/).

## パッケージのインポート

Java プロジェクトで、Aspose.3D ライブラリをインポートします。これは、これから扱う機能にアクセスするために重要です。次の import ステートメントをコードに追加します。

```java
import com.aspose.threed.*;

import java.io.IOException;
```

ここで、例を複数のステップに分けてみましょう。

## ステップ 1: シーンをセットアップする

押し出される基本プロファイルを初期化します。この場合は、`RectangleShape`指定された丸め半径を使用します。作業する 3D シーンを作成します。

```java
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
Scene scene = new Scene();
```

## ステップ 2: ノードの作成

シーン内に左右のノードを生成します。空間的な変化に合わせて、左側のノードの移動を調整します。

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## ステップ 3: スライスを使用した線形押し出し

両方のノードで線形押し出しを実行し、それぞれのスライス数を指定します。ここで魔法が起こります。

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(2);}});
right.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(10);}});
```

## ステップ 4: シーンを保存する

3D シーンを希望の形式 (この場合は Wavefront OBJ ファイル) で保存します。

```java
scene.save(MyDir + "SlicesInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## 結論

おめでとう！ Aspose.3D for Java を使用して線形押し出しでスライスを指定する方法を学習しました。このスキルは、3D モデリングの旅に新たな可能性をもたらします。

## よくある質問

### Q1: Java 用 Aspose.3D をダウンロードするにはどうすればよいですか?

 A1: ライブラリをダウンロードできます。[ここ](https://releases.aspose.com/3d/java/).

### Q2: Aspose.3D のドキュメントはどこで見つけられますか?

 A2: ドキュメントを参照してください。[ここ](https://reference.aspose.com/3d/java/).

### Q3: 無料トライアルはありますか?

 A3: はい、無料トライアルを試すことができます[ここ](https://releases.aspose.com/).

### Q4: Aspose.3D のサポートを受けるにはどうすればよいですか?

 A4: サポート フォーラムにアクセスしてください。[ここ](https://forum.aspose.com/c/3d/18).

### Q5: 一時ライセンスを購入できますか?

 A5: はい、一時ライセンスを取得できます。[ここ](https://purchase.aspose.com/temporary-license/).