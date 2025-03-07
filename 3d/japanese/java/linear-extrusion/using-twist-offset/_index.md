---
title: Aspose.3D for Java による線形押し出しでのツイスト オフセットの使用
linktitle: Aspose.3D for Java による線形押し出しでのツイスト オフセットの使用
second_title: Aspose.3D Java API
description: Aspose.3D for Java を使用して 3D モデリング スキルを強化します。この包括的なチュートリアルでは、線形押し出しでのツイスト オフセットの使用方法を学習します。

weight: 15
url: /ja/java/linear-extrusion/using-twist-offset/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose.3D for Java による線形押し出しでのツイスト オフセットの使用

## 導入

3D グラフィックスのダイナミックな世界では、線形押し出しの技術を習得することがゲームチェンジャーとなります。 Aspose.3D for Java を使用すると、ツイスト オフセット機能を線形押し出しプロセスに組み込むことで、3D モデリングのスキルを向上させることができます。このチュートリアルでは、Aspose.3D for Java を使用して線形押し出しでツイスト オフセットを利用する手順を説明し、見事な 3D シーンを作成するツールを提供します。

## 前提条件

チュートリアルに入る前に、次の前提条件が満たされていることを確認してください。

- Java 環境: システムに Java 開発環境がセットアップされていることを確認してください。
-  Aspose.3D for Java: Aspose.3D ライブラリを次の場所からダウンロードしてインストールします。[ダウンロードリンク](https://releases.aspose.com/3d/java/).
- ドキュメント:[Aspose.3D for Java ドキュメント](https://reference.aspose.com/3d/java/).

## パッケージのインポート

Java プロジェクトで、Aspose.3D for Java の使用を開始するために必要なパッケージをインポートします。シームレスな統合に必要なライブラリが含まれていることを確認してください。

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## ステップ 1: 環境をセットアップする

まず、Java 開発環境をセットアップし、Aspose.3D for Java が正しくインストールされていることを確認します。

## ステップ 2: 基本プロファイルを初期化する

押し出し用のベース プロファイルを作成します。この場合は、丸み半径 0.3 の RectangleShape です。

```java
//ドキュメントディレクトリへのパス。
String MyDir = "Your Document Directory";
//押し出すベースプロファイルを初期化します。
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## ステップ 3: 3D シーンを作成する

押し出したオブジェクトを収容する 3D シーンを構築します。

```java
//シーンを作成する
Scene scene = new Scene();
```

## ステップ 4: ノードの作成

シーン内にノードを生成して、さまざまなエンティティを表します。

```java
//左側のノードを作成する
Node left = scene.getRootNode().createChildNode();
//適切なノードを作成する
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## ステップ 5: 線形押し出しを実行する

さまざまなプロパティを持つ左右のノードの両方で線形押し出しを利用します。

```java
//ツイストとスライスのプロパティを使用して、左側のノードで線形押し出しを実行します。
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});

//ツイスト、ツイスト オフセット、スライス プロパティを使用して、右側のノードで線形押し出しを実行します。
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setTwistOffset(new Vector3(3, 0, 0)); }});
```

## ステップ 6: 3D シーンを保存する

新しく作成した 3D シーンを指定したファイル形式で保存します。

```java
// 3Dシーンを保存する
scene.save(MyDir + "TwistOffsetInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## 結論

おめでとう！ Aspose.3D for Java を使用して Linear Extrusion に Twist Offset を実装することに成功しました。この強力な機能により、3D モデリングの取り組みに可能性の世界が開かれ、複雑で魅力的なシーンを作成できるようになります。

## よくある質問

### Q1: Aspose.3D for Java を非営利プロジェクトで使用できますか?

 A1: はい、Aspose.3D for Java は商用プロジェクトと非商用プロジェクトの両方で使用できます。チェックしてください[ライセンスオプション](https://purchase.aspose.com/buy)詳細については。

### Q2: Aspose.3D for Java のサポートはどこで見つけられますか?

 A2: にアクセスしてください。[Aspose.3D for Java フォーラム](https://forum.aspose.com/c/3d/18)支援を受けたり、コミュニティとつながったりするためです。

### Q3: Aspose.3D for Java の無料トライアルはありますか?

 A3: はい、次のサイトから無料試用版を試すことができます。[リリースページ](https://releases.aspose.com/).

### Q4: Aspose.3D for Java の一時ライセンスを取得するにはどうすればよいですか?

 A4: にアクセスして、プロジェクトの一時ライセンスを取得します。[このリンク](https://purchase.aspose.com/temporary-license/).

### Q5: 追加の例やチュートリアルはありますか?

 A5: はい、を参照してください。[ドキュメンテーション](https://reference.aspose.com/3d/java/)より多くの例と詳細なチュートリアルについては、こちらをご覧ください。
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
