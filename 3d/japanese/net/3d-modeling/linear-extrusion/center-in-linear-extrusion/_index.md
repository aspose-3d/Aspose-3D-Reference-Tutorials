---
date: 2026-01-07
description: Aspose.3D for .NET を使用して線形押し出しを行いながら、グラウンドプレーンの追加方法と Wavefront OBJ ファイルのエクスポート方法を学びましょう。3‑D
  モデリングにおけるセンタリングとグラウンド設定のテクニックをマスターしてください。
linktitle: Add Ground Plane and Center in Linear Extrusion
second_title: Aspose.3D .NET API
title: 線形押し出しで基準平面と中心を追加
url: /ja/net/3d-modeling/linear-extrusion/center-in-linear-extrusion/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 線形押し出しでのグラウンドプレーンとセンタリングの追加

## はじめに

Aspose.3D for .NET を使用した線形押し出しのマスターガイドへようこそ。モデルに **グラウンドプレーンを追加**し、**Wavefront OBJ** ファイルとしてエクスポートしながら、押し出しをセンタリングしたい方に最適です。このチュートリアルでは、線形押し出しのテクニックに焦点を当て、特にセンタリングの方法と、グラウンドプレーンが結果の可視化にどのように役立つかを解説します。

## クイック回答
- **「グラウンドプレーンを追加」すると何が得られますか？** X‑Z 平面上で押し出しがどこに位置しているかを視覚的に確認できる基準が得られます。  
- **モデルのエクスポートに使用する形式は？** シーンは Wavefront OBJ ファイル (`FileFormat.WavefrontOBJ`) として保存されます。  
- **コード実行にライセンスは必要ですか？** 開発段階は無料トライアルで動作しますが、本番環境では永続ライセンスが必要です。  
- **押し出しの長さは変更できますか？** はい – `LinearExtrusion` の第2パラメータを変更してください。  
- **センタリングはオプションですか？** `Center = true` に設定するとプロファイルの中心に押し出しが配置され、`false` にすると片側に寄ります。

## 前提条件

このエキサイティングな旅に出る前に、以下の前提条件が整っていることを確認してください。

- C# プログラミング言語の基本的な理解。  
- Visual Studio がインストールされていること。  
- Aspose.3D for .NET ライブラリ（[Aspose.3D .NET ドキュメント](https://reference.aspose.com/3d/net/) からダウンロード可能）。  
- チュートリアル全体で参照できるよう、[Aspose.3D .NET ドキュメント](https://reference.aspose.com/3d/net/) へアクセスできること。

## 名前空間のインポート

まずは必要な名前空間をインポートしましょう。これが 3D モデリングの土台となります。

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## 手順 1: 基本プロファイルの初期化

押し出す矩形プロファイルを定義します。`RoundingRadius` は角にさりげないフィレットを付加します。

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## 手順 2: 3D シーンの作成

`Scene` オブジェクトは、すべてのジオメトリ、ライト、カメラのコンテナとして機能します。

```csharp
Scene scene = new Scene();
```

## 手順 3: 左右ノードの作成

ルートの下に 2 つの兄弟ノードを作成します。左側は **センタリングなし**、右側は **センタリングあり** の押し出しをデモします。また、左ノードは重ならないように平行移動します。

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(5, 0, 0);
```

## 手順 4: 左ノードでの線形押し出し（センタリングなし）

ここではセンタリングせずにプロファイルを押し出します。`Center = false` フラグに注目してください。

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 2) { Center = false, Slices = 3 });
```

## 手順 5: 参照用グラウンドプレーンの追加（左ノード）

薄いボックスを追加して **グラウンドプレーン** とし、押し出しがベース上にどのように配置されているかを明確にします。

```csharp
left.CreateChildNode(new Box(0.01, 3, 3));
```

## 手順 6: 右ノードでの線形押し出し（センタリングあり）

同じプロファイルを使用しますが、今回はセンタリングを有効にします。ジオメトリはプロファイルの原点を中心に対称的に配置されます。

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 2) { Center = true, Slices = 3 });
```

## 手順 7: 参照用グラウンドプレーンの追加（右ノード）

右ノードにも 2 番目のグラウンドプレーンを追加し、視覚的比較を一貫させます。

```csharp
right.CreateChildNode(new Box(0.01, 3, 3));
```

## 手順 8: Wavefront OBJ ファイルのエクスポート

最後に **Wavefront OBJ** としてエクスポートし、任意の標準 3‑D ビューアで結果を開けるようにします。

```csharp
scene.Save("Your Output Directory" + "CenterInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## なぜグラウンドプレーンを追加するのか？

グラウンドプレーンを追加すると、押し出しの高さと配置に関する即時の視覚的手がかりが得られます。センタリング済みと未センタリングの結果を比較する際に特に有用です。

## よくある問題とヒント

- **グラウンドプレーンが表示されない場合:** `Box` コンストラクタの厚さ (`0.01`) が押し出しを隠さない程度に小さく、かつ描画可能な大きさであることを確認してください。  
- **エクスポートが失敗する場合:** 出力ディレクトリが存在し、書き込み権限があるか確認してください。  
- **センタリングされた押し出しがずれて見える場合:** `Center` プロパティを再確認してください。`true` がプロファイルを中心に、`false` が片側に寄せます。

## FAQ（よくある質問）

### Q1: Aspose.3D for .NET を他のプログラミング言語で使用できますか？

A1: Aspose.3D は主に C# や VB.NET などの .NET 言語をサポートしています。

### Q2: Aspose.3D に関するサポートはどこで受けられますか？

A2: 専用サポートとディスカッションは [Aspose.3D フォーラム](https://forum.aspose.com/c/3d/18) をご利用ください。

### Q3: Aspose.3D for .NET の無料トライアルはありますか？

A3: はい、無料トライアルは [こちら](https://releases.aspose.com/) から入手できます。

### Q4: Aspose.3D for .NET の一時ライセンスはどこで取得できますか？

A4: 一時ライセンスは [こちら](https://purchase.aspose.com/temporary-license/) から取得できます。

### Q5: Aspose.3D for .NET の正式ライセンスはどこで購入できますか？

A5: 正式ライセンスは [こちら](https://purchase.aspose.com/buy) で購入してください。

### Q6: OBJ 以外の形式でシーンをエクスポートできますか？

A6: はい、Aspose.3D は STL、FBX、GLTF など多数の形式をサポートしています。`Save` メソッドの `FileFormat` 列挙値を変更するだけです。

### Q7: 押し出しのスライス数はどう変更しますか？

A7: `LinearExtrusion` コンストラクタの `Slices` プロパティを調整してメッシュ密度を制御できます。

---

**最終更新日:** 2026-01-07  
**テスト環境:** Aspose.3D for .NET 最新バージョン  
**作成者:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}