---
title: ロードと保存 - カスタムロードオプション
linktitle: ロードと保存 - カスタムロードオプション
second_title: Aspose.3D .NET API
description: シームレスな 3D モデルの読み込みと保存のための究極のソリューションである Aspose.3D for .NET を探索してください。
type: docs
weight: 15
url: /ja/net/loading-and-saving/custom-load-options/
---
## 導入

Aspose.3D for .NET の世界へようこそ。これは、開発者が 3D ファイルをシームレスに操作できるようにする強力なライブラリです。このチュートリアルでは、カスタム ロード オプションに焦点を当てて、3D モデルのロードと保存の複雑さを詳しく説明します。経験豊富な開発者であっても、初心者であっても、このガイドではプロセスを段階的に説明し、Aspose.3D for .NET の可能性を最大限に活用できるようにします。

## 前提条件

この作業を開始する前に、次の前提条件が満たされていることを確認してください。

-  Aspose.3D for .NET: ライブラリがインストールされていることを確認してください。ダウンロードできます[ここ](https://releases.aspose.com/3d/net/).

- ドキュメント ディレクトリ: 3D モデル ファイルを保存するディレクトリを作成します。

必要なものが揃ったので、3D モデル操作のエキサイティングな世界に飛び込みましょう!

## 名前空間のインポート

まず最初に、必要な名前空間をインポートしましょう。これにより、Aspose.3D 領域への旅の準備が整います。

```csharp
using System;
using System.IO;
using System.Collections.Generic;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Formats;
```

## ロードと保存 - カスタムロードオプション

### ステップ 1: Discreet3DS ファイルをロードする

```csharp
private static void Discreet3DSLoadOption()
{
    //ドキュメントディレクトリへのパス。
    string dataDir = "Your Document Directory";
    Discreet3dsLoadOptions loadOpts = new Discreet3dsLoadOptions();

    //カスタムオプションを設定する
    loadOpts.ApplyAnimationTransform = true;
    loadOpts.FlipCoordinateSystem = true;
    loadOpts.GammaCorrectedColor = true;
    loadOpts.LookupPaths = new List<string>(new string[] { dataDir });
}
```

### ステップ 2: OBJ ファイルのロード

```csharp
private static void ObjLoadOption()
{
    //ドキュメントディレクトリへのパス。
    string dataDir = "Your Document Directory";
    ObjLoadOptions loadObjOpts = new ObjLoadOptions();

    //カスタムオプションを設定する
    loadObjOpts.EnableMaterials = true;
    loadObjOpts.FlipCoordinateSystem = true;
    loadObjOpts.LookupPaths = new List<string>(new string[] { dataDir });
}
```

### ステップ 3: STL ファイルのロード

```csharp
private static void STLLoadOption()
{
    //ドキュメントディレクトリへのパス。
    string dataDir = "Your Document Directory";
    StlLoadOptions loadSTLOpts = new StlLoadOptions();

    //カスタムオプションを設定する
    loadSTLOpts.FlipCoordinateSystem = true;
    loadSTLOpts.LookupPaths = new List<string>(new string[] { dataDir });
}
```

### ステップ 4: U3D ファイルをロードする

```csharp
private static void U3DLoadOption()
{
    //ドキュメントディレクトリへのパス。
    string dataDir = "Your Document Directory";
    U3dLoadOptions loadU3DOpts = new U3dLoadOptions();

    //カスタムオプションを設定する
    loadU3DOpts.FlipCoordinateSystem = true;
    loadU3DOpts.LookupPaths = new List<string>(new string[] { dataDir });
}
```

### ステップ 5: glTF ファイルのロード

```csharp
private static void glTFLoadOptions()
{
    //ドキュメントディレクトリへのパス。
    string dataDir = "Your Document Directory";
    Scene scene = new Scene();
    GltfLoadOptions loadOpt = new GltfLoadOptions();

    //カスタムオプションを設定する
    loadOpt.FlipTexCoordV = true;
    scene.Open(dataDir + "Duck.gltf", loadOpt);
}
```

### ステップ 6: PLY ファイルをロードする

```csharp
private static void PlyLoadOptions()
{
    //ドキュメントディレクトリへのパス。
    string dataDir = "Your Document Directory";
    Scene scene = new Scene();
    PlyLoadOptions loadPLYOpts = new PlyLoadOptions();

    //カスタムオプションを設定する
    loadPLYOpts.FlipCoordinateSystem = true;
    scene.Open(RunExamples.GetDataFilePath("vase-v2.ply"), loadPLYOpts);
}
```

### ステップ 7: FBX ファイルをロードする

```csharp
private static void FBXLoadOptions()
{
    //ドキュメントディレクトリへのパス。
    string dataDir = "Your Document Directory";
    Scene scene = new Scene();
    FbxLoadOptions opt = new FbxLoadOptions() { KeepBuiltinGlobalSettings = true };

    //カスタムオプションを設定する
    scene.Open(dataDir + "test.FBX", opt);

    //FBX ファイルの GlobalSettings で定義された出力プロパティ
    foreach (Property property in scene.RootNode.AssetInfo.Properties)
    {
        Console.WriteLine(property);
    }
}
```

## 結論

おめでとう！ Aspose.3D for .NET を使用して、3D モデルの読み込みと保存の複雑な世界を無事にナビゲートできました。このチュートリアルでは、さまざまなファイル形式とそのカスタム ロード オプションについて説明し、3D アセットを簡単に操作できるようにしました。

## よくある質問

### Q1: Aspose.3D for .NET は初心者に適していますか?

A1: もちろんです！ Aspose.3D for .NET はユーザーフレンドリーなインターフェイスを提供し、あらゆるレベルの開発者がアクセスできるようにします。

### Q2: Aspose.3D を商用プロジェクトに使用できますか?

A2: はい、Aspose.3D for .NET には商用ライセンスが付属しており、プロジェクトで使用できます。

### Q3: サポートされるファイル形式に制限はありますか?

 A3: Aspose.3D for .NET は、OBJ、STL、FBX などの一般的な 3D ファイル形式を幅広くサポートしています。を参照してください。[ドキュメンテーション](https://reference.aspose.com/3d/net/)包括的なリストについては、

### Q4: 体験版はありますか?

A4: はい、Aspose.3D for .NET の機能を調べるには、[無料トライアル](https://releases.aspose.com/).

### Q5: Aspose.3D for .NET のサポートはどこに問い合わせればよいですか?

A5: にアクセスしてください。[Aspose.3D フォーラム](https://forum.aspose.com/c/3d/18)コミュニティのサポートと支援のために。