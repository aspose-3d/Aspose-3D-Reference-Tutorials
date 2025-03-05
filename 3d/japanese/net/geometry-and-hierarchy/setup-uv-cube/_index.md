---
title: Cube に UV を設定する
linktitle: Cube に UV を設定する
second_title: Aspose.3D .NET API
description: Aspose.3D for .NET を使用して 3D キューブに UV マッピングを設定する方法を学びます。正確なテクスチャ マッピングを使用して、視覚的に素晴らしいシーンを作成します。
type: docs
weight: 18
url: /ja/net/geometry-and-hierarchy/setup-uv-cube/
---
## 導入

魅力的で視覚的に魅力的な 3D シーンを作成するには、多くの場合、幾何学的形状に UV マッピングを設定するという綿密なプロセスが必要になります。このチュートリアルでは、Aspose.3D for .NET を使用して立方体に UV を設定する方法を検討します。 Aspose.3D は、3D モデリングと操作のための包括的な機能セットを提供する強力な .NET ライブラリです。

## 前提条件

チュートリアルに入る前に、次の前提条件を満たしていることを確認してください。

1. Aspose.3D for .NET ライブラリ: Aspose.3D ライブラリがインストールされていることを確認します。ダウンロードできます[ここ](https://releases.aspose.com/3d/net/).

2. 開発環境: 必要なツールを使用して .NET 開発環境をセットアップします。

それでは、チュートリアルに進みましょう。

## 名前空間のインポート

まず、.NET アプリケーションの Aspose.3D 機能にアクセスするために必要な名前空間をインポートします。

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

## ステップ 1: キューブの UV を定義する

立方体の各頂点の UV 座標を定義します。これには、立方体の各隅の U 値と V 値を指定することが含まれます。

```csharp
// ExStart:UV の定義
Vector4[] uvs = new Vector4[]
{
    new Vector4(0.0, 1.0, 0.0, 1.0),
    new Vector4(1.0, 0.0, 0.0, 1.0),
    new Vector4(0.0, 0.0, 0.0, 1.0),
    new Vector4(1.0, 1.0, 0.0, 1.0)
};
//ExEnd:UV の定義
```

## ステップ 2: UV インデックスを定義する

立方体の各ポリゴンの UV 座標のインデックスを指定します。これは、UV が立方体のサーフェスにどのようにマッピングされるかを定義します。

```csharp
// ExStart:UVIndices の定義
int[] uvsId = new int[]
{
    0, 1, 3, 2, 2, 3, 5, 4, 4, 5, 7, 6, 6, 7, 9, 8, 1, 10, 11, 3, 12, 0, 2, 13
};
//ExEnd:UVIndices の定義
```

## ステップ 3: メッシュを作成する

Aspose.3D ライブラリを利用して、ポリゴン ビルダー メソッドを使用してメッシュを作成します。これは 3D キューブの基礎として機能します。

```csharp
// ExStart:メッシュの作成
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
//ExEnd:メッシュの作成
```

## ステップ 4: UV 要素を作成する

メッシュ内に UV 要素を作成して、UV マッピング データを保存します。

```csharp
// ExStart:UVElement の作成
VertexElementUV elementUV = mesh.CreateElementUV(TextureMapping.Diffuse, MappingMode.PolygonVertex, ReferenceMode.IndexToDirect);
//ExEnd:UVElement の作成
```

## ステップ 5: UV データをメッシュにコピーする

以前に定義した UV 座標とインデックスをメッシュの UV 頂点要素にコピーします。

```csharp
// ExStart:UVData のコピー
elementUV.Data.AddRange(uvs);
elementUV.Indices.AddRange(uvsId);
//ExEnd:CopyUVData
```

## 結論

おめでとう！ Aspose.3D for .NET を使用してキューブに UV マッピングをセットアップすることに成功しました。これにより、正確なテクスチャ マッピングを使用して、複雑で視覚的に素晴らしい 3D シーンを作成する可能性が広がります。

## よくある質問

### Q1: Aspose.3D for .NET とは何ですか?

A1: Aspose.3D for .NET は、.NET アプリケーションでの 3D モデリングと操作のための強力なライブラリです。

### Q2: Aspose.3D ドキュメントはどこで見つけられますか?

 A2: ドキュメントは入手可能です[ここ](https://reference.aspose.com/3d/net/).

### Q3: 無料トライアルはありますか?

 A3: はい、無料トライアルにアクセスできます。[ここ](https://releases.aspose.com/).

### Q4: Aspose.3D のサポートを受けるにはどうすればよいですか?

 A4: サポート フォーラムにアクセスしてください。[ここ](https://forum.aspose.com/c/3d/18).

### Q5: 一時ライセンスは利用できますか?

 A5: はい、一時ライセンスを取得できます。[ここ](https://purchase.aspose.com/temporary-license/).