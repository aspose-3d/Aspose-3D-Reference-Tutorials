---
title: カスタム保存オプション
linktitle: カスタム保存オプション
second_title: Aspose.3D .NET API
description: Aspose.3D for .NET の威力を体験してください。 Collada、USD、3DS、FBX、OBJ、STL、U3D、glTF、DRC、および RVM 形式に関するステップバイステップのガイドを使用して、3D シーンの保存をカスタマイズする方法を学びます。
weight: 21
url: /ja/net/loading-and-saving/custom-save-options/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# カスタム保存オプション

## 導入

Aspose.3D for .NET の世界へようこそ! 3D 開発能力を強化したい場合は、ここが最適な場所です。このチュートリアルでは、特にカスタム保存オプションに焦点を当てて、読み込みと保存の機能について詳しく説明します。 Aspose.3D for .NET は、開発者が 3D シーンを効率的に操作および保存できるようにする強力なライブラリです。

## 前提条件

Aspose.3D の魅力的な機能の探索を開始する前に、次の前提条件を満たしていることを確認してください。

- C# および .NET 開発の基本的な理解。
-  Aspose.3D for .NET ライブラリがインストールされています。からダウンロードできます。[リリースページ](https://releases.aspose.com/3d/net/).
- Visual Studio またはその他の推奨される C# IDE でセットアップされた開発環境。

## 名前空間のインポート

まず、必要な名前空間をインポートしましょう。

```csharp
using System;
using System.IO;
using System.Collections.Generic;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using Aspose.ThreeD.Shading;
using System.Drawing;
```

準備が整ったので、チュートリアルを複数のステップに分割してみましょう。

## ステップ 1: Collada 保存オプション

人気の 3D ファイル形式である Collada から始めましょう。 Collada の保存オプションをカスタマイズするには、次の手順に従います。

### 1. ディレクトリを設定します。
   ```csharp
   string dataDir = "Your Document Directory";
   ```

### 2. Collada 保存オプションを初期化します。
   ```csharp
   ColladaSaveOptions saveColladaOpts = new ColladaSaveOptions();
   ```

### 3. オプションを構成します。
   ```csharp
   saveColladaOpts.Indented = true;
   saveColladaOpts.TransformStyle = ColladaTransformStyle.Matrix;
   saveColladaOpts.LookupPaths = new List<string>(new string[] { dataDir });
   ```

## ステップ 2: 控えめな 3DS 保存オプション

それでは、Discreet 3DS とそのカスタマイズ オプションを見てみましょう。

### 1. ディレクトリを設定します。
   ```csharp
   string dataDir = "Your Document Directory";
   ```

### 2. 3DS 保存オプションを初期化します。
   ```csharp
   Discreet3dsSaveOptions saveOpts = new Discreet3dsSaveOptions();
   ```

### 3. オプションを構成します。
   ```csharp
   saveOpts.DuplicatedNameCounterBase = 2;
   //追加の構成オプション...
   ```

FBX、OBJ、STL、U3D、glTF、および DRC 保存オプションに対してこの段階的なアプローチを続け、要件に応じてそれぞれをカスタマイズします。

## ステップ 3: glTF 保存オプション

ここで、Web アプリケーションやモバイル アプリケーションで広く使用されている形式である glTF に焦点を当てましょう。次の手順で glTF 保存オプションをカスタマイズします。

### 1. シーン オブジェクトを初期化します。
   ```csharp
   Scene scene = new Scene();
   scene.RootNode.CreateChildNode("sphere", new Sphere());
   ```

### 2. glTF 保存オプションを設定します。
   ```csharp
   GltfSaveOptions opt = new GltfSaveOptions(FileContentType.ASCII);
   opt.EmbedAssets = true;
   opt.UseCommonMaterials = true;
   opt.BufferFile = "mybuf.bin";
   ```

### 3. glTF ファイルを保存します。
   ```csharp
   scene.Save("Your Output Directory" + "glTFSaveOptions_out.gltf", opt);
   ```

DRC や RVM などの他の保存オプションでも同様の構造に従います。

## 結論

おめでとう！ Aspose.3D for .NET のカスタム保存オプションを正常に調査しました。この強力なライブラリは、3D シーンの保存プロセスをカスタマイズするための無数のオプションを提供します。

## よくある質問

### Q1: Aspose.3D for .NET を他の .NET フレームワークと一緒に使用できますか?

A1: はい、Aspose.3D はさまざまな .NET フレームワークと互換性があり、開発環境の柔軟性を確保します。

### Q2: Aspose.3D で利用できるライセンス オプションはありますか?

 A2: はい、ライセンス オプションを検討できます。[ここ](https://purchase.aspose.com/buy).

### Q3: Aspose.3D 関連のクエリのサポートはどこで見つけられますか?

 A3: サポートを求めることができます。[Aspose.3D フォーラム](https://forum.aspose.com/c/3d/18).

### Q4: 無料トライアルはありますか?

 A4: はい、無料トライアルにアクセスできます。[ここ](https://releases.aspose.com/).

### Q5: Aspose.3D の一時ライセンスを取得するにはどうすればよいですか?

 A5: 仮免許を取得する[ここ](https://purchase.aspose.com/temporary-license/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
