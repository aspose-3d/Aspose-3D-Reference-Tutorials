---
title: Nastavení směru v lineárním vytlačování s Aspose.3D pro Java
linktitle: Nastavení směru v lineárním vytlačování s Aspose.3D pro Java
second_title: Aspose.3D Java API
description: Zvládněte lineární vytlačování s Aspose.3D pro Java! Postupujte podle našeho průvodce pro bezproblémové 3D programování. Stáhněte si nyní a zažijte strhující zážitek.
type: docs
weight: 12
url: /cs/java/linear-extrusion/setting-direction/
---
## Úvod

Vítejte v našem podrobném průvodci nastavením směru při lineárním vytlačování pomocí Aspose.3D pro Java. Aspose.3D je výkonná Java knihovna, která umožňuje vývojářům bezproblémově pracovat s 3D soubory a scénami. V tomto tutoriálu se zaměříme na konkrétní úkol, kterým je nastavení směru při lineárním vytlačování, čímž zvýšíme vaši odbornost v 3D programování.

## Předpoklady

Než se pustíme do výukového programu, ujistěte se, že máte splněny následující předpoklady:

- Základní znalost programovacího jazyka Java.
-  Nainstalovaná knihovna Aspose.3D. Můžete si jej stáhnout z[tady](https://releases.aspose.com/3d/java/).
- Integrované vývojové prostředí (IDE) pro Javu, jako je Eclipse nebo IntelliJ.

## Importujte balíčky

Ujistěte se, že importujete potřebné balíčky pro nastartování vašeho projektu:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Krok 1: Inicializujte základní profil

 Začněte inicializací základního profilu, který má být vytlačen. V tomto příkladu používáme a`RectangleShape` s poloměrem zaoblení 0,3:

```java
// Cesta k adresáři dokumentů.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Krok 2: Vytvořte scénu

Dále vytvořte 3D scénu, která bude obsahovat vysunuté objekty:

```java
Scene scene = new Scene();
```

## Krok 3: Vytvořte uzly

Vytvořte levý a pravý uzel ve scéně:

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Krok 4: Proveďte lineární vysunutí na levém uzlu

 Proveďte lineární vysunutí na levém uzlu pomocí`LinearExtrusion`třída se zadanými parametry, jako je twist and slices:

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## Krok 5: Proveďte lineární vysunutí na pravém uzlu se směrem

 Proveďte lineární extruzi na pravém uzlu a zaveďte`setDirection` vlastnost pro definování směru vytlačování:

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## Krok 6: Uložte 3D scénu

Uložte 3D scénu do požadovaného formátu souboru. V tomto příkladu jej uložíme jako soubor Wavefront OBJ:

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Závěr

Gratulujeme! Úspěšně jste se naučili, jak nastavit směr v lineárním vytlačování pomocí Aspose.3D pro Java. Tento tutoriál zlepší vaše dovednosti v 3D programování a otevře nové možnosti pro kreativní projekty.

## FAQ

### Q1: Mohu používat Aspose.3D s jinými programovacími jazyky?

A1: Aspose.3D podporuje různé programovací jazyky, včetně .NET a Java.

### Q2. Je k dispozici bezplatná zkušební verze pro Aspose.3D?

 Odpověď 2: Ano, funkce Aspose.3D můžete prozkoumat pomocí bezplatné zkušební verze[tady](https://releases.aspose.com/).

### Q3: Kde najdu podrobnou dokumentaci k Aspose.3D for Java?

 A3: K dispozici je komplexní dokumentace[tady](https://reference.aspose.com/3d/java/).

### Q4: Jak mohu získat podporu pro Aspose.3D?

 A4: Navštivte[Aspose.3D fórum](https://forum.aspose.com/c/3d/18) pro jakoukoli pomoc nebo dotazy.

### Q5: Jsou k dispozici dočasné licence pro Aspose.3D?

 A5: Ano, můžete získat dočasnou licenci[tady](https://purchase.aspose.com/temporary-license/).