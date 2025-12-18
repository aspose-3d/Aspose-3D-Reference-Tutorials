---
date: 2025-12-18
description: Aspose.3D を使用して Java で形状を押し出す方法を学び、3D シーンを作成し、Wavefront OBJ ファイルを簡単にエクスポートします。
linktitle: How to Extrude Shape in Java with Aspose.3D Linear Extrusion
second_title: Aspose.3D Java API
title: Java と Aspose.3D の線形押し出しで形状を押し出す方法
url: /ja/java/linear-extrusion/performing-linear-extrusion/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose.3D for Javaでの線形押し出しの実行

## はじめに

Aspose.3D for Javaで**how to extrude shape**の包括的なチュートリアルへようこそ！Javaを使用して3Dモデリングスキルを向上させたい方に最適です。3Dシーンの作成、線形押し出しの実行、結果をWavefront OBJファイルとしてエクスポートする手順を、明確なステップバイステップのコード例とともにご案内します。

## クイック回答
- **What is linear extrusion?** 2Dプロファイルを直線パスに沿って伸ばし、3Dソリッドを作成することです。  
- **Which library handles this in Java?** Aspose.3D for Java。  
- **Can I export to OBJ?** はい、Wavefront OBJエクスポート機能を使用します。  
- **Do I need a license for development?** テストには無料トライアルが利用でき、本番環境ではライセンスが必要です。  
- **What Java version is required?** Java 1.6 以降。

## “how to extrude shape”とは何ですか？

線形押し出しは**3d modeling java**における基本的な手法で、矩形のような平面プロファイルを定義された距離だけ引き伸ばすことで体積オブジェクトに変換します。この手法は機械部品、建築要素、装飾モデルの作成に広く利用されています。

## 線形押し出しにAspose.3Dを使用する理由は？

- **Full control**（ジオメトリのスライス、ツイスト、オフセット）。  
- **Seamless integration**（Javaプロジェクトへのシームレスな統合）—ネイティブ依存なし。  
- **Built‑in exporters**（Wavefront OBJを含む一般的なフォーマット向けの組み込みエクスポーター）により、下流パイプライン用の**generate 3d model**ファイルを簡単に作成できます。

## 前提条件

チュートリアルに入る前に、以下の前提条件が整っていることを確認してください。

1. **Java Development Environment** – JDK（1.6以上）とお好みのIDE。  
2. **Aspose.3D Library** – 公式サイトの**[here](https://releases.aspose.com/3d/java/)**からライブラリをダウンロードしてインストールしてください。

## パッケージのインポート

開発環境とAspose.3Dライブラリの設定が完了したら、必要なパッケージをインポートします。

```java
import com.aspose.threed.*;
```

### ステップ1: ドキュメントディレクトリの設定

生成されたファイルを保存するフォルダーを定義します。

```java
String MyDir = "Your Document Directory";
```

> これにより、**generate 3d model**操作がOBJファイルを既知の場所に書き込むことが保証されます。

### ステップ2: 基本形状の初期化

押し出しプロファイルとして使用する矩形を作成します。

```java
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

丸み半径を調整して角を丸めることができ、完璧な矩形にしたい場合は`0`に設定します。

### ステップ3: 線形押し出しの実行

ここでは矩形をZ軸に沿って押し出し、スライスを追加し、センタリングを有効にし、オフセット付きでツイストを適用します。

```java
LinearExtrusion extrusion = new LinearExtrusion(profile, 10) {{ setSlices(100); setCenter(true); setTwist(360); setTwistOffset(new Vector3(10, 0, 0));}};
```

- **Extrusion length** – `10` ユニット。  
- **Slices** – 滑らかなジオメトリのために`100`。  
- **Twist** – `360°`でフル回転を作成します。  
- **Twist offset** – ツイストの原点を`(10, 0, 0)`に移動します。

### ステップ4: 3Dシーンの作成

シーンコンテナを作成し、押し出しを子ノードとして追加します。このステップで**creates 3d scene**が作成され、複数のオブジェクトを保持できます。

```java
Scene scene = new Scene();
scene.getRootNode().createChildNode(extrusion);
```

### ステップ5: 3Dシーンの保存

シーンをWavefront OBJファイルにエクスポートします。これにより**wavefront obj export**と**save 3d obj**の機能が実証されます。

```java
scene.save(MyDir +  "LinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

コードを実行すると、指定したディレクトリに`LinearExtrusion.obj`が作成され、任意の3Dビューアで開くか、さらに処理できる状態になります。

## 一般的な問題と解決策

| 問題 | 原因 | 対策 |
|------|------|------|
| OBJファイルが空 | 出力ディレクトリのパスが間違っているか、書き込み可能ではありません | `MyDir`が存在し、書き込み権限のあるフォルダーを指していることを確認してください。 |
| ツイストが適用されない | `setCenter(true)`が省略されている | センタリングが有効になっていることを確認するか、`setTwistOffset`の値を調整してください。 |
| `LinearExtrusion`でのコンパイルエラー | 古いAspose.3Dバージョンを使用している | 最新のAspose.3Dリリースに更新してください。 |

## よくある質問

**Q: Aspose.3DはすべてのJavaバージョンと互換性がありますか？**  
A: Aspose.3DはJava 1. 以降で動作します。

**Q: Aspose.3Dを商用プロジェクトで使用できますか？**  
A: はい、有効なライセンスがあれば商用利用が可能です。ライセンスは**[here](https://purchase.aspose.com/buy)**から取得できます。

**Q: 問題が発生した場合、どこでサポートを受けられますか？**  
A: コミュニティサポートは**[Aspose.3D forum](https://forum.aspose.com/c/3d/18)**をご覧ください。プレミアムサポートが必要な場合は**[temporary license](https://purchase.aspose.com/temporary-license/)**をご購入ください。

**Q: Aspose.3Dは他にどのような3Dモデリング機能を提供していますか？**  
A: ライブラリにはメッシュ操作、ブーリアン演算、テクスチャマッピングなどが含まれます。機能一覧は**[here](https://reference.aspose.com/3d/java/)**をご覧ください。

**Q: 無料トライアルは利用できますか？**  
A: はい、トライアル版は**[here](https://releases.aspose.com/)**からダウンロードできます。

## 結論

これで、Aspose.3D for Javaを使用した**how to extrude shape**の方法、3Dシーンの作成、Wavefront OBJファイルへのエクスポートを学びました。この手法により、**3d modeling java**プロジェクト（シンプルな部品から複雑なアセンブリまで）に幅広く応用できます。ブーリアン演算やテクスチャマッピングなどの追加機能を探求し、モデルをさらに充実させてください。

---

**最終更新日:** 2025-12-18  
**テスト環境:** Aspose.3D 24.11 for Java  
**作者:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

## 対象キーワード:

**Primary Keyword (HIGHEST PRIORITY):**  
how to extrude shape

**Secondary Keywords (SUPPORTING):**  
create 3d scene, 3d modeling java, generate 3d model, wavefront obj export, save 3d obj