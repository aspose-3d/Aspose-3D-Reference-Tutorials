---
date: 2026-02-22
description: Aspose.3D for Java を使用して、線形押し出しツイストとツイストオフセットを用いた 3D シーンの作成とエクスポート方法を学びましょう。
linktitle: Using Twist Offset in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Aspose.3D for Java を使用して、線形押し出しでツイストオフセットを適用した 3D シーンの作成方法
url: /ja/java/linear-extrusion/using-twist-offset/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose.3D for Java での線形押し出しにおけるツイストオフセットの使用

## はじめに

ダイナミックな 3D グラフィックスの世界では、**create 3d scene** の技術を習得することは、あらゆる Java 3D モデリングプロジェクトにとって画期的です。Aspose.3D for Java を使用すれば、形状を線形に押し出すだけでなく、ツイストオフセットを追加して複雑でねじれたジオメトリを生成できます。このチュートリアルでは、**create 3d scene** の手順、線形押し出しツイストの適用、そして最終的に **export 3d scene** を一般的な OBJ ファイルにエクスポートするまでのすべてのステップを解説します。

## よくある質問
- **What does Twist Offset do?** ツイストの開始点をシフトし、押し出しパスに沿った回転をオフセットできるようにします。  
- **Which class performs linear extrusion?** `LinearExtrusion` – これに対してツイスト、スライス、ツイストオフセットを設定できます。  
- **Can I export the result?** はい、`scene.save(..., FileFormat.WAVEFRONTOBJ)` を呼び出して 3D シーンをエクスポートします。  
- **Do I need a license for development?** テスト用には一時ライセンスで動作しますが、本番環境では正式ライセンスが必要です。  
- **What Java version is supported?** Java 8 以降のランタイムであれば、最新の Aspose.3D ライブラリが動作します。

## Aspose.3D の「3D シーンの作成」とは何ですか？
3D シーンを作成するとは、`Scene` オブジェクトをインスタンス化し、ノード（オブジェクト）を階層に追加し、最後に希望のファイル形式でシーンを保存することを意味します。これは Java におけるすべての 3D モデリングワークフローの基礎です。

## ツイストオフセット付きの線形押し出しツイストを使用する理由は何ですか？
押し出し時にツイストを加えることで、らせん状の柱や装飾ハンドルなどの形状が得られます。ツイストオフセットを使用すると、ツイストの開始位置を任意に設定でき、最終形状を細かく制御できます。機械部品、アートモデル、建築ディテールなどに最適です。

## 前提条件

チュートリアルを開始する前に、以下の前提条件を満たしていることを確認してください。

- **Java Environment:** システムに Java 開発環境が設定されていることを確認してください。  
- **Aspose.3D for Java:** [download link](https://releases.aspose.com/3d/java/) から Aspose.3D ライブラリをダウンロードしてインストールしてください。  
- **Documentation:** [Aspose.3D for Java documentation](https://reference.aspose.com/3d/java/) を熟読してください。

## パッケージのインポート

Javaプロジェクトで、Aspose.3D for Javaの使用を開始するために必要なパッケージをインポートしてください。シームレスな統合のために、必要なライブラリが含まれていることを確認してください。

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## 3Dシーンの作成方法 – ステップバイステップガイド

### ステップ1：環境設定
まず Java 開発環境を整え、Aspose.3D for Java が正しくインストールされていることを確認します。このステップは **java 3d modeling** の作業に不可欠です。

### ステップ2：ベースプロファイルの初期化
押し出し用のベースプロファイルを作成します。この例では、丸み半径 0.3 の `RectangleShape` を使用します。プロファイルは押し出しパスに沿って掃引される断面を定義します。

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
// Initialize the base profile to be extruded
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

### ステップ3：3Dシーンを作成する
押し出したオブジェクトを格納する 3D シーンを構築します。ここで各ジオメトリ部品を表す **create child node** 要素を作成します。

```java
// Create a scene
Scene scene = new Scene();
```

### ステップ4：ノードを作成する
シーン内にノードを生成し、異なるエンティティを表現します。ここでは、プレーンな押し出し用のノードと、ツイストオフセットを使用するノードの 2 つの兄弟ノードを作成します。

```java
// Create left node
Node left = scene.getRootNode().createChildNode();
// Create right node
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### ステップ5：ツイストとツイストオフセットを用いた線形押し出しを実行する
両方のノードに線形押し出しを適用します。左側のノードは基本的なツイストを示し、右側のノードはツイストオフセットを追加して、この機能による追加の制御を示します。

```java
// Perform linear extrusion on left node using twist and slices property
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});

// Perform linear extrusion on right node using twist, twist offset, and slices property
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setTwistOffset(new Vector3(3, 0, 0)); }});
```

> **Pro tip:** より滑らかな曲率が必要な場合は、`setSlices()` を調整してメッシュ解像度を上げてください。

### ステップ6：3Dシーンを保存する（3Dシーンをエクスポートする）
最後に、組み立てたシーンを OBJ ファイルとしてエクスポートし、任意の標準 3D ビューアで表示したり、他のパイプラインにインポートしたりできるようにします。

```java
// Save 3D scene
scene.save(MyDir + "TwistOffsetInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

コードが正常に実行されると、指定したディレクトリに `TwistOffsetInLinearExtrusion.obj` が生成され、Blender、MeshLab、または任意の CAD ソフトウェアで開くことができます。

## よくある問題と解決策
| 問題 | 原因 | 解決策 |
|-------|----------------|-----|
| **Scene saves as empty file** | `MyDir` パスが正しくないか、書き込み権限がありません。 | ディレクトリが存在し、書き込み可能か確認するか、絶対パスを使用してください。 |
| **Twist looks flat** | `setSlices()` が低すぎて、粗いメッシュになります。 | スライス数を増やす（例: 200）と、ツイストが滑らかになります。 |
| **Twist offset has no effect** | オフセットベクトルが押し出し方向と同一直線上にあります。 | X または Y 成分に非ゼロの値を設定して、オフセットのシフトを確認してください。 |

## よくある質問

### Q1: Aspose.3D for Java を非商用プロジェクトで使用できますか？
A1: はい、Aspose.3D for Java は商用・非商用プロジェクトの両方で使用可能です。詳細は [licensing options](https://purchase.aspose.com/buy) をご確認ください。

### Q2: Aspose.3D for Java のサポートはどこで受けられますか？
A2: [Aspose.3D for Java forum](https://forum.aspose.com/c/3d/18) を訪れて支援を受け、コミュニティとつながりましょう。

### Q3: Aspose.3D for Java の無料トライアルはありますか？
A3: はい、[releases page](https://releases.aspose.com/) から無料トライアル版を試すことができます。

### Q4: Aspose.3D for Java の一時ライセンスはどう取得しますか？
A4: プロジェクト用の一時ライセンスは [this link](https://purchase.aspose.com/temporary-license/) から取得してください。

### Q5: 追加のサンプルやチュートリアルはありますか？
A5: はい、[documentation](https://reference.aspose.com/3d/java/) にて、より多くのサンプルと詳細なチュートリアルをご覧ください。

---

**最終更新日:** 2026-02-22  
**テスト環境:** Aspose.3D for Java 24.11 (latest)  
**作者:** Aspose

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
