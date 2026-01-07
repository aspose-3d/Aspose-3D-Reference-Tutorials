---
date: 2026-01-07
description: Aspose.3D for .NET を使用して 2D プロファイルを線形押し出しし、3D モデル OBJ をエクスポートする方法を学びましょう。この線形押し出しチュートリアルは、ステップバイステップで案内します。
linktitle: Performing Linear Extrusion
second_title: Aspose.3D .NET API
title: Aspose.3D for .NETでリニア押し出しを行う方法
url: /ja/net/3d-modeling/linear-extrusion/performing-linear-extrusion/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose.3D for .NET で how to linear extrude の方法

## はじめに

Welcome to our **linear extrusion tutorial**! In this guide you’ll discover **how to linear extrude** a 2‑D profile and turn it into a fully fledged 3‑D object using Aspose.3D for .NET. Whether you’re building a CAD‑style application or just need to **export 3d model obj** files for downstream processing, this step‑by‑step walkthrough will give you the confidence to add powerful geometry creation to your projects.

## クイック回答
- **What is linear extrusion?** 2‑D 形状を直線パスに沿って伸ばし、3‑D ソリッドを作成することです。  
- **Which library do we use?** Aspose.3D for .NET.  
- **Do I need a license?** テスト用には一時ライセンスで動作しますが、本番環境ではフルライセンスが必要です。  
- **Can I export to OBJ?** はい – 最終シーンは Wavefront OBJ ファイルとして保存されます。  
- **How many lines of code?** 説明コメントを含めても 30 行未満の C# です。  

## Linear Extrusion とは？

Linear extrusion は、平面のプロファイル（矩形や円など）を直線に沿って掃引し、必要に応じてねじれ、スケーリング、オフセットを加える手法です。その結果、レンダリング、編集、または他の 3‑D ツールで使用するためにエクスポートできるソリッドが得られます。

## Linear Extrusion に Aspose.3D を使用する理由

* **Zero‑dependency:** 外部の CAD カーネルは不要です。  
* **Full .NET support:** .NET Framework、.NET Core、.NET 5/6+ で動作します。  
* **Export flexibility:** OBJ、STL、FBX など多数のフォーマットに直接保存できます。  
* **Rich API:** スライス、ねじれ、オフセットを数プロパティだけで制御できます。  

## 前提条件

開始する前に、以下が揃っていることを確認してください：

1. **Aspose.3D installed** – [here](https://releases.aspose.com/3d/net/) からダウンロードしてください。  
2. **Documentation access** – セットアップガイドは [here](https://reference.aspose.com/3d/net/) を参照してください。  
3. 必要な名前空間が参照されている .NET 開発環境（Visual Studio、VS Code、または Rider）。  

## 名前空間のインポート

Aspose.3D の機能を利用するために、必須の名前空間をインクルードします：

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

これらの名前空間により、`Scene`、`LinearExtrusion`、`RectangleShape`、および `Vector3` などのユーティリティクラスにアクセスできます。

## Linear Extrusion の実行

以下に完全なワークフローを示します。各ステップは対応するコードブロックの前に平易な言葉で説明しているので、コードが何をしているか推測することなく進められます。

### ステップ 1: ベースプロファイルの初期化

まず、押し出す 2‑D 形状を作成します。この例では、丸み半径が小さい矩形を使用します。

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

*Why this matters:* プロファイルは最終的な 3‑D オブジェクトの断面を定義します。`RoundingRadius`、幅、または高さを調整してさまざまなシルエットを作れます。

### ステップ 2: Linear Extrusion の適用

次に、プロファイルを Z 軸方向に 10 ユニット掃引し、滑らかさのために 100 スライスを追加し、ジオメトリをセンタリングし、オフセット付きで 360° のねじれを適用します。

```csharp
var extrusion = new LinearExtrusion(profile, 10) { Slices = 100, Center = true, Twist = 360, TwistOffset = new Vector3(10, 0, 0) };
```

*Pro tip:* `Slices` を調整してパフォーマンスと画質のバランスを取り、`Twist` を試してスパイラル効果を作り出してください。

### ステップ 3: シーンの作成

`Scene` はすべての 3‑D エンティティのコンテナとして機能します—キャンバスと考えてください。

```csharp
Scene scene = new Scene();
```

### ステップ 4: 押し出しジオメトリをシーンに追加

押し出されたジオメトリをシーンのルートノードにアタッチし、レンダラブルな階層の一部にします。

```csharp
scene.RootNode.CreateChildNode(extrusion);
```

### ステップ 5: 3‑D モデルの保存

最後に、シーンを広くサポートされている OBJ ファイルにエクスポートします。これは Aspose.3D の **export 3d model obj** 機能のデモです。

```csharp
scene.Save(RunExamples.GetOutputFilePath("LinearExtrusion.obj"), FileFormat.WavefrontOBJ);
```

生成された `LinearExtrusion.obj` を任意の 3‑D ビューアで開くと、ねじれた矩形プリズムが表示されます—コードが記述した通りです。

## よくある落とし穴とヒント

| Issue | Why it Happens | How to Fix |
|-------|----------------|------------|
| **Profile not visible** | 押し出しをシーンに追加し忘れたため。 | `CreateChildNode` が呼び出されていることを確認してください。 |
| **Twist looks flat** | `Slices` が少なすぎて粗いジオメトリになるため。 | `Slices` を増やす（例: 200）とねじれが滑らかになります。 |
| **Export fails** | 出力フォルダーが存在しない、または書き込み権限がないため。 | `RunExamples.GetOutputFilePath` を使用するか、ディレクトリを手動で作成してください。 |
| **Unexpected scaling** | `Center` が `false` に設定されてジオメトリがシフトするため。 | オフセットが不要な限り `Center = true` に設定してください。 |

## よくある質問

### Q1: Aspose.3D は初心者に適していますか？

A1: もちろんです！Aspose.3D はユーザーフレンドリーな API を提供しており、このチュートリアルでは Linear Extrusion の基本を段階的に解説します。

### Q2: 商用プロジェクトで Aspose.3D を使用できますか？

A2: はい、Aspose.3D には個人利用と商用利用の両方に対応したライセンスオプションがあります。詳細は [here](https://purchase.aspose.com/buy) をご確認ください。

### Q3: テスト用の一時ライセンスはどう取得できますか？

A3: テスト目的の一時ライセンスは [this link](https://purchase.aspose.com/temporary-license/) から取得できます。

### Q4: コミュニティサポートはどこで得られますか？

A4: 活発なコミュニティとつながり、支援を受けるには [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) に参加してください。

### Q5: 無料トライアルはありますか？

A5: もちろんです！無料トライアル版は [here](https://releases.aspose.com/) からダウンロードして、Aspose.3D の機能を直接体験してください。

**最終更新日:** 2026-01-07  
**テスト環境:** Aspose.3D 24.11 for .NET  
**作者:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

## ターゲットキーワード:

**主要キーワード（最優先）:**  
how to linear extrude  

**サブキーワード（サポート）:**  
export 3d model obj, linear extrusion tutorial  

**キーワード統合戦略:**
1. 主要キーワード: 3〜5回使用する（タイトル、メタ、最初の段落、H2 見出し、本文）  
2. サブキーワード: 各 1〜2回使用する（見出し、本文）  
3. すべてのキーワードは自然に組み込み、可読性をキーワード数より優先してください  
4. キーワードが自然に合わない場合は、意味的なバリエーションを使用するか省略してください