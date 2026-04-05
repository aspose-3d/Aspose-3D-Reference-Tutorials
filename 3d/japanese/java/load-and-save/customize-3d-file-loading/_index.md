---
date: 2026-02-25
description: Aspose.3D の LoadOptions を使用して、Java で座標系を反転させ、3D インポートをカスタマイズする方法を学びましょう。3DS、OBJ、STL、U3D、glTF、PLY、X、そしてオプションで
  FBX のステップバイステップガイドです。
linktitle: Customize 3D File Loading in Java with Aspose.3D LoadOptions
second_title: Aspose.3D Java API
title: 座標系の反転 – Aspose.3D を使用した Java の 3D ファイル読み込みをカスタマイズ
url: /ja/java/load-and-save/customize-3d-file-loading/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 座標系の反転 – Aspose.3D for Javaで3Dファイルの読み込みをカスタマイズ

3Dデザインと開発が常に進化する中で、モデルをインポートする際に **座標系を反転** することは一般的な要件です。右手系から左手系への変換や、エンジンの軸規約に合わせてモデルを整列させる必要がある場合でも、Aspose.3D for Java は細かな制御を提供します。このチュートリアルでは、Aspose.3D の `LoadOptions` を使用して **3Dインポートをカスタマイズ** する方法を解説し、3DS、OBJ、STL、U3D、glTF、PLY、X、オプションのFBX といった主要フォーマットを対象とします。

## クイック回答
- **“座標系の反転”は何をしますか？** ターゲットの座標規約に合わせて X/Y/Z 軸を入れ替えます。  
- **どのフォーマットが反転をサポートしていますか？** すべての主要フォーマット（3DS、OBJ、STL、U3D、glTF、PLY、X、FBX）は `setFlipCoordinateSystem` オプションを提供します。  
- **追加のライブラリは必要ですか？** Aspose.3D for Java の JAR だけで、外部コンバータは不要です。  
- **同時にマテリアルを読み込めますか？** はい—OBJ ファイルでは `setEnableMaterials(true)` を使用します。  
- **本番環境でライセンスは必要ですか？** トライアル以外のデプロイには有効な Aspose.3D ライセンスが必要です。

## “座標系の反転”とは何ですか？
座標系を反転すると、インポートされたモデルが使用する軸の向きが変更されます。ソースファイルがレンダリングエンジンと異なるハンドネス（右手系 vs 左手系）を使用している場合に必須で、モデルが鏡像や逆さまに表示されるのを防ぎます。

## 3Dインポートをカスタマイズする理由は？
- アニメーション変換を保持する (`setApplyAnimationTransform`)。  
- カラー処理を正しく行う (`setGammaCorrectedColor`)。  
- `getLookupPaths()` を使用して外部リソースパスを解決する。  
- 必要なものだけをロードしてメモリ使用量を最適化する。

## 前提条件

