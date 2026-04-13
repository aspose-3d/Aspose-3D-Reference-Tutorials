---
date: 2026-03-26
description: Aspose.3D for .NET を使用してシリンダーを作成し、OBJ ファイルをエクスポートする方法を学びましょう。この初心者向けガイドでは、3D
  シーンの設定と OBJ エクスポートについて解説します。
linktitle: Customized Shear Bottom Cylinder
second_title: Aspose.3D .NET API
title: Shear Bottom を使用したシリンダーの作成方法 – Aspose.3D for .NET
url: /ja/net/3d-modeling/working-with-cylinder/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# シアーボトム付きシリンダーの作成方法 – Aspose.3D for .NET

## はじめに
.NET 環境でカスタマイズされたシアーボトムを持つ **シリンダー** オブジェクトの作成方法に興味があるなら、ここが正しい場所です。このチュートリアルでは、3‑D シーンの設定から最終モデルを OBJ ファイルとしてエクスポートするまでのすべての手順を順に解説し、**Aspose.3D for .NET** を使用して *初心者向け 3D モデリング* スキルを向上させることができます。

## クイック回答
- **3D モデルを開始するための主要クラスは何ですか？** `Scene` はすべてのジオメトリのルートコンテナを作成します。  
- **モデルを OBJ にエクスポートするメソッドはどれですか？** `scene.Save(..., FileFormat.WavefrontOBJ)`。  
- **テストにライセンスは必要ですか？** 無料トライアルが利用可能です — FAQ のトライアルリンクをご参照ください。  
- **シアー角度を変更できますか？** はい、`ShearBottom` を `Vector2` 値で変更します。  
- **初心者に適していますか？** もちろんです。API は低レベルのメッシュ処理を抽象化しています。

## 3D シーンとは何ですか？
*3D シーン* は、すべてのジオメトリエンティティ、ライト、カメラ、変換を保持する階層型コンテナです。Aspose.3D では `Scene` クラスがモデルを整理し、後でエクスポートするためのシンプルな方法を提供します。

## なぜ OBJ にエクスポートするのか？
OBJ は多くの 3‑D アプリケーション（Blender、Maya、Unity）でインポート可能な、広くサポートされたテキストベースのフォーマットです。OBJ にエクスポートすることで、.NET の外部でシリンダーモデルを共有したり、さらに編集したりできます。

## 前提条件
- C# と .NET 開発の基本的な知識。  
- **Aspose.3D for .NET** がインストールされていること – **[here](https://releases.aspose.com/3d/net/)** からダウンロードできます。  
- .NET IDE（Visual Studio、Rider、または VS Code）でコーディングできる環境。

## 名前空間のインポート
まず、必要な名前空間をスコープに持ち込み、API の型が認識されるようにします。

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

## ステップ 1: 3D シーンの作成
`Scene` オブジェクトはモデル階層のルートとして機能します。

```csharp
Scene scene = new Scene();
```

## ステップ 2: シリンダー 1 の作成
半径 2、 高さ 10、 20 個のラジアルセグメントを持つ最初のシリンダーを生成します。

```csharp
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```

## ステップ 3: シリンダー 1 のシアーボトムをカスタマイズ
シアー変換を適用し、ファンシリンダー生成を有効にし、その他のプロパティを調整して目的の形状を実現します。

```csharp
// Shear 47.5deg in the xy plane (z-axis)
cylinder1.ShearBottom = new Vector2(0, 0.83); 

// Set GenerateFanCylinder to true
cylinder1.GenerateFanCylinder = true;
// Set ThetaLength
cylinder1.ThetaLength = MathUtils.ToRadian(270);

// Set OffsetTop
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```

## ステップ 4: シリンダー 1 をシーンに追加
平行移動変換を使用して、最初のシリンダーを便利な位置に配置します。

```csharp
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```

## ステップ 5: シリンダー 2 の作成
同じ基本寸法でカスタムシアーなしの第2シリンダーを作成します—並列比較に最適です。

```csharp
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```

## ステップ 6: シリンダー 2 をシーンに追加
単に第2シリンダーをシーングラフに添付します。

```csharp
scene.RootNode.CreateChildNode(cylinder2);
```

## ステップ 7: シーンを OBJ ファイルとしてエクスポート
最後に、シーン全体を OBJ ファイルとして保存し、任意の標準 3‑D ビューアで開けるようにします。

```csharp
scene.Save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WavefrontOBJ);
```

## 一般的な問題と解決策
| 問題 | 発生原因 | 対策 |
|------|----------|------|
| **OBJ ファイルが空です** | シーンにジオメトリが添付されていません。 | `scene.RootNode` に両方のシリンダーが追加されていることを確認してください。 |
| **シアーが正しくありません** | `ShearBottom` は角度のタンジェントを期待します。 | `Math.Tan(angleInRadians)` を使用するか、約 47.5° に相当する `0.83` を使用してください。 |
| **ファイルパスエラー** | ディレクトリが無効または存在しません。 | `Path.Combine(Environment.CurrentDirectory, "CustomizedShearBottomCylinder.obj")` を使用してください。 |

## よくある質問
### Aspose.3D for .NET は初心者に適していますか？
もちろんです！Aspose.3D for .NET は、3‑D モデリングの数学的に重い部分を抽象化したハイレベル API を提供し、あらゆるスキルレベルの開発者にとって取り組みやすくなっています。

### シリンダーに異なるシアー角度を適用できますか？
はい、各 `Cylinder` インスタンスは独自の `ShearBottom` プロパティを持っているため、オブジェクトごとに異なる角度を割り当てることができます。

### トライアル版は利用可能ですか？
はい、無料トライアル版は **[here](https://releases.aspose.com/)** でご確認いただけます。

### 追加サポートはどこで見つけられますか？
コミュニティの支援、コードサンプル、ディスカッションは **[Aspose.3D forum](https://forum.aspose.com/c/3d/18)** をご覧ください。

### 一時ライセンスはどのように取得できますか？
一時ライセンスは **[here](https://purchase.aspose.com/temporary-license/)** で取得できます。

**追加の Q&A**

**Q: モデルを STL のような別の形式でエクスポートするには？**  
A: `scene.Save` 呼び出しで `FileFormat.WavefrontOBJ` を `FileFormat.STL` に置き換えます。

**Q: 作成後にシリンダーをアニメーションさせることはできますか？**  
A: はい、Aspose.3D が提供する `Animation` クラスを使用して、ノード変換にキーフレームアニメーションを追加できます。

**Q: API は .NET Core をサポートしていますか？**  
A: このライブラリは .NET Core、.NET 5 以降、.NET 6 以降と完全に互換性があります。

---

**最終更新日:** 2026-03-26  
**テスト対象:** Aspose.3D for .NET (latest release)  
**作者:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}