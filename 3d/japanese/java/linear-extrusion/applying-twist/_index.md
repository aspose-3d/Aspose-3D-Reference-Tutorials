---
date: 2025-12-17
description: Aspose.3D for Java を使用して、線形押し出しツイストでねじれた 3D モデルを作成し、OBJ ファイルとしてエクスポートする方法を学びましょう。ステップバイステップのガイドに従ってください。
linktitle: Applying Twist in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: ねじれた3Dモデルの作成 – Aspose.3D for Java を使用した線形押し出しでのツイスト適用
url: /ja/java/linear-extrusion/applying-twist/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose.3D for Java を使用した線形押し出しでのツイスト適用

## はじめに

Aspose.3D for Java を使用して線形押し出し中にツイストを適用し、**ねじれた 3D モデルの作成方法**をステップバイステップでご紹介します。建築ビジュアライゼーション、ゲームアセット、エンジニアリングプロトタイプのいずれを作成していても、ツイストを加えるだけで数行のコードでジオメトリに動的で螺旋状の外観を与えることができます。

## クイック回答
- **押し出しにおける「ツイスト」とは何ですか？** 形状が伸長される際に、プロファイルを押し出し軸の周りで回転させます。  
- **どの API クラスがツイストを処理しますか？** `LinearExtrusion` が `setTwist` メソッドを提供します。  
- **サンプルを実行するのにライセンスは必要ですか？** 無料トライアルで評価は可能ですが、商用利用には商用ライセンスが必要です。  
- **結果を OBJ としてエクスポートできますか？** はい、`scene.save(..., FileFormat.WAVEFRONTOBJ)` を使用します。  
- **必要な Java バージョンは何ですか？** Java 8 以降が完全にサポートされています。

## 前提条件

チュートリアルに入る前に、以下の前提条件が整っていることを確認してください。

- Java 開発環境: システムに Java がインストールされていることを確認してください。  
- Aspose.3D ライブラリ: [download link](https://releases.aspose.com/3d/java/) から Java 用 Aspose.3D ライブラリをダウンロードしてインストールしてください。  
- ドキュメント: 詳細なガイダンスは [Aspose.3D documentation](https://reference.aspose.com/3d/java/) を参照してください。

## パッケージのインポート

コーディングを開始する前に、必要なパッケージを Java プロジェクトにインポートします。以下はその例です。

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## ドキュメントディレクトリの設定

まず、生成された 3D ファイルの保存先ディレクトリを定義します。

```java
// ExStart:SetDocumentDirectory
String MyDir = "Your Document Directory";
// ExEnd:SetDocumentDirectory
```

## 基本プロファイルの初期化

次に、押し出す形状を作成します。この例では、角が小さく丸められた矩形を使用します。

```java
// ExStart:InitializeBaseProfile
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
// ExEnd:InitializeBaseProfile
```

## シーンの作成

`Scene` オブジェクトはすべての 3D ノードのコンテナとして機能します。

```java
// ExStart:CreateScene
Scene scene = new Scene();
// ExEnd:CreateScene
```

## ノードの作成

シーンに 2 つの子ノードを追加します – 1 つはそのまま直線、もう 1 つはツイストが適用されます。

```java
// ExStart:CreateNodes
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
// ExEnd:CreateNodes
```

## 線形押し出しツイスト

ここで、両方のノードに対して **線形押し出しツイスト** を実行します。左側のノードは 0° のツイスト（直線）で、右側のノードは 90° のツイストを付与し、螺旋状の形状を作ります。また、スムーズなジオメトリになるようにスライス数も設定します。

```java
// ExStart:LinearExtrusionWithTwist
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(0); setSlices(100); }});
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(90); setSlices(100); }});
// ExEnd:LinearExtrusionWithTwist
```

## OBJ ファイルのエクスポート（Java）

最後に、広くサポートされている OBJ 形式でシーンを保存します。これにより、Aspose.3D の **export OBJ file Java** 機能が実証されます。

```java
// ExStart:Save3DScene
scene.save(MyDir + "TwistInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:Save3DScene
```

## これが重要な理由

ツイストされた 3D モデルを作成することで、外部のモデリングツールを使用せずに強力なビジュアル効果を得られます。特に以下の用途で有用です。

- **機械部品** でねじ状の特徴が必要なもの（例: スプリング、ねじ）。  
- **アーティスティックデザイン** で、微妙な螺旋が視覚的な興味を加える場合。  
- **ゲームアセット** で、低ポリゴンかつ手続き的に生成されたジオメトリが有利な場合。

## よくある問題とヒント

| 問題 | 解決策 |
|-------|----------|
| ツイストが平坦に見える、または欠落している | `setSlices` を十分に高く設定してください（例: 100）で滑らかな回転を実現します。 |
| OBJ ファイルがビューアで開かない | 出力パス（`MyDir`）が正しいか、ファイルの書き込み権限があるか確認してください。 |
| 予期しないスケーリング | ソースプロファイルの単位系を確認してください。Aspose.3D はデフォルトでメートル単位で動作します。 |

## よくある質問

**Q: Aspose.3D for Java を使用して他の 3D ファイル形式とやり取りできますか？**  
A: はい、Aspose.3D は FBX、STL、3MF など幅広い形式をサポートしています。

**Q: Aspose.3D for Java のサポートはどこで受けられますか？**  
A: コミュニティの助けや公式サポートは [Aspose.3D forum](https://forum.aspose.com/c/3d/18) をご覧ください。

**Q: 無料トライアルは利用できますか？**  
A: はい、[here](https://releases.aspose.com/) からトライアル版をダウンロードできます。

**Q: テスト用の一時ライセンスはどう取得しますか？**  
A: [temporary license page](https://purchase.aspose.com/temporary-license/) から取得してください。

**Q: フルライセンスはどこで購入できますか？**  
A: [buying page](https://purchase.aspose.com/buy) から Aspose.3D for Java を購入してください。

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Last Updated:** 2025-12-17  
**Tested With:** Aspose.3D 24.11 for Java  
**Author:** Aspose  

---