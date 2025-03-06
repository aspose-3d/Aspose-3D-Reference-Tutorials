---
title: CancelToken の使用
linktitle: CancelToken の使用
second_title: Aspose.3D .NET API
description: Aspose.3D for .NET を使用して、シームレスな 3D モデリングの世界を探索してください。 CancelToken を使用して 3D ドキュメントを効率的にロードおよび保存する方法を学びます。
weight: 10
url: /ja/net/loading-and-saving/cancellation-token/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# CancelToken の使用

## 導入

Aspose.3D for .NET を利用して 3D モデリングおよびレンダリング プロジェクトを強化するための包括的なガイドへようこそ。 Aspose.3D は、.NET 開発者が 3D ファイルをシームレスに操作できるようにする強力なライブラリです。このチュートリアルでは、読み込みと保存の側面を詳しく掘り下げ、特に非同期タスクを効率的に管理するための CancelToken の使用法に焦点を当てます。

## 前提条件

この作業を開始する前に、次の前提条件が満たされていることを確認してください。

-  Aspose.3D for .NET: からライブラリをダウンロードしてインストールします。[ここ](https://releases.aspose.com/3d/net/).
- .NET 環境: 互換性のある .NET 開発環境がセットアップされていることを確認します。
- C# の基本的な理解: C# プログラミング言語に精通していることが推奨されます。

## 名前空間のインポート

開始するには、プロジェクトに必要な名前空間が含まれていることを確認してください。これらの名前空間は、3D ファイル操作に必要な機能へのアクセスを提供します。

```csharp
using Aspose.ThreeD;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
```

## ロードと保存 - cancelToken の使用

### ステップ 1: cancelanceTokenSource を作成する

```csharp
//ExStart:CancelTokenSource

CancellationTokenSource cts = new CancellationTokenSource();
```

ここでは、非同期操作でのキャンセルを管理するための重要なコンポーネントである cancelTokenSource をインスタンス化します。

### ステップ 2: 3D シーンを初期化する

```csharp
Scene scene = new Scene();
```

Scene クラスのインスタンスを作成します。これが 3D モデリング活動のキャンバスになります。

### ステップ 3: CancelToken タイムアウトを設定する

```csharp
cts.CancelAfter(1000);
```

キャンセルタイムアウトを設定するには、`CancelAfter`方法。この例では、タイムアウトは 1000 ミリ秒 (1 秒) に設定されています。

### ステップ 4: 3D ドキュメントを開く

```csharp
try
{
    scene.Open("Your Output Directory" + "document.fbx", cts.Token);
    Console.WriteLine("Import is done within 1000ms");
}
catch (ImportException e)
{
    if (e.InnerException is OperationCanceledException)
    {
        Console.WriteLine("It takes too long time to import, import has been canceled.");
    }
}
```

指定された時間枠内で 3D ドキュメントを開こうとします。の`cts.Token`パラメータを使用すると、設定されたタイムアウトを超えた場合に操作をキャンセルできるようになります。

### ステップ 5: インポート例外を処理する

ImportException が発生した場合は、OperationCanceledException が原因かどうかを確認して適切に処理します。

```csharp
catch (ImportException e)
{
    if (e.InnerException is OperationCanceledException)
    {
        Console.WriteLine("It takes too long time to import, import has been canceled.");
    }
}
// ExEnd:CancelTokenSource
```

## 結論

おめでとう！ Aspose.3D for .NET と CancelToken を使用して 3D ドキュメントの読み込みを管理するプロセスを正常に完了しました。この手法により、効率的かつタイムリーなインポート操作が保証され、3D アプリケーションの全体的なパフォーマンスが向上します。

## よくある質問

### Q1: Aspose.3D はすべての 3D ファイル形式と互換性がありますか?

 A1: Aspose.3D は、FBX、STL、OBJ などを含む幅広い 3D ファイル形式をサポートしています。を参照してください。[ドキュメンテーション](https://reference.aspose.com/3d/net/)完全なリストについては、

### Q2: Aspose.3D の一時ライセンスを取得するにはどうすればよいですか?

 A2: 訪問して仮免許を取得してください。[このリンク](https://purchase.aspose.com/temporary-license/).

### Q3: Aspose.3D のサポートはどこで見つけられますか?

 A3: コミュニティ ディスカッションに参加してください。[Aspose.3D フォーラム](https://forum.aspose.com/c/3d/18).

### Q4: 購入する前に、Aspose.3D を無料で試すことはできますか?

 A4: はい、無料トライアルを利用して機能を試してください。[ここ](https://releases.aspose.com/).

### Q5: Aspose.3D for .NET の最新バージョンは何ですか?

 A5: をチェックして最新の状態を維持してください。[ダウンロードページ](https://releases.aspose.com/3d/net/)最新リリース用。
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
