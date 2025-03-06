---
title: Aspose.3D for Java での線形押し出しの実行
linktitle: Aspose.3D for Java での線形押し出しの実行
second_title: Aspose.3D Java API
description: Aspose.3D for Java を使用して 3D モデリングの世界を探索してください。直線押し出しを簡単に実行する方法を学びましょう。
weight: 10
url: /ja/java/linear-extrusion/performing-linear-extrusion/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose.3D for Java での線形押し出しの実行

## 導入

Aspose.3D for Java で線形押し出しを実行するためのこの包括的なチュートリアルへようこそ! Java を使用して 3D モデリングのスキルを向上させたい場合は、ここが正しい場所です。このチュートリアルでは、3D モデリング用の強力な Java ライブラリである Aspose.3D を使用して線形押し出しを実行するプロセスを説明します。

## 前提条件

チュートリアルに入る前に、次の前提条件が満たされていることを確認してください。

1. Java 開発環境: マシン上に Java 開発環境がセットアップされていることを確認します。

2.  Aspose.3D ライブラリ: Aspose.3D ライブラリをダウンロードしてインストールします。図書館を見つけることができます[ここ](https://releases.aspose.com/3d/java/).

## パッケージのインポート

開発環境をセットアップし、Aspose.3D ライブラリをインストールしたら、必要なパッケージをインポートします。 Java コードに次の内容を含めます。

```java
import com.aspose.threed.*;
```

明確に理解できるように、各ステップを詳しく見てみましょう。

## ステップ 1: ドキュメント ディレクトリを設定する

ドキュメント ディレクトリへのパスを定義します。

```java
String MyDir = "Your Document Directory";
```

これにより、生成された 3D モデルが指定されたディレクトリに保存されます。

## ステップ 2: 基本形状を初期化する

押し出しの基本プロファイルとして長方形の形状を作成します。

```java
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

必要に応じて丸み半径を調整し、形状をカスタマイズします。

## ステップ 3: 線形押し出しを実行する

基本プロファイルで線形押し出しを実行します。

```java
LinearExtrusion extrusion = new LinearExtrusion(profile, 10) {{ setSlices(100); setCenter(true); setTwist(360); setTwistOffset(new Vector3(10, 0, 0));}};
```

ここでは、シェイプを 10 単位で押し出し、スライスの数を設定し、センタリングを有効にして、ツイストとツイスト オフセットを適用します。

## ステップ 4: 3D シーンの作成

3D シーンを作成し、押し出しを子ノードとして追加します。

```java
Scene scene = new Scene();
scene.getRootNode().createChildNode(extrusion);
```

## ステップ 5: 3D シーンを保存する

生成された 3D シーンを Wavefront OBJ ファイルとして保存します。

```java
scene.save(MyDir +  "LinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

これで、Aspose.3D for Java を使用して線形押し出しが正常に実行されました。

## 結論

おめでとう！ Aspose.3D for Java を利用して線形押し出しを実行する方法を学習しました。この強力なライブラリは、3D モデリング プロジェクトの可能性の世界を開きます。

## よくある質問

### Q1: Aspose.3D はすべての Java バージョンと互換性がありますか?

A1: Aspose.3D は、Java 1.6 以降のバージョンで動作するように設計されています。

### Q2: Aspose.3D を商用プロジェクトに使用できますか?

A2: はい、Aspose.3D は個人プロジェクトと商用プロジェクトの両方に使用できます。ライセンスの詳細を確認する[ここ](https://purchase.aspose.com/buy).

### Q3: Aspose.3D のサポートを受けるにはどうすればよいですか?

 A3: にアクセスしてください。[Aspose.3D フォーラム](https://forum.aspose.com/c/3d/18)コミュニティのサポートを求めるか、購入を検討してください。[仮免許](https://purchase.aspose.com/temporary-license/)プレミアムサポートの場合。

### Q4: Aspose.3D には他の 3D モデリング機能はありますか?

 A4：もちろんです！広範なドキュメントを参照してください[ここ](https://reference.aspose.com/3d/java/)機能と例の包括的なリストをご覧ください。

### Q5: Aspose.3D の無料トライアルはありますか?

 A5: はい、無料トライアルにアクセスできます。[ここ](https://releases.aspose.com/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
