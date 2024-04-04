---
title: メッシュ ジオメトリ データの操作
linktitle: メッシュ ジオメトリ データの操作
second_title: Aspose.3D .NET API
description: Aspose.3D for .NET を使用して 3D グラフィックス プログラミングの技術をマスターしましょう。見事な 3D シーンを簡単に作成、操作、保存できます。
type: docs
weight: 15
url: /ja/net/geometry-and-hierarchy/mesh-geometry-data/
---
## 導入

Aspose.3D for .NET を使用した 3D グラフィックス プログラミングのエキサイティングな世界へようこそ!このチュートリアルでは、.NET 開発者向けの強力で多用途なライブラリである Aspose.3D を使用して、3D シーンでメッシュ ジオメトリ データを操作する複雑な作業について詳しく説明します。経験豊富なプログラマであっても、3D グラフィックスを始めたばかりであっても、このステップバイステップのガイドは、メッシュ ジオメトリ データを簡単に処理する技術を習得するのに役立ちます。

## 前提条件

この 3D の旅に着手する前に、次の前提条件が満たされていることを確認してください。

- C# および .NET プログラミングに関する実践的な知識。
- Visual Studio がマシンにインストールされていること。
- Aspose.3D for .NET ライブラリ (ダウンロード可能)[ここ](https://releases.aspose.com/3d/net/).

これで準備は完了です。3D グラフィックス プログラミングの魅力的な世界に飛び込みましょう。

## 名前空間のインポート

C# プロジェクトで、必要な名前空間をインポートすることから始めます。

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using Aspose.ThreeD.Shading;
```

これらの名前空間は、3D シーンとメッシュ ジオメトリ データを操作するために必要な必須のクラスとメソッドへのアクセスを提供します。

## ステップ 1: シーンを初期化する

```csharp
//シーンオブジェクトを初期化する
Scene scene = new Scene();
```

これにより、3D モデルを構築および操作できる空の 3D シーンが作成されます。

## ステップ 2: カラー ベクトルを定義する

```csharp
//カラーベクトルを定義する
Vector3[] colors = new Vector3[] {
    new Vector3(1, 0, 0),
    new Vector3(0, 1, 0),
    new Vector3(0, 0, 1)
};
```

3D シーンのさまざまな部分に適用されるカラー ベクトルの配列を指定します。

## ステップ 3: メッシュの作成と色の設定

```csharp
//ポリゴン ビルダー メソッドを使用して共通クラスのメッシュ作成を呼び出し、メッシュ インスタンスを設定します
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();

int idx = 0;
foreach (Vector3 color in colors)
{
    //キューブノードオブジェクトの初期化
    Node cube = new Node("cube");
    cube.Entity = mesh;
    LambertMaterial mat = new LambertMaterial();
    
    //色を設定する
    mat.DiffuseColor = color;
    
    //セット素材
    cube.Material = mat;
    
    //翻訳を設定する
    cube.Transform.Translation = new Vector3(idx++ * 20, 0, 0);
    
    //キューブノードの追加
    scene.RootNode.ChildNodes.Add(cube);
}
```

ポリゴン ビルダー メソッドを使用してメッシュを作成し、シーンのさまざまな部分に色を適用します。

## ステップ 4: 3D シーンを保存する

```csharp
//ドキュメントディレクトリへのパス。
var output = "Your Output Directory" + "MeshGeometryData.fbx";

//3D シーンをサポートされているファイル形式で保存する
scene.Save(output, FileFormat.FBX7400ASCII);
```

出力ディレクトリを指定し、3D シーンを FBX7400ASCII ファイル形式で保存します。

## 結論

おめでとう！ Aspose.3D for .NET を使用して 3D シーンでメッシュ ジオメトリ データを操作する方法を学習しました。このチュートリアルでは、3D モデルを作成および操作するための重要な手順を説明しました。実験、探索し、3D グラフィックス プログラミング スキルを新たな高みに引き上げましょう。

## よくある質問

### Q1: Aspose.3D for .NET を他のプログラミング言語で使用できますか?

A1: Aspose.3D は主に .NET 用に設計されていますが、さまざまなプラットフォームや言語をサポートする他の Aspose 製品を検討することもできます。

### Q2: Aspose.3D の無料トライアルはありますか?

 A2: はい、無料トライアルにアクセスできます。[ここ](https://releases.aspose.com/).

### Q3: 追加のサポートやリソースはどこで入手できますか?

 A3: にアクセスしてください。[Aspose.3D フォーラム](https://forum.aspose.com/c/3d/18)コミュニティのサポートとディスカッションのために。

### Q4: Aspose.3D の一時ライセンスを取得するにはどうすればよいですか?

 A4: 仮免許を取得できます。[ここ](https://purchase.aspose.com/temporary-license/).

### Q5: 3D シーンの保存にはどのようなファイル形式がサポートされていますか?

 A5: Aspose.3D は、FBX、STL などを含むさまざまなファイル形式をサポートしています。を参照してください。[ドキュメンテーション](https://reference.aspose.com/3d/net/)完全なリストについては、