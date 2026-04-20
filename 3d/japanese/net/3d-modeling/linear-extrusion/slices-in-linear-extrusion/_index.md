---
date: 2026-03-23
description: Aspose.3D for .NET を使用して、スライスによる線形押し出しの方法を学びましょう。ステップバイステップのコード例で詳細な
  3D モデルを作成できます。
linktitle: How to Linear Extrusion with Slices
second_title: Aspose.3D .NET API
title: Aspose.3D for .NET を使用したスライスによる線形押し出しの方法
url: /ja/net/3d-modeling/linear-extrusion/slices-in-linear-extrusion/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose.3D for .NET を使用したスライス付き線形押し出しの方法

## はじめに

Aspose.3D for .NET を使用した 3D デザインの世界へようこそ！このチュートリアルでは、モデルの詳細度を制御できるテクニックである **スライス付き線形押し出し** の方法を学びます。経験豊富な開発者でも、これから始める方でも、すべての手順を丁寧に案内し、各操作の理由を説明し、すぐに活用できる実践的なヒントを提供します。

## クイック回答
- **スライス付き線形押し出しとは何ですか？** 2D プロファイルを 3D に伸ばす方法で、生成される中間断面（スライス）の数を指定します。  
- **なぜスライスを使用するのですか？** スライス数を増やすと曲面が滑らかになり、スライス数を減らすとメッシュが軽量になります。  
- **前提条件は？** Aspose.3D for .NET、.NET 対応 IDE、基本的な C# の知識。  
- **典型的な実行時間は？** サンプルは最新の PC で 1 秒未満で実行されます。  
- **出力フォーマットは？** 例は Wavefront OBJ に保存しますが、Aspose.3D は多数のフォーマットをサポートしています。

## スライス付き線形押し出しとは？

線形押し出しは、2‑D の形状（プロファイル）を直線に沿って伸ばし、3‑D のソリッドを作成します。**Slices** プロパティは、押し出しの開始点と終了点の間に挿入される中間断面の数を決定し、滑らかさとポリゴン数に影響します。

## 線形押し出しでスライスを使用する理由

- **メッシュ密度の制御:** 視覚品質とファイルサイズのバランスを微調整します。  
- **パフォーマンス最適化:** リアルタイムアプリケーションではスライスを少なくし、高解像度レンダリングでは多く使用します。  
- **クリエイティブな柔軟性:** オブジェクトごとに異なるスライス数を組み合わせて、デザイン意図を強調できます。

## 前提条件

