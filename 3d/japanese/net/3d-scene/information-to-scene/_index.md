---
date: 2026-03-26
description: Aspose.3D for .NET を使用して、3D シーンにベンダー情報を追加する方法と FBX ファイルを保存する方法を学びましょう。実行可能なコードが用意されたステップバイステップのガイドに従ってください。
linktitle: Extracting Information to Scene Assets
second_title: Aspose.3D .NET API
title: Aspose.3D を使用してベンダー情報を追加し、FBX シーンを保存する方法
url: /ja/net/3d-scene/information-to-scene/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose.3D を使用してベンダー情報を追加し FBX シーンを保存する方法

## はじめに

この包括的なチュートリアルへようこそ。**ベンダー**情報を 3D シーンに追加し、続いて Aspose.3D for .NET を使用して **FBX** ファイルを保存する方法を解説します。建築ビジュアライゼーション、ゲームアセット、エンジニアリングモデルのいずれを作成する場合でも、ベンダーやアプリケーションのメタデータを埋め込むことで、シーンがより情報豊富になり、下流での管理が容易になります。手順を順に見ていきましょう。

## クイック回答
- **「ベンダーを追加する」とは何ですか？** シーンの `AssetInfo` ブロック内にアプリケーション名とベンダー名を格納します。  
- **どのフォーマットがベンダー情報に対応していますか？** FBX（ASCII またはバイナリ）は保存時にメタデータを保持します。  
- **FBX を保存するには？** `scene.Save(path, FileFormat.FBX7500ASCII)` またはバイナリ版を使用します。  
- **ライセンスは必要ですか？** 開発用には無料トライアルで動作しますが、製品版には商用ライセンスが必要です。  
- **測定単位は変更できますか？** はい、`AssetInfo.UnitName` と `AssetInfo.UnitScaleFactor` を設定します。

## 3D シーンで「ベンダー情報を追加する」とは何か？
ベンダー情報を追加するとは、`Scene` オブジェクトの `AssetInfo` プロパティに値を設定することです。これらのプロパティはファイルに同梱され、FBX ファイルの受取側は作成アプリケーションやベンダーを確認できます。

## ベンダー情報を追加する理由
- **トレーサビリティ:** 大規模パイプラインでモデルの出所をすばやく特定できます。  
- **コンプライアンス:** 業界によっては資産管理のために明示的なベンダータグ付けが求められます。  
- **自動化:** スクリプトがベンダーメタデータに基づいてファイルをフィルタリングまたは処理できます。

## 前提条件

- Aspose.3D for .NET がインストールされていること。ダウンロードは [Aspose.3D for .NET ページ](https://releases.aspose.com/3d/net/) から行えます。

## 名前空間のインポート

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
```

## ベンダー情報の追加方法

### 手順 1: 3D シーンの初期化

```csharp
Scene scene = new Scene();
```

新しい `Scene` を作成すると、作業用のクリーンなキャンバスが得られます。

### 手順 2: アプリケーションとベンダー情報の設定

```csharp
scene.AssetInfo.ApplicationName = "Egypt";
scene.AssetInfo.ApplicationVendor = "Manualdesk";
```

ここでは **ベンダー情報を追加する** 方法として、`ApplicationName` と `ApplicationVendor` に意味のある文字列を割り当てています。

### 手順 3: 測定単位の定義

```csharp
scene.AssetInfo.UnitName = "pole";
scene.AssetInfo.UnitScaleFactor = 0.6;
```

単位系を指定することで、FBX ファイルを開くすべてのユーザーが正しい寸法で解釈できます。この例では、1 本の「ポール」が 60 cm に相当します。

## FBX シーンの保存方法

### 手順 4: シーンの保存（FBX の保存方法）

```csharp
var output = "Your Output Directory" + "InformationToScene.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

この行は **FBX を保存する** 方法を示しており、FBX 7.5.0 の ASCII バージョンを使用しています。バイナリ版が必要な場合は `FBX7500ASCII` を `FBX7500Binary` に置き換えてください。

> **プロのコツ:** ファイル拡張子 `.fbx` は選択したフォーマットと一致させてください。そうしないと、一部のビューアが内容を誤って解釈する可能性があります。

### 手順 5: 成功メッセージの表示

```csharp
Console.WriteLine("\nAsset information added successfully to Scene.\nFile saved at " + output);
```

コンソールに表示されるフレンドリーなメッセージは、ベンダーメタデータが含まれたシーンがディスクに正常に書き込まれたことを確認します。

## よくある問題と対策

| 問題 | 解決策 |
|------|--------|
| **ビューアにベンダー情報が表示されない** | **FBX ASCII** または **Binary** で保存したことを確認してください。古いビューアは片方の形式しか読めないことがあります。 |
| **パスにスペースが含まれる** | パスを引用符で囲むか、`Path.Combine` を使用して安全なファイルパスを構築してください。 |
| **単位スケールが正しくない** | `UnitScaleFactor` を再確認してください。これはメートルに対する倍率です。 |
| **ライセンス例外が発生** | テストには無料トライアルを使用し、製品版では正式なライセンスを取得してください。 |

## FAQ（よくある質問）

**Q: Aspose.3D for .NET を他のプログラミング言語で使用できますか？**  
A: Aspose.3D は主に .NET 言語をサポートしていますが、他言語向けの相互運用オプションを検討できます。

**Q: Aspose.3D for .NET の無料トライアルはありますか？**  
A: はい、無料トライアルは [こちら](https://releases.aspose.com/) から入手できます。

**Q: Aspose.3D に関するサポートはどこで受けられますか？**  
A: コミュニティとサポートは [Aspose.3D フォーラム](https://forum.aspose.com/c/3d/18) で提供されています。

**Q: Aspose.3D for .NET の一時ライセンスは購入できますか？**  
A: はい、一時ライセンスは [こちら](https://purchase.aspose.com/temporary-license/) から取得可能です。

**Q: Aspose.3D for .NET の詳細なドキュメントはどこにありますか？**  
A: 詳細情報は [ドキュメント](https://reference.aspose.com/3d/net/) を参照してください。

---

**最終更新日:** 2026-03-26  
**テスト環境:** Aspose.3D 24.11 for .NET  
**作者:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}