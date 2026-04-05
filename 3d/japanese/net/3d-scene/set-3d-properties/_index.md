---
date: 2026-03-28
description: Aspose.3D for .NET を使用して、マテリアルのプロパティを一覧表示し、拡散色を変更し、3D マテリアル属性を修正する方法を学びます。ステップバイステップのコード例が含まれています。
linktitle: List Material Properties in 3D Scenes with Aspose.3D
second_title: Aspose.3D .NET API
title: Aspose.3Dで3Dシーンのマテリアルプロパティを一覧表示
url: /ja/net/3d-scene/set-3d-properties/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose.3Dで3Dシーンのマテリアルプロパティを一覧表示

## はじめに

3Dモデルの**マテリアルプロパティを一覧表示**し、拡散色などを調整したい場合は、ここが最適です。Aspose.3D for .NET は、C# コードから離れることなく、マテリアル属性を検査、取得、変更できるクリーンでオブジェクト指向の API を提供します。このチュートリアルでは、シーンの読み込み、マテリアルプロパティの列挙、拡散成分などの値変更手順を順に解説し、モデルに思い通りの外観を与える方法を紹介します。

## クイック回答
- **主な目的は？** マテリアルプロパティを一覧表示し、（例：拡散色）を変更すること。  
- **必要なライブラリは？** Aspose.3D for .NET。  
- **ライセンスは必要？** 本番使用には一時ライセンスまたはフルライセンスが必要です。  
- **対応ファイル形式は？** FBX、OBJ、STL、STL‑ASCII、3MF など多数。  
- **実装にかかる目安は？** 基本的なプロパティ一覧スクリプトで約10‑15分。

## **list material properties** とは何ですか？
マテリアルプロパティの一覧表示とは、マテリアルの `PropertyCollection` を走査し、各プロパティ名と現在の値を取得することです。デバッグや視覚的検査、実行時にユーザーがマテリアル設定を調整できる UI コントロールの構築に役立ちます。

## Aspose.3Dで**material properties**にアクセスする理由は？
- **外部コンバータ不要** – ネイティブな .NET オブジェクトで直接操作。  
- **豊富なプロパティモデル** – 標準的な PBR 値に加えて、カスタム FBX 固有属性もサポート。  
- **クロスプラットフォーム** – .NET Framework、.NET Core、.NET 5/6+ で動作。

## 前提条件

