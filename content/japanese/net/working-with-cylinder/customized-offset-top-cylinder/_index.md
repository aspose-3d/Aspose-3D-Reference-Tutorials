---
title: カスタマイズされたオフセットトップシリンダー
linktitle: カスタマイズされたオフセットトップシリンダー
second_title: Aspose.3D .NET API
description: Aspose.3D for .NET を使用して 3D グラフィックスの驚異を体験してください。カスタマイズされたオフセット トップ シリンダーを簡単に作成する方法を学びましょう。今すぐコーディング体験を向上させましょう!
type: docs
weight: 11
url: /ja/net/working-with-cylinder/customized-offset-top-cylinder/
---
## 導入
Aspose.3D for .NET を使用した 3D グラフィックス操作の世界へようこそ!このチュートリアルでは、.NET アプリケーションで 3D シーン、オブジェクト、および形式を操作するための強力なライブラリである Aspose.3D を使用して、カスタマイズされたオフセット トップ シリンダーを作成するプロセスを説明します。
## 前提条件
チュートリアルに入る前に、次の前提条件を満たしていることを確認してください。
- C# プログラミング言語の基本的な知識。
- Visual Studio がマシンにインストールされていること。
- Aspose.3D for .NET ライブラリがダウンロードされ、プロジェクトで参照されます。
それでは、ステップバイステップのガイドを始めましょう。
## 名前空間のインポート
まず、必要な名前空間を C# コードにインポートしてください。
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```
## ステップ 1: シーンを作成する
```csharp
//シーンを作成する
Scene scene = new Scene();
```
これにより、Aspose.3D を使用して新しい 3D シーンが初期化されます。
## ステップ 2: シリンダーを初期化する
```csharp
//シリンダーの初期化
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```
ここでは、半径、高さ、スライスなどの特定のパラメーターを使用して円柱を作成します。
## ステップ 3: 最初のシリンダーの OffsetTop を設定する
```csharp
//オフセットトップを設定
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```
これにより、最初のシリンダーのカスタマイズされたオフセット上部が設定されます。
## ステップ 4: 最初のシリンダーの ChildNode を作成する
```csharp
//子ノードの作成
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```
最初の円柱を子ノードとしてシーンに追加し、その位置を調整します。
## ステップ 5: 2 番目のシリンダーを初期化する
```csharp
//OffsetTop をカスタマイズせずに 2 番目のシリンダを初期化する
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```
番目のシリンダーは、カスタマイズされたオフセット トップなしで初期化されます。
## ステップ 6: 2 番目のシリンダーの ChildNode を作成する
```csharp
//子ノードの作成
scene.RootNode.CreateChildNode(cylinder2);
```
番目の円柱を子ノードとしてシーンに追加します。
## ステップ 7: シーンを保存する
```csharp
//保存
scene.Save("Your Document Directory" + "CustomizedOffsetTopCylinder.obj", FileFormat.WavefrontOBJ);
```
これにより、カスタマイズされたオフセット上部シリンダーを含む 3D シーンが Wavefront OBJ 形式で保存されます。
これで、Aspose.3D for .NET を使用して、カスタマイズされたオフセット トップ シリンダーが正常に作成されました。
## 結論
このチュートリアルでは、Aspose.3D for .NET を使用してカスタマイズされたオフセット トップ シリンダーを作成する基本を学習しました。このライブラリは、.NET アプリケーション内での 3D グラフィックス操作の可能性を無限に広げます。
## よくある質問
### Q: Aspose.3D for .NET のドキュメントはどこで見つけられますか?
 A: ドキュメントは入手可能です[ここ](https://reference.aspose.com/3d/net/).
### Q: Aspose.3D for .NET をダウンロードするにはどうすればよいですか?
答え: ダウンロードできますよ[ここ](https://releases.aspose.com/3d/net/).
### Q: Aspose.3D for .NET の無料トライアルはありますか?
 A: はい、無料トライアルを利用できます[ここ](https://releases.aspose.com/).
### Q: Aspose.3D for .NET のサポートはどこで受けられますか?
 A: にアクセスしてください。[Aspose.3D フォーラム](https://forum.aspose.com/c/3d/18)サポートのための。
### Q: Aspose.3D for .NET の一時ライセンスを取得できますか?
 A: はい、一時ライセンスを取得できます。[ここ](https://purchase.aspose.com/temporary-license/).