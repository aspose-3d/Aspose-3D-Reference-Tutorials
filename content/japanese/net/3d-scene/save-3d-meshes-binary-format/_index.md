---
title: 3D メッシュをカスタム バイナリ形式で保存する
linktitle: 3D メッシュをカスタム バイナリ形式で保存する
second_title: Aspose.3D .NET API
description: Aspose.3D for .NET を使用して 3D の世界を探索してください。メッシュをカスタム バイナリ形式で保存する方法を学びます。
type: docs
weight: 13
url: /ja/net/3d-scene/save-3d-meshes-binary-format/
---
## 導入

Aspose.3D for .NET の世界へようこそ。これは、開発者が 3D ファイルを簡単に操作できるようにする強力なライブラリです。このチュートリアルでは、Aspose.3D for .NET を使用して 3D メッシュをカスタム バイナリ形式で保存するプロセスを詳しく説明します。このガイドは、C# の基本を理解しており、Aspose.3D ライブラリに精通していることを前提としています。

## 前提条件

チュートリアルに進む前に、次のものが整っていることを確認してください。

-  Aspose.3D for .NET: Aspose.3D ライブラリがインストールされていることを確認してください。からダウンロードできます[ここ](https://releases.aspose.com/3d/net/).

- 開発環境: Visual Studio など、好みの C# 開発環境をセットアップします。

- 入力 3D ファイル: カスタム バイナリ形式に変換する 3D ファイル (test.fbx など) を用意します。

## 名前空間のインポート

C# コードに、Aspose.3D 機能にアクセスするために必要な名前空間を含めます。

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
```

## ステップ 1: 3D ファイルをロードする

Aspose.3D を使用して 3D ファイルを読み込みます。この例では、「test.fbx」という名前のファイルをロードします。

```csharp
Scene scene = Scene.FromFile("test.fbx");
```

## ステップ 2: カスタム バイナリ形式を定義する

3D メッシュを保存するカスタム バイナリ形式の構造を定義します。この例では、コンポーネントとして MeshBlock、Vertex、Triangle を含む構造を使用します。

```csharp
//頂点のメモリ レイアウトは次のとおりです。
// float[3] 位置;
// float[3] 通常;
// float[3] uv;
var vertexDeclaration = new VertexDeclaration();
vertexDeclaration.AddField(VertexFieldDataType.FVector3, VertexFieldSemantic.Position);
vertexDeclaration.AddField(VertexFieldDataType.FVector3, VertexFieldSemantic.Normal);
vertexDeclaration.AddField(VertexFieldDataType.FVector3, VertexFieldSemantic.UV);

```

## ステップ 3: 書き込み用にファイルを開く

書き込み用にバイナリ ファイルを開きます。変換された 3D メッシュが保存されます。

```csharp
using (var writer = new BinaryWriter(new FileStream("Your Output Directory" + "Save3DMeshesInCustomBinaryFormat_out", FileMode.Create, FileAccess.Write)))
```

## ステップ 4: ノードとエンティティを反復処理する

3D シーンの各ノードにアクセスし、メッシュ エンティティをカスタム バイナリ形式に変換します。ライト、カメラ、その他の非メッシュ エンティティを無視します。

```csharp
scene.RootNode.Accept(delegate(Node node)
{
    foreach (Entity entity in node.Entities)
    {
        if (!(entity is IMeshConvertible))
            continue;
        // ... (処理を続行)
    }
    return true;
});
```

## ステップ 5: 制御点と三角形の変換と書き込み

メッシュ エンティティごとに、コントロール ポイントをワールド空間に変換し、三角形のインデックスとともにバイナリ ファイルに書き込みます。

```csharp
Mesh m = ((IMeshConvertible)entity).ToMesh();

var triMesh = TriMesh.FromMesh(vertexDeclaration, m);


//メッシュのメモリ レイアウトは次のとおりです。
// float[16] 変換行列;
// int 頂点数;
// int インデックス数;
//頂点[頂点数] 頂点;
// ushort[indices_count] インデックス;


//書き込み変換
var transform = node.GlobalTransform.TransformMatrix.ToArray();
for(int i = 0; i < transform.Length; i++)
    writer.Write((float)transform[i]);
//頂点/インデックスの数を書き込む
writer.Write(triMesh.VerticesCount);
writer.Write(triMesh.IndicesCount);
//頂点とインデックスを書き込む
writer.Flush();
triMesh.WriteVerticesTo(writer.BaseStream);
triMesh.Write16bIndicesTo(writer.BaseStream);

```

## 結論

このチュートリアルでは、Aspose.3D for .NET を使用して 3D メッシュをカスタム バイナリ形式で保存するプロセスについて説明しました。この強力なライブラリは、3D ファイルをシームレスに操作するために必要なツールを開発者に提供します。プロジェクトで Aspose.3D の可能性を最大限に引き出すために、さまざまな形式と設定を試してください。

## よくある質問

### Q1: Aspose.3D for .NET を他のプログラミング言語で使用できますか?

A1: Aspose.3D は主に .NET 言語をサポートしていますが、他の言語の互換性オプションを検討することもできます。

### Q2: 追加の例やリソースはどこで入手できますか?

 A2:[Aspose.3D フォーラム](https://forum.aspose.com/c/3d/18)は、サポートや事例を見つけ、コミュニティと交流するのに最適な場所です。

### Q3: Aspose.3D の試用版はありますか?

 A3: はい、以下から無料トライアルを利用できます。[ここ](https://releases.aspose.com/).

### Q4: Aspose.3D の一時ライセンスを取得するにはどうすればよいですか?

 A4: 訪問[このリンク](https://purchase.aspose.com/temporary-license/)テスト目的で一時ライセンスを取得します。

### Q5: Aspose.3D for .NET を購入できますか?

 A5: はい、Aspose.3D は次のサイトから購入できます。[購入ページ](https://purchase.aspose.com/buy).