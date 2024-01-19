---
title: 線形押し出しのツイスト オフセット
linktitle: 線形押し出しのツイスト オフセット
second_title: Aspose.3D .NET API
description: 線形押し出しのツイスト オフセットに関するステップバイステップ ガイドで、Aspose.3D for .NET の魅力を探ってください。 3D プロジェクトを簡単にレベルアップします。
type: docs
weight: 15
url: /ja/net/linear-extrusion/twist-offset-in-linear-extrusion/
---
## 導入

Aspose.3D for .NET の世界へようこそ。これは、開発者が 3D 操作を簡単に処理できるようにする多用途ライブラリです。このチュートリアルでは、興味深い機能の 1 つである「線形押し出しのツイスト オフセット」について詳しく説明します。 3D プログラミング スキルを向上させる準備ができている場合は、すぐに始めてみましょう。

## 前提条件

このエキサイティングな旅に乗り出す前に、次の前提条件が満たされていることを確認してください。

-  Aspose.3D for .NET ライブラリ: からライブラリをダウンロードしてインストールします。[リリースページ](https://releases.aspose.com/3d/net/).

- 開発環境: 開発環境がセットアップされ、展開できる状態になっていることを確認します。

## 名前空間のインポート

まず、Aspose.3D for .NET が提供する機能にアクセスするために必要な名前空間をインポートします。コードでは、これは次のようになります。

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

ここで、線形押し出しのツイスト オフセットをマスターするために、例を管理しやすい手順に分解してみましょう。

## ステップ 1: 基本プロファイルを初期化する

まず、基本プロファイルを作成します。ここでは、指定された丸み半径を持つ長方形の形状が例として挙げられます。

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## ステップ 2: シーンを作成する

ノードとシェイプをホストする 3D シーンを生成します。

```csharp
Scene scene = new Scene();
```

## ステップ 3: ノードの作成

シーン内の左右両方にノードを構築します。

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(18, 0, 0);
```

## ステップ 4: 左側のノードの線形押し出し

ツイストとスライスのプロパティを使用して、左側のノードで線形押し出しを実行します。

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100 });
```

## ステップ 5: ツイスト オフセットを使用した右ノードの線形押し出し

右側のノードで、ツイスト、ツイスト オフセット、スライス プロパティを使用して線形押し出しを実行します。

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100, TwistOffset = new Vector3(3, 0, 0) });
```

## ステップ 6: 3D シーンを保存する

ファイル形式を WavefrontOBJ として指定して、3D シーンを目的の出力ディレクトリに保存します。

```csharp
scene.Save("Your Output Directory" + "TwistOffsetInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

おめでとう！ Aspose.3D for .NET を使用して、線形押し出しでツイスト オフセットを正常に実装しました。

## 結論

このチュートリアルでは、特に線形押し出しのツイスト オフセットに焦点を当てて、Aspose.3D for .NET の強力な機能を検討しました。これらの新たに得たスキルを使えば、3D プロジェクトにダイナミズムを吹き込むための準備が整います。

## よくある質問

### Q1: Aspose.3D for .NET を他のプログラミング言語で使用できますか?

A1: Aspose.3D は主に .NET 言語をサポートしますが、Aspose は Java およびその他のプラットフォーム用に同様のライブラリを提供します。

### Q2: Aspose.3D for .NET の一時ライセンスを取得するにはどうすればよいですか?

 A2: 訪問[このリンク](https://purchase.aspose.com/temporary-license/)テスト目的で一時ライセンスを取得します。

### Q3: Aspose.3D for .NET のコミュニティ フォーラムはありますか?

A3：もちろんです！でコミュニティに参加してください[Aspose.3D フォーラム](https://forum.aspose.com/c/3d/18)他の開発者と交流し、支援を求めることができます。

### Q4: 追加の例やドキュメントはありますか?

A4: を探索してください。[ドキュメンテーション](https://reference.aspose.com/3d/net/)広範なガイドと例を参照してください。

### Q5: Aspose.3D for .NET はどこで購入できますか?

 A5: に向かいます[このリンク](https://purchase.aspose.com/buy)購入して、Aspose.3D の可能性を最大限に引き出してください。