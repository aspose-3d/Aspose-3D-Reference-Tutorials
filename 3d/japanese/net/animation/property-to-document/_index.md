---
date: 2026-03-28
description: .NET 用 Aspose.3D を使用して 3D シーンでキューブをアニメーションさせ、アニメーションされたシーンを FBX 形式でエクスポートする方法を学びます。このガイドでは、アニメーション
  カーブの作成、キー フレームのバインド、3D プロパティのアニメーション方法を示します。
linktitle: Animating Properties to Document in 3D Scenes
second_title: Aspose.3D .NET API
title: Aspose.3D for .NET を使用して 3D シーンでキューブをアニメーションする方法
url: /ja/net/animation/property-to-document/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose.3D for .NET を使用した 3D シーンでキューブをアニメーションする方法

## はじめに

.NET での 3D シーン作成とアニメーションの領域に飛び込むなら、Aspose.3D が最適なツールキットです。このステップバイステップ ガイドでは、**キューブのアニメーション方法** を、プロパティのアニメーション、アニメーション カーブの作成、キーフレームのバインドを通じて解説します。最後までで、人気のある 3D フォーマットにエクスポートできる完全にアニメーション化されたキューブが手に入ります。

## クイック回答
- **使用されているライブラリは？** Aspose.3D for .NET  
- **このチュートリアルがカバーする主なタスクは？** 3D シーンでキューブをアニメーションする方法  
- **主要な手順は？** 名前空間のインポート、シーンの作成、キーフレームのバインド、ファイルの保存  
- **ライセンスは必要ですか？** 学習目的なら無料トライアルで動作しますが、商用利用には商用ライセンスが必要です  
- **サポートされている出力フォーマットは？** FBX (ASCII 7500) および Aspose.3D がサポートするその他のフォーマット  

## Aspose.3D における「キューブのアニメーション方法」とは？
キューブをアニメーションするとは、キーフレーム データを使用して時間経過に伴い変換プロパティ（Translation、Rotation、Scale など）を変更することです。Aspose.3D は、シーン ノード上で **animation curves** を作成し、**keyframes** をバインドし、**3D プロパティ** を直接アニメーション化するためのシンプルな API を提供します。

## なぜ Aspose.3D でキューブをアニメーションするのか？
- **完全な .NET 統合** – .NET Framework、.NET Core、.NET 5/6 で動作します。  
- **外部依存なし** – シンプルなアニメーションに Unity や他のエンジンは不要です。  
- **エクスポートの柔軟性** – アニメーションシーンは FBX、OBJ、GLTF などの形式で保存でき、下流パイプラインで利用可能です。

## 前提条件

このエキサイティングな旅に出る前に、以下の前提条件が整っていることを確認してください：

