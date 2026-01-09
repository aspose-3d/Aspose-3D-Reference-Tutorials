---
date: 2026-01-09
description: Aspose.3D for .NET を使用して 3D シーンの作成と 3D モデルの保存方法を学びます。Wavefront OBJ のエクスポートや線形押し出しスライスも含まれます。
linktitle: Create 3D Scene with Linear Extrusion Slices
second_title: Aspose.3D .NET API
title: 線形押し出しスライスで3Dシーンを作成
url: /ja/net/3d-modeling/linear-extrusion/slices-in-linear-extrusion/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 線形押し出しスライスで3Dシーンを作成する

## はじめに

Aspose.3D for .NET を使用した 3D デザインの世界へようこそ！このチュートリアルでは **3d シーン** オブジェクトを作成し、カスタムスライス数で線形押し出しを適用し、最後に **3d モデル** を Wavefront OBJ ファイルとして **保存** します。簡単なプロトタイプでも本番向けの可視化でも、以下の手順で **Aspose** を使用して C# から高品質なジオメトリを直接生成する方法が分かります。

## クイック回答
- **「3d シーンを作成する」とは何ですか？** シーンオブジェクトを作成し、すべての 3D エンティティ（メッシュ、ライト、カメラ）を保持することを意味します。  
- **エクスポートに使用されるフォーマットは？** サンプルは **Wavefront OBJ** (`export wavefront obj`) にエクスポートします。  
- **何スライスまで設定できますか？** 任意の整数を設定可能です。デモでは 2 スライスと 10 スライスを示しています。  
- **ライセンスは必要ですか？** 本番利用には一時ライセンスまたはフルライセンスが必要です。  
- **.NET Core でも実行できますか？** はい、Aspose.3D は .NET Framework と .NET Core の両方をサポートしています。

## 前提条件

Aspose.3D を使用した 3D デザインに取り組む前に、以下の前提条件を確認してください。

- Aspose.3D for .NET ライブラリ: Aspose.3D ライブラリがインストールされていることを確認してください。ダウンロードは [こちら](https://releases.aspose.com/3d/net/) から。  
- 統合開発環境 (IDE): .NET 開発に対応した任意の IDE を使用してください。  
- C# の基本知識: C# の基礎文法に慣れておくことをおすすめします。  
- 3D デザインへの探求心: ビジュアルに優れた 3D モデルを作成したい情熱を持ってください！

## 名前空間のインポート

Aspose.3D で 3D デザインを始めるには、必要な名前空間をインポートします。これにより、コードから必要なクラスや機能にアクセスできるようになります。

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## 線形押し出しで 3d シーンを作成する方法

以下では、シーンの構築、押し出しの適用、そして **OBJ ファイルとして 3d モデルを保存** するまでの各ステップを順に解説します。説明は会話調で書かれているので、気軽に進められます。

### 手順 1: ベースプロファイルの初期化

まず、押し出す 2‑D 形状を定義します。この例では角が丸められた長方形です。

```csharp
// ExStart:InitializeBaseProfile
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
// ExEnd:InitializeBaseProfile
```

### 手順 2: 3D シーンの作成

`Scene` オブジェクトはすべてのジオメトリ、ライト、カメラを格納するコンテナで、**3d シーンを作成**する際の中心的存在です。

```csharp
// ExStart:Create3DScene
Scene scene = new Scene();
// ExEnd:Create3DScene
```

### 手順 3: 左右のノードを作成

シーンのルートに 2 つの子ノードを追加します。左側はスライス数が少なく、右側は多く設定して、視覚的な違いを確認できます。

```csharp
// ExStart:CreateLeftRightNodes
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(15, 0, 0);
// ExEnd:CreateLeftRightNodes
```

### 手順 4: 左ノードで線形押し出しを実行

ここでは **2 スライス** で長方形を押し出します。スライスが少ないと粗い外観になります。

```csharp
// ExStart:LinearExtrusionLeftNode
left.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 2 });
// ExEnd:LinearExtrusionLeftNode
```

### 手順 5: 右ノードで線形押し出しを実行

同じプロファイルを **10 スライス** で押し出し、より滑らかな表面を生成します。

```csharp
// ExStart:LinearExtrusionRightNode
right.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 10 });
// ExEnd:LinearExtrusionRightNode
```

### 手順 6: 3D シーンの保存

最後にシーンを Wavefront OBJ ファイルへエクスポートします。これにより **obj の保存方法** と **wavefront obj のエクスポート** が Aspose.3D で実現できます。

```csharp
// ExStart:Save3DScene
scene.Save("Your Output Directory" + "SlicesInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
// ExEnd:Save3DScene
```

## よくある問題と対策

| 問題 | 発生原因 | 対策 |
|------|----------|------|
| OBJ ファイルが空になる | 出力パスが間違っている、または書き込み権限がない | ディレクトリが存在し、アプリケーションに書き込み権限があることを確認 |
| スライス数が滑らかさに影響しない | `Slices` の値がジオメトリのサイズに対して低すぎる | スライス数を増やすか、プロファイルの寸法を調整 |
| ライセンス例外が発生 | トライアル以外のビルドで有効なライセンスが設定されていない | `License license = new License(); license.SetLicense("Aspose.3D.lic");` で一時または永続ライセンスを適用 |

## FAQ

**Q: Aspose.3D for .NET を他のプログラミング言語でも使えますか？**  
A: Aspose.3D は主に .NET 向けに設計されていますが、.NET バインディングを利用して Python などの言語と連携する方法も検討できます。

**Q: Aspose.3D for .NET の詳細なドキュメントはどこで確認できますか？**  
A: 詳細情報はドキュメント [こちら](https://reference.aspose.com/3d/net/) をご参照ください。

**Q: Aspose.3D for .NET の無料トライアルはありますか？**  
A: はい、ライブラリの機能を試すための無料トライアルを [こちら](https://releases.aspose.com/) から取得できます。

**Q: Aspose.3D for .NET の技術サポートはどこで受けられますか？**  
A: Aspose.3D フォーラム [こちら](https://forum.aspose.com/c/3d/18) で質問や情報交換が可能です。

**Q: Aspose.3D for .NET の一時ライセンスは取得できますか？**  
A: はい、評価目的で使用できる一時ライセンスを [こちら](https://purchase.aspose.com/temporary-license/) から取得してください。

## 結論

おめでとうございます！Aspose.3D for .NET を使用して **3d シーン** を作成し、カスタムスライス数で線形押し出しを適用し、Wavefront OBJ ファイルとして **3d モデル** を **保存** する方法を習得できました。これは 3D デザインの旅の始まりに過ぎません。さまざまなプロファイルやスライス値、エクスポート形式を試して、 **3d modeling c#** の可能性を最大限に引き出してください。

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**最終更新日:** 2026-01-09  
**テスト環境:** Aspose.3D 24.11 for .NET  
**作者:** Aspose