---
title: 3D シーンでの 3 次元プロパティの設定
linktitle: 3D シーンでの 3 次元プロパティの設定
second_title: Aspose.3D .NET API
description: 3D プロパティの設定に関する Aspose.3D for .NET チュートリアルを参照してください。コード例を使って段階的に学習してください。 3D シーン操作スキルを向上させます。
weight: 14
url: /ja/net/3d-scene/set-3d-properties/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 3D シーンでの 3 次元プロパティの設定

## 導入

魅力的な 3D シーンを作成するには、多くの場合、さまざまなプロパティを操作して、プロジェクトに深みとリアリズムを加える能力が必要です。 Aspose.3D for .NET はこれを実現するための強力なツールセットを提供し、3D シーン内の 3 次元プロパティを簡単に設定および変更できるようにします。このチュートリアルでは、Aspose.3D for .NET を効果的に活用する方法について理解を深めながら、プロセスを段階的に説明します。

## 前提条件

チュートリアルに入る前に、次の前提条件を満たしていることを確認してください。

-  Aspose.3D for .NET: ライブラリが .NET プロジェクトにインストールされていることを確認してください。ダウンロードできます[ここ](https://releases.aspose.com/3d/net/).

- ドキュメント ディレクトリ: 3D ドキュメントを保存するディレクトリを作成します。

必要な要素が揃ったので、Aspose.3D for .NET を使用して 3D シーンに 3 次元プロパティを設定するプロセスを見てみましょう。

## 名前空間のインポート

まず、必要な名前空間をプロジェクトにインポートします。これらの名前空間は、Aspose.3D for .NET で 3 次元プロパティを操作するために必要なクラスとメソッドを提供します。

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

## ステップ 1: 3D シーンをロードする

3D シーンをロードすることから始めます。この例では、テクスチャが埋め込まれた FBX ファイルを使用します。

```csharp
//ExStart: Load3DScene
string dataDir = "Your Document Directory";
Scene scene = new Scene(dataDir + "EmbeddedTexture.fbx");
//ExEnd: Load3DScene
```

## ステップ 2: マテリアルのプロパティにアクセスする

ロードされた 3D シーンのマテリアル プロパティにアクセスして、その特性を操作します。

```csharp
//例開始: マテリアル プロパティへのアクセス
Material material = scene.RootNode.ChildNodes[0].Material;
PropertyCollection props = material.Properties;
//ExEnd: Accessマテリアルプロパティ
```

## ステップ 3: すべてのプロパティをリストする

foreach ループまたは序数の for ループを使用して、マテリアルのすべてのプロパティを一覧表示します。

```csharp
//ExStart:ListAllProperties
foreach (var prop in props)
{
    Console.WriteLine("{0} = {1}", prop.Name, prop.Value);
}

//または序数の for ループを使用する
for (int i = 0; i < props.Count; i++)
{
    var prop = props[i];
    Console.WriteLine("{0} = {1}", prop.Name, prop.Value);
}
//ExEnd:ListAllProperties
```

## ステップ 4: プロパティを名前で取得および変更する

特定のプロパティを名前で取得および変更します。

```csharp
//ExStart: GetModifyPropertyByName
var diffuse = props["Diffuse"];
Console.WriteLine(diffuse);

//プロパティ値を名前で変更する
props["Diffuse"] = new Vector3(1, 0, 1);
//ExEnd: GetModifyPropertyByName
```

## ステップ 5: プロパティ インスタンスを名前で取得する

さらに操作するために、名前でプロパティ インスタンスを取得します。

```csharp
//ExStart: GetPropertyInstanceByName
Property pdiffuse = props.FindProperty("Diffuse");
Console.WriteLine(pdiffuse);
//ExEnd: GetPropertyInstanceByName
```

## ステップ 6: プロパティのプロパティを走査する

以来`Property`から継承されます`A3DObject`、プロパティのプロパティを横断することができます。

```csharp
//ExStart: TraversePropertyProperties
Console.WriteLine("Property flags = {0}", pdiffuse.GetProperty("flags"));

//FBX ファイルでのみ定義されているいくつかのプロパティ:
Console.WriteLine("Label = {0}", pdiffuse.GetProperty("label"));
Console.WriteLine("Type Name = {0}", pdiffuse.GetProperty("typeName"));

//敷地内での通行が可能
foreach (var pp in pdiffuse.Properties)
{
    Console.WriteLine("Diffuse.{0} = {1}", pp.Name, pp.Value);
}
//ExEnd: TraversePropertyProperties
```

## 結論

おめでとう！これで、Aspose.3D for .NET を使用して 3D シーンで 3 次元プロパティを設定する技術を習得できました。さまざまなプロパティと値を試して、3D プロジェクトに命を吹き込みます。

## よくある質問

### Q1: Aspose.3D for .NET を他の 3D ファイル形式で使用できますか?

A1: はい、Aspose.3D は、FBX、STL などを含むさまざまな 3D ファイル形式をサポートしています。

### Q2: Aspose.3D for .NET の一時ライセンスを取得するにはどうすればよいですか?

 A2: 訪問[ここ](https://purchase.aspose.com/temporary-license/)仮免許を取得するためです。

### Q3: Aspose.3D ユーザー向けのコミュニティ フォーラムはありますか?

 A3: はい、次の場所でサポートとディスカッションを見つけることができます。[Aspose.3D フォーラム](https://forum.aspose.com/c/3d/18).

### Q4: Aspose.3D for .NET の詳細なドキュメントはどこで見つけられますか?

 A4: を参照してください。[ドキュメンテーション](https://reference.aspose.com/3d/net/)総合的な指導を行います。

### Q5: 購入する前に、Aspose.3D for .NET を無料で試用できますか?

 A5：確かに！ダウンロード[無料試用版](https://releases.aspose.com/)その特徴を探るために。

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
