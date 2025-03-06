---
title: Aspose.3D for Java を使用した線形押し出しのコントロール センター
linktitle: Aspose.3D for Java を使用した線形押し出しのコントロール センター
second_title: Aspose.3D Java API
description: Aspose.3D を使用して Java の 3D グラフィックスの世界を探索してください。直線押し出しの中心を簡単に制御します。
weight: 11
url: /ja/java/linear-extrusion/controlling-center/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose.3D for Java を使用した線形押し出しのコントロール センター

## 導入

3D グラフィックスと Java プログラミングの世界では、線形押し出しの中心を制御することが、プロジェクトで望ましい効果を達成する上で重要な役割を果たします。 Aspose.3D for Java は、そのようなタスクをシームレスに処理するための強力なツールキットを提供します。このチュートリアルでは、Aspose.3D for Java を使用して線形押し出しで中心を制御するプロセスを詳しく説明し、スムーズかつ包括的に理解できるように各ステップを詳しく説明します。

## 前提条件

このチュートリアルを開始する前に、次の前提条件が満たされていることを確認してください。

1. Java 開発環境: マシン上に Java 開発環境がセットアップされていることを確認します。

2.  Java 用 Aspose.3D: Aspose.3D ライブラリをダウンロードしてインストールします。ライブラリとそのドキュメントを見つけることができます[ここ](https://reference.aspose.com/3d/java/).

3. ドキュメント ディレクトリ: Java ドキュメントを保存するディレクトリを作成します。これを「あなたのドキュメント ディレクトリ」と呼びましょう。

## パッケージのインポート

Java 開発環境で、Aspose.3D に必要なパッケージをインポートします。これにより、コードがライブラリによって提供される機能に確実にアクセスできるようになります。

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## ステップ 1: 基本プロファイルを設定する

押し出すベースプロファイルを初期化します。この例では、丸め半径 0.3 の長方形を使用します。

```java
//ドキュメントディレクトリへのパス。
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## ステップ 2: 3D シーンを作成する

シーンを作成して 3D 世界の基礎を構築します。

```java
Scene scene = new Scene();
```

## ステップ 3: 左右のノードを作成する

シーン内に左右のノードを確立します。これらのノードは、3D オブジェクトのキャンバスとして機能します。

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## ステップ 4: 中心プロパティを使用した線形押し出し

左側のノードをセンタリングせずに線形押し出しを実行し、スライス数を 3 に設定します。

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

## ステップ 5: 基準となるグランドプレーンを設定する

左側のノードにグランド プレーンを追加して、視覚的な表現を強化します。

```java
left.createChildNode(new Box(0.01, 3, 3));
```

## ステップ 6: 中心プロパティを使用した線形押し出し (右ノード)

右側のノードで線形押し出しを実行し、今度は押し出しを中央に配置し、再度スライスの数を 3 に設定します。

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

## ステップ 7: 基準となるグランド プレーンを設定する (右側のノード)

左側のノードと同様に、参照のために右側のノードにグランド プレーンを追加します。

```java
right.createChildNode(new Box(0.01, 3, 3));
```

## ステップ 8: 3D シーンを保存する

3D シーンを Wavefront OBJ 形式で保存します。

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## 結論

Aspose.3D for Java を使用して線形押し出しの中心を制御すると、3D グラフィックス開発における刺激的な可能性が開かれます。このステップバイステップのガイドに従うことで、center プロパティを操作する方法を学び、Java プロジェクトで目的の視覚効果を実現できるようになりました。

## よくある質問

### Q1: Aspose.3D for Java を商用プロジェクトで使用できますか?

 A1: はい、Aspose.3D for Java は商用利用が可能です。ライセンスの詳細については、次のサイトを参照してください。[ここ](https://purchase.aspose.com/buy).

### Q2: 無料トライアルはありますか?

 A2: はい、Aspose.3D for Java の無料トライアルを試すことができます。[ここ](https://releases.aspose.com/).

### Q3: Aspose.3D for Java のサポートはどこで見つけられますか?

 A3: Aspose.3D コミュニティ フォーラムは、サポートを求め、経験を共有するのに最適な場所です。フォーラムにアクセスしてください[ここ](https://forum.aspose.com/c/3d/18).

### Q4: テストには一時ライセンスが必要ですか?

A4: はい、テスト目的で一時ライセンスが必要な場合は、取得できます。[ここ](https://purchase.aspose.com/temporary-license/).

### Q5: ドキュメントはどこで入手できますか?

 A5: Aspose.3D for Java のドキュメントが入手可能です。[ここ](https://reference.aspose.com/3d/java/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
