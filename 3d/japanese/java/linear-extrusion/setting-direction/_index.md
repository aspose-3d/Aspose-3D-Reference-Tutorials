---
title: Aspose.3D for Java を使用した線形押し出しの方向の設定
linktitle: Aspose.3D for Java を使用した線形押し出しの方向の設定
second_title: Aspose.3D Java API
description: Aspose.3D for Java で線形押し出しをマスターしましょう!シームレスな 3D プログラミングについてはガイドに従ってください。今すぐダウンロードして、魅力的な体験をお楽しみください。
weight: 12
url: /ja/java/linear-extrusion/setting-direction/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose.3D for Java を使用した線形押し出しの方向の設定

## 導入

Aspose.3D for Java を使用した線形押し出しの方向の設定に関するステップバイステップ ガイドへようこそ。 Aspose.3D は、開発者が 3D ファイルやシーンをシームレスに操作できるようにする強力な Java ライブラリです。このチュートリアルでは、線形押し出しの方向を設定する特定のタスクに焦点を当て、3D プログラミングの習熟度を高めます。

## 前提条件

チュートリアルに入る前に、次の前提条件が満たされていることを確認してください。

- Java プログラミング言語の基本的な知識。
-  Aspose.3D ライブラリがインストールされています。からダウンロードできます[ここ](https://releases.aspose.com/3d/java/).
- Eclipse や IntelliJ などの Java 用の統合開発環境 (IDE)。

## パッケージのインポート

プロジェクトを開始するために必要なパッケージをインポートしていることを確認してください。

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## ステップ 1: 基本プロファイルを初期化する

まず、押し出される基本プロファイルを初期化します。この例では、`RectangleShape`丸め半径 0.3 の場合:

```java
//ドキュメントディレクトリへのパス。
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## ステップ 2: シーンを作成する

次に、押し出されたオブジェクトを含む 3D シーンを作成します。

```java
Scene scene = new Scene();
```

## ステップ 3: ノードの作成

シーン内に左右のノードを作成します。

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## ステップ 4: 左側のノードで線形押し出しを実行する

を使用して、左側のノードで線形押し出しを実行します。`LinearExtrusion`ツイストやスライスなどのパラメータを指定したクラス:

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## ステップ 5: 方向を指定して右ノードで線形押し出しを実行する

右側のノードで線形押し出しを実行し、`setDirection`押し出し方向を定義するプロパティ:

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## ステップ 6: 3D シーンを保存する

3D シーンを希望のファイル形式で保存します。この例では、Wavefront OBJ ファイルとして保存します。

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## 結論

おめでとう！ Aspose.3D for Java を使用して線形押し出しの方向を設定する方法を学習しました。このチュートリアルは、3D プログラミングのスキルを向上させ、創造的なプロジェクトの新たな可能性を開きます。

## よくある質問

### Q1: Aspose.3D を他のプログラミング言語で使用できますか?

A1: Aspose.3D は、.NET や Java などのさまざまなプログラミング言語をサポートしています。

### Q2. Aspose.3D に利用できる無料トライアルはありますか?

 A2: はい、無料トライアルで Aspose.3D の機能を試すことができます。[ここ](https://releases.aspose.com/).

### Q3: Aspose.3D for Java の詳細なドキュメントはどこで見つけられますか?

 A3: 包括的なドキュメントが入手可能です。[ここ](https://reference.aspose.com/3d/java/).

### Q4: Aspose.3D のサポートを受けるにはどうすればよいですか?

 A4: にアクセスしてください。[Aspose.3D フォーラム](https://forum.aspose.com/c/3d/18)サポートやご質問がございましたら。

### Q5: Aspose.3D の一時ライセンスは利用できますか?

 A5: はい、一時ライセンスを取得できます。[ここ](https://purchase.aspose.com/temporary-license/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
