---
title: Aspose.3D for Java で底部をせん断した円柱を作成する
linktitle: Aspose.3D for Java で底部をせん断した円柱を作成する
second_title: Aspose.3D Java API
description: Aspose.3D for Java を使用して、底部をせん断したカスタマイズされた円柱を作成する方法を学びます。このステップバイステップのガイドで 3D モデリングのスキルを向上させましょう。
weight: 12
url: /ja/java/cylinders/creating-cylinders-with-sheared-bottom/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose.3D for Java で底部をせん断した円柱を作成する

## 導入

Aspose.3D for Java を使用して底部がせん断された円柱を作成するためのこのステップバイステップ ガイドへようこそ。 Aspose.3D は、3D ファイルを簡単に操作できる強力な Java ライブラリです。このチュートリアルでは、底部をせん断したカスタマイズされた円柱の作成について詳しく説明し、Aspose.3D を使用して 3D モデリング スキルを向上させる実践的な経験を提供します。

## 前提条件

始める前に、次の前提条件が満たされていることを確認してください。
- Java Development Kit (JDK) がシステムにインストールされています。
-  Aspose.3D for Java ライブラリがダウンロードされ、プロジェクトに追加されました。ダウンロードリンクが見つかります[ここ](https://releases.aspose.com/3d/java/).

## パッケージのインポート

まず、Java アプリケーションで Aspose.3D を操作するために必要なパッケージをインポートします。
```java
import com.aspose.threed.*;


import java.io.IOException;
```

## ステップ 1: シーンを作成する

まず、円柱を追加して操作する 3D シーンを作成します。
```java
//例開始:3
//シーンを作成する
Scene scene = new Scene();
//拡張終了:3
```

## ステップ 2: シリンダー 1 を作成する

次に、底部がせん断された最初の円柱を作成しましょう。
```java
//例開始:4
//シリンダー 1 を作成する
Cylinder cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
//シリンダー 1 のカスタマイズされたシャーボトム
cylinder1.setShearBottom(new Vector2(0, 0.83)); //xy 平面 (z 軸) で 47.5 度のせん断
//シリンダー 1 をシーンに追加
scene.getRootNode().createChildNode(cylinder1).getTransform().setTranslation(10, 0, 0);
//拡張終了:4
```

## ステップ 3: シリンダー 2 を作成する

次に、底部がせん断されていない 2 番目の円柱をシーンに追加しましょう。
```java
//例開始:5
//シリンダー 2 を作成する
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
//ShearBottom のないシリンダー 2 をシーンに追加します。
scene.getRootNode().createChildNode(cylinder2);
//拡張終了:5
```

## ステップ 4: シーンを保存する

カスタマイズしたシリンダーを含むシーンをドキュメント ディレクトリに保存します。
```java
//例開始:6
//シーンを保存する
scene.save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WAVEFRONTOBJ);
//拡張終了:6
```

おめでとう！ Aspose.3D for Java を使用して、底部がせん断された円柱を正常に作成できました。

## 結論

このチュートリアルでは、Aspose.3D for Java を活用して 3D モデリング プロジェクトを強化する方法を検討しました。底部をせん断したカスタマイズされた円柱を作成すると、デザインに独特のタッチが加わり、Aspose.3D によってプロセスが簡素化されます。

## よくある質問

### Q1: Aspose.3D for Java を他の Java 3D ライブラリと一緒に使用できますか?

A1: Aspose.3D for Java は独立して動作するように設計されています。他のライブラリと統合することもできますが、ほとんどの 3D モデリング タスクを単独で処理できるほど強力です。

### Q2: Aspose.3D は 3D モデリングの初心者に適していますか?

A2: はい、Aspose.3D はユーザーフレンドリーな API を提供するため、3D モデリングの初心者と経験豊富な開発者の両方に適しています。

### Q3: Aspose.3D for Java の追加サポートはどこで見つけられますか?

 A3: にアクセスしてください。[Aspose.3D フォーラム](https://forum.aspose.com/c/3d/18)コミュニティのサポートとディスカッションのために。

### Q4: Aspose.3D の一時ライセンスを取得するにはどうすればよいですか?

 A4: 仮免許は取得できます。[ここ](https://purchase.aspose.com/temporary-license/).

### Q5: Aspose.3D for Java を購入できますか?

 A5: はい、Aspose.3D for Java を購入できます。[ここ](https://purchase.aspose.com/buy).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
