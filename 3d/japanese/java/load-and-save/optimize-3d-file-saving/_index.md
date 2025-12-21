---
date: 2025-12-21
description: Aspose.3D SaveOptions を使用して Java で 3D ファイルを保存する方法を学びましょう – パフォーマンスの最適化、pretty‑print
  の有効化、HTML5 出力のカスタマイズなど。
linktitle: Save 3D File Java – Optimize 3D Saving with Aspose.3D SaveOptions
second_title: Aspose.3D Java API
title: 3DファイルをJavaで保存 – Aspose.3D SaveOptionsで3D保存を最適化
url: /ja/java/load-and-save/optimize-3d-file-saving/
weight: 16
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 3D ファイル Java の保存 – Aspose.3D SaveOptions で 3D 保存を最適化

## Introduction

**save 3d file java** プロジェクトを迅速かつ効率的に保存する必要がある場合、Aspose.3D for Java は出力を細かく調整できる強力なオプションを提供します。このチュートリアルでは、最も有用な `SaveOptions` 設定を解説し、パフォーマンス向上の方法を示し、GLTF ファイルの pretty‑print や自己完結型 HTML5 ビューアの生成といった実践的シナリオをデモンストレーションします。

## Quick Answers
- **保存の主要クラスは何ですか？** `Scene.save()` と特定の `*SaveOptions` サブクラスを組み合わせます。  
- **GLTF ファイルを人間が読みやすくするオプションはどれですか？** `GltfSaveOptions.setPrettyPrint(true)`。  
- **GLTF エクスポートにアセットを埋め込めますか？** はい – `GltfSaveOptions.setEmbedAssets(true)` を使用します。  
- **HTML5 エクスポートで UI をオフにするには？** `Html5SaveOptions.setShowUI(false)` を設定します。  
- **本番環境でライセンスは必要ですか？** 評価版以外の使用には商用ライセンスが必要です。

## Prerequisites

チュートリアルに入る前に、以下の前提条件が整っていることを確認してください。

