---
date: 2025-12-05
description: Aspose.3D for Javaで、オフセットされたトップを持つシリンダーモデルの作成方法を学び、子ノードを追加するJavaの手順を実行し、3DモデルのOBJファイルを簡単にエクスポートできます。
language: ja
linktitle: How to Create Cylinder with Offset Top in Aspose.3D for Java
second_title: Aspose.3D Java API
title: Aspose.3D for Javaでオフセットトップのシリンダーを作成する方法
url: /java/cylinders/creating-cylinders-with-offset-top/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose.3D for Javaでオフセットトップ付きシリンダーを作成する方法

## はじめに

Javaベースの3Dシーンでカスタムオフセットトップを持つ**how to create cylinder**オブジェクトを作成したい場合、Aspose.3Dはプロセスをシンプルにします。このチュートリアルでは、シーンの設定から最終モデルをOBJファイルとしてエクスポートするまでのすべての手順を解説し、オフセットトップ付きシリンダーを自信を持ってアプリケーションに統合できるようにします。

## クイック回答
- **使用されているライブラリは？** Aspose.3D for Java  
- **シリンダーのトップをオフセットできますか？** はい、`setOffsetTop` を使用します  
- **Javaで子ノードを追加するには？** ルートノードで `createChildNode` を呼び出します  
- **どの形式にエクスポートできますか？** Wavefront OBJ（`export 3d model obj`）  
- **テスト用にライセンスが必要ですか？** 評価用の一時ライセンスが利用可能です  

## オフセットトップ付きシリンダーとは何ですか？

オフセットトップ付きシリンダーを作成するとは、上部の円形面が基部に対してずれている状態を指し、手動で頂点を操作せずにテーパー形状や非対称形状をモデリングできます。Aspose.3Dは専用のコンストラクタと `OffsetTop` プロパティを提供しており、数行のコードで実現できます。

## なぜ Aspose.3D for Java を使用するのか？

- **High‑level API:** 低レベルのメッシュデータを管理する必要がありません。  
- **Cross‑platform:** 任意のJVM互換環境で動作します。  
- **Built‑in exporters:** OBJ、STL、FBX などに直接保存できます。  
- **Extensible:** 子ノードの追加、変換の適用、他のJavaライブラリとの統合が容易です。

## 前提条件

始める前に以下を用意してください：

- **Java Development Kit (JDK)** – 互換性のあるバージョンをインストール。  
- **Aspose.3D for Java library** – 公式サイトから最新のJARをダウンロードしてください [here](https://releases.aspose.com/3d/java/)。  
- お好みのIDE（Eclipse、IntelliJ IDEA、NetBeans など）。

## パッケージのインポート

まず、必要なクラスをインポートします。これらのステートメントをJavaファイルの先頭に配置してください。

```java
import com.aspose.threed.Cylinder;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Vector3;


import java.io.IOException;
```

## ステップバイステップガイド

### ステップ 1: シーンの作成

シーンはすべての3Dオブジェクトのコンテナとして機能します。

```java
// ExStart:1
// Create a scene
Scene scene = new Scene();
// ExEnd:1
```

### ステップ 2: オフセットトップ付きシリンダーの初期化

ここでは**how to create cylinder**にカスタムオフセットを適用する方法を示します。コンストラクタで半径、高さ、スライス、スタック、シリンダーが閉じているかどうかを定義し、その後 `setOffsetTop` で上部をシフトします。

```java
// ExStart:2
// Initialize cylinder
Cylinder cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
// Set OffsetTop
cylinder1.setOffsetTop(new Vector3(5, 3, 0));
// ExEnd:2
```

### ステップ 3: Javaで**add child node Java**する方法 – 最初のシリンダーをアタッチ

シーンのルートノードの下に子ノードを作成し、シリンダーを目的の位置に移動します。

```java
// ExStart:3
// Create ChildNode
scene.getRootNode().createChildNode(cylinder1).getTransform().setTranslation(10, 0, 0);
// ExEnd:3
```

### ステップ 4: 2 番目のシリンダーの初期化（オフセットなし）

比較のため、オフセットなしの通常シリンダーを追加します。

```java
// ExStart:4
// Initialize second cylinder without customized OffsetTop
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// ExEnd:4
```

### ステップ 5: Javaで**add child node Java**する方法 – 2 番目のシリンダーをアタッチ

```java
// ExStart:5
// Create ChildNode
scene.getRootNode().createChildNode(cylinder2);
// ExEnd:5
```

### ステップ 6: Javaで**export 3d model OBJ**する方法 – シーンを保存

最後に、両方のシリンダーを含むシーン全体をWavefront OBJファイルとしてエクスポートします。OBJは多くの3Dツールで広くサポートされています。

```java
// ExStart:6
// Save
scene.save("Your Document Directory" + "CustomizedOffsetTopCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

プログラムを実行すると、指定したディレクトリに `CustomizedOffsetTopCylinder.obj` が生成され、Blender、Maya、その他OBJ対応ビューアで開くことができます。

## 一般的な問題と解決策

| 問題 | 原因 | 対策 |
|-------|--------|-----|
| **OBJ file is empty** | シーンが正しく保存されていない、またはパスが間違っている。 | 出力ディレクトリが存在し、書き込み権限があることを確認してください。 |
| **Offset not applied** | 古いバージョンの Aspose.3D を使用している。 | `setOffsetTop` がサポートされている最新のライブラリに更新してください。 |
| **Child node not visible** | 変換が適用されていない。 | 子ノード作成後に `getTransform().setTranslation` を呼び出していることを確認してください。 |

## よくある質問

**Q: Aspose.3D はさまざまな Java IDE と互換性がありますか？**  
A: はい、Eclipse、IntelliJ IDEA、NetBeans などのIDEでシームレスに動作します。

**Q: 作成した3Dオブジェクトにテクスチャを適用できますか？**  
A: もちろんです！`Material` クラスを使用してテクスチャや表面プロパティを割り当てます。

**Q: Aspose.3D のライセンスオプションはありますか？**  
A: さまざまなライセンスモデルが用意されており、詳細は [here](https://purchase.aspose.com/buy) で確認できます。

**Q: サポートや情報共有はどこで行えますか？**  
A: Aspose.3D コミュニティフォーラム [here](https://forum.aspose.com/c/3d/18) に参加してサポートやディスカッションが可能です。

**Q: テスト用の一時ライセンスは入手できますか？**  
A: はい、評価用の一時ライセンスは [here](https://purchase.aspose.com/temporary-license/) から取得できます。

---

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---
**Last Updated:** 2025-12-05  
**Tested With:** Aspose.3D for Java 24.12 (latest)  
**Author:** Aspose