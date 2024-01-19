---
title: 3D シーンでのクォータニオンによるノードの変換
linktitle: 3D シーンでのクォータニオンによるノードの変換
second_title: Aspose.3D .NET API
description: Aspose.3D for .NET を使用して、クォータニオンを使用して 3D ノードを変換する方法を学びます。初心者向けのステップバイステップガイド。
type: docs
weight: 20
url: /ja/net/geometry-and-hierarchy/transformation-node-quaternion/
---
## 導入

Aspose.3D for .NET を使用して 3D シーンでクォータニオンによるノードの変換に関するステップバイステップ ガイドへようこそ。このチュートリアルでは、Aspose.3D for .NET の強力な機能を調べ、クォータニオンを使用して 3D ノードに変換を追加するプロセスを順を追って説明します。

## 前提条件

チュートリアルに入る前に、次の前提条件が満たされていることを確認してください。

-  Aspose.3D for .NET: Aspose.3D ライブラリがインストールされていることを確認してください。からダウンロードできます。[リリースページ](https://releases.aspose.com/3d/net/).

- 開発環境: 必要なツールと構成を使用して .NET 開発環境をセットアップします。

- 3D 概念の基本的な理解: 3D グラフィックスと概念に精通していると役に立ちます。

## 名前空間のインポート

.NET プロジェクトに、Aspose.3D に必要な名前空間を含めます。

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

## ステップ 1: シーン オブジェクトを初期化する

```csharp
// ExStart:AddTransformationToNodeByQuaternion
//シーンオブジェクトを初期化する
Scene scene = new Scene();
```

## ステップ 2: ノード クラス オブジェクトを初期化する

```csharp
//Nodeクラスオブジェクトの初期化
Node cubeNode = new Node("cube");
```

## ステップ 3: ポリゴン ビルダーを使用してメッシュを作成する

```csharp
//ポリゴン ビルダー メソッドを使用して共通クラスのメッシュ作成を呼び出し、メッシュ インスタンスを設定します
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
```

## ステップ 4: ノードをメッシュ ジオメトリにポイントする

```csharp
//ノードをメッシュ ジオメトリにポイントします
cubeNode.Entity = mesh;
```

## ステップ 5: クォータニオンを使用して回転を設定する

```csharp
//回転を設定する
cubeNode.Transform.Rotation = Quaternion.FromRotation(new Vector3(0, 1, 0), new Vector3(0.3, 0.5, 0.1));            
```

## ステップ 6: 翻訳を設定する

```csharp
//翻訳を設定する
cubeNode.Transform.Translation = new Vector3(0, 0, 20);            
```

## ステップ 7: キューブをシーンに追加する

```csharp
//シーンにキューブを追加する
scene.RootNode.ChildNodes.Add(cubeNode);
```

## ステップ 8: 3D シーンを保存する

```csharp
//ドキュメントディレクトリへのパス。
var output = "Your Output Directory" + "TransformationToNode.fbx";

//3D シーンをサポートされているファイル形式で保存する
scene.Save(output, FileFormat.FBX7500ASCII);
//ExEnd:AddTransformationToNodeByQuaternion
Console.WriteLine("\nTransformation added successfully to node.\nFile saved at " + output);
```

## 結論

おめでとう！ Aspose.3D for .NET を使用して 3D シーンでクォータニオンによってノードを変換する方法を学習しました。を参照して、さらに多くの機能と可能性を探ってください。[ドキュメンテーション](https://reference.aspose.com/3d/net/).

## よくある質問

### Q1: 3D グラフィックスのクォータニオンとは何ですか?

A1: クォータニオンは、3D 空間での回転を表すために使用される数学的エンティティです。

### Q2: Aspose.3D for .NET をダウンロードするにはどうすればよいですか?

 A2: ライブラリは以下からダウンロードできます。[リリースページ](https://releases.aspose.com/3d/net/).

### Q3: Aspose.3D for .NET の無料トライアルはありますか?

 A3: はい、以下から無料トライアルを利用できます。[ここ](https://releases.aspose.com/).

### Q4: Aspose.3D for .NET のサポートはどこで見つけられますか?

 A4: にアクセスしてください。[Aspose.3D フォーラム](https://forum.aspose.com/c/3d/18)サポートとディスカッションのため。

### Q5: Aspose.3D の一時ライセンスを取得するにはどうすればよいですか?

 A5: 仮免許を取得する[ここ](https://purchase.aspose.com/temporary-license/).
