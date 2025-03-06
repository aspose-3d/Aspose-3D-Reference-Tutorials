---
title: Aspose.3D を使用して Java でクォータニオンを使用して 3D ノードを変換する
linktitle: Aspose.3D を使用して Java でクォータニオンを使用して 3D ノードを変換する
second_title: Aspose.3D Java API
description: Aspose.3D を使用して Java アプリケーションを強化し、強力な 3D 変換を実現します。このステップバイステップ ガイドでは、クォータニオンを使用してノードを変換する方法を学びます。
weight: 20
url: /ja/java/geometry/transform-3d-nodes-with-quaternions/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose.3D を使用して Java でクォータニオンを使用して 3D ノードを変換する

## 導入

Aspose.3D を使用して Java でクォータニオンを使用して 3D ノードを変換するためのこのステップバイステップ ガイドへようこそ。強力な 3D 変換を使用して Java アプリケーションを強化したい場合は、このチュートリアルが最適です。 Aspose.3D for Java は、3D グラフィックスを操作するための堅牢な機能セットを提供します。このチュートリアルでは、クォータニオンを使用した 3D ノードの変換に焦点を当てます。

## 前提条件

チュートリアルに入る前に、次の前提条件が満たされていることを確認してください。

- Java プログラミングの基本的な知識。
- Java 用 Aspose.3D がインストールされています。ダウンロードできます[ここ](https://releases.aspose.com/3d/java/).
- 3D シーンを保存するために設定されたドキュメント ディレクトリ。

## パッケージのインポート

このセクションでは、Aspose.3D を使用して 3D 変換を開始するために必要なパッケージをインポートします。

```java
import com.aspose.threed.*;
```

## ステップ 1: シーン オブジェクトを初期化する

まず、3D 要素のコンテナとして機能するシーン オブジェクトを作成します。

```java
Scene scene = new Scene();
```

## ステップ 2: ノード クラス オブジェクトを初期化する

ここで、ノード クラス オブジェクト (この場合は立方体を表す) を作成します。

```java
Node cubeNode = new Node("cube");
```

## ステップ 3: ポリゴン ビルダーを使用してメッシュを作成する

共通クラスを利用してポリゴンビルダーメソッドでメッシュを作成します。

```java
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

## ステップ 4: メッシュ ジオメトリを設定する

作成したメッシュをキューブノードに割り当てます。

```java
cubeNode.setEntity(mesh);
```

## ステップ 5: クォータニオンを使用して回転を設定する

クォータニオンを使用してキューブ ノードに回転を適用します。

```java
cubeNode.getTransform().setRotation(Quaternion.fromRotation(new Vector3(0, 1, 0), new Vector3(0.3, 0.5, 0.1)));
```

## ステップ 6: 翻訳を設定する

キューブ ノードの変換を指定します。

```java
cubeNode.getTransform().setTranslation(new Vector3(0, 0, 20));
```

## ステップ 7: キューブをシーンに追加する

キューブ ノードをシーンに含めます。

```java
scene.getRootNode().getChildNodes().add(cubeNode);
```

## ステップ 8: 3D シーンを保存する

3D シーンをサポートされているファイル形式 (FBX7500ASCII など) で保存します。

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "TransformationToNode.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
System.out.println("\nTransformation added successfully to node.\nFile saved at " + MyDir);
```

## 結論

おめでとう！ Aspose.3D を使用して Java でクォータニオンを使用して 3D ノードを変換する方法を学習しました。さまざまな変換を試して、3D アプリケーションに命を吹き込みます。

## よくある質問

### Q1: Aspose.3D for Java を無料で使用できますか?

A1: Aspose.3D for Java は無料トライアルを提供しています。見つけられますよ[ここ](https://releases.aspose.com/).

### Q2: Aspose.3D for Java のドキュメントはどこで見つけられますか?

 A2: ドキュメントは入手可能です[ここ](https://reference.aspose.com/3d/java/).

### Q3: Aspose.3D for Java のサポートを受けるにはどうすればよいですか?

 A3: にアクセスしてください。[Aspose.3D フォーラム](https://forum.aspose.com/c/3d/18)サポートのための。

### Q4: 一時ライセンスは利用できますか?

 A4: はい、仮免許を取得できます。[ここ](https://purchase.aspose.com/temporary-license/).

### Q5: Aspose.3D for Java はどこで購入できますか?

 A5: 買えますよ[ここ](https://purchase.aspose.com/buy).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
