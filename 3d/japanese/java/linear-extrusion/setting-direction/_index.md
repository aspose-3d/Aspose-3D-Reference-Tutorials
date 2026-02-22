---
date: 2026-02-22
description: Aspose.3D for Java を使用して、線形押し出しの方向設定方法と 3D モデル OBJ のエクスポート方法を学びましょう。ステップバイステップのガイドに従ってください。
linktitle: Setting Direction in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Aspose.3D for Javaで線形押し出しの方向を設定する方法
url: /ja/java/linear-extrusion/setting-direction/
weight: 12
---

Let's produce final content.

We'll keep the shortcodes exactly as given.

Proceed.

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose.3D for Java で線形押し出しの方向を設定する方法

## はじめに

この包括的なチュートリアルでは、Aspose.3D for Java を使用して **線形押し出しの方向を設定する方法** を学びます。CAD のようなツールを作成する場合や、ゲームエンジン向けにジオメトリを生成する場合でも、押し出し方向を制御することで必要な形状を正確に作成できます。プロファイルの初期化から OBJ ファイルとして保存するまでの手順を順に解説し、**Java から直接 3D モデル OBJ ファイルをエクスポート** できるようにします。

## クイック回答
- **線形押し出しの主要クラスはどれですか？** `LinearExtrusion`
- **どのメソッドで押し出し方向を定義しますか？** `setDirection(Vector3 direction)`
- **結果を OBJ としてエクスポートできますか？** はい、`scene.save(..., FileFormat.WAVEFRONTOBJ)` を使用します
- **開発にライセンスは必要ですか？** 無料トライアルがありますが、本番環境ではライセンスが必要です
- **どの Java IDE が最適ですか？** IntelliJ IDEA または Eclipse が完全にサポートされています

## 線形押し出しとは？

線形押し出しは、2‑D のプロファイル（矩形や円など）を直線に沿って伸ばし、3‑D のソリッドを作成します。デフォルトでは正の Z 軸方向に押し出されますが、Aspose.3D では `setDirection` プロパティでその方向を変更できます。

## 線形押し出しで方向を設定する理由

カスタム方向を設定すると次のようなケースで便利です：
- シーン内の既存オブジェクトとジオメトリを整列させるとき
- 余分な変換ステップなしで斜めや傾斜した部品を作成したいとき
- 特定の座標系（例：3‑D プリントやゲームエンジン向け）に合わせてモデルをエクスポートしたいとき

## 前提条件

作業を始める前に以下を用意してください：

- Java の基本的な知識
- Aspose.3D ライブラリがインストール済み。ダウンロードは [here](https://releases.aspose.com/3d/java/) から
- Eclipse または IntelliJ IDEA などの IDE

## パッケージのインポート

まず、コア 3‑D クラスとユーティリティ型を提供する名前空間をインポートします。

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## 手順 1: 基本プロファイルの初期化

押し出す形状を作成します。この例では、エッジを滑らかにするために小さな丸み半径を持つ `RectangleShape` を使用します。

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## 手順 2: シーンの作成

`Scene` オブジェクトは、すべての 3‑D ノード、ライト、カメラ、マテリアルのコンテナとして機能します。

```java
Scene scene = new Scene();
```

## 手順 3: ノードの作成

シーンのルートに子ノードを 2 つ追加します――左側の押し出し用と右側の押し出し用です。右側のノードは、2 つのオブジェクトが重ならないように平行移動します。

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## 手順 4: 左側ノードで線形押し出しを実行

左側ノードでデフォルトの Z 軸方向でプロファイルを押し出します。さらに 360° のツイストを加え、スライス数を増やしてメッシュを滑らかにします。

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## 手順 5: 右側ノードで方向付き線形押し出しを実行

ここで **方向を設定** します。カスタム `Vector3` を `setDirection` に渡すことで、ベクトル (0.3, 0.2, 1) に沿って押し出され、斜めの形状が生成されます。

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## 手順 6: 3D シーンの保存

最後に、シーンを Wavefront OBJ 形式でエクスポートします。この手順は **Java で obj ファイルを保存** する方法を示し、任意の 3‑D ビューアで結果を簡単に確認できます。

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## よくある問題と解決策

| 問題 | 発生理由 | 解決策 |
|------|----------|--------|
| OBJ ファイルが空になる | プロファイルがノードに追加されていない | 有効なノードで `createChildNode` が呼び出されていることを確認 |
| 方向が変わらない | `setDirection` が押し出し構築後に呼び出された | 示したように `LinearExtrusion` 初期化時に方向を設定 |
| メッシュが低解像度になる | `setSlices` の値が低すぎる | スライス数を増やす（例: 100 以上） |

## 結論

これで **線形押し出しの方向を設定する方法**、ツイストやスライス設定の調整方法、そして Aspose.3D for Java を使用した **3D モデル OBJ のエクスポート** 方法が分かりました。これらのテクニックにより、ジオメトリ作成を細かく制御でき、3‑D アセットを大規模なパイプラインに統合するのが容易になります。

## FAQ

### Q1: Aspose.3D を他のプログラミング言語で使用できますか？

A1: Aspose.3D は .NET や Java など、さまざまなプログラミング言語をサポートしています。

### Q2. Aspose.3D の無料トライアルはありますか？

A2: はい、無料トライアルは [here](https://releases.aspose.com/) から利用できます。

### Q3: Aspose.3D for Java の詳細なドキュメントはどこで見られますか？

A3: 包括的なドキュメントは [here](https://reference.aspose.com/3d/java/) にあります。

### Q4: Aspose.3D のサポートはどこで受けられますか？

A4: サポートや質問は [Aspose.3D forum](https://forum.aspose.com/c/3d/18) で受け付けています。

### Q5: Aspose.3D の一時ライセンスは取得できますか？

A5: はい、一時ライセンスは [here](https://purchase.aspose.com/temporary-license/) から取得可能です。

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**最終更新日:** 2026-02-22  
**テスト環境:** Aspose.3D for Java（最新リリース）  
**作者:** Aspose