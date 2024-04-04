---
title: 3D を PDF で保存する
linktitle: 3D を PDF で保存する
second_title: Aspose.3D .NET API
description: Aspose.3D for .NET を探索してください。シームレスな 3D モデリングとレンダリングのための頼りになるライブラリ。 3D モデルを PDF で簡単に保存できます。
type: docs
weight: 19
url: /ja/net/loading-and-saving/pdf/save-3d-in-pdf/
---
## 導入

Aspose.3D for .NET の使用に関する包括的なガイドへようこそ!このチュートリアルでは、3D モデルを PDF 形式で保存するという特定のタスクに焦点を当てて、3D モデルのロードと保存のプロセスを説明します。 Aspose.3D for .NET は、3D ファイルを操作するための効率的なツールを提供する強力なライブラリであり、この分野の開発者や愛好家にとって不可欠なリソースとなっています。

## 前提条件

チュートリアルに入る前に、次の前提条件が満たされていることを確認してください。

-  Aspose.3D for .NET: ライブラリがインストールされていることを確認してください。そうでない場合は、からダウンロードできます。[Aspose.3D for .NET ドキュメント](https://reference.aspose.com/3d/net/).

- 開発環境: 好みの .NET 開発環境をセットアップします。

- 3D 概念の基本的な理解: このガイドは 3D モデリングの基本的な知識を前提としているため、基本的な 3D 概念を理解してください。

## 名前空間のインポート

.NET プロジェクトでは、Aspose.3D が提供する機能にアクセスするために必要な名前空間をインポートしてください。

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Formats;
using System.Drawing;
```

## ステップ 1: 新しいシーンを作成する

まず、Aspose.3D ライブラリを使用して新しい 3D シーンを初期化します。これは 3D モデルの基礎として機能します。

```csharp
Scene scene = new Scene();
```

## ステップ 2: シリンダー子ノードを追加する

保存プロセスを示すために、単純な 3D モデル、つまり円柱を作成してみましょう。円柱を子ノードとしてシーンに追加します。

```csharp
scene.RootNode.CreateChildNode("cylinder", new Cylinder()).Material = new PhongMaterial() { DiffuseColor = new Vector3(Color.DarkCyan) };
```

## ステップ 3: レンダリング モードと照明スキームを設定する

3D シーンのレンダリング モードと照明スキームを定義します。このステップでは、モデルの外観をカスタマイズできます。

```csharp
PdfSaveOptions opt = new PdfSaveOptions();
opt.LightingScheme = PdfLightingScheme.CAD;
opt.RenderMode = PdfRenderMode.ShadedIllustration;
```

## ステップ 4: PDF 形式で保存する

最後に、出力ディレクトリとファイル名を指定して保存処理を実行します。この場合、3D モデルを PDF 形式で保存します。

```csharp
scene.Save("Your Output Directory" + "output_out.pdf", opt);
```

「出力ディレクトリ」を目的のパスに置き換えてください。

## 結論

おめでとう！ Aspose.3D for .NET を使用して単純な 3D モデルを作成し、PDF 形式で保存する方法を学習しました。これは、この強力なライブラリで達成できることのほんの始まりにすぎません。のさらなる機能と可能性を探ってください。[Aspose.3D ドキュメント](https://reference.aspose.com/3d/net/).

## よくある質問

### Q1: Aspose.3D for .NET はすべての 3D ファイル形式と互換性がありますか?

A1: はい、Aspose.3D for .NET は幅広い 3D ファイル形式をサポートし、さまざまな業界標準との互換性を保証します。

### Q2: 保存プロセス中に 3D モデルの視覚的な側面をカスタマイズできますか?

A2: もちろんです！チュートリアルで示されているように、レンダリング モード、照明スキームなどを調整して、望ましい視覚的結果を達成できます。

### Q3: Aspose.3D for .NET のサポートはどこで見つけられますか?

 A3: にアクセスしてください。[Aspose.3D フォーラム](https://forum.aspose.com/c/3d/18) Aspose.3D for .NET に関連するコミュニティ サポートとディスカッション用。

### Q4: Aspose.3D for .NET の無料トライアルはありますか?

 A4: はい、アクセスできます。[無料トライアル](https://releases.aspose.com/)購入する前に、Aspose.3D for .NET の機能を確認してください。

### Q5: Aspose.3D for .NET の一時ライセンスを取得するにはどうすればよいですか?

 A5: 一時ライセンスを取得するには、次のサイトにアクセスしてください。[このリンク](https://purchase.aspose.com/temporary-license/)そして、提供された指示に従ってください。