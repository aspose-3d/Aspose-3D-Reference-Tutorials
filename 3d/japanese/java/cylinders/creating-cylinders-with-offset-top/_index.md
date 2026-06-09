---
date: 2026-04-08
description: Aspose.3D for Javaでオフセットされた上部を持つシリンダーの作成方法を学び、子ノードを追加し、上部オフセットを設定して3Dモデルを生成し、Asposeの一時ライセンスを使用してOBJ形式でエクスポートします。
keywords:
- aspose temporary license
- generate 3d model
- add child node java
- java export obj
- set offset top
linktitle: Aspose 一時ライセンス – オフセットトップでシリンダーを作成 (Java)
second_title: Aspose.3D Java API
title: Aspose 一時ライセンス – オフセットトップ付きシリンダーの作成 (Java)
url: /ja/java/cylinders/creating-cylinders-with-offset-top/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose 一時ライセンス – オフセットトップ付きシリンダーの作成 (Java)

## はじめに

Java ベースの 3D シーンでカスタム オフセットトップを持つ **create cylinder** オブジェクトを作成したい場合、Aspose.3D はプロセスをシンプルにします。このチュートリアルでは、シーンの設定から最終モデルを OBJ ファイルとしてエクスポートするまでのすべての手順を順に説明しますので、オフセットトップ シリンダーを自信を持ってアプリケーションに統合できます。ガイドの最後までに、**aspose temporary license** がフル購入なしでこれらの機能を評価できることも理解できるようになります。

## クイック回答

- **使用されているライブラリは何ですか？** Aspose.3D for Java  
- **シリンダーのトップをオフセットできますか？** Yes, using `setOffsetTop`  
- **Java で子ノードを追加するには？** Call `createChildNode` on the root node  
- **エクスポートできるフォーマットは？** Wavefront OBJ (`java export obj`)  
- **テストにライセンスは必要ですか？** An **aspose temporary license** is available for evaluation  

## Aspose 一時ライセンスとは？

**aspose temporary license** は、開発およびテスト中に Aspose.3D for Java のフル機能セットを解放する、短期間の無料評価キーです。評価用の透かしが除去され、OBJ、STL、FBX などの 3D モデルファイルを有料ライセンスと同様に生成できます。

## なぜ Aspose.3D for Java を使用するのか？

- **High‑level API:** 低レベルのメッシュデータを管理する必要はありません。  
- **Cross‑platform:** 任意の JVM 互換環境で動作します。  
- **Built‑in exporters:** OBJ、STL、FBX などに直接保存できます。  
- **Extensible:** 子ノードの追加や変換の適用、他の Java ライブラリとの統合が容易です。  

## 前提条件

