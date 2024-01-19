---
title: ロードと保存 - 非 PBR から PBR マテリアルへの変換
linktitle: ロードと保存 - 非 PBR から PBR マテリアルへの変換
second_title: Aspose.3D .NET API
description: Aspose.3D for .NET を探索する - 非 PBR マテリアルを PBR マテリアルに簡単に変換します。包括的なチュートリアルと強力な API。
type: docs
weight: 16
url: /ja/net/loading-and-saving/non-pbr-to-pbr-material-conversion/
---
## 導入

Aspose.3D for .NET を使用して非 PBR (物理ベース レンダリング) を PBR マテリアルに変換するためのこのステップバイステップ ガイドへようこそ。 Aspose.3D は、開発者が .NET アプリケーションで 3D ファイル形式をシームレスに操作できるようにする強力な API です。

## 前提条件

チュートリアルに入る前に、次の前提条件を満たしていることを確認してください。

-  Aspose.3D for .NET: Aspose.3D for .NET ライブラリがインストールされていることを確認してください。ダウンロードリンクが見つかります[ここ](https://releases.aspose.com/3d/net/).

- C# の基本的な理解: このチュートリアルは、C# プログラミングの基本を理解していることを前提としています。

- IDE (統合開発環境): Visual Studio などの .NET 開発用の優先 IDE を選択します。

## 名前空間のインポート

C# コードで、必要な名前空間をインポートすることから始めます。

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
```

## ステップ 1: 新しい 3D シーンを初期化する

まず、次のコードを使用して新しい 3D シーンを作成します。

```csharp
// ExStart:Non_PBRtoPBRマテリアル
//新しい 3D シーンを初期化する
var scene = new Scene();
```

## ステップ 2: 3D オブジェクトを作成する

次に、3D オブジェクト (ボックスなど) を作成します。

```csharp
var box = new Box();
scene.RootNode.CreateChildNode("box1", box).Material = new PhongMaterial() { DiffuseColor = new Vector3(1, 0, 1) };
```

## ステップ 3: マテリアル変換を構成する

非 PBR から PBR への変換のためのマテリアル変換オプションを設定します。

```csharp
GltfSaveOptions options = new GltfSaveOptions(FileFormat.GLTF2);
options.MaterialConverter = delegate (Material material)
{
    PhongMaterial phongMaterial = (PhongMaterial)material;
    return new PbrMaterial() { Albedo = new Vector3(phongMaterial.DiffuseColor.x, phongMaterial.DiffuseColor.y, phongMaterial.DiffuseColor.z) };
};
```

## ステップ 4: GLTF 2.0 形式で保存する

変換されたシーンを GLTF 2.0 形式で保存します。

```csharp
scene.Save("Your Output Directory" + "Non_PBRtoPBRMaterial_Out.gltf", options);
// ExEnd:Non_PBRtoPBRマテリアル
```

特定の使用例に必要に応じてこれらの手順を繰り返し、各詳細が正しく構成されていることを確認します。

## 結論

おめでとう！ Aspose.3D for .NET を使用して非 PBR マテリアルを PBR マテリアルに変換する方法を学習しました。この強力なツールは、.NET アプリケーションでの 3D グラフィックス操作の可能性を無限に広げます。

## よくある質問

### Q1: Aspose.3D はすべての 3D ファイル形式と互換性がありますか?

A1: はい、Aspose.3D は幅広い 3D ファイル形式をサポートしており、プロジェクトに柔軟性をもたらします。

### Q2: Aspose.3D を商用アプリケーションに使用できますか?

 A2: もちろんです！ Aspose.3D は商用製品なので購入できます。[ここ](https://purchase.aspose.com/buy).

### Q3: テストには一時ライセンスが必要ですか?

A3: はい、テスト目的で一時ライセンスを取得できます。[ここ](https://purchase.aspose.com/temporary-license/).

### Q4: Aspose.3D のサポートはどこで見つけられますか?

 A4: にアクセスしてください。[Aspose.3D フォーラム](https://forum.aspose.com/c/3d/18)コミュニティのサポートとディスカッションのために。

### Q5: 無料トライアルはありますか?

 A5: はい、無料試用版を試すことができます。[ここ](https://releases.aspose.com/).