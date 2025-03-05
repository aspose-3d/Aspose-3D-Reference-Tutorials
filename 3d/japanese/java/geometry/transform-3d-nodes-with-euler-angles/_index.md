---
title: Aspose.3D を使用して Java でオイラー角を使用して 3D ノードを変換する
linktitle: Aspose.3D を使用して Java でオイラー角を使用して 3D ノードを変換する
second_title: Aspose.3D Java API
description: Aspose.3D を使用して、Java での 3D 変換の世界を探索してください。ステップバイステップのガイドに従って、動的なオイラー角を 3D ノードに追加します。
type: docs
weight: 19
url: /ja/java/geometry/transform-3d-nodes-with-euler-angles/
---
## 導入

Aspose.3D を使用して、Java でオイラー角を使用して 3D ノードを変換するステップバイステップのチュートリアルへようこそ。このガイドでは、オイラー角を使用して動的な位置決めと方向付けを実現し、3D ノードに変換を追加するプロセスを詳しく説明します。

## 前提条件

チュートリアルに入る前に、次の前提条件が満たされていることを確認してください。

- Java プログラミングの基本的な知識。
- Java Development Kit (JDK) がマシンにインストールされています。
-  Aspose.3D ライブラリは、以下から入手できます。[Aspose.3D Java ドキュメント](https://reference.aspose.com/3d/java/).

## パッケージのインポート

まず、必要なパッケージを Java プロジェクトにインポートします。 Aspose.3D ライブラリがクラスパスに正しく追加されていることを確認してください。まだダウンロードしていない場合は、ダウンロード リンクを見つけてください。[ここ](https://releases.aspose.com/3d/java/).

```java
import com.aspose.threed.*;
```

## ステップ 1. シーンとノードを初期化する

```java
//ExStart:AddTransformationToNodeByEulerAngles
//シーンオブジェクトを初期化する
Scene scene = new Scene();

//Nodeクラスオブジェクトの初期化
Node cubeNode = new Node("cube");
```

## ステップ 2. メッシュの作成とジオメトリの設定

```java
//ポリゴン ビルダー メソッドを使用して共通クラスのメッシュ作成を呼び出し、メッシュ インスタンスを設定します
Mesh mesh = Common.createMeshUsingPolygonBuilder();

//ノードをメッシュ ジオメトリにポイントします
cubeNode.setEntity(mesh);
```

## ステップ 3. オイラー角と平行移動を設定する

```java
//オイラー角
cubeNode.getTransform().setEulerAngles(new Vector3(0.3, 0.1, -0.5));

//翻訳を設定する
cubeNode.getTransform().setTranslation(new Vector3(0, 0, 20));
```

## ステップ 4. シーンにノードを追加する

```java
//シーンにキューブを追加する
scene.getRootNode().getChildNodes().add(cubeNode);
```

## ステップ 5. 3D シーンを保存する

```java
//ドキュメントディレクトリへのパス。
String MyDir = "Your Document Directory";
MyDir = MyDir + "TransformationToNode.fbx";

//3D シーンをサポートされているファイル形式で保存する
scene.save(MyDir, FileFormat.FBX7500ASCII);
//ExEnd:AddTransformationToNodeByEulerAngles
System.out.println("\nTransformation added successfully to node.\nFile saved at " + MyDir);
```

「Your Document Directory」をマシン上の適切なパスに置き換えてください。

## 結論

おめでとう！ Aspose.3D を使用して Java でオイラー角を使用して 3D ノードを正常に変換しました。さまざまな角度や変換を試して、ダイナミックで魅力的な 3D シーンを作成します。

## よくある質問

### Q1: Aspose.3D for Java を商用プロジェクトで使用できますか?

 A1: はい、可能です。訪問[購入ページ](https://purchase.aspose.com/buy)ライセンスの詳細については、

### Q2: Aspose.3D のサポートはどこで見つけられますか?

 A2:[Aspose.3D フォーラム](https://forum.aspose.com/c/3d/18)は支援を求め、コミュニティとつながる場所です。

### Q3: 無料トライアルはありますか?

 A3: はい、探索できます。[無料トライアル](https://releases.aspose.com/) Aspose.3D の機能を体験してください。

### Q4: 仮免許はどうやって取得できますか?

 A4: 仮免許を取得できます。[ここ](https://purchase.aspose.com/temporary-license/).

### Q5: ドキュメントはどこで入手できますか?

 A5:[ドキュメンテーション](https://reference.aspose.com/3d/java/) Aspose.3D for Java の使用に関する包括的なガイダンスを提供します。