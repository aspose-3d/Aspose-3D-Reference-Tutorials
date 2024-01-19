---
title: Aspose.3D を使用した変換行列による 3D ノードの変換
linktitle: Aspose.3D を使用した Java の変換行列による 3D ノードの変換
second_title: Aspose.3D Java API
description: Aspose.3D を使用して Java の 3D グラフィックスの世界を探索してください。変換行列を使用してノードを簡単に変換する方法を学びます。
type: docs
weight: 21
url: /ja/java/geometry/transform-3d-nodes-with-matrices/
---
## 導入

Aspose.3D を使用して Java で変換行列を使用して 3D ノードを変換するためのこのステップバイステップ ガイドへようこそ。 3D グラフィックスとモデリングのスキルを向上させたいと考えている Java 開発者にとって、ここは正しい場所です。このチュートリアルでは、Aspose.3D フレームワーク内で 3D ノードに変換を適用するプロセスについて詳しく説明します。

## 前提条件

始める前に、次の前提条件を満たしていることを確認してください。

- Java プログラミングの基本的な知識。
-  Aspose.3D ライブラリがインストールされています。からダウンロードできます[ここ](https://releases.aspose.com/3d/java/).
- Java 開発用の実用的な統合開発環境 (IDE)。

## パッケージのインポート

Java プロジェクトで、Aspose.3D から必要なパッケージをインポートします。 Aspose.3D ライブラリを使用するようにプロジェクトが正しく構成されていることを確認してください。 import ステートメントのサンプルを次に示します。

```java
import com.aspose.threed.*;

```

## 3D ノードの変換

### ステップ 1: シーン オブジェクトを初期化する

まず、3D 要素のコンテナとして機能するシーン オブジェクトを初期化します。

```java
Scene scene = new Scene();
```

### ステップ 2: ノード クラス オブジェクトを初期化する

変換を受けるキューブなどの Node クラス オブジェクトを作成します。

```java
Node cubeNode = new Node("cube");
```

### ステップ 3: ポリゴン ビルダーを使用してメッシュを作成する

Common クラスを利用して、ポリゴン ビルダー メソッドを使用してメッシュを作成します。これにより、立方体のメッシュ インスタンスが設定されます。

```java
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

### ステップ 4: ノードをメッシュ ジオメトリにポイントする

作成したメッシュをキューブノードに割り当てます。

```java
cubeNode.setEntity(mesh);
```

### ステップ 5: カスタム翻訳マトリックスの設定

カスタム変換行列をキューブ ノードに適用します。この例では、変換用の変換行列を設定します。

```java
cubeNode.getTransform().setTransformMatrix(new Matrix4(
    1, -0.3, 0, 0,
    0.4, 1, 0.3, 0,
    0, 0, 1, 0,
    0, 20, 0, 1
));
```

### ステップ 6: キューブをシーンに追加する

キューブ ノードをシーンのルート ノードに含めます。

```java
scene.getRootNode().addChildNode(cubeNode);
```

### ステップ 7: 3D シーンを保存する

FBX などのサポートされているファイル形式で 3D シーンを保存するためのディレクトリとファイル名を指定します。

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "TransformationToNode.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
System.out.println("\nTransformation added successfully to node.\nFile saved at " + MyDir);
```

## 結論

おめでとう！ Java で Aspose.3D を使用して 3D ノードを変換する方法を学習しました。さまざまなマトリックスを試して、3D グラフィックスの無限の可能性を探求してください。

## よくある質問

### Q1: 単一の 3D ノードに複数の変換を適用できますか?

A1: はい、複数の変換行列を連結して複雑な変換を行うことができます。

### Q2: Aspose.3D で 3D オブジェクトを回転するにはどうすればよいですか?

A2: 目的の回転を行うには、変換行列で適切な回転行列を使用します。

### Q3: 作成できる 3D シーンのサイズに制限はありますか?

A3: 3D シーンのサイズはシステム リソースによって制限される場合がありますが、Aspose.3D は効率を重視して設計されています。

### Q4: 追加の例やドキュメントはどこで入手できますか?

 A4: にアクセスしてください。[Aspose.3D ドキュメント](https://reference.aspose.com/3d/java/)より多くの例と詳細については。

### Q5: Aspose.3D の一時ライセンスを取得するにはどうすればよいですか?

 A5: 仮免許は取得できます。[ここ](https://purchase.aspose.com/temporary-license/).