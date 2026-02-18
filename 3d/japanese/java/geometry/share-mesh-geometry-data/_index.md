---
date: 2026-02-17
description: Aspose.3D を使用して Java 3D でマテリアルカラーを設定し、メッシュジオメトリデータを共有しながら、メッシュを FBX に変換する方法を学びましょう。
linktitle: Convert Mesh to FBX and Set Material Color in Java 3D
second_title: Aspose.3D Java API
title: メッシュをFBXに変換し、Java 3Dでマテリアルの色を設定する
url: /ja/java/geometry/share-mesh-geometry-data/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# メッシュを FBX に変換し、Java 3D でマテリアルカラーを設定する

## はじめに

Java ベースの 3D アプリケーションを構築する際、同じジオメトリを複数のオブジェクトで再利用しつつ、各インスタンスに固有の外観を与える必要が頻繁にあります。このチュートリアルでは **メッシュを FBX に変換する方法** を学び、複数のノード間で基礎となるメッシュジオメトリを共有し、**各ノードに異なるマテリアルカラーを設定する方法** を解説します。最後には、任意のエンジンやビューアにドロップできる、エクスポート可能な FBX シーンが完成します。

## クイックアンサー
- **主な目標は何ですか？** メッシュをFBXに変換し、メッシュジオメトリを共有し、各ノードに異なるマテリアルカラーを設定します。
- **必要なライブラリは？** Aspose.3D for Java
- **結果をどのようにエクスポートしますか？** `FileFormat.FBX7400ASCII` を使用して、シーンをFBXファイルとして保存します。
- **ライセンスは必要ですか？** 本番環境での使用には、一時ライセンスまたはフルライセンスが必要です。
- **どのJavaバージョンで動作しますか？** Java8以上の環境であればどれでも構いません。

## **メッシュをFBXに変換する**とは？

`convert mesh to fbx` は、メモリ上で作成または操作したメッシュオブジェクトを FBX ファイル形式に書き出すプロセスです。FBX は Maya、Blender、Unity などの 3D ツールで広くサポートされています。Aspose.3D が重い処理を担うので、適切な `FileFormat` を指定して `scene.save(...)` を呼び出すだけで完了します。

## メッシュジオメトリデータを共有する理由は何ですか？

ジオメトリを共有すると、メモリ使用量が削減され、レンダリング速度が向上します。基礎となる頂点バッファが一度だけ格納されるためです。この手法は、森林、群衆、モジュラー建築など、同じオブジェクトが多数出現するシーンに最適です。各インスタンスは変換やマテリアルだけが異なります。

## 前提条件

チュートリアルに入る前に、以下の前提条件を確認してください。

- **Java Development Environment** – Java 8 以上が動作する任意の IDE またはコマンドライン環境。  
- **Aspose.3D Library** – 公式サイトから最新の JAR をダウンロード: [here](https://releases.aspose.com/3d/java/).

## パッケージのインポート

必要なパッケージを Java プロジェクトにインポートします。このステップは Aspose.3D の機能にアクセスするために必須です。

```java
import com.aspose.threed.*;
```

## ステップ 1: シーンオブジェクトの初期化 (シーン Java の初期化)

シーンオブジェクトを初期化して、3D のキャンバスを用意します。

```java
// Initialize scene object
Scene scene = new Scene();
```

## ステップ 2: カラーベクターの定義

このステップでは、シーン内の各要素に適用するカラー ベクトルの配列を定義します。

```java
// Define color vectors
Vector3[] colors = new Vector3[] {
    new Vector3(1, 0, 0),
    new Vector3(0, 1, 0),
    new Vector3(0, 0, 1)
};
```

## ステップ 3: ポリゴンビルダーを使用して 3D メッシュ Java を作成する (3D メッシュ Java の作成)

Common クラスを利用して、ポリゴン ビルダー方式でメッシュを作成します。このメッシュが 3D 要素の基盤となります。

```java
// Call Common class create mesh using polygon builder method to set mesh instance
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

## 各ノードのマテリアルカラーを設定する方法

カラー ベクトルを走査しながらキューブ ノードを作成し、マテリアル、**set material color**、平行移動などの属性を設定します。これが各メッシュインスタンスの外観を制御する核心です。

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

## ステップ 5: 3D シーンを保存する (シーンを FBX で保存し、メッシュを FBX に変換する)

サポートされているファイル形式（この例では FBX7400ASCII）で 3D シーンを保存するディレクトリとファイル名を指定します。このステップは **convert mesh to FBX** を実演します。

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
MyDir = MyDir + "MeshGeometryData.fbx";

// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7400ASCII);
```

## よくある落とし穴とヒント

- **Path Issues** – ファイル名を付加する前に、ディレクトリ パスの末尾がファイル区切り文字（`/` または `\\`）で終わっていることを確認してください。  
- **License Initialization** – `scene.save` を呼び出す前に Aspose.3D のライセンスを設定し忘れると、トライアル モードで動作しウォーターマークが埋め込まれる可能性があります。  
- **Material Overwrites** – 同じ `LambertMaterial` インスタンスを複数ノードで再利用すると、すべてのノードが同一カラーになります。イテレーションごとに新しいマテリアルを作成してください（上記コード参照）。  
- **Large Meshes** – 頂点数が数百万に達するメッシュの場合、インデックス付きポリゴンを使用した `MeshBuilder` を活用し、FBX ファイルサイズを抑えることを検討してください。

## その他のよくある質問

**Q1:​​ Aspose.3D を他の Java フレームワークと併用できますか？**
A1: はい。Aspose.3D は、さまざまな Java フレームワークとシームレスに連携するように設計されています。

**Q2: Aspose.3D にはライセンスオプションがありますか？**
A2: はい。ライセンスオプションについては、[こちら](https://purchase.aspose.com/buy) をご覧ください。

**Q3: Aspose.3D のサポートを受けるにはどうすればよいですか？**
A3: サポートやディスカッションについては、Aspose.3D [フォーラム](https://forum.aspose.com/c/3d/18) をご覧ください。

**Q4: 無料トライアルはありますか？**
A4: はい。[こちら](https://releases.aspose.com/) から無料トライアルを入手できます。

**Q5: Aspose.3D の一時ライセンスを取得するにはどうすればよいですか？**
A5: 一時ライセンスは [こちら](https://purchase.aspose.com/temporary-license/) から取得できます。

## まとめ

おめでとうございます！Aspose.3D for Java を使用して、**メッシュを FBX に変換**し、複数のノード間でメッシュジオメトリデータを共有し、個別のマテリアルカラーを設定することができました。このワークフローにより、軽量で再利用可能なメッシュアーキテクチャを構築でき、FBX 対応のあらゆるパイプラインにエクスポートできます。

---

**最終更新日:** 2026年2月17日
**テスト環境:** Aspose.3D 24.11 for Java
**作成者:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}