- Aspose.3D for Java: Aspose.3D ライブラリが Java プロジェクトに統合されていることを確認してください。ダウンロードは[here](https://releases.aspose.com/3d/java/) から可能です。  
- Java 開発環境: マシン上に機能する Java 開発環境が設定されていること。  
- ドキュメントディレクトリ: 3D ファイルを保存したいディレクトリを作成し、後で使用するためにそのパスをメモしておいてください。

## Import Packages

Java プロジェクトで Aspose.3D を使用するために必要なパッケージをインポートします。これには `Scene` クラスや各種 `SaveOptions` クラスが含まれます。以下は基本的な例です。

```java
import com.aspose.threed.*;


import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
```

## How to Save 3D File Java Using Aspose.3D SaveOptions

以下では、最も一般的な `SaveOptions` 設定を分解して説明します。各コードスニペットの後に簡単な解説が続き、設定が **なぜ** 重要かが分かります。

### Step 1: Pretty Print in GLTF SaveOption

ステップ 1: GLTF SaveOption の Pretty Print

`prettyPrintInGltfSaveOption` メソッドを使用すると、インデントされた JSON コンテンツを持つ GLTF ファイルを生成し、人間が読みやすくなります。

```java
public static void prettyPrintInGltfSaveOption() throws IOException {
    // Initialize 3D scene
    Scene scene = new Scene(new Sphere());
    
    // Initialize GLTFSaveOptions
    GltfSaveOptions opt = new GltfSaveOptions(FileFormat.GLTF2);
    
    // Enable pretty print for better readability
    opt.setPrettyPrint(true);
    
    // Save 3D Scene
    scene.save("Your Document Directory" + "prettyPrintInGltfSaveOption.gltf", opt);
}
```

### Step 2: HTML5 SaveOption

ステップ 2: HTML5 SaveOption

`html5SaveOption` メソッドは、カスタマイズオプションを含めて 3D シーンを HTML5 ファイルとして保存する方法を示します。

```java
public static void html5SaveOption() throws IOException {
    // Initialize a scene
    Scene scene = new Scene();
    
    // Create a child node with a cylinder
    Node node = scene.getRootNode().createChildNode(new Cylinder());
    
    // Set properties for the child node
    LambertMaterial mat = new LambertMaterial();
    mat.setDiffuseColor(new Vector3(0.34, 0.59, 0.41));
    node.setMaterial(mat);
    
    // Add a light to the scene
    Light light = new Light();
    light.setLightType(LightType.POINT);
    scene.getRootNode().createChildNode(light).getTransform().setTranslation(10, 0, 10);
    
    // Initialize HTML5SaveOptions
    Html5SaveOptions opt = new Html5SaveOptions();
    
    // Customize options (e.g., turn off grid and user interface)
    opt.setShowGrid(false);
    opt.setShowUI(false);
    
    // Save the scene as an HTML5 file
    scene.save("Your Document Directory" + "html5SaveOption.html", FileFormat.HTML5);
}
```

`colladaSaveOption`、`discreet3DSSaveOption`、`fbxSaveOption`、`objSaveOption`、`STLSaveOption`、`U3DSaveOption`、`glTFSaveOptions`、`drcSaveOptions` など、他の `SaveOptions` メソッドについても同様に分解して続けます。各手順は同じパターンです: シーンを作成し、適切な `*SaveOptions` オブジェクトを設定し、`scene.save()` を呼び出します。

## Common Pitfalls & Tips

- **アセットの埋め込み** – 単一の自己完結型ファイルが必要な場合は、`GltfSaveOptions` で `setEmbedAssets(true)` を呼び出すことを忘れないでください。  
- **パフォーマンス** – 大規模シーンの場合、保存前にメッシュの複雑さを減らすか、Draco 圧縮（`DracoSaveOptions`）を使用することを検討してください。  
- **ファイルシステムの取り扱い** – OBJ ファイルをエクスポートする際、`setFileSystem(new DummyFileSystem())` を使用してマテリアルファイルの生成を制御し、不要な副ファイルを防げます。  
- **UI 要素** – HTML5 エクスポートにはデフォルトの UI が含まれます。`setShowUI(false)` で無効にし、クリーンなビューアを生成します。

## Conclusion

この包括的なチュートリアルに従うことで、Aspose.3D の `SaveOptions` を使用して **save 3d file java** を効率的に保存する方法を学びました。pretty‑print された GLTF ファイル、軽量な HTML5 ビューア、または高度に圧縮された Draco 出力が必要な場合でも、これらのオプションにより 3D グラフィックワークフローを完全に制御できます。

## FAQ

### Q1: glTF ファイルにアセットを埋め込むには？

A1: アセットを埋め込むには、`GltfSaveOptions` クラスの `setEmbedAssets(true)` メソッドを使用します。

### Q2: `DracoSaveOptions` の `setPositionBits` メソッドの目的は何ですか？

A2: `setPositionBits` メソッドは、Draco 圧縮アルゴリズムにおける位置の量子化ビット数を設定します。

### Q3: U3D ファイルに法線データをエクスポートできますか？

A3: はい、`U3dSaveOptions` クラスで `setExportNormals(true)` を設定することで法線データをエクスポートできます。

### Q4: OBJ エクスポートでマテリアルファイルの保存を破棄するには？

A4: `ObjSaveOptions` クラスの `setFileSystem(new DummyFileSystem())` メソッドを使用して、マテリアルファイルの保存を破棄します。

### Q5: OBJ ファイルで依存関係をローカルディレクトリに保存する方法はありますか？

A5: はい、`ObjSaveOptions` クラスの `setFileSystem(new LocalFileSystem(MyDir))` メソッドを使用して、依存関係をローカルに保存できます。

## Frequently Asked Questions

**Q: これらの SaveOptions をヘッドレスサーバ環境で使用できますか？**  
A: もちろんです。すべての `SaveOptions` は UI なしで動作し、バックエンド処理パイプラインに最適です。

**Q: Aspose.3D は新しい glTF 2.0 仕様への保存をサポートしていますか？**  
A: はい。`GltfSaveOptions(FileFormat.GLTF2)` を使用して glTF 2.0 フォーマットを対象にします。

**Q: OBJ にエクスポートする際の詳細度をどう制御しますか？**  
A: 保存前にメッシュの簡略化を調整するか、`ObjSaveOptions` で頂点精度を設定します。

**Q: ディスクに書き込まずに保存されたファイルをプレビューする方法はありますか？**  
A: `ByteArrayOutputStream` に保存し、そのバイトをビューアやクライアントにストリームできます。

**Q: 本番利用にはどのようなライセンスが必要ですか？**  
A: 評価版以外の導入には商用の Aspose.3D ライセンスが必要です。

---

**最終更新:** 2025-12-21  
**テスト環境:** Aspose.3D for Java 24.12 (執筆時点での最新)  
**作者:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}