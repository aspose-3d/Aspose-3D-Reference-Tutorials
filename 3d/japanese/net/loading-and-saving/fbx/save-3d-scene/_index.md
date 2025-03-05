---
title: 3D シーンを FBX ファイルに保存する
linktitle: 3D シーンを FBX ファイルに保存する
second_title: Aspose.3D .NET API
description: Aspose.3D for .NET の威力を体験してください。シームレスな 3D シーン操作のための多用途ライブラリ。読み込み、保存、圧縮が簡単に行えます。
type: docs
weight: 20
url: /ja/net/loading-and-saving/fbx/save-3d-scene/
---
## 導入

Aspose.3D for .NET を使用した 3D シーン操作の領域へのエキサイティングな旅へようこそ!経験豊富な開発者であっても、好奇心旺盛な愛好家であっても、このチュートリアルでは、3D シーンを簡単にロード、保存、圧縮するプロセスをガイドします。

## 前提条件

3D シーン操作の魅力的な世界に飛び込む前に、次の前提条件が満たされていることを確認してください。

-  Aspose.3D for .NET: Aspose.3D ライブラリを次の場所からダウンロードしてインストールします。[ダウンロードリンク](https://releases.aspose.com/3d/net/).
- ドキュメント: 包括的なドキュメントを通じてライブラリの機能を理解します。[ドキュメンテーション](https://reference.aspose.com/3d/net/).
- 出力ディレクトリ: チュートリアル中に生成された出力ファイルを保存するディレクトリを設定します。

## 名前空間のインポート

必要な名前空間を .NET 環境にインポートして、探索を開始しましょう。

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Formats;
```

## ロードと保存 - 3D シーンの保存

### ステップ 1: 3D ドキュメントをロードする

```csharp
Scene scene = Scene.FromFile("document.fbx");
```

このステップでは、新しい`Scene`オブジェクトを作成し、`FromFile`方法。

### ステップ 2: シーンをストリームに保存する

```csharp
MemoryStream dstStream = new MemoryStream();
scene.Save(dstStream, FileFormat.FBX7500ASCII);
```

ロードした 3D シーンをメモリ ストリームに保存します。`Save`メソッドを使用して、目的のファイル形式 (この場合は FBX7500ASCII) を指定します。


### ステップ 3: シーンをローカル パスに保存する

```csharp
scene.Save("output_out.fbx", FileFormat.FBX7500ASCII);
```

意味のある出力ディレクトリとファイル名を指定して、3D シーンをローカル パスに保存します。

## 圧縮

次に、3D シーンの圧縮オプションを見てみましょう。

### ステップ 1: 3D ドキュメントをロードする

```csharp
Scene scene = new Scene("document.fbx");
```

前の例と同様に、3D ドキュメントを`Scene`物体。

### ステップ 2: 圧縮を無効にして保存する

```csharp
scene.Save("UncompressedDocument.fbx", new FbxSaveOptions(FileFormat.FBX7500ASCII) { EnableCompression = false });
```

3D シーンの保存中に圧縮を無効にし、明確な出力パスとファイル名を提供します。

## 結論

このチュートリアルでは、Aspose.3D for .NET を使用した 3D シーンの読み込み、保存、圧縮の基本的な側面を詳しく掘り下げました。この知識を身につければ、独自の 3D の旅に乗り出し、Aspose.3D の領域内で創造的な可能性を解き放つ準備が整います。

## よくある質問

### Q1: Aspose.3D はさまざまな 3D ファイル形式と互換性がありますか?

A1: はい、Aspose.3D は幅広い 3D ファイル形式をサポートしており、プロジェクトに柔軟性をもたらします。

### Q2: Aspose.3D を他の .NET ライブラリと統合できますか?

A2: もちろんです！ Aspose.3D は他の .NET ライブラリとシームレスに統合し、アプリケーションの機能を強化します。

### Q3: Aspose.3D の一時ライセンスを取得するにはどうすればよいですか?

 A3: にアクセスしてください。[仮免許](https://purchase.aspose.com/temporary-license/) Aspose Web サイトのページにアクセスして一時ライセンスを取得します。

### Q4: どこに助けを求めたり、コミュニティと連絡をとったりできますか?

 A4: の活発な Aspose.3D コミュニティに参加してください。[フォーラム](https://forum.aspose.com/c/3d/18)サポートを求め、経験を共有し、愛好家同士で協力します。

### Q5: Aspose.3D の無料トライアルはありますか?

 A5: はい、Aspose.3D の機能を調べてください。[無料トライアル](https://releases.aspose.com/)今日！