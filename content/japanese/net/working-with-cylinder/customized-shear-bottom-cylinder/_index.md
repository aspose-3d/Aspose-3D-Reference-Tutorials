---
title: カスタマイズされたシャーボトムシリンダー
linktitle: カスタマイズされたシャーボトムシリンダー
second_title: Aspose.3D .NET API
description: 詳細なステップバイステップ ガイドで、Aspose.3D for .NET を使用してカスタマイズされたシア ボトム シリンダーを作成する方法を学びます。今すぐ 3D モデリングのスキルを向上させましょう!
type: docs
weight: 12
url: /ja/net/working-with-cylinder/customized-shear-bottom-cylinder/
---
## 導入
Aspose.3D for .NET を使用してカスタマイズされたシアボトム シリンダーを作成するための包括的なガイドへようこそ。 3D モデリングのスキルを向上させ、プロジェクトに独自の機能を追加したい場合は、ここが最適な場所です。このチュートリアルでは、明確な説明とコード スニペットを使用して、プロセスを段階的に説明します。
## 前提条件
チュートリアルに入る前に、次のものが揃っていることを確認してください。
- C# および .NET プログラミングの基本的な理解。
-  Aspose.3D for .NET ライブラリがインストールされています。ダウンロードできます[ここ](https://releases.aspose.com/3d/net/).
- .NET プログラミング用にセットアップされた開発環境。
## 名前空間のインポート
C# コードで、必要な名前空間をインポートすることから始めます。
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
まず、Aspose.3D を使用して 3D シーンを作成します。
```csharp
Scene scene = new Scene();
```
## ステップ 2: シリンダー 1 を作成する
最初のシリンダーを生成し、そのプロパティを設定します。
```csharp
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```
## ステップ 3: シリンダー 1 のシアボトムをカスタマイズする
カスタマイズしたシアーボトムを最初のシリンダーに適用します。
```csharp
cylinder1.ShearBottom = new Vector2(0, 0.83); //xy 平面 (z 軸) で 47.5 度のせん断
```
## ステップ 4: シリンダー 1 をシーンに追加する
最初の円柱をシーンに追加し、その変換を設定します。
```csharp
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```
## ステップ 5: シリンダー 2 を作成する
同様のプロパティを持つ 2 番目の円柱を生成します。
```csharp
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```
## ステップ 6: シリンダー 2 をシーンに追加する
せん断底部を持たない 2 番目の円柱をシーンに追加します。
```csharp
scene.RootNode.CreateChildNode(cylinder2);
```
## ステップ 7: シーンを保存する
シーンを Wavefront OBJ ファイルとしてドキュメント ディレクトリに保存します。
```csharp
scene.Save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WavefrontOBJ);
```
## 結論
おめでとう！ Aspose.3D for .NET を使用して、カスタマイズされたせん断底部シリンダーが正常に作成されました。このチュートリアルは、3D モデリングとプログラミングにおけるさまざまなレベルの専門知識を持つユーザーに段階的なガイドを提供することを目的としています。
## よくある質問
### Aspose.3D for .NET は初心者に適していますか?
絶対に！ Aspose.3D for .NET はユーザーフレンドリーなインターフェイスを提供しており、初心者と経験豊富な開発者の両方がアクセスできます。
### シリンダーに異なるせん断角度を適用できますか?
はい、各シリンダーのシアボトムを個別にカスタマイズして、独自の効果を実現できます。
### 試用版はありますか?
はい、無料試用版を試すことができます[ここ](https://releases.aspose.com/).
### 追加のサポートはどこで見つけられますか?
訪問[Aspose.3D フォーラム](https://forum.aspose.com/c/3d/18)コミュニティのサポートとディスカッションのために。
### 仮免許はどうやって取得できますか?
仮免許を取得する[ここ](https://purchase.aspose.com/temporary-license/).