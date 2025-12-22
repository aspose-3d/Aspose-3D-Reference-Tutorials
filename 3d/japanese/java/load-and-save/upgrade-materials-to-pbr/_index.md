---
date: 2025-12-22
description: Aspose.3D を使用して Java でシーンを glTF にエクスポートし、3D マテリアルを PBR にアップグレードしてリアリズムを向上させる方法を学びましょう。
linktitle: Export Scene to glTF in Java with Aspose.3D
second_title: Upgrade 3D Materials to PBR
title: Java と Aspose.3D でシーンを glTF にエクスポート
url: /ja/java/load-and-save/upgrade-materials-to-pbr/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Java と Aspose.3D でシーンを glTF にエクスポート – マテリアルを PBR にアップグレード

## はじめに

このチュートリアルでは、**シーンを glTF にエクスポート**しながら、3D マテリアルを Physically‑Based Rendering (PBR) にアップグレードする方法を Java と Aspose.3D で学びます。PBR にアップグレードすることで、モデルによりリアルな外観が得られ、広くサポートされている glTF 2.0 形式にエクスポートすれば、エンジン、ブラウザ、AR/VR プラットフォーム間で高品質なアセットを共有できます。前提条件の確認、必要なパッケージのインポート、各サンプルのステップバイステップ解説を通じて、実際のプロジェクトにこの手法を適用できるようになります。

## クイック回答
- **「export scene to glTF」とは何ですか？** Aspose.3D のシーンを glTF 2.0 ファイル形式に変換し、ジオメトリ、マテリアル、階層構造を保持します。  
- **なぜマテリアルを先に PBR にアップグレードするのですか？** PBR マテリアルは glTF の metallic‑roughness ワークフローに直接マッピングでき、余計な変換ステップなしでリアルなライティングが得られます。  
- **コード実行にライセンスは必要ですか？** 開発用には無料トライアルで動作しますが、商用利用には商用ライセンスが必要です。  
- **対応している Java IDE はどれですか？** Java をコンパイルできる IDE ならどれでも使用可能です（Eclipse、IntelliJ IDEA、VS Code など）。  
- **大規模シーンのエクスポートは可能ですか？** はい、Aspose.3D はデータを効率的にストリーミングします。非常に大きなモデルの場合は、十分なヒープメモリを確保してください。

## 「export scene to glTF」とは？
シーンを glTF にエクスポートするとは、メッシュ、ノード、カメラ、ライト、マテリアルなど、3D シーン全体を GL Transmission Format (glTF) にシリアライズすることです。glTF はリアルタイムレンダリング向けに最適化されたオープン標準フォーマットで、Web、モバイル、ゲームエンジンでの利用に最適です。

## エクスポート前にマテリアルを PBR にアップグレードする理由
PBR（Physically‑Based Rendering）マテリアルは、アルベド、メタリック、ラフネスといったパラメータで光と表面の相互作用を記述します。glTF 2.0 は PBR をネイティブにサポートしているため、Phong やカスタムマテリアルを PBR に変換しておくと、任意の glTF 対応ビューアで色、反射、シェーディングが正しく表示されます。

## 前提条件

開始する前に以下を用意してください：