- プロジェクトに Aspose.3D for .NET をインストール済みであること。ダウンロードは[こちら](https://releases.aspose.com/3d/net/)。  
- ディスク上に 3‑D ソースファイルを格納するフォルダー（例：埋め込みテクスチャを持つ FBX ファイル）が用意されていること。

基本が整ったので、コードに入りましょう。

## 名前空間のインポート

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```

## 手順 1: 3Dシーンのロード

```csharp
//ExStart: Load3DScene
string dataDir = "Your Document Directory";
Scene scene = new Scene(dataDir + "EmbeddedTexture.fbx");
//ExEnd: Load3DScene
```

## 手順 2: 最初のノードの**material properties**にアクセス

```csharp
//ExStart: AccessMaterialProperties
Material material = scene.RootNode.ChildNodes[0].Material;
PropertyCollection props = material.Properties;
//ExEnd: AccessMaterialProperties
```

## 手順 3: **list material properties** – すべての名前/値ペアを表示

```csharp
//ExStart: ListAllProperties
foreach (var prop in props)
{
    Console.WriteLine("{0} = {1}", prop.Name, prop.Value);
}

//or using ordinal for loop
for (int i = 0; i < props.Count; i++)
{
    var prop = props[i];
    Console.WriteLine("{0} = {1}", prop.Name, prop.Value);
}
//ExEnd: ListAllProperties
```

## 手順 4: **diffuse** の変更方法 – Diffuse プロパティを更新

```csharp
//ExStart: GetModifyPropertyByName
var diffuse = props["Diffuse"];
Console.WriteLine(diffuse);

//modify property value by name
props["Diffuse"] = new Vector3(1, 0, 1); // sets a magenta diffuse color
//ExEnd: GetModifyPropertyByName
```

## 手順 5: 名前でプロパティを取得 – 強く型付けされたインスタンスを取得

```csharp
//ExStart: GetPropertyInstanceByName
Property pdiffuse = props.FindProperty("Diffuse");
Console.WriteLine(pdiffuse);
//ExEnd: GetPropertyInstanceByName
```

## 手順 6: プロパティ自身のサブプロパティを走査（上級者向け）

```csharp
//ExStart: TraversePropertyProperties
Console.WriteLine("Property flags = {0}", pdiffuse.GetProperty("flags"));

//and some properties that only defined in FBX file:
Console.WriteLine("Label = {0}", pdiffuse.GetProperty("label"));
Console.WriteLine("Type Name = {0}", pdiffuse.GetProperty("typeName"));

//traversal on property's property is possible
foreach (var pp in pdiffuse.Properties)
{
    Console.WriteLine("Diffuse.{0} = {1}", pp.Name, pp.Value);
}
//ExEnd: TraversePropertyProperties
```

## **diffuse** 以外の3Dマテリアルカラーの変更方法
スペキュラ、アンビエント、エミッシブカラーを変更したい場合は、上記の `props["..."]` 代入で `"Diffuse"` を `"Specular"` や `"Ambient"` に置き換えるだけです。`Vector3` や `Vector4` 構造体は同様に使用できます。

## C#で**material color**を更新する方法
マテリアルの外観変更は、`PropertyCollection` の該当プロパティを更新するだけです。拡散、スペキュラ、またはカスタムカラー属性を変更する場合でも、手順は変わりません。

1. 正確な名前（大文字小文字を区別）でプロパティを取得。  
2. 新しい `Vector3`（RGB）または `Vector4`（RGBA）値を代入。

API が直接 C# オブジェクトと連携するため、**C#で material color を更新**するコードは中間ファイルやコンバータを必要とせず、リアルタイムエディタやバッチ処理パイプラインに最適です。

## よくある落とし穴とヒント
- **プロパティ名の大文字小文字** – Aspose.3D のキーはケースセンシティブです。一覧出力に表示された正確な名前を使用してください。  
- **プロパティが存在しない** – すべてのマテリアルがすべての PBR 属性を公開しているわけではありません。アクセス前に `props.ContainsKey("Specular")` で確認しましょう。  
- **変更の保存** – プロパティ変更後は `scene.Save("output.fbx");` を呼び出して変更を永続化してください。

## 結論

これで **マテリアルプロパティの一覧表示**、**名前でプロパティを取得**、そして **diffuse 色（または他のマテリアル属性）を変更**する方法を Aspose.3D for .NET を使って習得しました。さまざまなプロパティタイプを試して 3‑D アセットの外観を微調整し、**C#で material color を更新**するコードを 1 行で実装できることを覚えておいてください。

## FAQ

### Q1: Aspose.3D for .NET を他の 3D ファイル形式と一緒に使用できますか？

A1: はい、Aspose.3D は FBX、STL など多数の 3D ファイル形式をサポートしています。

### Q2: Aspose.3D for .NET の一時ライセンスはどこで取得できますか？

A2: [こちら](https://purchase.aspose.com/temporary-license/) から一時ライセンスを取得してください。

### Q3: Aspose.3D ユーザー向けのコミュニティフォーラムはありますか？

A3: はい、[Aspose.3D フォーラム](https://forum.aspose.com/c/3d/18) でサポートやディスカッションが行われています。

### Q4: Aspose.3D for .NET の詳細ドキュメントはどこにありますか？

A4: 詳細なガイドは[ドキュメント](https://reference.aspose.com/3d/net/)をご参照ください。

### Q5: 購入前に Aspose.3D for .NET を無料で試すことはできますか？

A5: もちろんです！[無料トライアル版](https://releases.aspose.com/) をダウンロードして機能を確認してください。

## よくある質問

**Q: `Vector3(1, 0, 1)` は何を表していますか？**  
A: 線形カラー空間で拡散色をマゼンタ（赤 = 1、緑 = 0、青 = 1）に設定します。

**Q: プロパティ変更後に `scene.Save` を呼び出す必要がありますか？**  
A: はい、シーンを保存しないと変更はメモリ上に留まります。

**Q: カスタム FBX 属性を列挙できますか？**  
A: 可能です。`PropertyCollection` にカスタム属性が含まれ、`GetProperty("customName")` で取得できます。

**Q: 複数のマテリアルを一括で更新する方法はありますか？**  
A: `scene.RootNode.ChildNodes` をループし、各マテリアルに対して同じプロパティ変更手順を繰り返してください。

**Q: Aspose.3D は .NET 6 をサポートしていますか？**  
A: はい、.NET 6 以降のバージョンと完全に互換性があります。

---

**最終更新日:** 2026-03-28  
**テスト環境:** Aspose.3D 24.11 for .NET  
**作者:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}