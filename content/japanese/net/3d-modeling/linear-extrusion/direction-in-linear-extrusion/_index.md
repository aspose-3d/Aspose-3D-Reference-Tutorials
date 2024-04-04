---
title: 線形押出の方向
linktitle: 線形押出の方向
second_title: Aspose.3D .NET API
description: Aspose.3D for .NET で 3D モデリングの世界を解き放ちます。方向線形押し出しを学び、創造性を高め、没入型アプリケーションを簡単に作成します。
type: docs
weight: 11
url: /ja/net/3d-modeling/linear-extrusion/direction-in-linear-extrusion/
---
## 導入

ソフトウェア開発のダイナミックな世界では、没入型 3D モデルの作成は不可欠なスキルです。 Aspose.3D for .NET は、アプリケーションで 3D モデリングの可能性を活用するための堅牢なツール セットを開発者に提供します。このチュートリアルでは、線形押し出しの興味深い世界を掘り下げ、「線形押し出しの方向」機能の微妙な違いを探っていきます。

## 前提条件

このエキサイティングな旅に乗り出す前に、次の前提条件が満たされていることを確認してください。

-  Aspose.3D for .NET: からライブラリをダウンロードしてインストールします。[Aspose.3D .NET ドキュメント](https://reference.aspose.com/3d/net/).

- 開発環境: 動作する .NET 開発環境がセットアップされていることを確認します。

## 名前空間のインポート

.NET プロジェクトで、Aspose.3D の機能にアクセスするために必要な名前空間をインポートします。コードの先頭に次の行を追加します。

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## ステップ 1: 基本プロファイルを初期化する

まず、押し出される基本プロファイルを初期化します。この例では、丸め半径 0.3 の長方形を作成します。

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## ステップ 2: 3D シーンを作成する

シーンを作成して、3D 傑作の基礎を構築します。

```csharp
Scene scene = new Scene();
```

## ステップ 3: ノードの作成

シーン内にノードを生成して、3D 環境のさまざまなコンポーネントを表します。

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(8, 0, 0);
```

## ステップ 4: 方向なしの線形押し出し

を使用して、左側のノードで線形押し出しを実行します。`Twist`そして`Slices`プロパティ。

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100 });
```

## ステップ 5: 方向を指定した線形押し出し

を組み込むことで押出能力を拡張します。`Direction`右側のノードのプロパティ。

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100, Direction = new Vector3(0.3, 0.2, 1) });
```

## ステップ 6: 3D シーンを保存する

 3D シーンを保存して、作成物を保存します。交換する`"Your Output Directory"`目的のディレクトリを指定します。

```csharp
scene.Save("Your Output Directory" + "DirectionInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

おめでとう！従来のアプローチと方向性アプローチの両方を検討し、Aspose.3D for .NET を使用して線形押し出しを正常に実装しました。

## 結論

このチュートリアルでは、Aspose.3D for .NET を使用して 3D モデリングの魅力的な領域をナビゲートしました。直線押し出しは、方向の有無にかかわらず、視覚的に素晴らしいアプリケーションを作成しようとしている開発者に無限の可能性をもたらします。 Aspose.3D を使用すると、3D モデリングのパワーを簡単に利用できます。

## よくある質問

### Q1: Aspose.3D for .NET の一時ライセンスを取得するにはどうすればよいですか?

 A1: 訪問[一時ライセンスを剥奪する](https://purchase.aspose.com/temporary-license/)仮免許を取得するためです。

### Q2: Aspose.3D のサポートはどこで見つけられますか?

 A2: に参加してください。[Aspose.3D フォーラム](https://forum.aspose.com/c/3d/18)支援を求め、コミュニティとつながるために。

### Q3: 無料トライアルはありますか?

A3: はい、無料トライアルで機能を試してください。[Aspose.3D リリース](https://releases.aspose.com/).

### Q4: Aspose.3D for .NET を購入するにはどうすればよいですか?

 A4: に移動します。[Aspose購入ページ](https://purchase.aspose.com/buy)ライセンス オプションと購入の詳細については、こちらをご覧ください。

### Q5: Aspose.3D for .NET の詳細なドキュメントはどこで見つけられますか?

 A5: 総合を参照してください。[Aspose.3D .NET ドキュメント](https://reference.aspose.com/3d/net/)詳細な情報については。