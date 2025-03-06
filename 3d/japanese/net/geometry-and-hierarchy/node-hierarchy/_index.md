---
title: ノード階層を理解する
linktitle: ノード階層を理解する
second_title: Aspose.3D .NET API
description: Aspose.3D for .NET のパワーを解放してください!このステップバイステップのガイドを使用して、ノード階層の操作について詳しく説明します。見事な 3D シーンを簡単に作成できます。
weight: 16
url: /ja/net/geometry-and-hierarchy/node-hierarchy/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# ノード階層を理解する

## 導入

Aspose.3D for .NET の世界へようこそ。これは、開発者が .NET アプリケーションで 3D シーンやモデルをシームレスに操作できるようにする強力なライブラリです。このチュートリアルでは、Aspose.3D を使用して 3D シーンのノード階層を理解する際の複雑さを掘り下げていきます。このガイドを読み終えるまでに、ノードを通じて 3D シーンの構造を操作する方法をしっかりと理解し、素晴らしい視覚体験を作成できるようになります。

## 前提条件

この 3D の旅に着手する前に、次の前提条件が満たされていることを確認してください。

-  Aspose.3D for .NET ライブラリ: Aspose.3D ライブラリが .NET プロジェクトに統合されていることを確認します。まだこれを行っていない場合は、次のページに進んでください。[ドキュメンテーション](https://reference.aspose.com/3d/net/)指導のために。

- ライブラリをダウンロードする: Aspose.3D ライブラリをダウンロードしていない場合は、次の場所から最新バージョンを取得します。[ダウンロードリンク](https://releases.aspose.com/3d/net/)ドキュメントに記載されているインストール手順に従ってください。

- ライセンスの取得: Aspose.3D の可能性を最大限に引き出すには、有効なライセンスが必要です。お持ちでない場合は入手できます[ここ](https://purchase.aspose.com/buy)または、[無料トライアル](https://releases.aspose.com/)その機能を探るために。

- サポートとコミュニティ: Aspose.3D コミュニティに参加してください。[サポートフォーラム](https://forum.aspose.com/c/3d/18)他の開発者とつながり、助けを求め、最新の開発情報を入手できます。

- 一時ライセンス (オプション): 購入前に Aspose.3D を検討している場合は、ライセンスの取得を検討してください。[仮免許](https://purchase.aspose.com/temporary-license/)拡張アクセス用。

ツールの準備ができたので、Aspose.3D を使用した 3D ノード階層操作のエキサイティングな世界に飛び込んでみましょう。

## 名前空間のインポート

.NET プロジェクトでは、Aspose.3D が提供する機能を利用するために必要な名前空間をインポートしていることを確認してください。コードに次の行を追加します。

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

これらの名前空間を使用すると、3D シーンを操作するための重要なクラスとメソッドにアクセスできます。

## ステップ 1: シーン オブジェクトを初期化する

```csharp
Scene scene = new Scene();
```

まず、次のコマンドを使用して新しい 3D シーンを作成します。`Scene`クラス。

## ステップ 2: 子ノードを作成する

```csharp
Node top = scene.RootNode.CreateChildNode();
Node cube1 = top.CreateChildNode("cube1");
Node cube2 = top.CreateChildNode("cube2");
```

ノード間に親子関係を作成して階層構造を確立します。この例では、`cube1`そして`cube2`の子ノードです`top`ノード。

## ステップ 3: メッシュの作成と割り当て

```csharp
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
cube1.Entity = mesh;
cube2.Entity = mesh;
```

適切な方法を使用してメッシュを生成します (ここでは、`CreateMeshUsingPolygonBuilder`) を子ノードに割り当てます。

## ステップ 4: 翻訳を設定する

```csharp
cube1.Transform.Translation = new Vector3(-10, 0, 0);
cube2.Transform.Translation = new Vector3(10, 0, 0);
```

各キューブ ノードの変換を定義し、3D 空間に配置します。

## ステップ 5: 親ノードに回転を適用する

```csharp
top.Transform.Rotation = Quaternion.FromEulerAngle(Math.PI, 4, 0);
```

親ノードを回転します (`top`)、この変換がすべての子ノードにどのような影響を与えるかを観察します。

## ステップ 6: 3D シーンを保存する

```csharp
string output = "Your Output Directory" + "NodeHierarchy.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

出力ディレクトリを指定し、3D シーンを希望のファイル形式 (ここでは FBX7500ASCII) で保存します。

## ステップ 7: 成功メッセージを表示する

```csharp
Console.WriteLine("\nNode hierarchy added successfully to document.\nFile saved at " + output);
```

ノード階層の追加が成功したことと保存されたファイルの場所をユーザーに通知します。

## 結論

おめでとう！ Aspose.3D for .NET の 3D ノード階層の複雑な世界を無事にナビゲートできました。このチュートリアルでは、3D シーンを簡単に作成、操作、保存するための知識を習得しました。旅を続けながら、さらに多くの機能を探索し、.NET プロジェクトで Aspose.3D の可能性を最大限に引き出してください。

## よくある質問

### Q1: ライセンスなしで Aspose.3D for .NET を使用できますか?

A1: ライセンスによりすべての機能のロックが解除されますが、無料トライアルを使用すると、限られた機能で Aspose.3D を探索できます。

### Q2: 3D シーンを保存するためにサポートされている他のファイル形式はありますか?

A2: はい、Aspose.3D はさまざまな形式をサポートしています。包括的なリストについては、ドキュメントを参照してください。

### Q3: Aspose.3D コミュニティに貢献するにはどうすればよいですか?

A3: サポート フォーラムに参加し、経験を共有し、他の人の質問を支援することで貢献してください。

### Q4: Aspose.3D はゲーム開発に適していますか?

A4：もちろんです！ Aspose.3D は多用途であり、ゲーム開発プロジェクトに統合できます。

### Q5: 一時ライセンスと完全ライセンスの違いは何ですか?

A5: 一時ライセンスでは評価目的での短期間のアクセスが提供されますが、完全ライセンスでは無制限の使用が提供されます。
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
