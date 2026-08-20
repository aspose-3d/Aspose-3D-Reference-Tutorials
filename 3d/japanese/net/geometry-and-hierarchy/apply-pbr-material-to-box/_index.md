---
date: 2026-04-12
description: Aspose.3D for .NET を使用してボックスに PBR マテリアルを適用し、PBR マテリアルを作成し、物理ベースレンダリングで
  STL ASCII ファイルをエクスポートする方法を学びましょう。
keywords:
- how to apply pbr
- create pbr material
- export stl ascii
- physically based rendering
- create box mesh
linktitle: 箱にPBRマテリアルを適用する
second_title: Aspose.3D .NET API
title: ボックスにPBRマテリアルを適用する方法
url: /ja/net/geometry-and-hierarchy/apply-pbr-material-to-box/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# ボックスに PBR マテリアルを適用する方法

## はじめに

3D グラフィックスの魅力的な世界へようこそ！このステップバイステップのチュートリアルでは、Aspose.3D for .NET を使用してボックスに **pbr** マテリアルを適用する方法を学びます。PBR マテリアルの作成、メッシュへの適用、そして最終的に **STL ASCII のエクスポート** を行い、モデルを任意の downstream ワークフローで使用できるようにします。ゲームプロトタイプ、製品ビジュアライザー、または 3D 印刷用のラピッドプロトタイプを作成する場合でも、このワークフローを習得すれば、.NET アプリケーションでリアルで物理ベースのレンダリング (PBR) を実現できます。

## クイック回答
- **主な目的は何ですか？** ボックスに PBR マテリアルを適用し、STL ASCII としてエクスポートします。  
- **使用するライブラリは？** Aspose.3D for .NET（aspose の使用方法）。  
- **ライセンスは必要ですか？** はい、製品環境では一時ライセンスまたはフルライセンスが必要です。  
- **サポートされている出力形式は？** STL ASCII（export stl ascii）およびその他多数の 3D フォーマット。  
- **所要時間はどれくらいですか？** 基本的な実装で約 10‑15 分です。

## PBR マテリアルとは？
Physically Based Rendering (PBR) は、光が実世界の表面とどのように相互作用するかをシミュレートするシェーディングモデルです。metallic や roughness といった属性を調整することで、複雑なシェーダを手動でチューニングすることなく、非常にリアルな結果を得ることができます。

## なぜ Physically Based Rendering (PBR) を使用するのか？
- **リアリズム:** 材料は光に対して実際の物理と一致する方法で反応します。  
- **一貫性:** 同じ材料がどの照明環境でも正しく見えます。  
- **効率性:** 現代の GPU は PBR 計算に最適化されており、無料でパフォーマンスが得られます。

## 前提条件

コードに入る前に、以下が揃っていることを確認してください：

### Aspose.3D for .NET のダウンロードとインストール
詳細なダウンロードとインストール手順については、[Aspose.3D for .NET のドキュメント](https://reference.aspose.com/3d/net/)をご覧ください。

### ライセンスの取得
Aspose.3D のすべての機能を利用するには、有効なライセンスを取得してください。一時ライセンスは[こちら](https://purchase.aspose.com/temporary-license/)で取得でき、フルライセンスは[こちら](https://purchase.aspose.com/buy)で購入できます。

## 名前空間のインポート
まず、Aspose.3D for .NET の機能を活用できるように、必要な名前空間をインポートしてください：

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Shading;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
```

## ステップバイステップ ガイド

### 手順 1: シーンの初期化
まず空の 3D シーンを作成します。このコンテナは、後で追加するすべてのジオメトリ、マテリアル、ライトを保持します。

```csharp
Scene scene = new Scene();
```

### 手順 2: PBR マテリアルの作成
ここで、ボックスにリアルな外観を与える **pbr マテリアルを作成** します。`PbrMaterial` クラスは、物理ベースのレンダリングに必要なすべてのパラメータを提供します。

```csharp
PbrMaterial mat = new PbrMaterial();
```

### 手順 3: マテリアルプロパティの設定
マテリアルのプロパティを微調整します。この例では、表面をほぼ金属的で非常に粗く設定し、ブラッシュドメタルの箱に最適な外観にします。

```csharp
mat.MetallicFactor = 0.9;
mat.RoughnessFactor = 0.9;
```

### 手順 4: ボックスメッシュの作成
シンプルなボックスジオメトリを生成します。これは、主要キーワードが参照する **create box mesh** 手順です。

```csharp
var boxNode = scene.RootNode.CreateChildNode("box", new Box());
```

### 手順 5: ボックスに PBR マテリアルを適用する
先に設定した **add pbr material** を、作成したボックスノードに割り当てます。

```csharp
boxNode.Material = mat;
```

### 手順 6: STL ASCII のエクスポート（STL のエクスポート方法）
最後に、モデルを任意の標準 3D ビューアやスライサで開けるように **export stl ascii** を実行します。`FileFormat.STLASCII` を使用すると、人間が読めるファイルが保証されます。

```csharp
scene.Save("Your Output Directory" + "PBR_Material_Box_Out.stl", FileFormat.STLASCII);
```

## よくある落とし穴とヒント
- **ライセンスが見つからない:** Aspose の呼び出しの *前に* ライセンスファイルがロードされていることを確認してください。そうでないと、ライブラリは評価モードで動作します。  
- **ファイルパスが正しくない:** 異なる OS でパス区切り文字が欠落しないように、`Path.Combine` を使用してください。  
- **Roughness と Metallic のバランス:** 両方の係数を高く設定しすぎると表面がフラットに見えることがあります。バランスの取れた外観のために `0.5‑0.9` の範囲で値を試してください。  
- **パフォーマンスのヒント:** 同じマテリアルを複数のメッシュに適用する場合は、単一の `PbrMaterial` インスタンスを再利用するとメモリオーバーヘッドが削減されます。

## よくある質問

**Q1: Aspose.3D は他の 3D ファイル形式と互換性がありますか？**  
A1: はい、Aspose.3D は幅広い 3D ファイル形式をサポートしており、プロジェクトの柔軟性を確保します。

**Q2: Aspose.3D を商用アプリケーションで使用できますか？**  
A2: もちろんです！Aspose.3D は商用ライセンスを提供しており、製品ソフトウェアへのシームレスな統合が可能です。

**Q3: 試用版はありますか？**  
A3: はい、無料トライアルをダウンロードして Aspose.3D の機能を体験できます。[こちら](https://releases.aspose.com/)から入手してください。

**Q4: コミュニティサポートやディスカッションはどこで見つけられますか？**  
A4: サポートやディスカッションは、[Aspose.3D フォーラム](https://forum.aspose.com/c/3d/18)に参加してください。

**Q5: Aspose.3D の一時ライセンスはどう取得しますか？**  
A5: 評価目的で一時ライセンスは[こちら](https://purchase.aspose.com/temporary-license/)から取得できます。

## 結論
Aspose.3D for .NET を使用した 3D グラフィックスへの取り組みは、無限の創造的可能性への扉を開きます。直感的な API と堅牢な機能により、視覚的に魅力的なシーンの作成が開発者にとって楽しい体験になります。**pbr** マテリアルをボックスに適用し、**STL ASCII をエクスポート**する方法が分かったので、ボックスをより複雑なメッシュに置き換えたり、テクスチャマップで実験して、リアルタイムで光がどのように反応するかを確認してみてください。

---

**最終更新日:** 2026-04-12  
**テスト環境:** Aspose.3D 24.11 for .NET  
**作者:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}
{{< blocks/products/products-backtop-button >}}