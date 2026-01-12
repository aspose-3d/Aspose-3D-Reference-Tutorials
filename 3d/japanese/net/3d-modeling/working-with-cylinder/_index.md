---
date: 2026-01-12
description: Aspose.3D for .NET を使用して、シアーボトムシリンダーの作成方法と 3D モデル OBJ のエクスポート方法を学びましょう。このステップバイステップガイドに従って、3D
  モデリングをマスターしてください。
linktitle: Customized Shear Bottom Cylinder
second_title: Aspose.3D .NET API
title: Aspose.3D for .NET を使用してシアボトムシリンダーを作成する方法
url: /ja/net/3d-modeling/working-with-cylinder/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# カスタマイズされたシアーボトムシリンダー

## はじめに
Aspose.3D for .NET を使用して **シアーボトムシリンダー** モデルの作成方法を学べる包括的なガイドへようこそ。ゲームアセット、機械部品、ビジュアルデモのいずれを作成する場合でも、本チュートリアルではシリンダーの底部を形作り、シアーを適用し、最終的に **3Dモデル OBJ** ファイルをエクスポートして任意のパイプラインで使用できる手順を正確に示します。各ステップを一緒に確認し、数分でカスタムジオメトリの作成を始めましょう。

## クイック回答
- **シアーボトムシリンダーとは？** 底面が平らではなく斜め（シアー）になっているシリンダーです。  
- **使用するライブラリは？** Aspose.3D for .NET。  
- **モデルのエクスポート方法は？** `scene.Save(..., FileFormat.WavefrontOBJ)` を使用します。  
- **ライセンスは必要ですか？** 試用版は利用可能ですが、商用利用には商用ライセンスが必要です。  
- **前提条件は？** .NET 開発環境と Aspose.3D NuGet パッケージが必要です。

## シアーボトムシリンダーとは？
シアーボトムシリンダーは、底面がシアー操作によって変形された標準的な円柱メッシュです。これにより、頂点を手動で編集することなく、傾斜したベースやランプ、カスタムコネクタを簡単に作成できます。

## なぜ Aspose.3D をこのタスクに使うのか？
- **ジオメトリパラメータ（半径、高さ、セグメント）をフルコントロール** できる。  
- **`ShearBottom` プロパティによる組み込みシアーサポート** があり、低レベルのメッシュ操作が不要。  
- **OBJ、FBX、STL などの一般的なフォーマットへのワンクリックエクスポート** が可能で、他ツールとの連携がシームレス。

## 前提条件
作業を始める前に以下を確認してください。

- C# と .NET の基本知識。  
- Aspose.3D for .NET がインストール済み。**[こちら](https://releases.aspose.com/3d/net/)** からダウンロードできます。  
- .NET 対応の IDE（Visual Studio、Rider、または VS Code）。

## 名前空間のインポート
C# ファイルの先頭で必要な名前空間をインポートします。

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```

## 手順 1: シーンの作成
まず、すべてのオブジェクトを保持する新しい 3‑D シーンをインスタンス化します。

```csharp
Scene scene = new Scene();
```

## 手順 2: Cylinder 1 の作成
シアー底部でカスタマイズするメインのシリンダーを作成します。

```csharp
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```

## 手順 3: Cylinder 1 のシアーボトムをカスタマイズ
シアーを適用し、ファン生成を有効にし、その他のプロパティを調整して目的の形状を実現します。

```csharp
// Shear 47.5deg in the xy plane (z‑axis)
cylinder1.ShearBottom = new Vector2(0, 0.83); 

// Set GenerateFanCylinder to true
cylinder1.GenerateFanCylinder = true;
// Set ThetaLength
cylinder1.ThetaLength = MathUtils.ToRadian(270);

// Set OffsetTop
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```

## 手順 4: Cylinder 1 をシーンに追加
カスタマイズしたシリンダーをシーンに配置し、右方向に少し移動させて両方のオブジェクトを横に並べて表示できるようにします。

```csharp
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```

## 手順 5: Cylinder 2 の作成
比較用にシンプルなシリンダーをもう一つ作成します。

```csharp
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```

## 手順 6: Cylinder 2 をシーンに追加
シアーをカスタマイズしないシリンダーを追加します。これにより、前ステップの効果が視覚的に分かりやすくなります。

```csharp
scene.RootNode.CreateChildNode(cylinder2);
```

## 手順 7: シーンの保存
最後に、シーン全体を OBJ ファイルとしてエクスポートし、Blender、Maya、その他の 3‑D ビューアで開けるようにします。

```csharp
scene.Save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WavefrontOBJ);
```

## よくある問題とヒント
- **シアー値**: `Vector2` は X と Y のシアー係数を受け取ります。`0.83` の値は約 47.5° に相当しますが、角度に応じて調整可能です。  
- **エクスポート先パス**: 指定したフォルダーが存在し、書き込み権限があることを確認してください。権限がないと `scene.Save` が例外をスローします。  
- **パフォーマンス**: セグメント数が非常に多いシリンダーの場合、例の `20` から減らすことで OBJ ファイルサイズを抑えられます。

## FAQ

### Aspose.3D for .NET は初心者に適していますか？
はい！Aspose.3D for .NET はユーザーフレンドリーな API を提供しており、初心者から経験豊富な開発者まで幅広く利用できます。

### シリンダーごとに異なるシアー角度を適用できますか？
可能です。各シリンダーの `ShearBottom` を個別に設定すれば、ユニークな効果を実現できます。

### 試用版はありますか？
あります。**[こちら](https://releases.aspose.com/)** から無料トライアルをご利用ください。

### 追加のサポートはどこで得られますか？
**[Aspose.3D フォーラム](https://forum.aspose.com/c/3d/18)** でコミュニティサポートやディスカッションが行われています。

### 一時ライセンスはどこで取得できますか？
**[こちら](https://purchase.aspose.com/temporary-license/)** から一時ライセンスを取得できます。

**追加 Q&A**

**Q: エクスポート形式を FBX に変更するには？**  
A: `scene.Save` 呼び出しで `FileFormat.WavefrontOBJ` を `FileFormat.FBX` に置き換えます。

**Q: エクスポート後にシリンダーをアニメーション化できますか？**  
A: OBJ はアニメーションをサポートしません。アニメーションが必要な場合は FBX または GLTF を使用してください。

**Q: シリンダーの半径を大きくしたい場合は？**  
A: `Cylinder` コンストラクタの最初の 2 つのパラメータを変更します（例: `new Cylinder(4, 4, …)`）。

## 結論
これで **シアーボトムシリンダー** モデルを作成し、Aspose.3D for .NET を使用して OBJ ファイルとしてエクスポートする方法を習得しました。プロジェクトの要件に合わせてシアー値、セグメント数、エクスポート形式を自由に試してみてください。モデリングを楽しんでください！

---

**最終更新日:** 2026-01-12  
**テスト環境:** Aspose.3D for .NET 24.11（執筆時点での最新バージョン）  
**作者:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}