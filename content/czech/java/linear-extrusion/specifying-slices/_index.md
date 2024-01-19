---
title: Určení řezů v lineárním vytlačování pomocí Aspose.3D pro Javu
linktitle: Určení řezů v lineárním vytlačování pomocí Aspose.3D pro Javu
second_title: Aspose.3D Java API
description: Naučte se specifikovat řezy v lineárním vytlačování pomocí Aspose.3D for Java. Zvyšte své dovednosti v oblasti 3D modelování pomocí tohoto podrobného průvodce.
type: docs
weight: 13
url: /cs/java/linear-extrusion/specifying-slices/
---
## Úvod

Vytváření složitých 3D modelů často vyžaduje víc než jen kreativitu; vyžaduje důkladné pochopení nástrojů, které máte k dispozici. Aspose.3D for Java v tomto ohledu mění hru. V tomto tutoriálu se zaměříme na konkrétní aspekt – specifikaci řezů v lineárním vytlačování.

## Předpoklady

Než se pustíte do výukového programu, ujistěte se, že máte splněny následující předpoklady:

1. Prostředí Java: Ujistěte se, že máte ve svém systému nastavené vývojové prostředí Java.
2.  Aspose.3D for Java: Stáhněte a nainstalujte knihovnu Aspose.3D. Potřebné balíčky najdete[tady](https://releases.aspose.com/3d/java/).

## Importujte balíčky

Do svého projektu Java importujte knihovnu Aspose.3D. To je klíčové pro přístup k funkcím, se kterými budeme pracovat. Přidejte do kódu následující příkaz pro import:

```java
import com.aspose.threed.*;

import java.io.IOException;
```

Nyní si příklad rozdělíme do několika kroků.

## Krok 1: Nastavte scénu

Inicializujte základní profil, který se má vytlačit, v tomto případě a`RectangleShape` se zadaným poloměrem zaoblení. Vytvořte 3D scénu, se kterou budete pracovat.

```java
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
Scene scene = new Scene();
```

## Krok 2: Vytvořte uzly

Generujte levý a pravý uzel ve scéně. Upravte translaci levého uzlu pro prostorové variace.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Krok 3: Lineární vytlačování s plátky

Proveďte lineární vysunutí na obou uzlech a určete počet řezů pro každý z nich. Tady se děje kouzlo.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(2);}});
right.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(10);}});
```

## Krok 4: Uložte scénu

Uložte 3D scénu v požadovaném formátu, v tomto případě do souboru Wavefront OBJ.

```java
scene.save(MyDir + "SlicesInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Závěr

Gratulujeme! Úspěšně jste se naučili, jak specifikovat řezy v lineárním vytlačování pomocí Aspose.3D for Java. Tato dovednost otevírá nové možnosti na vaší cestě 3D modelováním.

## FAQ

### Q1: Jak si mohu stáhnout Aspose.3D pro Java?

 A1: Můžete si stáhnout knihovnu[tady](https://releases.aspose.com/3d/java/).

### Q2: Kde najdu dokumentaci k Aspose.3D?

 A2: Viz dokumentace[tady](https://reference.aspose.com/3d/java/).

### Q3: Je k dispozici bezplatná zkušební verze?

 A3: Ano, můžete prozkoumat bezplatnou zkušební verzi[tady](https://releases.aspose.com/).

### Q4: Jak mohu získat podporu pro Aspose.3D?

 A4: Navštivte fórum podpory[tady](https://forum.aspose.com/c/3d/18).

### Q5: Mohu si zakoupit dočasnou licenci?

 A5: Ano, lze získat dočasnou licenci[tady](https://purchase.aspose.com/temporary-license/).