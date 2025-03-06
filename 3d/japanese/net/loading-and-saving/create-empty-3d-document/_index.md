---
title: 空の 3D ドキュメントの作成
linktitle: 空の 3D ドキュメントの作成
second_title: Aspose.3D .NET API
description: Aspose.3D for .NET を使用して 3D ドキュメント作成の世界を探索してください。見事な 3D シーンを簡単に作成、編集、保存できます。
weight: 11
url: /ja/net/loading-and-saving/create-empty-3d-document/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 空の 3D ドキュメントの作成

## 導入

Aspose.3D for .NET を使用した 3D ドキュメント作成の世界へようこそ!このチュートリアルでは、3D ドキュメントの読み込みと保存の基本を学習します。 Aspose.3D for .NET は、3D シーンを操作するための強力なツール セットを提供しており、スムーズに開始できるように各ステップをガイドします。

## 前提条件

チュートリアルに入る前に、次の前提条件が満たされていることを確認してください。

-  Aspose.3D for .NET: ライブラリがインストールされていることを確認してください。からダウンロードできます[ここ](https://releases.aspose.com/3d/net/).

## 名前空間のインポート

まず、必要な名前空間を .NET プロジェクトにインポートします。

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
```

## ロードと保存 - 空の 3D ドキュメントの作成

### ステップ 1: 出力ディレクトリを設定する

```csharp
//ドキュメントディレクトリへのパス。
var output = "Your Output Directory" + "document.fbx";
```

### ステップ 2: 空の 3D ドキュメントを作成する

```csharp
//ExStart:空の 3D ドキュメントの作成

// Sceneクラスのオブジェクトを作成する
Scene scene = new Scene();

//3D シーン ドキュメントを FBX 形式で保存します
scene.Save(output);

//ExEnd:CreateEmpty3DDocument
```

### ステップ 3: 結果を表示する

```csharp
Console.WriteLine("\nAn empty 3D document created successfully.\nFile saved at " + output);
```

おめでとう！ Aspose.3D for .NET を使用して、最初の空の 3D ドキュメントが作成されました。このライブラリの可能性を最大限に引き出すために、さらに多くの機能を自由に探索してください。

## 結論

このチュートリアルでは、Aspose.3D for .NET を使用して空の 3D ドキュメントを作成する基本について説明しました。 3D 開発の旅を続ける際には、次のセクションを参照してください。[ドキュメンテーション](https://reference.aspose.com/3d/net/)深い洞察と高度な機能が得られます。

## よくある質問

### Q1: Aspose.3D for .NET は初心者に適していますか?

A1: はい、Aspose.3D for .NET はユーザーフレンドリーなインターフェイスを提供しており、初心者と経験豊富な開発者の両方がアクセスできます。

### Q2: 購入する前に Aspose.3D for .NET を試してみることはできますか?

 A2: もちろんです！無料トライアルにアクセスできます[ここ](https://releases.aspose.com/).

### Q3: Aspose.3D for .NET のサポートを受けるにはどうすればよいですか?

 A3: にアクセスしてください。[Aspose.3D フォーラム](https://forum.aspose.com/c/3d/18)支援を求め、コミュニティとつながるために。

### Q4: Aspose.3D for .NET の一時ライセンスは利用できますか?

 A4: はい、一時ライセンスを取得できます。[ここ](https://purchase.aspose.com/temporary-license/).

### Q5: Aspose.3D for .NET はどこで購入できますか?

 A5: ライブラリを購入できます。[ここ](https://purchase.aspose.com/buy).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
