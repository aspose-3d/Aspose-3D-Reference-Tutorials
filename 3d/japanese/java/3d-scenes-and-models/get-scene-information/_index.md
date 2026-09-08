---
date: 2026-09-08
description: Aspose.3D を使用して、Javaで単位を定義しシーンを FBX にエクスポートする方法を学びます。このステップバイステップガイドでは、application
  name の設定、measurement units の指定、そして 3D scene information の取得方法を示します。
keywords:
- how to define units
- export scene to fbx
- how to set application name
- define measurement units
lastmod: 2026-09-08
linktitle: Javaで FBX を保存し、3D Scene Info を取得する方法
og_description: Aspose.3D を使用して、Javaで単位を定義しシーンを FBX にエクスポートする方法を学びます。このガイドでは、application
  name の設定、measurement units の指定、そして 3D scene info の取得を数ステップで解説します。
og_image_alt: Guide showing how to define units and export a 3D scene to FBX using
  Aspose.3D Java
og_title: Javaで単位を定義し、シーンをFBXにエクスポートする方法
schemas:
- author: Aspose
  dateModified: '2026-09-08'
  description: Learn how to define units and export a scene to FBX in Java using Aspose.3D.
    This step‑by‑step guide shows setting the application name, measurement units,
    and retrieving 3D scene information.
  headline: How to define units and export scene to FBX in Java
  type: TechArticle
- description: Learn how to define units and export a scene to FBX in Java using Aspose.3D.
    This step‑by‑step guide shows setting the application name, measurement units,
    and retrieving 3D scene information.
  name: How to define units and export scene to FBX in Java
  steps:
  - name: initialize a 3D scene
    text: The `Scene` class is Aspose.3D's top‑level container that represents an
      entire 3D scene, including geometry, lights, cameras, and metadata. First, create
      an empty `Scene` object. This will be the container for all geometry, lights,
      cameras, and asset metadata.
  - name: define measurement units
    text: The unit system determines the real‑world scale of the scene; Aspose.3D
      lets you specify a unit name and a scale factor relative to meters. In this
      example we use an ancient Egyptian unit called “pole” with a custom scale factor.
      > **Tip:** Adjust `unitScaleFactor` to match the real‑world size of yo
  - name: export scene to FBX
    text: Now that the asset information is attached, we save the scene as an FBX
      file. The `FileFormat.FBX7500ASCII` option produces a human‑readable ASCII FBX,
      which is handy for debugging. > **Remember:** Replace `"Your Document Directory"`
      with an absolute path or a path relative to your project's working
  type: HowTo
- questions:
  - answer: Replace `FileFormat.FBX7500ASCII` with `FileFormat.FBX7500` when calling
      `scene.save(...)`.
    question: How do I change the output format to binary FBX?
  - answer: Yes, use `scene.getUserData().add("Key", "Value")` to embed additional
      key‑value pairs.
    question: Can I add custom user‑defined metadata beyond the built‑in asset fields?
  - answer: It does. Simply change the `FileFormat` enum to `OBJ` or `GLTF2` as needed.
    question: Does Aspose.3D support other export formats like OBJ or GLTF?
  - answer: Aspose.3D for Java supports Java 8 and later.
    question: What version of Java is required?
  - answer: Absolutely. Load the file with `new Scene("input.fbx")`, modify `scene.getAssetInfo()`,
      then save.
    question: Is it possible to load an existing FBX, modify its asset info, and resave?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- export scene to fbx
- Aspose.3D
- Java 3D
- define units
- 3D asset metadata
title: Javaで単位を定義し、シーンをFBXにエクスポートする方法
url: /ja/java/3d-scenes-and-models/get-scene-information/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Javaで単位を定義し、シーンをFBXにエクスポートする方法

## はじめに

