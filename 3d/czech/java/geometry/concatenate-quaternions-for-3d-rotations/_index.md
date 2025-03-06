---
title: Zřetězit čtveřice pro 3D rotace v Javě s Aspose.3D
linktitle: Zřetězit čtveřice pro 3D rotace v Javě s Aspose.3D
second_title: Aspose.3D Java API
description: Naučte se, jak zřetězit čtveřice pro 3D rotace v Javě pomocí Aspose.3D. Postupujte podle našeho podrobného průvodce pro bezproblémové transformace animací.
weight: 11
url: /cs/java/geometry/concatenate-quaternions-for-3d-rotations/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Zřetězit čtveřice pro 3D rotace v Javě s Aspose.3D

## Úvod

Čtveřice zřetězení je základní koncept ve 3D grafice, který vám umožňuje bezproblémově kombinovat více rotačních transformací. Aspose.3D zjednodušuje tento proces v Javě a nabízí efektivní a intuitivní způsob, jak zvládnout operace čtveřice. V tomto tutoriálu vás provedeme procesem zřetězení čtveřic a jejich aplikováním na 3D objekty pomocí Aspose.3D.

## Předpoklady

Než se ponoříte do výukového programu, ujistěte se, že máte následující předpoklady:

- Základní znalost programování v Javě.
- Nainstalovaný Aspose.3D for Java. Můžete si jej stáhnout[tady](https://releases.aspose.com/3d/java/).

## Importujte balíčky

Nezapomeňte importovat potřebné balíčky, abyste mohli využívat funkce Aspose.3D. Zahrňte do kódu Java následující řádky:

```java
import com.aspose.threed.*;
```

Nyní si ukázkový kód rozdělíme do několika kroků, abychom vytvořili komplexní tutoriál:

## Krok 1: Nastavte scénu

```java
Scene scene = new Scene();
```

## Krok 2: Definujte kvaterniony

```java
Quaternion q1 = Quaternion.fromEulerAngle(Math.PI * 0.5, 0, 0);
Vector3.X_AXIS.x = 3;
Quaternion q2 = Quaternion.fromAngleAxis(-Math.PI * 0.5, Vector3.X_AXIS);
```

## Krok 3: Spojte kvaterniony

```java
Quaternion q3 = q1.concat(q2);
```

## Krok 4: Vytvořte 3 válce

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

## Krok 5: Uložit do souboru

```java
MyDir = MyDir + "test_out.fbx";
scene.save(MyDir, FileFormat.FBX7400ASCII);
// ExEnd:ConcatenateQuaternions
```

## Krok 6: Tisk zprávy o úspěchu

```java
System.out.println("\nQuaternions concatenated successfully.\nFile saved at " + MyDir);
```

## Závěr

Podle tohoto tutoriálu jste se naučili, jak zřetězit čtveřice pro 3D rotace v Javě pomocí Aspose.3D. Experimentujte s různými kombinacemi čtveřice, abyste dosáhli různých a přesných rotací ve svých 3D projektech.

## FAQ

### Q1: Mohu používat Aspose.3D pro Javu zdarma?

 A1: Aspose.3D nabízí a[zkušební verze zdarma](https://releases.aspose.com/) abyste mohli prozkoumat jeho vlastnosti. Pro delší použití zvažte nákup a[licence](https://purchase.aspose.com/buy).

### Q2: Kde najdu komplexní dokumentaci k Aspose.3D?

 A2:[dokumentace](https://reference.aspose.com/3d/java/) poskytuje podrobné informace a příklady, které vám pomohou začít.

### Q3: Jak mohu vyhledat podporu pro Aspose.3D?

 A3: Navštivte[Aspose.3D fórum](https://forum.aspose.com/c/3d/18) klást otázky, sdílet zkušenosti a získat pomoc od komunity.

### Q4: Jsou k dispozici dočasné licence pro Aspose.3D?

 A4: Ano, můžete získat a[dočasná licence](https://purchase.aspose.com/temporary-license/) pro účely testování a hodnocení.

### Q5: Jaké formáty souborů jsou podporovány pro ukládání 3D scén?

Odpověď 5: Aspose.3D podporuje různé formáty a můžete ukládat scény ve formátu FBX, jak je ukázáno v tomto návodu.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
