---
title: Aspose.3D for Java を使用した線形押し出しでのツイストの適用
linktitle: Aspose.3D for Java を使用した線形押し出しでのツイストの適用
second_title: Aspose.3D Java API
description: Aspose.3D for Java を使用して 3D モデルにひねりを加える方法を学びます。線形押し出し効果を強化するには、ステップバイステップのガイドに従ってください。
type: docs
weight: 14
url: /ja/java/linear-extrusion/applying-twist/
---
## 導入

Aspose.3D for Java を使用して線形押し出しにツイストを適用するためのこのステップバイステップのチュートリアルへようこそ。 Aspose.3D は、開発者が 3D ファイル形式を操作できるようにする強力な Java ライブラリで、3D シーンの作成、操作、レンダリングのための堅牢な機能を提供します。このチュートリアルでは、線形押し出しプロセス中にツイスト効果を適用して 3D モデルを強化する方法を検討します。

## 前提条件

チュートリアルに入る前に、次の前提条件が満たされていることを確認してください。

- Java 開発環境: システムに Java がインストールされていることを確認してください。
-  Aspose.3D ライブラリ: Java 用の Aspose.3D ライブラリを次の場所からダウンロードしてインストールします。[ダウンロードリンク](https://releases.aspose.com/3d/java/).
- ドキュメント: を参照してください。[Aspose.3D ドキュメント](https://reference.aspose.com/3d/java/)総合的な指導を行います。

## パッケージのインポート

コーディングプロセスを開始する前に、必要なパッケージを Java プロジェクトにインポートします。これを行う方法の例を次に示します。

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## ステップ 1: ドキュメント ディレクトリを設定する

まず、3D シーンを保存するドキュメント ディレクトリを設定します。

```java
// ExStart:SetDocumentDirectory
String MyDir = "Your Document Directory";
// ExEnd:SetDocumentDirectory
```

## ステップ 2: 基本プロファイルを初期化する

押し出すベースプロファイルを初期化します。この例では、丸み半径のある長方形を使用します。

```java
// ExStart:InitializeBaseProfile
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
// ExEnd:InitializeBaseProfile
```

## ステップ 3: シーンを作成する

押し出されたノードをホストする 3D シーンを作成します。

```java
//ExStart:シーンの作成
Scene scene = new Scene();
//ExEnd:CreateScene
```

## ステップ 4: ノードの作成

シーン内に左右のノードを作成します。左側のノードの移動を調整します。

```java
// ExStart:ノードの作成
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
//ExEnd:ノードの作成
```

## ステップ 5: ツイストを使用して線形押し出しを実行する

ツイストとスライスのプロパティを適用して、左右のノードの両方で線形押し出しを実行します。

```java
// ExStart:ツイスト付き線形押し出し
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(0); setSlices(100); }});
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(90); setSlices(100); }});
//ExEnd:ツイスト付き線形押し出し
```

## ステップ 6: 3D シーンを保存する

3D シーンを Wavefront OBJ ファイル形式で保存します。

```java
// ExStart:3DScene の保存
scene.save(MyDir + "TwistInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
//ExEnd:Save3DScene
```

## 結論

おめでとう！ Aspose.3D for Java を使用して線形押し出しにツイストを適用することに成功しました。このチュートリアルでは、3D モデリング機能を強化するのに役立つ詳細なステップバイステップ ガイドを提供しました。

## よくある質問

### Q1: Aspose.3D for Java を使用して他の 3D ファイル形式を操作できますか?

A1: はい、Aspose.3D はさまざまな 3D ファイル形式をサポートしており、さまざまな種類のファイルをインポート、エクスポート、操作できます。

### Q2: Aspose.3D for Java のサポートはどこで見つけられますか?

 A2: にアクセスしてください。[Aspose.3D フォーラム](https://forum.aspose.com/c/3d/18)コミュニティのサポートとディスカッションのために。

### Q3: Aspose.3D for Java の無料トライアルはありますか?

 A3: はい、以下から無料試用版にアクセスできます。[ここ](https://releases.aspose.com/).

### Q4: Aspose.3D for Java の一時ライセンスを取得するにはどうすればよいですか?

 A4: から一時ライセンスを取得します。[一時ライセンスのページ](https://purchase.aspose.com/temporary-license/).

### Q5: Aspose.3D for Java はどこで購入できますか?

A5: Aspose.3D for Java を次のサイトから購入します。[購入ページ](https://purchase.aspose.com/buy).