---
date: 2025-12-12
description: Aspose.3D を使用して Java 3D でメッシュジオメトリ データを共有しながらマテリアルの色を設定し、シーンを FBX として保存する方法を学びましょう。
linktitle: Set Material Color and Share Mesh Geometry Data in Java 3D with Aspose.3D
second_title: Aspose.3D Java API
title: Aspose.3D を使用した Java 3D でマテリアルカラーを設定し、メッシュジオメトリデータを共有する
url: /ja/java/geometry/share-mesh-geometry-data/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Java 3DでAspose.3Dを使用してマテリアルカラーを設定し、メッシュジオメトリデータを共有する

## はじめに

Java 3Dの世界へAspose.3Dと共に踏み出すことで、驚くべきビジュアライゼーションや没入型体験を作り出す可能性が広がります。このチュートリアルでは、**メッシュを共有する方法**をAspose.3Dを使ってJava 3Dで実現する順と、各メッシュインスタンスの**マテリアルカラーを設定する方法**を詳しく解説します。各ステップを注意深く実行すれば、複数ノード間でメッシュデータをシームレスにやり取りし、カラーコントロールとFBXへのエクスポートが可能になります。

## クイック回答
- **目的は何ですか？** 各ノードのマテリアルカラーを設定し、メッシュジオメトリデータを共有します。  
- **必要なライブラリは？** Aspose.3D for Java。  
- **結果はどうやってエクスポートしますか？** シーンをFBXファイル（FBX7400ASCII）として保存します。  
- **ライセンスは必要ですか？** 本番環境で使用するには、一時ライセンスまたはフルライセンスが必要です。  
- **対応するJavaバージョンは？** Java 8以降の環境であればどれでも動作します。

## 前提条件

チュートリアルに入る前に、以下の前提条件が整っていることを確認してください。

- **Java開発環境:** システムにJava開発環境がセットアップされていることを確認してください。  
- **Aspose.3D ライブラリ:** Aspose.3D ライブラリをダウンロードしてインストールしてください。ライブラリは[こちら](https://releases.aspose.com/3d/java/)から入手できます。

## パッケージのインポート

必要なパッケージをJavaプロジェクトにインポートします。このステップは、Aspose.3D ライブラリが提供する機能にアクセスするために重要です。

```java
import com.aspose.threed.*;
```

## ステップ 1: シーンオブジェクトの初期化 (initialize scene java)

シーンオブジェクトを初期化してプロセスを開始します。このシーンは、3Dマジックが展開されるキャンバスとなります。

```java
// Initialize scene object
Scene scene = new Scene();
```

## ステップ 2: カラーベクトルの定義

このステップでは、3Dシーン内のさまざまな要素に適用するカラーベクトルの配列を定義します。

```java
// Define color vectors
Vector3[] colors = new Vector3[] {
    new Vector3(1, 0, 0),
    new Vector3(0, 1, 0),
    new Vector3(0, 0, 1)
};
```

## ステップ 3: ポリゴンビルダーを使用して3Dメッシュを作成 (create 3d mesh java)

Common クラスを利用して、ポリゴンビルダー方式でメッシュを作成します。このメッシュが3D要素の基盤となります。

```java
// Call Common class create mesh using polygon builder method to set mesh instance
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

## 各ノードのマテリアルカラーを設定する方法は？

カラーベクトルを反復処理し、キューブノードを作成して、material、**set material color**、translation などの属性を設定します。これが各メッシュインスタンスの外観を制御する核心です。

```java
int idx = 0;
for(Vector3 color : colors) {
    // Initialize cube node object
    Node cube = new Node("cube");
    cube.setEntity(mesh);
    LambertMaterial mat = new LambertMaterial();
    // Set color
    mat.setDiffuseColor(color);
    // Set material
    cube.setMaterial(mat);
    // Set translation
    cube.getTransform().setTranslation(new Vector3(idx++ * 20, 0, 0));
    // Add cube node
    scene.getRootNode().addChildNode(cube);
}
```

## ステップ 5: 3Dシーンの保存 (save scene fbx, convert mesh to fbx)

サポートされているファイル形式（この場合は FBX7400ASCII）で3Dシーンを保存するディレクトリとファイル名を指定します。このステップでは**convert mesh to FBX**も実演します。

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
MyDir = MyDir + "MeshGeometryData.fbx";

// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7400ASCII);
```

## 結論

おめでとうございます！**マテリアルカラーを設定**し、複数ノード間でメッシュジオメトリデータを共有し、Aspose.3D for Java を使用して結果を FBX ファイルとしてエクスポートすることに成功しました。これにより、視覚的に魅力的でインタラクティブな 3D アプリケーションを作成する無限の可能性が広がります。

## FAQ

### Q1: Aspose.3Dを他のJavaフレームワークと併用できますか？

A1: はい、Aspose.3D はさまざまな Java フレームワークとシームレスに連携できるよう設計されています。

### Q2: Aspose.3Dのライセンスオプションはありますか？

A2: はい、ライセンスオプションは[こちら](https://purchase.aspose.com/buy)でご確認いただけます。

### Q3: Aspose.3Dのサポートはどこで受けられますか？

A3: サポートやディスカッションは Aspose.3D の[フォーラム](https://forum.aspose.com/c/3d/18)をご利用ください。

### Q4: 無料トライアルはありますか？

A4: はい、無料トライアルは[こちら](https://releases.aspose.com/)から入手できます。

### Q5: Aspose.3Dの一時ライセンスはどこで取得できますか？

A5: 一時ライセンスは[こちら](https://purchase.aspose.com/temporary-license/)から取得できます。

## 追加のよくある質問

**Q: FBX 以外の形式にシーンをエクスポートできますか？**  
A: はい、Aspose.3D は OBJ、STL、3MF などをサポートしています。`save` 呼び出し時に `FileFormat` 列挙体を変更するだけです。

**Q: シーン作成後にマテリアルを変更したい場合はどうすればよいですか？**  
A: ノードを取得し、`LambertMaterial`（例: `setDiffuseColor`）を変更してからシーンを再保存してください。

**Q: ライブラリは大規模メッシュを効率的に処理できますか？**  
A: Aspose.3D は最適化されたデータ構造を使用していますが、極めて大きなメッシュの場合はストリーミングやシーン分割を検討してください。

**Q: カラー変更をアニメーションさせる方法はありますか？**  
A: はい、`AnimationController` API を使用してマテリアルプロパティをアニメーション化できます。

---

**最終更新:** 2025-12-12  
**テスト環境:** Aspose.3D 24.11 for Java  
**作者:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}