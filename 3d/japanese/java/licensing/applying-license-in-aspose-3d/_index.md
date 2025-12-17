---
date: 2025-12-17
description: Aspose.3D for Javaでライセンスを設定する方法と、メータリングライセンスのために公開鍵と秘密鍵を使用する方法を学びましょう。
linktitle: Applying a License in Aspose.3D for Java
second_title: Aspose.3D Java API
title: Aspose.3D for Java のライセンス設定方法 – 完全ガイド
url: /ja/java/licensing/applying-license-in-aspose-3d/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose.3D for Java のライセンス設定方法

## はじめに

ようこそ！このステップバイステップのチュートリアルでは、Java アプリケーションで Aspose.3D の **ライセンス設定方法** を学び、さらにメーター制ライセンス用の **公開鍵と秘密鍵の使用方法** も習得できます。Aspose.3D は 3D ファイル形式の操作を簡素化する強力な Java ライブラリで、有効なライセンスを取得するとすべての機能が解放されます。本ガイドの最後までに、任意の Java プロジェクトにシームレスにライセンスを統合できるようになります。

## クイック回答
- **ライセンスを設定する主な方法は何ですか？** `License` クラスを使用し、ファイルパスまたはストリームを渡して `setLicense` を呼び出します。  
- **ストリームからライセンスを読み込むことはできますか？** はい、`FileInputStream` が完全に機能します。  
- **公開鍵/秘密鍵の用途は何ですか？** `Metered` クラスを介してメーター制ライセンスを有効にします。  
- **開発にライセンスは必要ですか？** テストには一時的またはトライアルライセンスで十分です。本番環境ではフルライセンスが必要です。  
- **サポートされている Java バージョンはどれですか？** Aspose.3D は Java 6 以降で動作します。

## 前提条件

開始する前に、以下をご用意ください：

- Java プログラミングの基本的な理解
- プロジェクトに Aspose.3D ライブラリを追加済み。[release page](https://releases.aspose.com/3d/java/) からダウンロードしてください。
- 有効な `.lic` ファイルまたはメーター制の公開鍵と秘密鍵

## パッケージのインポート

Java ソースファイルに必要なインポートを追加します。Aspose.3D の JAR がクラスパスに含まれていることを確認してください。

```java
import com.aspose.threed.License;
import com.aspose.threed.Metered;

import java.io.FileInputStream;
import java.io.IOException;
```

## ファイルを使用したライセンス設定方法

### ステップ 1: ライセンスオブジェクトの作成

`License` クラスをインスタンス化します。このオブジェクトがライセンス情報を保持します。

```java
License license = new License();
```

### ステップ 2: ファイルからライセンスを設定

`.lic` ファイルへの相対パスまたは絶対パスを指定し、適用します。

```java
license.setLicense("Aspose._3D.lic");
```

> **プロのコツ:** ライセンスファイルはソース管理ディレクトリの外に置き、誤って公開されるのを防ぎましょう。

## ストリームを使用したライセンス設定方法

### ステップ 1: ライセンスオブジェクトの作成

前述と同様に、新しい `License` インスタンスを作成します。

```java
License license = new License();
```

### ステップ 2: ストリームからライセンスを設定

`License` ファイルを `FileInputStream` で読み込み、そのストリームを `setLicense` に渡します。try‑with‑resources ブロックにより、ストリームは自動的にクローズされます。

```java
try (FileInputStream myStream = new FileInputStream("Aspose._3D.lic")) {
    license.setLicense(myStream);
}
```

## メーター制ライセンスのための公開鍵・秘密鍵の使用方法

### ステップ 1: Metered ライセンスオブジェクトの初期化

メーター制（従量課金）ライセンスを扱う `Metered` クラスのインスタンスを作成します。

```java
Metered metered = new Metered();
```

### ステップ 2: 公開鍵と秘密鍵の設定

Aspose から提供されたキーを設定します。これらのキーにより、ライブラリは使用状況をライセンスサーバーに報告できるようになります。

```java
metered.setMeteredKey("your-public-key", "your-private-key");
```

> **警告:** 公開配布される JAR に秘密鍵をハードコードしないでください。安全な場所や環境変数から読み込むことを検討してください。

## 一般的なユースケース

- **エンタープライズ 3D レンダリングパイプライン** – ライセンス設定後に高性能 API を解放します。  
- **自動テスト環境** – 一時ライセンス（FAQ 参照）を使用して、フルライセンスを購入せずに機能を検証します。  
- **メーター制 SaaS ソリューション** – 公開鍵/秘密鍵を統合し、実際の使用量に基づいて顧客に課金します。  

## 結論

おめでとうございます！これで、ファイルやストリームを使用して Java で Aspose.3D の **ライセンス設定方法** と、メーター制ライセンスのために **公開鍵・秘密鍵を使用する方法** が分かりました。これらの手順に従えば、Aspose.3D を任意の Java アプリケーションに自信を持って統合し、3D 処理機能を最大限に活用できます。

## よくある質問

**Q1: Aspose.3D はすべての Java バージョンと互換性がありますか？**  
A1: はい、Aspose.3D は Java 6 以降のバージョンで動作します。

**Q2: 追加のドキュメントはどこで見つけられますか？**  
A2: ドキュメントは [here](https://reference.aspose.com/3d/java/) を参照してください。

**Q3: 購入前に Aspose.3D を試すことはできますか？**  
A3: はい、無料トライアルは [here](https://releases.aspose.com/) でご利用いただけます。

**Q4: Aspose.3D のサポートはどこで受けられますか？**  
A4: コミュニティおよび公式サポートは [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) をご覧ください。

**Q5: テスト用に一時ライセンスが必要ですか？**  
A5: はい、一時ライセンスは [here](https://purchase.aspose.com/temporary-license/) から取得してください。

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}
{{< blocks/products/products-backtop-button >}}

---

**Last Updated:** 2025-12-17  
**Tested With:** Aspose.3D 24.11 for Java  
**Author:** Aspose  

---