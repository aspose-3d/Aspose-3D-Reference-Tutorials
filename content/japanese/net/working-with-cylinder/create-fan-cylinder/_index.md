---
title: ファンシリンダーの作成
linktitle: ファンシリンダーの作成
second_title: Aspose.3D .NET API
description: Aspose.3D for .NET で 3D デザインの世界を解き放ちましょう!美しいファンシリンダーと非ファンシリンダーを簡単に作成できます。今すぐ試用版をダウンロードしてください。
type: docs
weight: 10
url: /ja/net/working-with-cylinder/create-fan-cylinder/
---
## 導入
Aspose.3D for .NET を使用した 3D モデリングと視覚化の世界へようこそ!このステップバイステップ ガイドでは、Aspose.3D for .NET を使用して魅力的なファン シリンダーを作成する方法を説明します。 Aspose.3D は、.NET アプリケーションで 3D コンテンツを操作するための広範な機能を提供する強力なライブラリです。
## 前提条件
3D モデリングのエキサイティングな世界に入る前に、次の前提条件を満たしていることを確認してください。
- .NET プログラミングの基本的な理解。
- Visual Studio がマシンにインストールされていること。
-  Aspose.3D for .NET ライブラリ (ダウンロード可能)[ここ](https://releases.aspose.com/3d/net/).
- 3D デザインを通じて創造性を解き放つことに純粋に興味がある方。
## 名前空間のインポート
まず、必要な名前空間をインポートして、.NET プロジェクトで Aspose.3D 機能を使用できるようにしましょう。
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
// Aspose.3D 名前空間をインポートする
```
すべての準備が整ったので、ファン シリンダーの作成プロセスを管理しやすい手順に分割してみましょう。
## ステップ 1: シーンを作成する
```csharp
//シーンを作成する
Scene scene = new Scene();
```
新しい 3D シーンを初期化することから始めます。これは、ファンシリンダーに命を吹き込むキャンバスとして機能します。
## ステップ 2: ファン シリンダーを作成する
```csharp
//円柱を作成する
var fan = new Cylinder(2, 2, 10, 20, 1, false);
```
半径、高さ、解像度などのパラメータを指定して、ファン シリンダの特性を定義します。
## ステップ 3: ファンシリンダーのプロパティをカスタマイズする
```csharp
//GenerateFanCylinder を true に設定します
fan.GenerateFanCylinder = true;
//ThetaLength を設定する
fan.ThetaLength = MathUtils.ToRadian(270);
```
ファン パーツの生成を有効にし、ThetaLength を使用して角度スイープを調整することで、ファン シリンダを調整します。
## ステップ 4: シーン内にファン シリンダーを配置します。
```csharp
//子ノードの作成
scene.RootNode.CreateChildNode(fan).Transform.Translation = new Vector3(10, 0, 0);
```
ファン シリンダーを子ノードとしてシーンのルート ノードに追加し、3D 空間内に配置します。
## ステップ 5: 非ファンシリンダーの作成
```csharp
//ファンのないシリンダーを作成する
var nonfan = new Cylinder(2, 2, 10, 20, 1, false);
```
ファン部分のない円柱を作成して、Aspose.3D の柔軟性を試してください。
## ステップ 6: 非ファンシリンダーのプロパティをカスタマイズする
```csharp
//GenerateFanCylinder を false に設定します
nonfan.GenerateFanCylinder = false;
//ThetaLength を設定する
nonfan.ThetaLength = MathUtils.ToRadian(270);
```
ファン部分の生成を無効にすることで、非ファンシリンダを区別します。
## ステップ 7: シーン内に非ファンシリンダーを配置します。
```csharp
//子ノードの作成
scene.RootNode.CreateChildNode(nonfan);
```
同様に、非ファン シリンダを子ノードとしてシーンのルート ノードに追加します。
## ステップ 8: シーンを保存する
```csharp
//シーンを保存する
scene.Save("Your Document Directory" + "CreateFanCylinder.obj", FileFormat.WavefrontOBJ);
```
傑作を希望の形式と場所に保存します。これで、Aspose.3D for .NET を使用してファン シリンダーと非ファン シリンダーを作成することができました。
## 結論
Aspose.3D for .NET を使用した 3D モデリングのハンズオン ガイドが完了しました。おめでとうございます。デジタル領域で創造力を発揮し、ファンやファン以外のシリンダーを簡単に作成できました。
## よくある質問
### Aspose.3D for .NET を他の .NET フレームワークと一緒に使用できますか?
はい、Aspose.3D はさまざまな .NET フレームワークと互換性があり、開発プロジェクトに多用途性を提供します。
### Aspose.3D for .NET に利用できる無料トライアルはありますか?
はい、無料トライアルを試すことができます[ここ](https://releases.aspose.com/).
### Aspose.3D for .NET の詳細なドキュメントはどこで見つけられますか?
ドキュメントは利用可能です[ここ](https://reference.aspose.com/3d/net/).
### Aspose.3D for .NET のサポートを受けるにはどうすればよいですか?
サポートフォーラムにアクセスしてください[ここ](https://forum.aspose.com/c/3d/18)コミュニティや Aspose の専門家からの支援が必要です。
### Aspose.3D for .NET の一時ライセンスは利用できますか?
はい、一時ライセンスを取得できます[ここ](https://purchase.aspose.com/temporary-license/).