- Java プログラミングの基本的な理解。  
- Java Development Kit (JDK) がインストール済み。  
- Aspose.3D for Java ライブラリをダウンロード済み。入手は [here](https://releases.aspose.com/3d/java/) から。  
- 3DS、OBJ、STL、U3D、glTF、PLY、X、FBX などの 3D ファイルフォーマットに精通していること。

## パッケージのインポート

Java プロジェクトで、必要な Aspose.3D パッケージをインポートしてください。

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## LoadOptions を使用した 3D インポートのカスタマイズ方法

以下は、サポートされている各フォーマットで **座標系の反転** オプションを有効にする手順を示すコードスニペットです。スニペットはそのままプロジェクトにコピーでき、`"Your Document Directory"` を実際のアセットディレクトリに置き換えるだけです。

### ステップ 1: 3DS ファイルのロードをカスタマイズ

```java
public static void discreet3DSLoadOption() {
    String MyDir = "Your Document Directory";
    Discreet3dsLoadOptions loadOpts = new Discreet3dsLoadOptions();
    loadOpts.setApplyAnimationTransform(true);
    loadOpts.setFlipCoordinateSystem(true);
    loadOpts.setGammaCorrectedColor(true);
    loadOpts.getLookupPaths().add(MyDir);
}
```

### ステップ 2: OBJ ファイルのロードをカスタマイズ

```java
public static void objLoadOption() {
    String MyDir = "Your Document Directory";
    ObjLoadOptions loadObjOpts = new ObjLoadOptions();
    loadObjOpts.setEnableMaterials(true);
    loadObjOpts.setFlipCoordinateSystem(true);
    loadObjOpts.getLookupPaths().add(MyDir);
}
```

### ステップ 3: STL ファイルのロードをカスタマイズ

```java
public static void stlLoadOption() {
    String MyDir = "Your Document Directory";
    StlLoadOptions loadSTLOpts = new StlLoadOptions();
    loadSTLOpts.setFlipCoordinateSystem(true);
    loadSTLOpts.getLookupPaths().add(MyDir);
}
```

### ステップ 4: U3D ファイルのロードをカスタマイズ

```java
public static void u3dLoadOption() {
    String MyDir = "Your Document Directory";
    U3dLoadOptions loadU3DOpts = new U3dLoadOptions();
    loadU3DOpts.setFlipCoordinateSystem(true);
    loadU3DOpts.getLookupPaths().add(MyDir);
}
```

### ステップ 5: glTF ファイルのロードをカスタマイズ

```java
public static void gltfLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    GltfLoadOptions loadOpt = new GltfLoadOptions();
    loadOpt.setFlipTexCoordV(true);
    scene.open(MyDir + "Duck.gltf", loadOpt);
}
```

### ステップ 6: PLY ファイルのロードをカスタマイズ

```java
public static void plyLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    PlyLoadOptions loadPLYOpts = new PlyLoadOptions();
    loadPLYOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "vase-v2.ply", loadPLYOpts);
}
```

### ステップ 7: X ファイルのロードをカスタマイズ

```java
public static void xLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    XLoadOptions loadXOpts = new XLoadOptions(FileContentType.ASCII);
    loadXOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "warrior.x", loadXOpts);
}
```

### ステップ 8: FBX ファイルのロードをカスタマイズ（オプション）

```java
private static void FBXLoadOptions() throws IOException {
    String dataDir = "Your Document Directory";
    Scene scene = new Scene();
    FbxLoadOptions opt = new FbxLoadOptions();
    opt.setKeepBuiltinGlobalSettings(true);
    scene.open(dataDir + "test.FBX", opt);
    for(Property property:scene.getRootNode().getAssetInfo().getProperties()) {
        System.out.println(property);
    }
}
```

## 一般的な問題と解決策
- **ロード後にモデルが鏡像になる** – 正しいフォーマットで `setFlipCoordinateSystem(true)` が設定されているか確認してください。  
- **マテリアルが欠落している** – OBJ ファイルの場合、`setEnableMaterials(true)` が有効で、マテリアルファイル（.mtl）が lookup パスのいずれかに配置されていることを確認してください。  
- **テクスチャ座標が上下逆になる** – glTF では、軸の反転に加えて `setFlipTexCoordV(true)` が必要になる場合があります。  
- **ファイルが見つからないエラー** – 外部リソース（テクスチャ、補助ファイル）を含むディレクトリを `loadOpts.getLookupPaths()` に追加してください。

## 結論

Aspose.3D の `LoadOptions` を活用することで、事実上すべての主要フォーマットに対して **座標系の反転** と **3D インポートのカスタマイズ** が可能になります。このレベルの制御により、ポストプロセススクリプトが不要となり、アセットが初回から正しくレンダリングされます。

## よくある質問

### Q1: Aspose.3D for Java のドキュメントはどこで見つけられますか？
A1: ドキュメントは [here](https://reference.aspose.com/3d/java/) で利用できます。

### Q2: Aspose.3D for Java をダウンロードするには？
A2: [here](https://releases.aspose.com/3d/java/) からダウンロードできます。

### Q3: 無料トライアルはありますか？
A3: はい、無料トライアルは [here](https://releases.aspose.com/) で利用できます。

### Q4: Aspose.3D for Java のサポートはどこで受けられますか？
A4: サポートフォーラムは [here](https://forum.aspose.com/c/3d/18) をご覧ください。

### Q5: テスト用に一時ライセンスは必要ですか？
A5: はい、一時ライセンスは [here](https://purchase.aspose.com/temporary-license/) で取得してください。

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**最終更新日:** 2026-02-25  
**テスト対象:** Aspose.3D for Java 24.11 (latest)  
**作者:** Aspose