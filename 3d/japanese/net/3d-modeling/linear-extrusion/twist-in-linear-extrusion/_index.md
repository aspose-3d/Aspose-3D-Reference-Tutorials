---
date: 2026-03-23
description: Aspose.3D for .NET を使用して、ねじれた押し出しの作成方法を学びましょう。このステップバイステップガイドでは、直線押し出しねじれのテクニックを解説しています。
linktitle: Twist in Linear Extrusion
second_title: Aspose.3D .NET API
title: 直線押出しでねじれた押出しを作成する方法
url: /ja/net/3d-modeling/linear-extrusion/twist-in-linear-extrusion/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 線形押出しでねじれを加える押し出しの作成方法

## はじめに

.NET アプリケーションで目を引く 3D ビジュアルが必要な場合、**押し出しの作り方**は基本的なスキルであることにすぐ気付くでしょう。Aspose.3D for .NET は、シンプルな 2‑D プロファイルを高度な 3‑D モデルに変換するためのクリーンで高性能な API を提供します—特にねじれを加える場合に威力を発揮します。このチュートリアルでは、シーンの設定から最終的な OBJ ファイルの保存まで、すべての手順を順を追って解説し、線形押出しねじれの実際の効果を体感できるようにします。

## クイック回答
- **押し出しの主要クラスはどれですか？** `LinearExtrusion`
- **回転を加えるプロパティはどれですか？** `Twist`
- **滑らかな結果を得るために必要なスライス数は？** 約 100 スライス（必要に応じて調整）
- **他の形状も使用できますか？** はい、`IProfile` を実装する任意の形状（円、ポリゴン、カスタム曲線など）を使用可能です
- **例で使用されているファイル形式は？** Wavefront OBJ（`.obj`）

## 前提条件

以下を事前に準備してください。

- Aspose.3D for .NET がインストール済みです。まだダウンロードしていない場合は **[here](https://releases.aspose.com/3d/net/)** から取得してください。
- 動作する .NET 開発環境（Visual Studio、VS Code、またはお好みの IDE）。
- C# の基本構文とオブジェクト指向の概念にある程度慣れていること。

## 名前空間のインポート

任意の .NET プロジェクトでは、名前空間の正しい使用が重要です。Aspose.3D の機能を効果的に活用できるよう、必要な名前空間をインポートします。以下のスニペットをご参照ください。

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## ステップバイステップガイド

### ステップ 1: 基本プロファイルの初期化

まず、押し出す形状を定義します。この例では、エッジに微妙な曲線を持たせるために小さな丸み半径を持つ長方形を使用します。

```csharp
// Initialize the base profile to be extruded
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

### ステップ 2: 3Dシーンの作成

`Scene` オブジェクトは、すべての 3‑D エンティティが存在するキャンバスとして機能します。押し出しの舞台と考えてください。

```csharp
// Create a scene 
Scene scene = new Scene();
```

### ステップ 3: 左右のノードを追加

ノードを使うことでオブジェクトを階層的に整理できます。ここでは、直線押出し用とねじれ版用の 2 つの兄弟ノードを作成します。

```csharp
// Create left node
var left = scene.RootNode.CreateChildNode();
// Create right node
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(15, 0, 0);
```

### ステップ 4: 左側ノードでねじれ付き線形押出しを実行

`Twist` プロパティは、押し出し中にプロファイルが回転する角度を制御します。**0** に設定すると、従来の直線押出しになります。

```csharp
// Twist property defines the degree of the rotation while extruding the profile
// Perform linear extrusion on the left node using twist and slices property
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 0, Slices = 100 });
```

### ステップ 5: 右側ノードでねじれ付き線形押出しを実行

同じプロファイルに 90 度のねじれを加えます。これにより **線形押出しねじれ** の効果がはっきりと示されます。

```csharp
// Perform linear extrusion on the right node using twist and slices property
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 90, Slices = 100 });
```

### ステップ 6: 3Dシーンを保存

最後に、シーンを任意の 3‑D ビューアで表示できる形式でエクスポートします。例では Wavefront OBJ を使用していますが、Aspose.3D は他にも多数の形式をサポートしています。

```csharp
// Save 3D scene
scene.Save("Your Output Directory" + "TwistInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## ねじれ付き線形押出しを使用する理由

- **高速プロトタイピング:** 2‑D スケッチを手動モデリングなしで 3‑D 部品に変換できます。
- **設計の柔軟性:** `Twist` の値を調整してスパイラル、ヘリカルリブ、装飾的なフィーチャーを作成できます。
- **パフォーマンスに優しい:** `Slices` パラメータでビジュアル精度と実行速度のバランスを取れます。

## よくある問題とヒント

- **スライスが多すぎる:** 100 スライスで滑らかに見えますが、極端に高い値は描画速度を低下させる可能性があります。パフォーマンスが懸念される場合は、より低い数でテストしてください。
- **負のねじれ値:** `Twist` に負の値を設定すると逆方向に回転します。鏡像デザインに便利です。
- **ファイルパス:** 出力ディレクトリが存在し、書き込み権限があることを確認してください。権限がないと `scene.Save` が例外をスローします。

## 結論

本チュートリアルでは、Aspose.3D for .NET を使用してねじれ付きの **押し出しの作り方** を示しました。`Twist` と `Slices` のプロパティを調整するだけで、単純なねじれバーから複雑なヘリカル構造まで、さまざまな形状を数行のコードで生成できます。

## よくある質問

**Q: 他の形状にもねじれ付き線形押出しを適用できますか？**  
A: もちろんです！`IProfile` を実装する任意のクラス（`CircleShape`、`PolygonShape`、カスタムスプラインなど）に対してねじれを加えて押し出すことができます。

**Q: `Twist` プロパティは実際に何を表していますか？**  
A: 押し出し長さ全体にわたってプロファイルに適用される総回転角度（度）を指定します。

**Q: スライス数を増やすとメモリ使用量に影響しますか？**  
A: はい、スライスが増えると頂点と面の数が増え、メモリ消費が増加します。そのため低スペックデバイスではパフォーマンスに影響が出る可能性があります。

**Q: 線形押出しを他の Aspose.3D 機能と組み合わせられますか？**  
A: 可能です。押し出し後にマテリアルやテクスチャを適用したり、ブーリアン演算を行ったりして、さらにリッチなモデルを作成できます。

**Q: 開発者同士で情報交換やサポートを受けられる場所はありますか？**  
A: **[Aspose Forum](https://forum.aspose.com/c/3d/18)** で Aspose.3D コミュニティに参加し、サポートやサンプル、ディスカッションをご利用ください。

---

**Last Updated:** 2026-03-23  
**Tested With:** Aspose.3D 24.11 for .NET  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}