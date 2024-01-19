---
title: 接線データと従法線データの構築
linktitle: 接線データと従法線データの構築
second_title: Aspose.3D .NET API
description: 接線データと従法線データの力を解き放ち、3D モデルを最適化して、レンダリングをよりスムーズにし、読み込み時間を短縮し、パフォーマンスを向上させます。
type: docs
weight: 10
url: /ja/net/objects/build-tangent-binormal-data/
---
## 導入
3D モデルの動作が遅いためにプロジェクトが行き詰まり、イライラしたことはありませんか?開発者の皆さん、心配しないでください。順風満帆の秘訣は接線データと従法線データにあります。これらの縁の下の力持ちはメッシュ レンダリングを最適化し、モデルをあらゆるステージでオペラの歌姫のように歌わせます。しかし、私たちは彼らの力をどのように利用するのでしょうか?心配しないでください。この包括的なガイドでは、数回クリックするだけで接線および従法線データの魔法を解き放つ Aspose.3D for .NET ツールキットが提供されます。

## 前提条件:

1.  Aspose.3D for .NET: 最新バージョンを次からダウンロードします。[ここ](https://releases.aspose.com/3d/net/)そしてそれをインストールします。
2. 3D モデル: FBX、OBJ、または STL ファイルを取得します。このチュートリアルでは「document.fbx」を使用します。

## 名前空間をインポートします。

必要な名前空間をインポートして、コードの領域に足を踏み入れます。

```C#
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
```

## 1. 3D ファイルをロードします。

 3D モデルが眠っている巨人であると想像してください。それを目覚めさせる時が来ました！使用`Scene`ファイルパスからモデルをロードするクラス:

```C#
Scene scene = new Scene(RunExamples.GetDataFilePath("document.fbx"));
```

## 2. シーンを三角形化します。

三角形を 3D 傑作の構成要素として考えてください。 Aspose.3D は便利な機能を提供します。`PolygonModifier`メッシュを効率的に三角形に変換するクラス。ただ電話してください`BuildTangentBinormal`シーン上のメソッド:

```C#
PolygonModifier.BuildTangentBinormal(scene);
```

## 3. 接線データと従法線データを解放します。

モデルを鎧を着た騎士としてイメージしてください。接線データと従法線データは、この装甲の隠れた継ぎ目として機能し、光がサーフェスとどのように相互作用するかをガイドします。 Aspose.3D を使用すると、このデータに簡単にアクセスできます。使用`Mesh`シーンのプロパティを使用して個々のメッシュにアクセスし、各メッシュをループします。`Polygons`コレクション：

```C#
foreach (Mesh mesh in scene.Meshes)
{
    foreach (Polygon polygon in mesh.Polygons)
    {
        //各頂点の接線ベクトルと従法線ベクトルにアクセスする
        var tangent = polygon.Tangent;
        var binormal = polygon.Binormal;
        //これらのベクトルを使って魔法をかけてみましょう!
    }
}
```

## 4. 変換されたモデルを保存します。

接線データと従法線データがメッシュに織り込まれているので、傑作を披露する時が来ました。使用`Save`シーン オブジェクトのメソッドで、出力ディレクトリと形式を指定します (例: "Your Output Directory"+"BuildTangentAndBinormalData_out.fbx"、FileFormat.FBX7400ASCII):

```C#
scene.Save("Your Output Directory"+"BuildTangentAndBinormalData_out.fbx", FileFormat.FBX7400ASCII);
```

## 結論
これで、3D モデルに接線データと従法線データの力が加わりました。よりスムーズなレンダリング、より速いロード時間、そして他の開発者からの羨望の視線を目撃してください。覚えておいてください、これはほんの始まりに過ぎません。 Aspose.3D は、3D 作品を操作、分析、エクスポートするための膨大なツールを提供します。あなたの内なる 3D アーティストの力を解放し、Aspose.3D でデジタル キャンバスをペイントしてください。

## よくある質問

### モデルが FBX 形式ではない場合はどうすればよいですか? 
Aspose.3D は、OBJ、STL、glTF などの多数の形式をサポートしています。続行する前に、モデルをサポートされている形式に変換してください。
### 接線と従法線データを手動で調整できますか? 
はい、Aspose.3D はこれらのベクトルをきめ細かく制御できます。を探索してください`Vertex`そして`Polygon`高度な操作オプションのクラス。
### Aspose.3D には無料トライアルがありますか? 
絶対に！無料トライアル版を以下からダウンロードしてください[ここ](https://releases.aspose.com/3d/net/)そして、コミットする前に魔法をテストしてください。
### さらに多くのリソースやサポートはどこで入手できますか? 
 Aspose.3D には、次の場所に包括的なドキュメント ポータルがあります。[ここ](https://docs.aspose.com/3d/net/)。さらに、Aspose コミュニティ フォーラム (次のサイト)[ここ](https://forum.aspose.com/)はいつも親切な開発者で賑わっています。
### Aspose.3D を商用プロジェクトに使用できますか? 
はい！ Aspose.3D は、ニーズに合わせてさまざまなライセンス オプションを提供します。料金ページは次のとおりです。[ここ](https://purchase.aspose.com/buy)