---
title: 3D シーンでの変換マトリックスによるノードの変換
linktitle: 3D シーンでの変換マトリックスによるノードの変換
second_title: Aspose.3D .NET API
description: Aspose.3D for .NET を使用して、3D シーンでノードを簡単に変換します。チュートリアルで段階的にノード変換を学習します。
type: docs
weight: 21
url: /ja/net/geometry-and-hierarchy/transformation-node-matrix/
---
## 導入

3D グラフィックスとビジュアライゼーションの動的な領域では、シーン内のオブジェクトを操作する機能が重要な側面となります。 Aspose.3D for .NET を使用すると、開発者は変換マトリックスを使用してノードをシームレスに変換し、3D シーンに創造性と制御の層を追加できます。このチュートリアルでは、3D シーン内のノードを変換するプロセスを段階的に説明します。

## 前提条件

チュートリアルに入る前に、次の前提条件が満たされていることを確認してください。

1.  Aspose.3D for .NET ライブラリ: Aspose.3D ライブラリが .NET プロジェクトにインストールされていることを確認します。ダウンロードできます[ここ](https://releases.aspose.com/3d/net/).

2. 開発環境: 動作する .NET 開発環境をセットアップします。まだセットアップしていない場合は、変換を実装する新しいプロジェクトを作成します。

## 名前空間のインポート

まず、必要な名前空間を .NET プロジェクトにインポートします。これらの名前空間は、3D シーン操作に不可欠なクラスとメソッドを提供します。

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

基本を説明したので、変換プロセスをステップバイステップのガイドに分解してみましょう。

## ステップ 1: シーンとノードを初期化する

```csharp
//ExStart:AddTransformationToNodeByTransformationMatrix
//シーンオブジェクトを初期化する
Scene scene = new Scene();

//Nodeクラスオブジェクトの初期化
Node cubeNode = new Node("cube");
```

このステップでは、新しい 3D シーンとそのシーン内に「cube」という名前のノードを作成します。

## ステップ 2: メッシュの作成とジオメトリの設定

```csharp
//ポリゴン ビルダー メソッドを使用して共通クラスのメッシュ作成を呼び出し、メッシュ インスタンスを設定します
Mesh mesh = Common.CreateMeshUsingPolygonBuilder(); 

//ノードをメッシュ ジオメトリにポイントします
cubeNode.Entity = mesh;
```

ここでは、ポリゴン ビルダー メソッドを使用してメッシュを生成し、それをノードに割り当てて、立方体のジオメトリを確立します。

## ステップ 3: カスタム翻訳マトリックスの設定

```csharp
//カスタム翻訳行列を設定する
cubeNode.Transform.TransformMatrix = new Matrix4(
    1, -0.3, 0, 0,
    0.4, 1, 0.3, 0,
    0, 0, 1, 0,
    0, 20, 0, 1
);        
```

カスタム変換行列を定義して、ノードに適用される特定の変換を決定します。必要な変換に必要なマトリックス値を調整します。

## ステップ 4: シーンにノードを追加する

```csharp
//シーンにキューブを追加する
scene.RootNode.ChildNodes.Add(cubeNode);            
```

キューブ ノードをシーンに含めて、3D 環境全体の一部にします。

## ステップ 5: シーンを保存する

```csharp
//ドキュメントディレクトリへのパス。
var output = "Your Output Directory" + "TransformationToNode.fbx";

//3D シーンをサポートされているファイル形式で保存する
scene.Save(output, FileFormat.FBX7500ASCII);
// ExEnd:AddTransformationToNodeByTransformationMatrix
Console.WriteLine("\nTransformation added successfully to node.\nFile saved at " + output);
```

出力ディレクトリとファイル名を指定し、3D シーンを希望のファイル形式で保存します。この例では、FBX7500ASCII 形式で保存しています。

## 結論

おめでとう！ Aspose.3D for .NET を使用して 3D シーンで変換マトリックスを使用してノードを正常に変換しました。この機能により、多様で視覚的に魅力的な 3D アプリケーションへの扉が開かれます。

## よくある質問

### Q1: 3D グラフィックスの変換行列とは何ですか?

A1: 変換マトリックスは、3D 空間内のオブジェクトにさまざまな変換 (移動、回転、スケーリング) を適用するために使用される数学的表現です。

### Q2: 単一のノードに複数の変換を適用できますか?

A2: はい、それぞれの行列を乗算し、その結果をノードに適用することで、複数の変換を組み合わせることができます。

### Q3: 3D シーンを保存するためにサポートされている他のファイル形式はありますか?

 A3: Aspose.3D for .NET は、STL、GLTF、OBJ などを含むさまざまなファイル形式をサポートしています。を参照してください。[ドキュメンテーション](https://reference.aspose.com/3d/net/)包括的なリストについては、

### Q4: Aspose.3D for .NET の一時ライセンスを取得するにはどうすればよいですか?

 A4: にアクセスしてください。[一時ライセンスのページ](https://purchase.aspose.com/temporary-license/) Aspose Web サイトにアクセスして、評価目的の一時ライセンスを取得します。

### Q5: どこでサポートを求めたり、Aspose.3D コミュニティに連絡したりできますか?

A5: にアクセスしてください。[Aspose.3D フォーラム](https://forum.aspose.com/c/3d/18) Aspose.3D を使用して、質問したり、経験を共有したり、他の開発者とつながったりできます。