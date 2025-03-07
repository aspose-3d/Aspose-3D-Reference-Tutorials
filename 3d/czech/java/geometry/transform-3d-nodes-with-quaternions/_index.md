---
title: Transformujte 3D uzly pomocí čtveřice v Javě pomocí Aspose.3D
linktitle: Transformujte 3D uzly pomocí čtveřice v Javě pomocí Aspose.3D
second_title: Aspose.3D Java API
description: Vylepšete své Java aplikace pomocí Aspose.3D pro výkonné 3D transformace. Naučte se transformovat uzly pomocí čtveřice v tomto podrobném průvodci.
weight: 20
url: /cs/java/geometry/transform-3d-nodes-with-quaternions/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Transformujte 3D uzly pomocí čtveřice v Javě pomocí Aspose.3D

## Úvod

Vítejte v tomto podrobném průvodci o transformaci 3D uzlů pomocí čtveřice v Javě pomocí Aspose.3D. Pokud chcete vylepšit svou aplikaci Java pomocí výkonných 3D transformací, tento tutoriál je pro vás. Aspose.3D for Java poskytuje robustní sadu funkcí pro práci s 3D grafikou a v tomto tutoriálu se zaměříme na transformaci 3D uzlů pomocí čtveřice.

## Předpoklady

Než se pustíme do výukového programu, ujistěte se, že máte splněny následující předpoklady:

- Základní znalost programování v Javě.
- Nainstalovaný Aspose.3D for Java. Můžete si jej stáhnout[tady](https://releases.aspose.com/3d/java/).
- Adresář dokumentů nastavený pro ukládání vašich 3D scén.

## Importujte balíčky

V této části naimportujeme potřebné balíčky, abychom mohli začít s 3D transformacemi pomocí Aspose.3D.

```java
import com.aspose.threed.*;
```

## Krok 1: Inicializujte objekt scény

Nejprve vytvořte objekt scény, který bude sloužit jako kontejner pro vaše 3D prvky.

```java
Scene scene = new Scene();
```

## Krok 2: Inicializujte objekt třídy uzlu

Nyní vytvořte objekt třídy uzlu, v tomto případě představující krychli.

```java
Node cubeNode = new Node("cube");
```

## Krok 3: Vytvořte síť pomocí Polygon Builder

Použijte společnou třídu k vytvoření sítě pomocí metody polygon builder.

```java
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

## Krok 4: Nastavte geometrii sítě

Vytvořenou síť přiřaďte uzlu krychle.

```java
cubeNode.setEntity(mesh);
```

## Krok 5: Nastavte Rotation pomocí Quaternion

Aplikujte rotaci na uzel krychle pomocí čtveřice.

```java
cubeNode.getTransform().setRotation(Quaternion.fromRotation(new Vector3(0, 1, 0), new Vector3(0.3, 0.5, 0.1)));
```

## Krok 6: Nastavte překlad

Zadejte překlad pro uzel krychle.

```java
cubeNode.getTransform().setTranslation(new Vector3(0, 0, 20));
```

## Krok 7: Přidejte kostku do scény

Zahrňte uzel krychle do scény.

```java
scene.getRootNode().getChildNodes().add(cubeNode);
```

## Krok 8: Uložte 3D scénu

Uložte 3D scénu v podporovaném formátu souboru, například FBX7500ASCII.

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "TransformationToNode.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
System.out.println("\nTransformation added successfully to node.\nFile saved at " + MyDir);
```

## Závěr

Gratulujeme! Úspěšně jste se naučili, jak transformovat 3D uzly pomocí quaternionů v Javě s Aspose.3D. Experimentujte s různými transformacemi, abyste oživili své 3D aplikace.

## FAQ

### Q1: Mohu používat Aspose.3D pro Javu zdarma?

A1: Aspose.3D for Java nabízí bezplatnou zkušební verzi. Můžete to najít[tady](https://releases.aspose.com/).

### Q2: Kde najdu dokumentaci k Aspose.3D for Java?

 A2: Dokumentace je k dispozici[tady](https://reference.aspose.com/3d/java/).

### Q3: Jak získám podporu pro Aspose.3D pro Java?

 A3: Navštivte[Aspose.3D fórum](https://forum.aspose.com/c/3d/18) pro podporu.

### Q4: Jsou k dispozici dočasné licence?

 A4: Ano, můžete získat dočasnou licenci[tady](https://purchase.aspose.com/temporary-license/).

### Q5: Kde mohu zakoupit Aspose.3D pro Java?

 A5: Můžete si to koupit[tady](https://purchase.aspose.com/buy).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