- **Java Development Kit (JDK)** – 互換バージョンがインストールされていること。  
- **Aspose.3D for Java library** – 公式サイトから最新の JAR をダウンロードしてください [here](https://releases.aspose.com/3d/java/)。  
- 好みの IDE (Eclipse、IntelliJ IDEA、NetBeans など)。  

## パッケージのインポート

まず、必要なクラスをインポートします。これらのステートメントを Java ファイルの先頭に配置してください。

```java
import com.aspose.threed.Cylinder;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Vector3;


import java.io.IOException;
```

## ステップバイステップガイド

### Step 1: Java 3D シーンの作成

**java 3d scene** はすべての 3D オブジェクトのコンテナとして機能します。

```java
// ExStart:1
// Create a scene
Scene scene = new Scene();
// ExEnd:1
```

### Step 2: オフセットトップ付きシリンダーの初期化

ここでは、カスタムオフセットを持つ **how to create cylinder** について説明します。コンストラクタで半径、高さ、スライス、スタック、シリンダーが閉じているかどうかを定義します。その後、`setOffsetTop` を使用してトップをシフトします。

```java
// ExStart:2
// Initialize cylinder
Cylinder cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
// Set OffsetTop
cylinder1.setOffsetTop(new Vector3(5, 3, 0));
// ExEnd:2
```

### Step 3: 子ノードの追加 Java – 最初のシリンダーをアタッチ

シーンのルートノードの下に子ノードを作成し、シリンダーを目的の位置に移動します。

```java
// ExStart:3
// Create ChildNode
scene.getRootNode().createChildNode(cylinder1).getTransform().setTranslation(10, 0, 0);
// ExEnd:3
```

### Step 4: 2 番目のシリンダーの初期化（オフセットなし）

比較のため、オフセットなしの通常のシリンダーを追加します。

```java
// ExStart:4
// Initialize second cylinder without customized OffsetTop
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// ExEnd:4
```

### Step 5: 子ノードの追加 Java – 2 番目のシリンダーをアタッチ

```java
// ExStart:5
// Create ChildNode
scene.getRootNode().createChildNode(cylinder2);
// ExEnd:5
```

### Step 6: Java Export OBJ – シーンを OBJ として保存

最後に、シーン全体（両方のシリンダー）を Wavefront OBJ ファイルとして **java export obj** します。この形式は 3D ツールで広くサポートされています。

```java
// ExStart:6
// Save
scene.save("Your Document Directory" + "CustomizedOffsetTopCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

プログラムを実行すると、指定したディレクトリに `CustomizedOffsetTopCylinder.obj` が生成され、Blender、Maya、またはその他の OBJ 対応ビューアで開くことができます。

## Java で 3D モデルを生成し OBJ にエクスポートする方法

`Scene.save(..., FileFormat.WAVEFRONTOBJ)` と **aspose temporary license** の組み合わせにより、外部コンバータを必要とせずに **generate 3d model** ファイルを迅速に作成できます。これは、プロトタイピング時やデザイナーとアセットを共有する際に特に便利です。

## 実際の使用例

- **Architectural visualisation:** オフセットトップシリンダーは天井に向かって細くなる柱をモデル化します。  
- **Mechanical parts:** トップ面が意図的にシフトされたピストンやギアハウジングを作成します。  
- **Game assets:** 手作業のメッシュが不要になるように、リアルタイムで多様な柱形状を生成します。  

## 一般的な問題と解決策

| 問題 | 原因 | 対策 |
|-------|--------|-----|
| **OBJ ファイルが空です** | シーンが正しく保存されていないか、パスが間違っています。 | 出力ディレクトリが存在し、書き込み権限があることを確認してください。 |
| **オフセットが適用されていません** | 古い Aspose.3D バージョンを使用しています。 | `setOffsetTop` がサポートされている最新のライブラリに更新してください。 |
| **子ノードが表示されません** | 変換が適用されていません。 | 子ノード作成後に `getTransform().setTranslation` を呼び出すことを確認してください。 |

## よくある質問

**Q: Aspose.3D はさまざまな Java IDE と互換性がありますか？**  
A: はい、Eclipse、IntelliJ IDEA、NetBeans、その他の IDE でもシームレスに動作します。

**Q: 作成した 3D オブジェクトにテクスチャを適用できますか？**  
A: もちろんです！`Material` クラスを使用してテクスチャや表面プロパティを割り当てます。

**Q: Aspose.3D のライセンスオプションはありますか？**  
A: さまざまなライセンスモデルが利用可能です。詳しくは [here](https://purchase.aspose.com/buy) をご覧ください。

**Q: サポートや経験を共有するにはどうすればよいですか？**  
A: サポートやディスカッションのために Aspose.3D コミュニティフォーラム [here](https://forum.aspose.com/c/3d/18) に参加してください。

**Q: テスト用の一時ライセンスは利用可能ですか？**  
A: はい、評価用の **aspose temporary license** は [here](https://purchase.aspose.com/temporary-license/) から取得できます。

---

**最終更新日:** 2026-04-08  
**テスト環境:** Aspose.3D for Java 24.12 (latest)  
**作者:** Aspose

---

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}