---
title: Aspose.3D for Java を使用して 3D シーンをさまざまな形式で保存する
linktitle: Aspose.3D for Java を使用して 3D シーンをさまざまな形式で保存する
second_title: Aspose.3D Java API
description: Aspose.3D を使用して、Java での 3D シーン操作のシームレスな世界を探索してください。シーンをさまざまな形式で簡単に保存する方法を学びましょう。
weight: 15
url: /ja/java/load-and-save/save-3d-scenes/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose.3D for Java を使用して 3D シーンをさまざまな形式で保存する

## 導入

3D シーンの作成と操作はプログラミングの魅力的な側面ですが、強力な Aspose.3D for Java ライブラリを使用すると、このタスクはさらに魅力的かつ効率的になります。このチュートリアルでは、Aspose.3D for Java を使用して 3D シーンをさまざまな形式で保存するプロセスを説明します。経験豊富な開発者であっても、初心者であっても、このステップバイステップのガイドは、Aspose.3D の機能を活用して Java アプリケーションを強化するのに役立ちます。

## 前提条件

チュートリアルに入る前に、次の前提条件を満たしていることを確認してください。

- Java プログラミングの基本的な理解。
-  Java ライブラリ用の Aspose.3D がインストールされています。ダウンロードできます[ここ](https://releases.aspose.com/3d/java/).
- Java 開発環境がセットアップされています。

## パッケージのインポート

まず、Aspose.3D に必要なパッケージを Java プロジェクトにインポートします。

```java
import com.aspose.threed.*;
import com.aspose.threed.utils.MemoryStream;

```

## 3D シーンの保存

ここで、3D シーンを保存するプロセスを複数のステップに分けてみましょう。

### ステップ 1: ドキュメント ディレクトリを設定する

```java
// ExStart:SetDocumentDirectory
String myDir = "Your Document Directory";
// ExEnd:SetDocumentDirectory
```

### ステップ 2: 3D ドキュメントをロードする

```java
//ExStart:Load3DDocument
Scene scene = new Scene();
scene.open(myDir + "document.fbx");
// ExEnd:Load3DDocument
```

### ステップ 3: シーンをストリームに保存する

```java
//ExStart:SaveSceneToStream
try (MemoryStream dstStream = new MemoryStream()) {
    scene.save(dstStream, FileFormat.FBX7500ASCII);
}
// ExEnd:SaveSceneToStream
```

### ステップ 4: シーンをローカル パスに保存する

```java
//ExStart:SaveSceneToLocalPath
scene.save(myDir + "output_out.fbx", FileFormat.FBX7500ASCII);
// ExEnd:SaveSceneToLocalPath
```

### ステップ 5: 成功メッセージを印刷する

```java
// ExStart:PrintSuccessMessage
System.out.println("\nConverted 3D document to stream successfully.");
// ExEnd:PrintSuccessMessage
```

おめでとう！ Aspose.3D for Java を使用して 3D シーンが正常に保存されました。

## 結論

このチュートリアルでは、Aspose.3D for Java を使用して 3D シーンをさまざまな形式で保存する基本について説明しました。このライブラリの直感的な機能により、Java アプリケーションを美しい 3D グラフィックスで強化したいと考えている開発者にとって貴重なツールになります。

## よくある質問

### Q1: Aspose.3D for Java を他の Java ライブラリと一緒に使用できますか?

A1: はい、Aspose.3D for Java は他の Java ライブラリとシームレスに統合して機能を強化できます。

### Q2: 無料トライアルはありますか?

 A2: はい、無料トライアルにアクセスできます。[ここ](https://releases.aspose.com/).

### Q3: 詳細なドキュメントはどこで入手できますか?

A3: ドキュメントを参照してください。[ここ](https://reference.aspose.com/3d/java/).

### Q4: Java 用 Aspose.3D のサポートを受けるにはどうすればよいですか?

 A4: サポート フォーラムにアクセスしてください。[ここ](https://forum.aspose.com/c/3d/18).

### Q5: 一時ライセンスを購入できますか?

 A5: はい、一時ライセンスを購入できます。[ここ](https://purchase.aspose.com/temporary-license/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
