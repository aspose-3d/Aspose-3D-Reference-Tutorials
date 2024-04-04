---
title: シーンのすべてのメッシュをマテリアルごとに分割する
linktitle: シーンのすべてのメッシュをマテリアルごとに分割する
second_title: Aspose.3D .NET API
description: Aspose.3D for .NET を使用して 3D メッシュをマテリアルごとに分割する方法を学びます。 3D モデルの効率的な編成と管理については、ステップバイステップのガイドに従ってください。
type: docs
weight: 21
url: /ja/net/meshes/split-all-meshes-by-material/
---
## 導入
Aspose.3D for .NET を使用して 3D シーンのすべてのメッシュをマテリアルごとに分割するためのこのステップバイステップ ガイドへようこそ。 3D モデルを操作していて、マテリアルに基づいてメッシュを効率的に編成したい場合は、このチュートリアルが最適です。 Aspose.3D は、3D ファイルを操作するためのさまざまな機能を提供する強力な .NET ライブラリであり、開発者にとって優れた選択肢となります。
## 前提条件
チュートリアルに入る前に、次の前提条件を満たしていることを確認してください。
- C# プログラミング言語の基本的な理解。
- Visual Studio がマシンにインストールされていること。
-  .NET ライブラリの Aspose.3D。からダウンロードできます[ここ](https://releases.aspose.com/3d/net/).
- 分割する入力 3D ファイル (「test.fbx」など)。
## 名前空間のインポート
まず、C# プロジェクトに必要な名前空間をインポートします。
```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
```
## ステップ 1: 3D ファイルをロードする
```csharp
//ドキュメントディレクトリへのパス。
string input = RunExamples.GetDataFilePath("test.fbx");
// 3D ファイルをロードする
Scene scene = new Scene(input);
```
このステップでは、Aspose.3D を使用して 3D ファイルをロードします。`Scene`クラス。
## ステップ 2: すべてのメッシュを分割する
```csharp
//すべてのメッシュを分割する
PolygonModifier.SplitMesh(scene, SplitMeshPolicy.CloneData);
```
ここで使用するのは、`SplitMesh`からのメソッド`PolygonModifier`マテリアルに基づいてすべてのメッシュを分割するクラス。
## ステップ 3: 分割シーンを保存する
```csharp
//ファイルを保存
var output = "Your Output Directory" + "test-splitted.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```
変更を保持するには、変更したシーンを新しいファイルに保存します。
## ステップ 4: 成功メッセージを表示する
```csharp
//成功メッセージを表示する
Console.WriteLine("\nSplitting all meshes of a scene per material successfully.\nFile saved at " + output);
```
操作が正常に完了したことを示す成功メッセージを出力します。
## 結論
おめでとう！ Aspose.3D for .NET を使用して、3D シーンのすべてのメッシュをマテリアルごとに分割する方法を学習しました。これは、複雑な 3D モデルを整理および管理するための貴重なテクニックとなります。
## よくある質問
### 1. Aspose.3D for .NET を他のプログラミング言語で使用できますか?
Aspose.3D は主に .NET 用に設計されていますが、.NET 言語バインディングを通じて他の言語との相互運用性を提供します。
### 2. 試用版はありますか?
はい、無料試用版にアクセスできます[ここ](https://releases.aspose.com/).
### 3. 他の例やドキュメントはどこで入手できますか?
次の場所にある包括的なドキュメントを参照してください。[Aspose.3D ドキュメント](https://reference.aspose.com/3d/net/).
### 4. Aspose.3D のサポートを得るにはどうすればよいですか?
訪問[Aspose.3D フォーラム](https://forum.aspose.com/c/3d/18)コミュニティのサポートとディスカッションのために。
### 5. 一時ライセンスを取得できますか?
はい、仮免許を取得できます[ここ](https://purchase.aspose.com/temporary-license/).