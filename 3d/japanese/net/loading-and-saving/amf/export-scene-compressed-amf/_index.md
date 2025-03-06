---
title: 3D シーンを圧縮 AMF 形式でエクスポートする
linktitle: 圧縮AMFへのシーンのエクスポート
second_title: Aspose.3D .NET API
description: Aspose.3D for .NET を使用して 3D シーンを圧縮 AMF 形式にエクスポートする方法を学びます。このステップバイステップのガイドを使用して、開発スキルを強化してください。
weight: 11
url: /ja/net/loading-and-saving/amf/export-scene-compressed-amf/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 3D シーンを圧縮 AMF 形式でエクスポートする

## 導入

3D モデリングとレンダリングの動的な世界では、効率と柔軟性が最も重要です。 Aspose.3D for .NET を使用すると、開発者は 3D シーンを圧縮 AMF (Additive Manufacturing File) 形式にシームレスにエクスポートし、品質を損なうことなく最適なファイル サイズを確保できます。このチュートリアルでは、プロセスを段階的にガイドし、初心者と経験豊富な開発者の両方が Aspose.3D for .NET の機能を簡単に利用できるようにします。

## 前提条件

チュートリアルに入る前に、次の前提条件を満たしていることを確認してください。

- 3D モデリングの概念の基本的な理解
- マシンにインストールされている Visual Studio
-  .NET ライブラリの Aspose.3D。ダウンロードできます[ここ](https://releases.aspose.com/3d/net/)
- 3D開発スキルを向上させたい！

## 名前空間のインポート

プロジェクトでは、Aspose.3D for .NET の機能を利用するために必要な名前空間をインポートしていることを確認してください。

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```

## ステップ 1: 3D シーンをロードする

まず、Aspose.3D for .NET を使用して 3D シーンをロードします。シーン オブジェクトを作成し、それにボックスなどのエンティティを追加します。

```csharp
Scene scene = new Scene();
var box = new Box();
var tr = scene.RootNode.CreateChildNode(box).Transform;
tr.Scale = new Vector3(12, 12, 12);
tr.Translation = new Vector3(10, 0, 0);
```

## ステップ 2: スケール変換

次に、シーン内の別のボックスにスケール変換を適用します。

```csharp
tr = scene.RootNode.CreateChildNode(box).Transform;
tr.Scaling = new Vector3(5, 5, 5);
```

## ステップ 3: オイラー角を設定する

変換のオイラー角を設定します。

```csharp
tr.EulerAngles = new Vector3(50, 10, 0);
```

## ステップ 4: 圧縮された AMF ファイルを保存する

最後に、3D シーンを圧縮 AMF ファイルとして目的の出力ディレクトリに保存します。

```csharp
scene.Save("Your Output Directory/" + "Aspose.amf", new AmfSaveOptions() { EnableCompression = false });
```

## 結論

おめでとう！ Aspose.3D for .NET を使用して、3D シーンを圧縮 AMF 形式にエクスポートできました。この強力なライブラリは 3D 開発者に可能性の世界を開き、効率的で視覚的に素晴らしいモデルを作成できるようにします。

## よくある質問

### Q1: Aspose.3D は一般的な 3D モデリング ソフトウェアと互換性がありますか?

A1: Aspose.3D はさまざまなファイル形式をサポートしているため、一般的な 3D モデリング ツールと互換性があります。

### Q2: AMF 以外のファイル形式の圧縮を有効にすることはできますか?

A2: はい、Aspose.3D には、さまざまなファイル形式の圧縮を有効にするオプションが用意されています。

### Q3: Aspose.3D は初心者と上級開発者の両方に適していますか?

A3：もちろんです！ Aspose.3D は、初心者向けのシンプルさと、熟練した開発者向けの高度な機能を提供します。

### Q4: エクスポートできる 3D シーンのサイズに制限はありますか?

A4: Aspose.3D は、さまざまな複雑さのシーンを処理できるように設計されており、厳密なサイズ制限はありません。

### Q5: 追加のサポートやコミュニティのディスカッションはどこで見つけられますか?

 A5: にアクセスしてください。[Aspose.3D フォーラム](https://forum.aspose.com/c/3d/18)サポートとディスカッションのため。
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
