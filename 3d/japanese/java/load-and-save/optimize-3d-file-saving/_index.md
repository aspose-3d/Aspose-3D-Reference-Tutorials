---
title: Aspose.3D SaveOptions を使用して Java での 3D ファイル保存を最適化する
linktitle: Aspose.3D SaveOptions を使用して Java での 3D ファイル保存を最適化する
second_title: Aspose.3D Java API
description: Aspose.3D SaveOptions を使用して Java で 3D ファイルの保存を最適化する方法を学びます。パフォーマンスを向上させ、出力を簡単にカスタマイズします。
weight: 16
url: /ja/java/load-and-save/optimize-3d-file-saving/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose.3D SaveOptions を使用して Java での 3D ファイル保存を最適化する

## 導入

Aspose.3D は、開発者が 3D モデルをシームレスに操作できるようにする機能豊富な Java ライブラリです。 3D ファイルの保存に関しては、SaveOptions クラスは、要件に応じて出力を微調整するための豊富な設定を提供します。このチュートリアルでは、さまざまな保存オプションと、それらを活用してプロセスを最適化する方法について説明します。

## 前提条件

チュートリアルに入る前に、次の前提条件が満たされていることを確認してください。

-  Aspose.3D for Java: Aspose.3D ライブラリが Java プロジェクトに統合されていることを確認します。ダウンロードできます[ここ](https://releases.aspose.com/3d/java/).

- Java 開発環境: 機能する Java 開発環境をマシン上にセットアップします。

- ドキュメント ディレクトリ: 3D ファイルを保存するディレクトリを作成し、後で使用できるようにそのパスをメモしておきます。

## パッケージのインポート

 Java プロジェクトに、Aspose.3D を操作するために必要なパッケージをインポートします。これには、`Scene`クラスとさまざまな SaveOptions クラス。以下に基本的な例を示します。

```java
import com.aspose.threed.*;


import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
```

次に、各例を複数のステップに分けて、さまざまな SaveOptions の使用法を示します。

## ステップ 1: GLTF SaveOption でのきれいな印刷

の`prettyPrintInGltfSaveOption`このメソッドを使用すると、人間が読みやすいようにインデントされた JSON コンテンツを含む GLTF ファイルを生成できます。

```java
public static void prettyPrintInGltfSaveOption() throws IOException {
    // 3Dシーンの初期化
    Scene scene = new Scene(new Sphere());
    
    //GLTFSaveOptions の初期化
    GltfSaveOptions opt = new GltfSaveOptions(FileFormat.GLTF2);
    
    //読みやすさを向上させるためにきれいな印刷を有効にする
    opt.setPrettyPrint(true);
    
    //3D シーンの保存
    scene.save("Your Document Directory" + "prettyPrintInGltfSaveOption.gltf", opt);
}
```

## ステップ 2: HTML5 の保存オプション

の`html5SaveOption`このメソッドでは、カスタマイズ オプションを含め、3D シーンを HTML5 ファイルとして保存する方法を示します。

```java
public static void html5SaveOption() throws IOException {
    //シーンを初期化する
    Scene scene = new Scene();
    
    //円柱を使用して子ノードを作成する
    Node node = scene.getRootNode().createChildNode(new Cylinder());
    
    //子ノードのプロパティを設定する
    LambertMaterial mat = new LambertMaterial();
    mat.setDiffuseColor(new Vector3(0.34, 0.59, 0.41));
    node.setMaterial(mat);
    
    //シーンにライトを追加する
    Light light = new Light();
    light.setLightType(LightType.POINT);
    scene.getRootNode().createChildNode(light).getTransform().setTranslation(10, 0, 10);
    
    //HTML5SaveOptions の初期化
    Html5SaveOptions opt = new Html5SaveOptions();
    
    //オプションをカスタマイズします (グリッドとユーザー インターフェイスをオフにするなど)
    opt.setShowGrid(false);
    opt.setShowUI(false);
    
    //シーンを HTML5 ファイルとして保存する
    scene.save("Your Document Directory" + "html5SaveOption.html", FileFormat.HTML5);
}
```

他の SaveOptions メソッドについても同様の内訳を続けます。`colladaSaveOption`, `discreet3DSSaveOption`, `fbxSaveOption`, `objSaveOption`, `STLSaveOption`, `U3DSaveOption`, `glTFSaveOptions` 、 そして`drcSaveOptions`.

## 結論

この包括的なチュートリアルに従うことで、Aspose.3D SaveOptions を使用して Java で 3D ファイルの保存を最適化する方法を学習しました。 GLTF ファイルのきれいな印刷に興味がある場合でも、HTML5 出力のカスタマイズに興味がある場合でも、Aspose.3D には 3D グラフィックスのワークフローを強化するツールが備わっています。

## よくある質問

### Q1: glTF ファイルにアセットを埋め込むにはどうすればよいですか?

 A1: アセットを埋め込むには、`setEmbedAssets(true)`のメソッド`GltfSaveOptions`クラス。

### Q2：その目的は何ですか？`setPositionBits` method in `DracoSaveOptions`?

 A2:`setPositionBits`このメソッドは、Draco 圧縮アルゴリズムの位置の量子化ビットを設定します。

### Q3: 通常のデータを U3D ファイルに書き出すことはできますか?

 A3: はい、設定により通常のデータをエクスポートできます。`setExportNormals(true)`の中に`U3dSaveOptions`クラス。

### Q4: OBJ エクスポートで保存した素材ファイルを破棄するにはどうすればよいですか?

A4: を活用してください。`setFileSystem(new DummyFileSystem())`のメソッド`ObjSaveOptions`素材ファイルを破棄するクラス。

### Q5: 依存関係を OBJ ファイルのローカル ディレクトリに保存する方法はありますか?

 A5: はい、使用してください。`setFileSystem(new LocalFileSystem(MyDir))`のメソッド`ObjSaveOptions`依存関係をローカルに保存するクラス。
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
