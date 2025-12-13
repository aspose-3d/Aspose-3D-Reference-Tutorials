---
date: 2025-12-13
description: Aspose 3D Java を使用して 3D ノードを変換する方法を学びます。このガイドでは、オイラー角の使用方法、3D 回転の追加、Java
  での平行移動の設定方法を示します。
linktitle: Aspose 3D Java – Transform 3D Nodes with Euler Angles
second_title: Aspose.3D Java API
title: Aspose 3D Java – オイラー角で3Dノードを変換
url: /ja/java/geometry/transform-3d-nodes-with-euler-angles/
weight: 19
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# JavaでAspose.3Dを使用してEuler角で3Dノードを変換する

## Introduction

このチュートリアルでは、**aspose 3d java** を使用して Euler 角を適用し、3D ノードを変換する方法を学びます。ガイドの最後までに、3D 回転を追加し、Javaで平行移動を設定し、リアルタイムデータに反応する動的シーンを作成できるようになります。

## Quick Answers
- **Javaで3D変換を処理するライブラリは何ですか？** Aspose 3D for Java.  
- **Euler角を使用して回転を設定するメソッドはどれですか？** ノードの transform 上の `setEulerAngles()`。  
- **ノードを空間内で移動させるには？** `Vector3` と共に `setTranslation()` を使用します。  
- **本番環境でライセンスが必要ですか？** はい、商用の Aspose 3D ライセンスが必要です。  
- **FBXへエクスポートできますか？** もちろんです – `scene.save(..., FileFormat.FBX7500ASCII)` がそのまま動作します。

## Prerequisites

チュートリアルに入る前に、以下の前提条件が整っていることを確認してください：

- Java プログラミングの基本的な知識。  
- マシンに Java Development Kit (JDK) がインストールされていること。  
- Aspose.3D ライブラリ。入手は [Aspose.3D Java Documentation](https://reference.aspose.com/3d/java/) から。

## Import Packages

Java プロジェクトに必要なパッケージをインポートします。Aspose.3D ライブラリがクラスパスに正しく追加されていることを確認してください。まだダウンロードしていない場合は、ダウンロードリンクを [here](https://releases.aspose.com/3d/java/) で見つけられます。

```java
import com.aspose.threed.*;
```

## aspose 3d java – Euler角の操作

### Step 1. Initialize Scene and Node

まず、シーンと、変換したいジオメトリを保持するノードを作成します。

```java
// ExStart:AddTransformationToNodeByEulerAngles
// Initialize scene object
Scene scene = new Scene();

// Initialize Node class object
Node cubeNode = new Node("cube");
```

### Step 2. Create Mesh and Set Geometry

次に、シンプルなメッシュ（この例では立方体）を生成し、ノードに添付します。

```java
// Call Common class create mesh using polygon builder method to set mesh instance
Mesh mesh = Common.createMeshUsingPolygonBuilder();

// Point node to the Mesh geometry
cubeNode.setEntity(mesh);
```

## Add Rotation 3D to a Node

### Step 3. Set Euler Angles and Translation

ここで Euler 角を使用して回転を適用し、ノードを可視位置へ移動します。

```java
// Euler angles
cubeNode.getTransform().setEulerAngles(new Vector3(0.3, 0.1, -0.5));

// Set translation
cubeNode.getTransform().setTranslation(new Vector3(0, 0, 20));
```

## Set Translation Java – ノードの位置設定

上記の平行移動ステップは、実際に **set translation java** を示しています。ノードは Z 軸方向に 20 ユニットシフトされ、レンダリング後に確認できます。

## Step 4. Add Node to Scene

変換されたノードをシーンのルートノードに添付します。

```java
// Add cube to the scene
scene.getRootNode().getChildNodes().add(cubeNode);
```

## Step 5. Save 3D Scene

最後に、シーンを FBX ファイル（または他のサポートされている形式）にエクスポートします。

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
MyDir = MyDir + "TransformationToNode.fbx";

// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7500ASCII);
// ExEnd:AddTransformationToNodeByEulerAngles
System.out.println("\nTransformation added successfully to node.\nFile saved at " + MyDir);
```

`"Your Document Directory"` をマシン上の適切なパスに置き換えてください。

## Conclusion

おめでとうございます！**aspose 3d java** を使用して Java で Euler 角により 3D ノードを正常に変換できました。さまざまな角度や平行移動を試して、動的で魅力的な 3D シーンを作成してください。

## FAQ's

### Q1: Aspose.3D for Java を商用プロジェクトで使用できますか？

A1: はい、使用できます。ライセンスの詳細は [purchase page](https://purchase.aspose.com/buy) をご覧ください。

### Q2: Aspose.3D のサポートはどこで得られますか？

A2: [Aspose.3D forum](https://forum.aspose.com/c/3d/18) が支援を求め、コミュニティとつながる場所です。

### Q3: 無料トライアルはありますか？

A3: はい、[free trial](https://releases.aspose.com/) で Aspose.3D の機能を体験できます。

### Q4: 一時ライセンスはどのように取得できますか？

A4: [here](https://purchase.aspose.com/temporary-license/) から一時ライセンスを取得できます。

### Q5: ドキュメントはどこで見つけられますか？

A5: [documentation](https://reference.aspose.com/3d/java/) に Aspose.3D for Java の包括的なガイドがあります。

## Frequently Asked Questions

**Q: Euler角とクォータニオン回転の違いは何ですか？**  
A: Euler角は直感的（ピッチ、ヨー、ロール）ですが、ジンバルロックが発生しやすいです。一方、クォータニオンはその問題を回避し、スムーズな補間に適しています。

**Q: 同じノードに複数の変換を連鎖させられますか？**  
A: はい。`setEulerAngles`、`setTranslation`、`setScale` を任意の順序で呼び出すと、ライブラリがそれらを単一の変換行列に合成します。

**Q: OBJ や STL など他の形式へエクスポートできますか？**  
A: もちろんです。`scene.save` 呼び出しで `FileFormat.FBX7500ASCII` を `FileFormat.OBJ` または `FileFormat.STL` に置き換えます。

**Q: 複数のノードに同じ回転を同時に適用するには？**  
A: 親ノードを作成し、回転を親に適用してから子ノードを追加します。すべての子は変換を継承します。

**Q: 保存後にクリーンアップメソッドを呼び出す必要がありますか？**  
A: Java のガベージコレクタがほとんどのリソースを処理しますが、長時間実行するアプリケーションで大規模シーンを扱う場合は `scene.dispose()` を明示的に呼び出すこともできます。

---

**Last Updated:** 2025-12-13  
**Tested With:** Aspose.3D 23.12 for Java  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}