---
title: クォータニオンの連結
linktitle: クォータニオンの連結
second_title: Aspose.3D .NET API
description: Aspose.3D for .NET を使用して、3D シーンにおけるクォータニオン操作の威力を体験してください。没入型変換のために四元数を段階的に連結する方法を学びます。
weight: 11
url: /ja/net/geometry-and-hierarchy/concatenate-quaternions/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# クォータニオンの連結

## 導入

Aspose.3D for .NET を使用して 3D シーンでクォータニオンを連結するためのこの包括的なチュートリアルへようこそ。クォータニオン操作のスキルを向上させたいと考えている開発者または 3D 愛好家にとって、ここは正しい場所です。このチュートリアルでは、プロセスを段階的にガイドし、スムーズな学習体験を保証します。

## 前提条件

チュートリアルに入る前に、次の前提条件が満たされていることを確認してください。

-  Aspose.3D for .NET ライブラリ: からライブラリをダウンロードしてインストールします。[Aspose ウェブサイト](https://releases.aspose.com/3d/net/).
- 開発環境: .NET 用の有効な開発環境があることを確認します。

## 名前空間のインポート

.NET プロジェクトに、Aspose.3D の機能を活用するために必要な名前空間を含めます。

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Utilities;
```

## ステップ 1: シーンを作成する

まず、Aspose.3D ライブラリを使用して 3D シーンを作成します。シーンはクォータニオン操作のキャンバスとして機能します。

```csharp
Scene scene = new Scene();
```

## ステップ 2: クォータニオンを定義する

 3 つの四元数を定義し、`q1`, `q2` 、 そして`q3`、それぞれが特定の回転を表します。

```csharp
Quaternion q1 = Quaternion.FromEulerAngle(Math.PI * 0.5, 0, 0);
Quaternion q2 = Quaternion.FromAngleAxis(-Math.PI * 0.5, Vector3.XAxis);
Quaternion q3 = q1.Concat(q2);
```

## ステップ 3: シリンダーを作成する

それぞれが四元数を表す 3 つの円柱を作成します。定義された四元数に基づいて、回転および平行移動のプロパティを設定します。

```csharp
Node cylinder = scene.RootNode.CreateChildNode("cylinder-q1", new Cylinder(0.1, 1, 2));
cylinder.Transform.Rotation = q1;
cylinder.Transform.Translation = new Vector3(-5, 2, 0);

// q2 と q3 についても繰り返します
```

## ステップ 4: ファイルに保存

出力形式とファイル名を指定して、シーンをファイルに保存します。

```csharp
var output = "Your Output Directory" + "test_out.fbx";
scene.Save(output, FileFormat.FBX7400ASCII);
```

## ステップ 5: 成功メッセージを表示する

クォータニオンが連結され、ファイルが保存されたら、ファイル パスとともに成功メッセージを出力します。

```csharp
Console.WriteLine("\nQuaternions concatenated successfully.\nFile saved at " + output);
```

## 結論

おめでとう！ Aspose.3D for .NET を使用して 3D シーンでクォータニオンを連結する方法を学習しました。プロジェクトで独自の変換を実現するには、さまざまなクォータニオンの組み合わせを試してください。

## よくある質問

### Q1: 3D グラフィックスのクォータニオンとは何ですか?

A1: クォータニオンは 3D 空間での回転を表すために使用される数学的エンティティであり、他の回転表現に比べて利点があります。

### Q2: Aspose.3D for .NET を他の .NET ライブラリと一緒に使用できますか?

A2: はい、Aspose.3D for .NET は他の .NET ライブラリとシームレスに動作するように設計されています。

### Q3: Aspose.3D for .NET の無料トライアルはありますか?

A3: はい、無料トライアルにアクセスできます。[ここ](https://releases.aspose.com/).

### Q4: Aspose.3D for .NET のサポートを受けるにはどうすればよいですか?

 A4: にアクセスしてください。[Aspose.3D フォーラム](https://forum.aspose.com/c/3d/18)コミュニティのサポートとディスカッションのために。

### Q5: Aspose.3D for .NET の一時ライセンスを使用できますか?

 A5: はい、一時ライセンスを取得できます。[ここ](https://purchase.aspose.com/temporary-license/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
