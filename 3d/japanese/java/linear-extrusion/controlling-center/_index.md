---
date: 2025-12-18
description: Aspose.3D for Java を使用して、線形押し出しにグラウンドプレーンを追加し、センタープロパティを設定する方法を、ステップバイステップのコード例とともに学びましょう。
linktitle: Controlling Center in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Aspose.3D for Javaで線形押し出しに地面平面とコントロールセンターを追加する方法
url: /ja/java/linear-extrusion/controlling-center/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose.3D for Java を使用した線形押し出しの中心制御

## はじめに

Javaで3Dシーンを構築する際、**add ground plane**（グラウンドプレーンの追加）機能と、線形押し出しの**set center property**（中心プロパティの設定）を正確に行えることは、単なるプロトタイプと洗練されたビジュアルの差を生み出します。このチュートリアルでは、Aspose.3D for Java を使用して押し出しの中心を制御し、グラウンドプレーンを追加する完全な手順を解説します。なぜ重要なのか、設定方法、そしてプロジェクトに適用できる実行可能なコードサンプルをご紹介します。

## クイック回答
- **“add ground plane” は何をするのですか？** 薄い参照ジオメトリを作成し、押し出しの位置をワールド座標系に対して確認しやすくします。  
- **線形押し出しの中心はどう設定しますか？** `LinearExtrusion` オブジェクトの `setCenter(boolean)` メソッドを使用します。  
- **サンプルを実行するのにライセンスは必要ですか？** テスト用には一時ライセンスで動作しますが、本番環境ではフルライセンスが必要です。  
- **保存に使用するファイル形式は何ですか？** 本例は Wavefront OBJ（`.obj`）形式で保存します。  
- **必要な Java バージョンは？** Java 8 以降であれば問題ありません。  

## 3Dシーンにおける “add ground plane” とは？

グラウンドプレーンを追加するとは、X‑Z 平面上に配置された薄い長方形ジオメトリ（通常は最小厚さのボックス）を挿入することです。視覚的な床として機能し、特に押し出し中心を試す際に、他のオブジェクトの高さや配置を判断しやすくなります。

## 線形押し出しで中心プロパティを設定する理由

デフォルトでは、線形押し出しはプロファイルの原点から開始します。中心プロパティ（`setCenter(true)`）を設定すると、プロファイルがシフトし、押し出しが原点を中心に配置されます。これは対称的なデザインや、複数オブジェクト間で一貫した配置が必要な場合に便利です。

## 前提条件

このチュートリアルを始める前に、以下の前提条件が整っていることを確認してください。

1. **Java 開発環境** – マシンに Java 開発環境がセットアップされていることを確認してください。  
2. **Aspose.3D for Java** – Aspose.3D ライブラリをダウンロードしてインストールします。ライブラリとドキュメントは[こちら](https://reference.aspose.com/3d/java/)にあります。  
3. **Document Directory** – Java ドキュメントを保存するディレクトリを作成します。ここでは「Your Document Directory」と呼びます。  

## パッケージのインポート

Java 開発環境で Aspose.3D に必要なパッケージをインポートします。これにより、ライブラリが提供する機能にコードからアクセスできるようになります。

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## ステップ 1: ベースプロファイルの設定

押し出すベースプロファイルを初期化します。この例では、丸み半径 0.3 の矩形シェイプを使用します。

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## ステップ 2: 3D シーンの作成

シーンを作成して、3D ワールドの基盤を構築します。

```java
Scene scene = new Scene();
```

## ステップ 3: 左右ノードの作成

シーン内に左側と右側のノードを作成します。これらのノードは 3D オブジェクトのキャンバスとして機能します。

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## ステップ 4: 中心プロパティ付き線形押し出し（左ノード）

左ノードで **センタリングせず** に線形押し出しを実行し、スライス数を 3 に設定します。`setCenter(false)` の呼び出しに注目してください – ここで **center プロパティ** を *false* に設定しています。

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

## ステップ 5: 参照用グラウンドプレーンの追加（左ノード）

左ノードに **グラウンドプレーンを追加** して視覚表現を強化します。薄いボックスが床として機能し、押し出しの高さがはっきりと確認できます。

```java
left.createChildNode(new Box(0.01, 3, 3));
```

## ステップ 6: 中心プロパティ付き線形押し出し（右ノード）

次に右ノードで線形押し出しを実行します。このとき **押し出しをセンタリング** します。`setCenter(true)` の呼び出しは **center プロパティ** を *true* に設定する方法を示しています。

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

## ステップ 7: 参照用グラウンドプレーンの追加（右ノード）

左側と同様に、右ノードにもグラウンドプレーンを追加し、一貫した視覚基準を提供します。

```java
right.createChildNode(new Box(0.01, 3, 3));
```

## ステップ 8: 3D シーンの保存

3D シーンを Wavefront OBJ 形式で保存し、任意の標準 3D ビューアで表示できるようにします。

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## よくある問題と解決策

| 問題 | 発生原因 | 対策 |
|------|----------|------|
| グラウンドプレーンが表示されない | ビューアのスケールに対してボックスの厚さが小さすぎます。 | `Box` の最初のパラメータで厚さを増やすか、ビューアでズームアウトしてください。 |
| 押し出しがずれて表示される | `setCenter` の値が意図した通りに設定されていません。 | `setCenter` に渡すブール値を再確認してください。 |
| ファイルが保存されない | ディレクトリパスが間違っているか、書き込み権限がありません。 | `MyDir` が書き込み可能な既存フォルダを指しているか確認してください。 |

## よくある質問

**Q1: Aspose.3D for Java を商用プロジェクトで使用できますか？**  
A1: はい、Aspose.3D for Java は商用利用が可能です。ライセンスの詳細は[こちら](https://purchase.aspose.com/buy)をご覧ください。

**Q2: 無料トライアルはありますか？**  
A2: はい、Aspose.3D for Java の無料トライアルは[こちら](https://releases.aspose.com/)でお試しできます。

**Q3: Aspose.3D for Java のサポートはどこで受けられますか？**  
A3: Aspose.3D コミュニティフォーラムはサポートを求めたり経験を共有したりするのに最適な場所です。フォーラムは[こちら](https://forum.aspose.com/c/3d/18)です。

**Q4: テスト用に一時ライセンスは必要ですか？**  
A4: はい、テスト目的で一時ライセンスが必要な場合は[こちら](https://purchase.aspose.com/temporary-license/)から取得できます。

**Q5: ドキュメントはどこで見つけられますか？**  
A5: Aspose.3D for Java のドキュメントは[こちら](https://reference.aspose.com/3d/java/)で入手できます。

## 結論

線形押し出しの中心を制御し、Aspose.3D for Java で **add ground plane** を学ぶことで、3D グラフィックス開発におけるエキサイティングな可能性が広がります。上記の手順に従うことで、中心化された押し出し、視覚的参照平面の作成、OBJ へのエクスポートという再利用可能なパターンが手に入ります。さまざまなプロファイル、スライス数、変換を試して、プロジェクトの要件に合わせて自由に実験してください。

---

**最終更新日:** 2025-12-18  
**テスト環境:** Aspose.3D 24.11 for Java（執筆時点での最新）  
**作成者:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}