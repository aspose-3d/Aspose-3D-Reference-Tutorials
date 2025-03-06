---
title: Aspose.3D LoadOptions を使用して Java での 3D ファイルの読み込みをカスタマイズする
linktitle: Aspose.3D LoadOptions を使用して Java での 3D ファイルの読み込みをカスタマイズする
second_title: Aspose.3D Java API
description: Aspose.3D のカスタマイズ可能な LoadOptions を使用して、Java での 3D ファイルの読み込みを強化します。 3DS、OBJ、STL、U3D、glTF、PLY、X、およびオプションの FBX のカスタマイズを段階的に学習します。
weight: 12
url: /ja/java/load-and-save/customize-3d-file-loading/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose.3D LoadOptions を使用して Java での 3D ファイルの読み込みをカスタマイズする

## 導入

進化し続ける 3D 設計と開発の状況では、3D ファイル形式を効率的に処理することが非常に重要です。 Aspose.3D for Java は、さまざまな 3D ファイル形式の読み込みをカスタマイズするための強力なソリューションを提供します。このチュートリアルでは、Aspose.3D の LoadOptions を使用して Java で 3D ファイルの読み込みをカスタマイズするプロセスを説明します。

## 前提条件

カスタマイズ プロセスに入る前に、次のものが揃っていることを確認してください。

- Java プログラミングの基本的な理解。
- Java 開発キット (JDK) がインストールされている。
-  Java ライブラリ用の Aspose.3D がダウンロードされました。入手できます[ここ](https://releases.aspose.com/3d/java/).
- 3DS、OBJ、STL、U3D、glTF、PLY、X、FBX などの 3D ファイル形式に精通していること。

## パッケージのインポート

Java プロジェクトで、必要な Aspose.3D パッケージを必ずインポートしてください。

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## 3D ファイルの読み込みをカスタマイズする

### ステップ 1: 3DS ファイルの読み込みをカスタマイズする

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

### ステップ 2: OBJ ファイルの読み込みをカスタマイズする

```java
public static void objLoadOption() {
    String MyDir = "Your Document Directory";
    ObjLoadOptions loadObjOpts = new ObjLoadOptions();
    loadObjOpts.setEnableMaterials(true);
    loadObjOpts.setFlipCoordinateSystem(true);
    loadObjOpts.getLookupPaths().add(MyDir);
}
```

### ステップ 3: STL ファイルの読み込みをカスタマイズする

```java
public static void stlLoadOption() {
    String MyDir = "Your Document Directory";
    StlLoadOptions loadSTLOpts = new StlLoadOptions();
    loadSTLOpts.setFlipCoordinateSystem(true);
    loadSTLOpts.getLookupPaths().add(MyDir);
}
```

### ステップ 4: U3D ファイルの読み込みをカスタマイズする

```java
public static void u3dLoadOption() {
    String MyDir = "Your Document Directory";
    U3dLoadOptions loadU3DOpts = new U3dLoadOptions();
    loadU3DOpts.setFlipCoordinateSystem(true);
    loadU3DOpts.getLookupPaths().add(MyDir);
}
```

### ステップ 5: glTF ファイルの読み込みをカスタマイズする

```java
public static void gltfLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    GltfLoadOptions loadOpt = new GltfLoadOptions();
    loadOpt.setFlipTexCoordV(true);
    scene.open(MyDir + "Duck.gltf", loadOpt);
}
```

### ステップ 6: PLY ファイルのロードをカスタマイズする

```java
public static void plyLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    PlyLoadOptions loadPLYOpts = new PlyLoadOptions();
    loadPLYOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "vase-v2.ply", loadPLYOpts);
}
```

### ステップ 7: X ファイルの読み込みをカスタマイズする

```java
public static void xLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    XLoadOptions loadXOpts = new XLoadOptions(FileContentType.ASCII);
    loadXOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "warrior.x", loadXOpts);
}
```

### ステップ 8: FBX ファイルの読み込みをカスタマイズする (オプション)

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

## 結論

Aspose.3D の LoadOptions を使用して Java での 3D ファイルの読み込みをカスタマイズすると、開発者はインポート プロセスを特定の要件に合わせて調整できます。アニメーション変換の調整、座標系の反転、外部依存関係の処理など、Aspose.3D はシームレスな統合に必要な柔軟性を提供します。

## よくある質問

### Q1: Aspose.3D for Java ドキュメントはどこで見つけられますか?

 A1: ドキュメントは入手可能です[ここ](https://reference.aspose.com/3d/java/).

### Q2: Java 用 Aspose.3D をダウンロードするにはどうすればよいですか?

 A2: ダウンロードできます[ここ](https://releases.aspose.com/3d/java/).

### Q3: 無料トライアルはありますか?

 A3: はい、無料トライアルにアクセスできます。[ここ](https://releases.aspose.com/).

### Q4: Aspose.3D for Java のサポートはどこで入手できますか?

 A4: サポート フォーラムにアクセスしてください。[ここ](https://forum.aspose.com/c/3d/18).

### Q5: テストには一時ライセンスが必要ですか?

 A5: はい、一時ライセンスを取得します。[ここ](https://purchase.aspose.com/temporary-license/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