- Aspose.3D for .NET: ライブラリがインストールされていることを確認してください。[Aspose.3D のウェブサイト](https://releases.aspose.com/3d/net/) からダウンロードできます。

- C# の知識: C# プログラミング言語に慣れていることが、例を理解し実装するために必須です。

- 統合開発環境 (IDE): Visual Studio など、お好みの IDE を使用して例に沿ってコーディングしてください。

- 基本的な 3D シーン概念: 基本的な 3D シーンの概念を把握していると、学習がスムーズになります。

## 名前空間のインポート

C# コードで、Aspose.3D に必要な名前空間をインポートしてください。以下が必要なセットです：

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using Aspose._3D.Examples.CSharp.Geometry_Hierarchy;
```

## 手順 1: シーン オブジェクトの初期化

ノードとアニメーションすべてを保持する空のシーンを作成します。

```csharp
Scene scene = new Scene();
```

## 手順 2: ポリゴン ビルダーを使用してメッシュを作成

`Common.CreateMeshUsingPolygonBuilder()` ヘルパーメソッドを使用して、シンプルなキューブ メッシュを生成します。

```csharp
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
```

## 手順 3: キューブ ノードの作成

キューブ メッシュをシーンのルートの子ノードとして追加します。ノード名 **cube1** は、後でキーフレームをバインドする際に使用されます。

```csharp
Node cube1 = scene.RootNode.CreateChildNode("cube1", mesh);
```

## 手順 4: Translation プロパティの取得

キューブの位置をアニメーションするには、ノードの Transform 上にある **Translation** プロパティを取得する必要があります。

```csharp
Property translation = cube1.Transform.FindProperty("Translation");
```

## 手順 5: バインド ポイントの作成

`BindPoint` はシーン プロパティとアニメーション カーブを結びつけます。ここでは Translation プロパティをバインドします。

```csharp
BindPoint bindPoint = new BindPoint(scene, translation);
```

## 手順 6: X 成分にアニメーション カーブをバインド

ここで **X** 軸用のアニメーション カーブを作成します。これは **create animation curve** 手順を示し、**bind keyframes** の方法を示します。

```csharp
bindPoint.BindKeyframeSequence("X", new KeyframeSequence()
{
    {0, 10.0f, Interpolation.Bezier},
    {3, 20.0f, Interpolation.Bezier},
    {5, 30.0f, Interpolation.Linear},
});
```

## 手順 7: Z 成分にアニメーション カーブをバインド

同様に、**Z** 軸をアニメーションさせ、キューブにより動的な動きのパスを付与します。

```csharp
bindPoint.BindKeyframeSequence("Z", new KeyframeSequence()
{
    {0, 10.0f, Interpolation.Bezier},
    {3, -10.0f, Interpolation.Bezier},
    {5, 0.0f, Interpolation.Linear},
});
```

## 手順 8: 3D シーンの保存

アニメーション化されたシーンを FBX ファイルにエクスポートします。`FBX7500ASCII` 形式は多くの 3D ツールで広くサポートされています。

```csharp
string output = "Your Output Directory" + "PropertyToDocument.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

## 手順 9: 成功メッセージの表示

アニメーションが正常に追加されたことをユーザーにフィードバックします。

```csharp
Console.WriteLine("\nAnimation property added successfully to document.\nFile saved at " + output);
```

## アニメーションシーンを FBX にエクスポート

キューブをアニメーションした後の最も一般的な作業の一つは、**アニメーションシーンを FBX にエクスポート** して他の 3D アプリケーションで利用できるようにすることです。上記のコードはすでにシーンを FBX7500ASCII 形式で保存しており、キーフレーム データを保持し、Autodesk Maya、Blender、Unity などのツールとシームレスに連携します。生成された `.fbx` ファイルを開くと、キーフレーム シーケンスで定義された通りに X 軸と Z 軸に沿ってキューブが動くのが確認できます。

## よくある問題と解決策

| 問題 | 原因 | 解決策 |
|------|------|--------|
| 動きが見られない | キーフレームの時間が再生範囲と合っていない | シーンのアニメーション タイムラインがキーフレームの時間（この例では 0‑5 秒）をカバーしていることを確認してください。 |
| ファイル パスが正しくない | `output` が存在しないディレクトリを指している | 先にディレクトリを作成するか、絶対パスを使用してください。 |
| ライセンス例外 | 本番環境で有効なライセンスなしで実行している | `Scene` を作成する前に Aspose.3D ライセンスを適用してください。 |

## よくある質問

### Q1: Aspose.3D のドキュメントはどこで見つけられますか？

A1: ドキュメントは[こちら](https://reference.aspose.com/3d/net/)で利用できます。

### Q2: Aspose.3D for .NET をどこからダウンロードできますか？

A2: [リリースページ](https://releases.aspose.com/3d/net/)からダウンロードできます。

### Q3: 無料トライアルは利用できますか？

A3: はい、[こちら](https://releases.aspose.com/)から無料トライアルを取得できます。

### Q4: Aspose.3D のサポートはどこで受けられますか？

A4: サポートは[Aspose.3D フォーラム](https://forum.aspose.com/c/3d/18)をご覧ください。

### Q5: 一時ライセンスは取得できますか？

A5: はい、[こちら](https://purchase.aspose.com/temporary-license/)で一時ライセンスを取得できます。

## 追加 FAQ (AI 最適化)

**Q: 回転やスケールなど、他のプロパティもアニメーションできますか？**  
A: もちろんです。`cube1.Transform.FindProperty("Rotation")` や "Scale" を使用し、同様にキーフレーム シーケンスをバインドしてください。

**Q: Aspose.3D はベジエやリニア以外のキーフレーム補間タイプをサポートしていますか？**  
A: はい、`Interpolation.Step` と `Interpolation.Cubic` もサポートしており、より細かい制御が可能です。

**Q: エクスポート前にアニメーションをプレビューするには？**  
A: Aspose.3D の API にシンプルなビューアが用意されています。または、エクスポートした FBX を Autodesk FBX Review などの 3D ビューアで開いてください。

**Q: 複数のキューブを同時にアニメーションさせることは可能ですか？**  
A: 各キューブごとに別々のノードを作成し、対応するプロパティを取得して、独立したキーフレーム シーケンスをバインドしてください。

## 結論

おめでとうございます！Aspose.3D for .NET を使用して 3D シーンで **キューブのアニメーション方法** を習得しました。これで **animation curves の作成**、**keyframes のバインド**、**animated scene FBX のエクスポート** ができ、静的ジオメトリに命を吹き込むことができます。回転やスケーリング、さらにはモーフ ターゲットなどを試して、アニメーション ツールキットを拡張してください。

---

**最終更新日:** 2026-03-28  
**テスト環境:** Aspose.3D 24.11 for .NET  
**作者:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}