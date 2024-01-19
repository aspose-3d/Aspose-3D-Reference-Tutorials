---
title: 線形押出の中心
linktitle: 線形押出の中心
second_title: Aspose.3D .NET API
description: Aspose.3D for .NET を使用して 3D モデリングの世界を探索してください。直線押し出し技術を中心に据えて、見事なデザインを作成し、創造性を解き放ちます。
type: docs
weight: 10
url: /ja/net/linear-extrusion/center-in-linear-extrusion/
---
## 導入

Aspose.3D for .NET を使用して線形押し出しをマスターするためのこの包括的なガイドへようこそ。 3D モデリングのスキルを向上させ、見事な押し出しを作成したい場合は、ここが正しい場所です。このチュートリアルでは、線形押し出し技術を詳しく掘り下げ、特にセンタリングの側面に焦点を当てて、デザインをまったく新しいレベルに引き上げます。

## 前提条件

このエキサイティングな旅に乗り出す前に、次の前提条件が満たされていることを確認してください。

- C# プログラミング言語の基本的な理解。
- Visual Studio がマシンにインストールされていること。
-  Aspose.3D for .NET ライブラリ。[Aspose.3D .NET ドキュメント](https://reference.aspose.com/3d/net/).
- にアクセスできることを確認してください[Aspose.3D .NET ドキュメント](https://reference.aspose.com/3d/net/)チュートリアル全体を通して参照してください。

## 名前空間のインポート

まず始めに、必要な名前空間をインポートしましょう。これらは、3D モデリングの傑作の基礎となります。

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## ステップ 1: 基本プロファイルを初期化する

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## ステップ 2: 3D シーンを作成する

```csharp
Scene scene = new Scene();
```

## ステップ 3: 左右のノードを作成する

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(5, 0, 0);
```

## ステップ 4: 左側のノードで線形押し出しを実行する

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 2) { Center = false, Slices = 3 });
```

## ステップ 5: 基準となるグランドプレーンを設定する

```csharp
left.CreateChildNode(new Box(0.01, 3, 3));
```

## ステップ 6: 右側のノードで線形押し出しを実行する

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 2) { Center = true, Slices = 3 });
```

## ステップ 7: 基準となるグランド プレーンを設定する (右側のノード)

```csharp
right.CreateChildNode(new Box(0.01, 3, 3));
```

## ステップ 8: 3D シーンを保存する

```csharp
scene.Save("Your Output Directory" + "CenterInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## 結論

おめでとう！ Aspose.3D for .NET を使用して、センタリングを伴う線形押し出しの技術を習得しました。さまざまなパラメータを自由に試して、この手法がもたらす広大な可能性を探求してください。

## よくある質問

### Q1: Aspose.3D for .NET を他のプログラミング言語で使用できますか?

A1: Aspose.3D は主に、C# や VB.NET などの .NET 言語をサポートしています。

### Q2: Aspose.3D 関連のクエリのサポートはどこで見つけられますか?

 A2: にアクセスしてください。[Aspose.3D フォーラム](https://forum.aspose.com/c/3d/18)献身的なサポートとディスカッションのために。

### Q3: Aspose.3D for .NET の無料トライアルはありますか?

 A3: はい、無料トライアルにアクセスできます。[ここ](https://releases.aspose.com/).

### Q4: Aspose.3D for .NET の一時ライセンスを取得するにはどうすればよいですか?

 A4: 仮免許を取得できます。[ここ](https://purchase.aspose.com/temporary-license/).

### Q5: Aspose.3D for .NET ライセンスはどこで購入できますか?

 A5: ライセンスを購入する[ここ](https://purchase.aspose.com/buy).
