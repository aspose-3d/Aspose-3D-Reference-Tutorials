---
title: プリミティブ 3D モデルの作成
linktitle: プリミティブ 3D モデルの作成
second_title: Aspose.3D .NET API
description: Aspose.3D for .NET を使用して 3D モデリングの世界を探索してください。魅力的なプリミティブ モデルを簡単に作成できます。
type: docs
weight: 10
url: /ja/net/3d-modeling/primitive-3d-models/
---
## 導入

Aspose.3D for .NET を使用したエキサイティングな 3D モデリングの世界へようこそ!この包括的なチュートリアルでは、Aspose.3D を使用してプリミティブ 3D モデルを作成するプロセスを段階的に説明します。経験豊富な開発者であっても、好奇心旺盛な初心者であっても、このガイドは、Aspose.3D の力を活用して、プロジェクト用に視覚的に素晴らしい 3D 要素を作成するのに役立ちます。

## 前提条件

3D モデリングの魅力的な領域に入る前に、次の前提条件が満たされていることを確認してください。

- Aspose.3D for .NET: Aspose.3D for .NET ライブラリを次の場所からダウンロードしてインストールします。[ダウンロードリンク](https://releases.aspose.com/3d/net/).

- 開発環境: .NET 開発環境をセットアップし、Aspose.3D との互換性を確保します。

必要なものが揃ったので、プリミティブ 3D モデルを段階的に作成する旅に乗り出しましょう。

## 名前空間のインポート

まず、Aspose.3D が提供する機能にアクセスするために必要な名前空間をインポートします。

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
```

これらの名前空間を適切に配置すると、.NET アプリケーションで Aspose.3D のパワーを解放する準備が整います。

## ステップ 1: シーン オブジェクトを初期化する

```csharp
//Scene オブジェクトを初期化する
Scene scene = new Scene();
```

3D 傑作のキャンバスとして機能する新しいシーン オブジェクトを作成します。

## ステップ 2: ボックス モデルを作成する

```csharp
//ボックスモデルを作成する
scene.RootNode.CreateChildNode("box", new Box());
```

ボックス モデルをシーンのルートに追加します。創造的なビジョンに応じて、ボックスの寸法とプロパティをカスタマイズします。

## ステップ 3: 円柱モデルを作成する

```csharp
//円柱モデルを作成する
scene.RootNode.CreateChildNode("cylinder", new Cylinder());
```

シリンダー モデルを導入してシーンを強化します。パラメータを調整して、目的の形状とサイズを実現します。

## ステップ 4: 図面を FBX 形式で保存する

```csharp
//図面をFBX形式で保存する
var output = "Your Output Directory" + "test.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

3D 傑作を FBX 形式で保存します。作成に適した出力ディレクトリとファイル名を選択します。

## ステップ 5: 成功メッセージを表示する

```csharp
//成功メッセージを表示する
Console.WriteLine("\nBuilding a scene from primitive 3D models successfully.\nFile saved at " + output);
```

あなたの功績を祝いましょう！シーンはプリミティブ 3D モデルから正常に構築され、ファイルが保存されます。

## 結論

おめでとう！ Aspose.3D for .NET を使用して、見事な 3D モデルを作成することに成功しました。このガイドでは基本を説明しましたが、可能性は無限です。を探索してください[ドキュメンテーション](https://reference.aspose.com/3d/net/)より高度な機能とテクニックをご覧ください。

## よくある質問

### Q1: Aspose.3D for .NET を他のプログラミング言語で使用できますか?

A1: Aspose.3D は主に .NET をサポートしていますが、Java やその他のプラットフォームで使用できる他のバージョンもあります。

### Q2: 無料トライアルはありますか?

 A2: はい、Aspose.3D の機能を調べることができます。[無料トライアル](https://releases.aspose.com/).

### Q3: Aspose.3D for .NET のサポートはどこで見つけられますか?

 A3: にアクセスしてください。[Aspose.3D フォーラム](https://forum.aspose.com/c/3d/18)コミュニティのサポートとディスカッションのために。

### Q4: 仮免許はどうやって取得できますか?

 A4: 仮免許を取得できます。[ここ](https://purchase.aspose.com/temporary-license/).

### Q5: サンプルチュートリアルはありますか?

 A5: はい、次のチュートリアルと例をご覧ください。[ドキュメンテーション](https://reference.aspose.com/3d/net/).