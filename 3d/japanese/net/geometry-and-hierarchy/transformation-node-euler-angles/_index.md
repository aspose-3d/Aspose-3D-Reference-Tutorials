---
title: オイラー角によるノードの変換
linktitle: オイラー角によるノードの変換
second_title: Aspose.3D .NET API
description: Aspose.3D for .NET を使用して 3D ノードを簡単に変換する方法を学びます。プロジェクトで素晴らしい結果を得るには、ステップバイステップのガイドに従ってください。
weight: 19
url: /ja/net/geometry-and-hierarchy/transformation-node-euler-angles/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# オイラー角によるノードの変換

## 導入

Aspose.3D for .NET を使用して 3D シーンでオイラー角によるノードの変換に関するこの包括的なチュートリアルへようこそ。このガイドでは、3D グラフィックスのエキサイティングな世界を深く掘り下げ、オイラー角を使用してノードに変換を追加するプロセスについて説明します。 Aspose.3D for .NET は、3D シーンとメッシュを操作するための強力なツールを提供しており、プロジェクトの多用途性と効率性を求める開発者にとって優れた選択肢となっています。

## 前提条件

チュートリアルに入る前に、次の前提条件が満たされていることを確認してください。

-  Aspose.3D for .NET ライブラリ: Aspose.3D ライブラリがインストールされていることを確認します。ダウンロードできます[ここ](https://releases.aspose.com/3d/net/).

- 開発環境: Visual Studio など、好みの .NET 開発環境をセットアップします。

## 名前空間のインポート

まず、Aspose.3D for .NET が提供する機能にアクセスするために必要な名前空間をインポートします。

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

ここで、明確に理解できるように、例を複数のステップに分けてみましょう。

## ステップ 1: シーン オブジェクトを初期化する

```csharp
//ExStart:AddTransformationToNodeByEulerAngles
//シーンオブジェクトを初期化する
Scene scene = new Scene();
```

まず、を使用して新しい 3D シーンを作成します。`Scene`クラス。


## ステップ 2: プリミティブ ボックスを使用してメッシュを作成する

```csharp
//ポリゴン ビルダー メソッドを使用して共通クラスのメッシュ作成を呼び出し、メッシュ インスタンスを設定します
Mesh mesh = (new Box()).ToMesh();
```

メソッドを呼び出します (この場合、`CreateMeshUsingPolygonBuilder`習慣から`Common`クラス) を使用して 3D オブジェクトのメッシュを生成します。

## ステップ 3: メッシュのコンテナ ノードを作成する

```csharp
//ノードをメッシュ ジオメトリにポイントします
Node cubeNode = scene.RootNode.CreateChildNode(mesh);
```

を使用してシーン内にノードを作成します。`Node`クラス。このノードは 3D オブジェクトのコンテナとして機能します。

## ステップ 4: オイラー角と平行移動を設定する

```csharp
//オイラー角
cubeNode.Transform.EulerAngles = new Vector3(0.3, 0.1, -0.5);            
//翻訳を設定する
cubeNode.Transform.Translation = new Vector3(0, 0, 20);
```

ノードのオイラー角と移動を定義して、ノードを 3D 空間に配置します。

## ステップ 5: 3D シーンを保存する

```csharp
//ドキュメントディレクトリへのパス。
var output = "TransformationToNode.fbx";

//3D シーンをサポートされているファイル形式で保存する
scene.Save(output);
//ExEnd:AddTransformationToNodeByEulerAngles
Console.WriteLine("\nTransformation added successfully to node.\nFile saved at " + output);
```

出力ディレクトリを指定し、変換されたノードを含む 3D シーンを目的のファイル形式 (この場合は FBX7500ASCII) で保存します。

## 結論

おめでとう！ Aspose.3D for .NET を使用して 3D シーンでオイラー角によってノードを変換する方法を学習しました。この強力なライブラリは、3D グラフィックス開発における無限の可能性への扉を開きます。

## よくある質問

### Q1: Aspose.3D は他の 3D モデリング ツールと互換性がありますか?

A1: Aspose.3D はさまざまな 3D ファイル形式をサポートしており、一般的なモデリング ツールとの互換性が強化されています。

### Q2: 単一のノードに複数の変換を適用できますか?

A2: はい、複数の変換を組み合わせて適用して、複雑な効果を実現できます。

### Q3: 追加の Aspose.3D ドキュメントはどこで見つけられますか?

 A3: を参照してください。[ドキュメンテーション](https://reference.aspose.com/3d/net/)詳細な情報と例については、

### Q4: Aspose.3D for .NET を使用するにはライセンスが必要ですか?

 A4: はい、ライセンスを取得できます。[ここ](https://purchase.aspose.com/buy)または、[無料トライアル](https://releases.aspose.com/).

### Q5: サポートが必要ですか、それとも具体的な質問がありますか?

 A5: にアクセスしてください。[Aspose.3D フォーラム](https://forum.aspose.com/c/3d/18)コミュニティサポートのために。
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
