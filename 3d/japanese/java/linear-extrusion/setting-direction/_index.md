---
date: 2025-12-18
description: Aspose.3D for Java を使用して 3D シーンを作成し、OBJ ファイルを保存する方法を学びましょう。線形押し出し方向に関するステップバイステップのガイドに従ってください。
linktitle: Setting Direction in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: 3Dシーンの作成 – 押し出し方向の設定 Aspose.3D Java
url: /ja/java/linear-extrusion/setting-direction/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 3Dシーンの作成 – 押し出し方向の設定 Aspose.3D Java

## Introduction

このチュートリアルでは、Aspose.3D for Java を使用して **how to create 3d scene** オブジェクトを作成し、押し出し方向を制御する方法を学びます。建築ビジュアライゼーション、製品プロトタイプ、ゲームアセットの作成など、線形押し出しをマスターすれば、複雑な形状を迅速にモデリングする柔軟性が得られます。Java でノードを追加することから **export 3d model obj** ファイルのエクスポートまで、すべての手順を順に解説するので、結果をすぐに確認できます。

## Quick Answers
- **What does “create 3d scene” mean?** Aspose.3D の `Scene` オブジェクトを初期化し、すべてのジオメトリ、ライト、カメラを保持することを意味します。  
- **How do I set extrusion direction?** `LinearExtrusion` インスタンスの `setDirection(Vector3)` メソッドを使用します。  
- **Which format should I use to export?** OBJ フォーマット（`FileFormat.WAVEFRONTOBJ`）は 3‑D ワークフローで広くサポートされています。  
- **Do I need a license for Aspose.3D?** 開発目的であれば無料トライアルで利用できますが、本番環境では商用ライセンスが必要です。  
- **Can I add more nodes in Java?** はい。`scene.getRootNode().createChildNode()` を使用して、必要なだけオブジェクトを追加できます。

## What is a “create 3d scene” workflow?

**create 3d scene** ワークフローは、空の `Scene` オブジェクトから開始し、ジオメトリ（押し出しプロファイルなど）を追加し、変換で位置決めし、最後にシーンを OBJ などのファイル形式で保存します。このパターンは Aspose.3D で構築されたほとんどの 3‑D アプリケーションの基盤です。

## Why set extrusion direction?

押し出し方向を設定すると、押し出し中に形状を傾けたり回転させたり歪めたりでき、追加の後処理なしで最終ジオメトリを制御できます。特に以下の場合に有用です：

- テーパー状の柱やカスタム形状のパイプの作成。  
- 機械部品で標準外の軸に合わせて押し出しを配置。  
- ビジュアルエフェクト用のアーティスティックな形状の生成。

## Prerequisites

本格的に始める前に、以下が揃っていることを確認してください：

- 基的な Java の知識。  
- Aspose.3D ライブラリがインストール済み – [here](https://releases.aspose.com/3d/java/) からダウンロード。  
- Eclipse や IntelliJ IDEA などの IDE。

## Import Packages

まず、必要な Aspose.3D クラスをインポートします：

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Step 1: Initialize Base Profile

押し出す 2‑D プロファイルを作成します。この例では角が丸い矩形を使用します：

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

> **Pro tip:** 押し出し前に矩形の角の鋭さや滑らかさを調整するには、ラウンド半径を変更してください。

## Step 2: Create a Scene

次に、オブジェクトをホストする **create 3d scene** を作成します：

```java
Scene scene = new Scene();
```

## Step 3: Add Nodes Java – Positioning the Objects

シーンのルートノードに左と右の 2 つの子ノードを追加し、左側のノードを少し横に移動します：

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Step 4: How to extrude – Left Node (default direction)

左側のノードのプロファイルをデルトの Z 軸方向で押し出します。また、360° のツイストを設定し、滑らかさのためにスライス数を増やします：

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## Step 5: How to set direction – Right Node

ここでは、カスタム `Vector3` を指定して **how to set direction** を行います。このベクトル (0.3, 0.2, 1) に向けて押し出しが傾きます：

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## Step 6: Save OBJ file – Export 3D model

最後に、**save obj file** を実行して、任意の 3‑D ビューアで結果を確認します：

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

生成された OBJ ファイルを開くと、2 つの押し出し矩形が表示されます。1 つはデフォルト方向、もう 1 つは設定したベクトルに従って傾いています。

## Common Issues and Solutions

| 問題 | 原因 | 対策 |
|-------|--------|-----|
| OBJ ファイルが空です | シーンが保存されていない、またはパスが正しくない | `MyDir` が書き込み可能なフォルダーを指しているか、ファイル名が `.obj` で終わっているか確認してください。 |
| 押し出しが平坦に見える | `setSlices` が低すぎる | 滑らかなジオメトリにするため、`setSlices` を増やしてください（例: 200）。 |
| 方向が変わらないように見える | ベクトルが正規化されていない | 正規化された `Vector3` を使用するか、望む傾きになるよう値を調整してください。 |

## Frequently Asked Questions

### Q1: Aspose.3D を他のプログラミング言語で使用できますか？
A1: Aspose.3D は .NET や Java など、さまざまな言語をサポートしています。

### Q2: Aspose.3D の無料トライアルはありますか？
A2: はい、[here](https://releases.aspose.com/) から無料トライアルで機能を試すことができます。

### Q3: Aspose.3D for Java の詳細なドキュメントはどこで見つけられますか？
A3: 包括的なドキュメントは [here](https://reference.aspose.com/3d/java/) にあります。

### Q4: Aspose.3D のサポートはどのように受けられますか？
A4: サポートや質問は [Aspose.3D forum](https://forum.aspose.com/c/3d/18) をご利用ください。

### Q5: Aspose.3D の一時ライセンスは利用できますか？
A5: はい、[here](https://purchase.aspose.com/temporary-license/) から一時ライセンスを取得できます。

---

**最終更新日:** 2025-12-18  
**テスト環境:** Aspose.3D 24.11 for Java  
**作者:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}