1. **Aspose.3D for Java** – [release page](https://releases.aspose.com/3d/java/) からダウンロード。  
2. **Java 開発環境** – JDK 8 以上とお好みの IDE。  
3. **Document Directory** – 3D ファイルの読み書きを行うローカルフォルダー。

## パッケージのインポート

プロジェクトに Aspose.3D のコア名前空間を追加します：

```java
import com.aspose.threed.*;
```

この単一インポートで `Scene`、`Box`、`PhongMaterial`、`PbrMaterial`、`GltfSaveOptions`、およびマテリアル変換 API が利用可能になります。

## Step 1: Initialize a New 3D Scene

ジオメトリとマテリアルを保持する新しいシーンを作成します：

```java
// ExStart:InitializeScene
String MyDir = "Your Document Directory";
Scene s = new Scene();
// ExEnd:InitializeScene
```

> **Pro tip:** 開発中は `MyDir` を絶対パスで保持し、ファイルが見つからないエラーを防ぎます。

## Step 2: Create a Box with a PhongMaterial

まずはクラシックな Phong マテリアルを使用したシンプルなボックスを作成します。このボックスはエクスポート時に PBR マテリアルへ変換されます：

```java
// ExStart:CreateBoxWithMaterial
Box box = new Box();
PhongMaterial mat = new PhongMaterial();
mat.setDiffuseColor(new Vector3(1, 0, 1));
s.getRootNode().createChildNode("box1", box).setMaterial(mat);
// ExEnd:CreateBoxWithMaterial
```

> **Why Phong?** PhongMaterial は設定が簡単で、変換ロジックの動作を示すのに適しています。

## Step 3: Save in GLTF 2.0 Format (Export Scene to glTF)

`PhongMaterial` を自動的に `PbrMaterial` に変換する GLTF 保存オプションを構成します。これが **export scene to glTF** の核心です：

```java
// ExStart:SaveInGLTF
GltfSaveOptions opt = new GltfSaveOptions(FileFormat.GLTF2);
opt.setMaterialConverter(new MaterialConverter() {
    @Override
    public Material call(Material material) {
        PhongMaterial m = (PhongMaterial) material;
        PbrMaterial ret = new PbrMaterial();
        ret.setAlbedo(m.getDiffuseColor());
        return ret;
    }
});
s.save(MyDir + "Non_PBRtoPBRMaterial_Out.gltf", opt);
// ExEnd:SaveInGLTF
```

このコードが実行されると、シーンは `Non_PBRtoPBRMaterial_Out.gltf` に書き出されます。カスタム `MaterialConverter` が Phong マテリアルを PBR マテリアルに変換するため、生成された glTF ファイルは任意の glTF ビューアでリアルなシェーディングで表示されます。

## よくある問題と解決策

| 問題 | 解決策 |
|------|--------|
| **FileNotFoundException** が発生したとき | `MyDir` が既存のフォルダーを指しているか、アプリケーションに書き込み権限があるか確認してください。 |
| **ClassCastException** がコンバータで発生したとき | コンバータに渡すマテリアルが実際に `PhongMaterial` であることを確認してください。マテリアルタイプを混在させる場合は `instanceof` チェックを追加します。 |
| **Missing textures** がエクスポート後に欠如している | glTF はテクスチャを別途提供することを前提としています。必要に応じてコンバータにテクスチャ処理を追加してください。 |

## Frequently Asked Questions

**Q: Aspose.3D は Eclipse 以外の Java 開発環境でも使用できますか？**  
A: はい、Aspose.3D は IntelliJ IDEA、NetBeans、VS Code など、任意の Java IDE で動作します。

**Q: Aspose.3D を商用プロジェクトで使用できますか？**  
A: はい、個人・商用問わず Aspose.3D を使用できます。ライセンスの詳細は [purchase page](https://purchase.aspose.com/buy) をご覧ください。

**Q: 無料トライアルは利用可能ですか？**  
A: はい、無料トライアルは [here](https://releases.aspose.com/) から取得できます。

**Q: Aspose.3D のサポートはどこで受けられますか？**  
A: コミュニティサポートは [Aspose.3D forum](https://forum.aspose.com/c/3d/18) でご確認ください。

**Q: Aspose.3D の一時ライセンスはどう取得しますか？**  
A: 一時ライセンスの情報は [this link](https://purchase.aspose.com/temporary-license/) から入手できます。

## 結論

上記の手順に従うことで、Java と Aspose.3D を使用して **シーンを glTF にエクスポート**し、Phong マテリアルを自動的に PBR にアップグレードする方法が習得できました。このワークフローにより、現代的なレンダリングパイプライン、Web ビューア、AR/VR 体験向けに準備された高品質な物理ベースアセットを作成できます。より複雑なジオメトリ、テクスチャ、ライティングに挑戦し、PBR と glTF の力を最大限に活用してください。

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**最終更新日:** 2025-12-22  
**テスト環境:** Aspose.3D 24.12 for Java  
**作者:** Aspose  

---