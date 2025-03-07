---
title: Aspose.3D を使用して Java で 3D 回転のクォータニオンを連結する
linktitle: Aspose.3D を使用して Java で 3D 回転のクォータニオンを連結する
second_title: Aspose.3D Java API
description: Aspose.3D を使用して Java で 3D 回転の四元数を連結する方法を学びます。シームレスなアニメーション変換については、ステップバイステップのガイドに従ってください。
weight: 11
url: /ja/java/geometry/concatenate-quaternions-for-3d-rotations/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose.3D を使用して Java で 3D 回転のクォータニオンを連結する

## 導入

クォータニオン連結は 3D グラフィックスの基本概念であり、複数の回転変換をシームレスに組み合わせることができます。 Aspose.3D は Java でのこのプロセスを簡素化し、クォータニオン操作を処理する効率的かつ直感的な方法を提供します。このチュートリアルでは、Aspose.3D を使用してクォータニオンを連結し、3D オブジェクトに適用するプロセスを説明します。

## 前提条件

チュートリアルに進む前に、次の前提条件を満たしていることを確認してください。

- Java プログラミングの基本的な知識。
- Java 用 Aspose.3D がインストールされています。ダウンロードできます[ここ](https://releases.aspose.com/3d/java/).

## パッケージのインポート

Aspose.3D 機能を利用するために必要なパッケージを必ずインポートしてください。 Java コードに次の行を含めます。

```java
import com.aspose.threed.*;
```

ここで、サンプル コードを複数のステップに分割して、包括的なチュートリアルを作成しましょう。

## ステップ 1: シーンをセットアップする

```java
Scene scene = new Scene();
```

## ステップ 2: クォータニオンを定義する

```java
Quaternion q1 = Quaternion.fromEulerAngle(Math.PI * 0.5, 0, 0);
Vector3.X_AXIS.x = 3;
Quaternion q2 = Quaternion.fromAngleAxis(-Math.PI * 0.5, Vector3.X_AXIS);
```

## ステップ 3: クォータニオンを連結する

```java
Quaternion q3 = q1.concat(q2);
```

## ステップ 4: 3 つの円柱を作成する

```java
Node cylinder = scene.getRootNode().createChildNode("cylinder-q1", new Cylinder(0.1, 1, 2));
cylinder.getTransform().setRotation(q1);
cylinder.getTransform().setTranslation(new Vector3(-5, 2, 0));
```

```java
cylinder = scene.getRootNode().createChildNode("cylinder-q2", new Cylinder(0.1, 1, 2));
cylinder.getTransform().setRotation(q2);
cylinder.getTransform().setTranslation(new Vector3(0, 2, 0));
```

```java
cylinder = scene.getRootNode().createChildNode("cylinder-q3", new Cylinder(0.1, 1, 2));
cylinder.getTransform().setRotation(q3);
cylinder.getTransform().setTranslation(new Vector3(5, 2, 0));
```

## ステップ 5: ファイルに保存

```java
MyDir = MyDir + "test_out.fbx";
scene.save(MyDir, FileFormat.FBX7400ASCII);
//ExEnd:クォータニオンの連結
```

## ステップ 6: 成功メッセージを印刷する

```java
System.out.println("\nQuaternions concatenated successfully.\nFile saved at " + MyDir);
```

## 結論

このチュートリアルに従うことで、Aspose.3D を使用して Java で 3D 回転のクォータニオンを連結する方法を学習しました。 3D プロジェクトで多様かつ正確な回転を実現するには、さまざまなクォータニオンの組み合わせを試してください。

## よくある質問

### Q1: Aspose.3D for Java を無料で使用できますか?

 A1: Aspose.3D は、[無料トライアル](https://releases.aspose.com/)その機能を探索してください。長期間使用するには、購入を検討してください。[ライセンス](https://purchase.aspose.com/buy).

### Q2: Aspose.3D の包括的なドキュメントはどこで見つけられますか?

 A2:[ドキュメンテーション](https://reference.aspose.com/3d/java/)開始に役立つ詳細な情報と例を提供します。

### Q3: Aspose.3D のサポートを求めるにはどうすればよいですか?

 A3: にアクセスしてください。[Aspose.3D フォーラム](https://forum.aspose.com/c/3d/18)質問したり、経験を共有したり、コミュニティから支援を得たりすることができます。

### Q4: Aspose.3D の一時ライセンスは利用できますか?

 A4: はい、入手できます。[仮免許](https://purchase.aspose.com/temporary-license/)テストと評価の目的で。

### Q5: 3D シーンの保存にはどのようなファイル形式がサポートされていますか?

A5: Aspose.3D はさまざまな形式をサポートしており、このチュートリアルで説明されているように、シーンを FBX 形式で保存できます。
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