3Dシーンから有用なメタデータを抽出しながら、**単位の定義方法**と**シーンをFBXにエクスポートする方法**についての明確で実践的なガイドをお探しなら、ここが最適です。このチュートリアルでは、**Aspose.3D for Java** ライブラリを使用して、シーンの作成、**アプリケーション名の設定**、**測定単位の定義**、そして最終的に **シーンをFBXにエクスポート** するまでのすべての手順を解説します。最後には、下流のパイプラインで必要となるアセット情報を保持した、すぐに使用できるFBXファイルが手に入ります。

## 簡単な回答

- **主な目的は何ですか？** カスタムアセット情報を含むシーンをFBXにエクスポートします。  
- **使用されているライブラリはどれですか？** Aspose.3D for Java。  
- **ライセンスは必要ですか？** 開発には無料トライアルで動作しますが、本番環境では商用ライセンスが必要です。  
- **測定単位を変更できますか？** はい – `setUnitName` と `setUnitScaleFactor` を使用します。  
- **出力はどこに保存されますか？** `scene.save(...)` で指定したパスに保存されます。  

## 前提条件

開始する前に、以下を確認してください：

- Javaの基本構文をしっかり理解していること。  
- **Aspose.3D for Java** をダウンロードし、プロジェクトに追加する（公式サイトから入手できます）[Aspose 3D download page](https://releases.aspose.com/3d/java/)。  
- 好みのJava IDE（IntelliJ IDEA、Eclipse、NetBeansなど）を適切に設定する。  

## パッケージのインポート

Javaのソースファイルで、シーン処理とファイル形式サポートを提供する Aspose.3D クラスをインポートします。

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
```

> **プロのコツ:** 不要な依存関係を避け、コンパイル時間を短縮するためにインポートリストは最小限に保ちましょう。

## FBXファイルを保存する手順は？

シーンをFBXファイルとして保存するには、`Scene` を作成し、必要なアセットメタデータを設定し、測定単位を定義した上で、`scene.save(path, FileFormat.FBX7500ASCII)` を呼び出します。この手順により、ジオメトリ、マテリアル、メタデータがASCII FBXに書き込まれ、下流ツールで検査またはインポートできるようになります。

### 手順 1: 3Dシーンの初期化

`Scene` クラスは、ジオメトリ、ライト、カメラ、メタデータを含む全体の3Dシーンを表す Aspose.3D の最上位コンテナです。まず、空の `Scene` オブジェクトを作成します。これがすべてのジオメトリ、ライト、カメラ、アセットメタデータのコンテナとなります。

```java
// ExStart:AddAssetInformationToScene
Scene scene = new Scene();
```

### Javaでアプリケーション名を設定する方法

`AssetInfo` オブジェクトは、シーンのアプリケーション名、ベンダー、バージョンなどのメタデータを保持します。カスタムメタデータを追加することで、下流ツールがファイルの出所を特定しやすくなります。ファイルを保存する前に、`AssetInfo` オブジェクトを使用して **アプリケーション名を設定**（ベンダーも同様）します。

```java
scene.getAssetInfo().setApplicationName("Egypt");
scene.getAssetInfo().setApplicationVendor("Manualdesk");
```

> **重要な理由:** 多くのパイプラインは、元となるアプリケーションに基づいてアセットをフィルタリングまたはタグ付けするため、このステップは大規模プロジェクトで不可欠です。

### 手順 3: 測定単位の定義

単位系はシーンの実世界スケールを決定します。Aspose.3D では、単位名とメートルに対するスケールファクターを指定できます。この例では、古代エジプトの単位「pole」をカスタムスケールファクターで使用します。

```java
scene.getAssetInfo().setUnitName("pole");
scene.getAssetInfo().setUnitScaleFactor(0.6);
```

> **ヒント:** `unitScaleFactor` を調整してモデルの実際のサイズに合わせてください。1.0 は選択した単位との 1 対 1 のマッピングを表します。

### 手順 4: シーンをFBXにエクスポート

アセット情報が付与されたので、シーンをFBXファイルとして保存します。`FileFormat.FBX7500ASCII` オプションは人間が読みやすい ASCII FBX を生成し、デバッグに便利です。

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "InformationToScene.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
System.out.println("\nAsset information added successfully to Scene.\nFile saved at " + MyDir);
// ExEnd:AddAssetInformationToScene
```

> **覚えておいてください:** `"Your Document Directory"` を絶対パスまたはプロジェクトの作業ディレクトリに対する相対パスに置き換えてください。

## なぜ Aspose.3D でシーンを FBX にエクスポートするのか？

Aspose.3D は **50 以上の入出力フォーマット** をサポートし、ファイル全体をメモリに読み込むことなく数百ページに及ぶシーンを処理できるため、エクスポートされるファイル（メタデータ、単位、ジオメトリ）をフルコントロールできます。重厚な 3D オーサリングアプリケーションは不要です。これにより、自動アセット生成、バッチ処理、サーバーサイド変換が高速かつ信頼性の高いものになります。

## 一般的なユースケース

- **ゲームアセットパイプライン** – バージョン管理のために作成者情報を FBX ファイルに直接埋め込む。  
- **建築ビジュアライゼーション** – レンダリングエンジンにインポートする際のスケーリングエラーを防ぐため、プロジェクト固有の単位を保存する。  
- **自動レポーティング** – 下流の分析ツールが読み取れるメタデータを含む FBX ファイルをリアルタイムで生成する。  
- **クラウドベースの 3D サービス** – GUI なしでプログラム的にシーンを作成・エクスポートでき、SaaS プラットフォームに最適。  

## トラブルシューティングとヒント

| Issue | Solution |
|-------|----------|
| **保存後にファイルが見つからない** | `MyDir` が既存のフォルダーを指していること、アプリケーションに書き込み権限があることを確認してください。 |
| **外部ビューアで単位が正しく表示されない** | `unitScaleFactor` を再確認してください。一部のビューアはメートルを基準単位として期待します。 |
| **アセットメタデータが欠落している** | 保存する **前に** `scene.getAssetInfo()` を呼び出していることを確認してください。`save()` 後に行った変更は永続化されません。 |
| **大規模シーンでのパフォーマンスボトルネック** | 保存前に `scene.optimize()` を使用してメモリ使用量を削減してください。 |
| **ASCII FBX が大きすぎる** | `FileFormat.FBX7500` を使用してバイナリ FBX に切り替えてください（FAQ 参照）。 |

## よくある質問

**Q: 出力形式をバイナリ FBX に変更するにはどうすればよいですか？**  
A: `scene.save(...)` を呼び出す際に、`FileFormat.FBX7500ASCII` を `FileFormat.FBX7500` に置き換えてください。

**Q: 組み込みのアセットフィールド以外に、カスタムユーザー定義メタデータを追加できますか？**  
A: はい、`scene.getUserData().add("Key", "Value")` を使用して追加のキー‑バリュー ペアを埋め込めます。

**Q: Aspose.3D は OBJ や GLTF などの他のエクスポート形式をサポートしていますか？**  
A: サポートしています。必要に応じて `FileFormat` 列挙型を `OBJ` または `GLTF2` に変更してください。

**Q: 必要な Java のバージョンは何ですか？**  
A: Aspose.3D for Java は Java 8 以降をサポートしています。

**Q: 既存の FBX をロードし、アセット情報を変更して再保存することは可能ですか？**  
A: もちろん可能です。`new Scene("input.fbx")` でファイルをロードし、`scene.getAssetInfo()` を変更してから保存してください。

**最終更新日:** 2026-09-08  
**テスト環境:** Aspose.3D for Java 24.11  
**作者:** Aspose

## 関連チュートリアル

- [3Dファイルサイズの削減 – Aspose.3D for Javaでシーンを圧縮](/3d/java/3d-scenes-and-models/compress-3d-scenes/)
- [vector3 カラーの設定方法（Java）: Diffuse Color を変更し、Aspose.3D を使用して Java シーンの 3D プロパティを管理](/3d/java/3d-scenes-and-models/managing-3d-properties-scenes/)

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}