---
title: 点群として PLY 形式にエクスポート
linktitle: 点群として PLY 形式にエクスポート
second_title: Aspose.3D .NET API
description: Aspose.3D for .NET を使用して 3D モデリングの世界を探索してください。モデルを PLY 形式に簡単にエクスポートする方法を学びましょう。素晴らしいビジュアルでプロジェクトを向上させます。
type: docs
weight: 16
url: /ja/net/working-with-point-cloud/export-to-ply-point-cloud/
---
## 導入
3D モデリングと開発の動的な世界では、Aspose.3D for .NET は強力なツールキットとして際立っています。このチュートリアルでは、Aspose.3D for .NET を使用して 3D モデルを点群として PLY 形式にエクスポートするプロセスを説明します。素晴らしいビジュアルでプロジェクトを強化する準備ができている場合は、この手順に従って、この多用途ライブラリの可能性を最大限に引き出してください。
## 前提条件
チュートリアルに入る前に、次の前提条件が満たされていることを確認してください。
-  Aspose.3D for .NET: からライブラリをダウンロードしてインストールします。[ダウンロードページ](https://releases.aspose.com/3d/net/).
- 開発環境: Visual Studio など、好みの .NET 開発環境をセットアップします。
## 名前空間のインポート
Aspose.3D for .NET の使用を開始するには、プロジェクトに必要な名前空間をインポートします。
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```
## ステップ 1: 3D モデルを作成する
まず、点群としてエクスポートする 3D モデルを作成します。たとえば、球を作成してみましょう。
```csharp
Sphere sphere = new Sphere();
```
## ステップ 2: エクスポート設定を定義する
ファイル形式 (PLY) を含むエクスポート設定を指定し、点群エクスポートを有効にします。
```csharp
PlySaveOptions saveOptions = new PlySaveOptions() { PointCloud = true };
```
## ステップ 3: エクスポート パスを設定する
エクスポートした PLY ファイルを保存するディレクトリを決定します。
```csharp
string exportPath = "Your Document Directory" + "sphere.ply";
```
## ステップ 4: エンコードしてエクスポートする
を活用してください。`Encode`3D モデルを PLY 形式にエクスポートする方法:
```csharp
FileFormat.PLY.Encode(sphere, exportPath, saveOptions);
```
## 結論
おめでとう！ Aspose.3D for .NET を使用して、3D モデルを点群として PLY 形式にエクスポートできました。これにより、没入型ビジュアルをアプリケーションに統合するための無限の可能性が開かれます。

## よくある質問
### 1. Aspose.3D はすべての .NET フレームワークと互換性がありますか?
Aspose.3D はさまざまな .NET フレームワークをサポートし、幅広い開発環境にわたる互換性を保証します。
### 2. Aspose.3D を商用プロジェクトに使用できますか?
絶対に！ Aspose.3D は、商用利用を含む柔軟なライセンス オプションを提供します。をチェックしてください[購入ページ](https://purchase.aspose.com/buy)詳細については。
### 3. Aspose.3D のサポートを得るにはどうすればよいですか?
訪問[Aspose.3D フォーラム](https://forum.aspose.com/c/3d/18)コミュニティとつながり、専門家の支援を受けることができます。
### 4. 無料トライアルはありますか?
はい、機能を調べてください[無料トライアル](https://releases.aspose.com/)約束をする前に。
### 5. 一時ライセンスを取得するにはどうすればよいですか?
一時ライセンスのオプションについては、次のサイトをご覧ください。[このリンク](https://purchase.aspose.com/temporary-license/).