- Aspose.3D for .NET ライブラリ – [here](https://releases.aspose.com/3d/net/) からダウンロードしてください。  
- C# をサポートする IDE（Visual Studio、Rider、VS Code など）。  
- C# の構文とオブジェクト指向概念の基本的な知識。  
- 3‑D ジオメトリを試す好奇心！

## 名前空間のインポート

まず、Aspose.3D のコアクラスにアクセスできる名前空間をインポートします。

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## ステップバイステップガイド

### ステップ 1: 基本プロファイルの初期化

まず、シンプルな長方形を作成し、エッジが完全に鋭くならないように小さな丸み半径を設定します。

```csharp
// ExStart:InitializeBaseProfile
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
// ExEnd:InitializeBaseProfile
```

### ステップ 2: 3D シーンの作成

`Scene` は、すべてのノード、メッシュ、ライト、カメラのコンテナとして機能します。

```csharp
// ExStart:Create3DScene
Scene scene = new Scene();
// ExEnd:Create3DScene
```

### ステップ 3: 左右のノードを追加

シーンのルートの下に 2 つの兄弟ノードを作成します。左側のノードには少ないスライス数、右側のノードには多いスライス数を設定し、視覚的な違いを比較できるようにします。

```csharp
// ExStart:CreateLeftRightNodes
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(15, 0, 0);
// ExEnd:CreateLeftRightNodes
```

### ステップ 4: 左側ノードで線形押し出しを実行（低詳細）

ここでは長方形を **2 スライス** だけで押し出します。粗いメッシュが生成され、クイックプレビューに最適です。

```csharp
// ExStart:LinearExtrusionLeftNode
left.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 2 });
// ExEnd:LinearExtrusionLeftNode
```

### ステップ 5: 右側ノードで線形押し出しを実行（高詳細）

今度は **10 スライス** を使用し、はるかに滑らかな結果を得ます。ジオメトリが細かくなる様子に注目してください。

```csharp
// ExStart:LinearExtrusionRightNode
right.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 10 });
// ExEnd:LinearExtrusionRightNode
```

### ステップ 6: 3D シーンの保存

最後に、シーンを OBJ ファイルに書き出します。`"Your Output Directory"` をマシン上の有効なパスに置き換えてください。

```csharp
// ExStart:Save3DScene
scene.Save("Your Output Directory" + "SlicesInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
// ExEnd:Save3DScene
```

## よくある問題と解決策

| Issue | Why It Happens | Fix |
|-------|----------------|-----|
| **ファイルが作成されません** | 出力パスが無効か、書き込み権限がありません。 | 絶対パスを使用し、フォルダーが存在することを確認してください。 |
| **オブジェクトが平坦に見える** | `Slices` が 1 または 0 に設定されている。 | `Slices` を少なくとも 2 に設定して、押し出しが見えるようにしてください。 |
| **予期しないジオメトリ** | 丸み半径が長方形のサイズに対して大きすぎる。 | `RoundingRadius` を長方形の最小辺の半分未満の値に調整してください。 |

## よくある質問

**Q: 押し出し方向を変更できますか？**  
A: はい。保存する前に、ノードの `Transform` プロパティを使用して押し出しジオメトリを回転または平行移動できます。

**Q: Aspose.3D は他の押し出しタイプをサポートしていますか？**  
A: もちろんです。`LinearExtrusion` に加えて、`RevolveExtrusion`、`SweepExtrusion` なども使用できます。

**Q: どのファイル形式にエクスポートできますか？**  
A: Aspose.3D は OBJ、STL、FBX、3MF、Collada など多数の形式をサポートしています。`FileFormat` 列挙体を変更するだけです。

**Q: プログラムでマテリアルを設定する方法はありますか？**  
A: はい。ノードを作成した後、その `Entity` コレクションに `Material` を割り当てます。

**Q: スライス数はメモリ使用量にどのように影響しますか？**  
A: スライス数が増えると頂点数と面数が増加し、メモリ消費が比例して増えます。対象プラットフォームに最適なバランスを見つけるためにプロファイリングを行ってください。

## オリジナル FAQ

### Q1: Aspose.3D for .NET を他のプログラミング言語と併用できますか？

A1: Aspose.3D は主に .NET 用に設計されていますが、.NET バインディングを使用して Python などの言語との相互運用オプションを検討できます。

### Q2: Aspose.3D for .NET の詳細なドキュメントはどこで見つけられますか？

A2: Aspose.3D の機能と使用方法に関する詳細情報は、ドキュメント [here](https://reference.aspose.com/3d/net/) を参照してください。

### Q3: Aspose.3D for .NET の無料トライアルはありますか？

A3: はい、購入前にライブラリの機能を試すために無料トライアルを [here](https://releases.aspose.com/) から取得できます。

### Q4: Aspose.3D for .NET のテクニカルサポートはどのように受けられますか？

A4: Aspose.3D フォーラム [here](https://forum.aspose.com/c/3d/18) にアクセスして支援を求め、コミュニティと交流してください。

### Q5: Aspose.3D for .NET の一時ライセンスを使用できますか？

A5: はい、評価目的で一時ライセンスを [here](https://purchase.aspose.com/temporary-license/) から取得してください。

## 結論

これで、Aspose.3D for .NET を使用したスライス付き **線形押し出し** の方法を確認し、異なるスライス数の影響を検証し、作品のエクスポート方法を学びました。別のプロファイルで実験したり、`Slices` の値を変更したり、マテリアルやライトを統合して、プロダクションレベルの 3‑D アセットを作成してみてください。

---

**Last Updated:** 2026-03-23  
**Tested With:** Aspose.3D 24.11 for .NET (latest at time of writing)  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}