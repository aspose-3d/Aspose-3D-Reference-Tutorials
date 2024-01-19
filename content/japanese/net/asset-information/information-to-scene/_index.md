---
title: シーンアセットへの情報の抽出
linktitle: シーンアセットへの情報の抽出
second_title: Aspose.3D .NET API
description: Aspose.3D for .NET を使用して 3D シーンを簡単に強化します。貴重な資産情報を追加する方法を段階的に学習します。今すぐダウンロードして、ダイナミックな 3D 体験を体験してください。
type: docs
weight: 10
url: /ja/net/asset-information/information-to-scene/
---
## 導入

Aspose.3D for .NET を使用して貴重な情報を抽出し、3D シーンを強化するためのこの包括的なチュートリアルへようこそ。 Aspose.3D は、開発者が .NET アプリケーション内で 3D シーンをシームレスに操作できるようにする強力なライブラリです。このチュートリアルでは、シーンにアセット情報を追加するという重要なタスクに焦点を当てます。

## 前提条件

チュートリアルに入る前に、次の前提条件を満たしていることを確認してください。

- Aspose.3D for .NET: ライブラリがインストールされていることを確認してください。からダウンロードできます。[Aspose.3D for .NET ページ](https://releases.aspose.com/3d/net/).

## 名前空間のインポート

.NET プロジェクトには、Aspose.3D 機能にアクセスするために必要な名前空間が含まれていることを確認してください。

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
```

## ステップ 1: 3D シーンを初期化する

```csharp
Scene scene = new Scene();
```

を使用して新しい 3D シーンを作成します。`Scene`クラス。

## ステップ 2: アプリケーションとベンダー情報を設定する

```csharp
scene.AssetInfo.ApplicationName = "Egypt";
scene.AssetInfo.ApplicationVendor = "Manualdesk";
```

3D シーンに関連付けられたアプリケーション名とベンダー名を定義します。

## ステップ 3: 測定単位を定義する

```csharp
scene.AssetInfo.UnitName = "pole";
scene.AssetInfo.UnitScaleFactor = 0.6;
```

シーンで使用される測定単位を指定します。この例では、「ポール」と呼ばれる古代エジプトの単位を使用しており、1 ポールは 60 cm に相当します。

## ステップ 4: シーンを保存する

```csharp
var output = "Your Output Directory" + "InformationToScene.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

アセット情報を追加したシーンを 3D サポートのファイル形式で保存します。必要に応じて出力ディレクトリを調整します。

## ステップ 5: 成功メッセージを表示する

```csharp
Console.WriteLine("\nAsset information added successfully to Scene.\nFile saved at " + output);
```

資産情報が正常に追加され、ファイルが保存されたことをユーザーに通知します。

## 結論

おめでとう！ Aspose.3D for .NET を使用して重要なアセット情報を抽出し、3D シーンに追加する方法を学習しました。この知識により、より有益で魅力的な 3D コンテンツを作成するための無限の可能性が開かれます。

## よくある質問

### Q1: Aspose.3D for .NET を他のプログラミング言語で使用できますか?

A1: Aspose.3D は主に .NET 言語をサポートしていますが、他の言語の相互運用性オプションを検討することもできます。

### Q2: Aspose.3D for .NET の無料トライアルはありますか?

 A2: はい、無料トライアルにアクセスできます。[ここ](https://releases.aspose.com/).

### Q3: Aspose.3D 関連のクエリのサポートを受けるにはどうすればよいですか?

 A3: にアクセスしてください。[Aspose.3D フォーラム](https://forum.aspose.com/c/3d/18)コミュニティとサポートのために。

### Q4: Aspose.3D for .NET の一時ライセンスを購入できますか?

 A4: はい、一時ライセンスを取得できます。[ここ](https://purchase.aspose.com/temporary-license/).

### Q5: Aspose.3D for .NET の詳細なドキュメントはどこで見つけられますか?

 A5: を参照してください。[ドキュメンテーション](https://reference.aspose.com/3d/net/)詳細な情報については。