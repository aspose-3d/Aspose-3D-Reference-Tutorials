---
title: Java アプリケーションの 3D シーンから情報を取得する
linktitle: Java アプリケーションの 3D シーンから情報を取得する
second_title: Aspose.3D Java API
description: Aspose.3D を使用して、Java での 3D シーン操作の世界を探索してください。このチュートリアルでは、情報を取得する方法を段階的に説明します。
type: docs
weight: 12
url: /ja/java/3d-scenes-and-models/get-scene-information/
---
## 導入

Aspose.3D を使用して Java アプリケーションの 3D シーンから情報を取得するためのこの包括的なガイドへようこそ。 Java 開発者で、3D シーン操作によるアプリケーションの機能の強化を検討している場合は、ここが正しい場所です。このチュートリアルでは、プロセスを段階的にガイドし、各概念を完全に理解できるようにします。

## 前提条件

チュートリアルに入る前に、次のものが整っていることを確認してください。

- Java プログラミングの基本的な理解。
-  Aspose.3D ライブラリがインストールされています。そうでない場合は、ダウンロードしてください[ここ](https://releases.aspose.com/3d/java/).
- Java IDE (統合開発環境) がインストールされ、構成されている。

## パッケージのインポート

Java プロジェクトで、Aspose.3D 機能を利用するために必要なパッケージをインポートします。コードに次の行を追加します。

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
```

## ステップ 1: 3D シーンを初期化する

```java
//ExStart:シーンにアセット情報を追加
Scene scene = new Scene();
```

まず、Aspose.3D を使用して新しい 3D シーンを作成します。`Scene`クラス。

## ステップ 2: アプリケーションとベンダー情報を設定する

```java
scene.getAssetInfo().setApplicationName("Egypt");
scene.getAssetInfo().setApplicationVendor("Manualdesk");
```

3D シーンに関連付けられたアプリケーションとベンダー名を指定します。

## ステップ 3: 測定単位を定義する

```java
scene.getAssetInfo().setUnitName("pole");
scene.getAssetInfo().setUnitScaleFactor(0.6);
```

3D シーンの測定単位を定義します。この例では、古代エジプトの単位を使用します。

## ステップ 4: シーンをファイルに保存する

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "InformationToScene.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
//ExEnd:AddAssetInformationToScene
```

3D シーンを保存するディレクトリとファイル名を指定します。この例では、シーンを ASCII エンコーディングの FBX 形式で保存します。

## ステップ 5: 成功メッセージを印刷する

```java
System.out.println("\nAsset information added successfully to Scene.\nFile saved at " + MyDir);
```

アセット情報がシーンに正常に追加されたことを示す成功メッセージを表示します。

## 結論

おめでとう！ Aspose.3D を使用して Java アプリケーションの 3D シーンから情報を取得する方法を学習しました。この強力なライブラリは、没入型 3D コンテンツで Java プロジェクトを強化するための無限の可能性を開きます。

## よくある質問

### Q1: Aspose.3D はすべての Java IDE と互換性がありますか?

A1: はい、Aspose.3D はすべての主要な Java IDE とシームレスに動作するように設計されています。

### Q2: Aspose.3D を商用プロジェクトに使用できますか?

A2: もちろんです。 Aspose.3D は開発者に商用ライセンスを提供し、ライセンス要件を確実に遵守できるようにします。

### Q3: Aspose.3D の追加サポートはどこで見つけられますか?

 A3: ご質問やサポートが必要な場合は、次のサイトにアクセスしてください。[Aspose.3D フォーラム](https://forum.aspose.com/c/3d/18).

### Q4: Aspose.3D の無料トライアルはありますか?

 A4: はい、無料トライアルを利用して機能を試すことができます。[ここ](https://releases.aspose.com/).

### Q5: Aspose.3D の一時ライセンスを取得するにはどうすればよいですか?

 A5: テスト目的で一時ライセンスを取得します。[ここ](https://purchase.aspose.com/temporary-license/).