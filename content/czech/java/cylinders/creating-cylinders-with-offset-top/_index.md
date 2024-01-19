---
title: Vytváření válců s odsazenou horní částí v Aspose.3D pro Java
linktitle: Vytváření válců s odsazenou horní částí v Aspose.3D pro Java
second_title: Aspose.3D Java API
description: Prozkoumejte zázraky 3D modelování v Javě s Aspose.3D. Naučte se bez námahy vytvářet podmanivé válce s ofsetovými vršky.
type: docs
weight: 11
url: /cs/java/cylinders/creating-cylinders-with-offset-top/
---
## Úvod

V oblasti 3D modelování založeného na Javě vyniká Aspose.3D jako výkonný nástroj, který vývojářům nabízí možnost snadno vytvářet složité 3D scény. V tomto tutoriálu se ponoříme do fascinujícího světa Aspose.3D pro Java a zaměříme se na konkrétní úkol – vytváření válců s odsazenými vršky. Na konci této příručky budete mít pevný přehled o procesu, který vám umožní bezproblémově integrovat tuto funkci do vašich 3D projektů.

## Předpoklady

Než se pustíme do této kreativní cesty, ujistěte se, že máte splněny následující předpoklady:

- Java Development Kit (JDK): Aspose.3D for Java vyžaduje na vašem počítači nainstalovaný kompatibilní JDK.
- Knihovna Aspose.3D: Stáhněte si a integrujte knihovnu Aspose.3D do svého projektu Java. Najdete zde knihovnu a podrobnou dokumentaci[tady](https://releases.aspose.com/3d/java/).

## Importujte balíčky

Začněme proces importem potřebných balíčků pro náš projekt Java. Do kódu zahrňte následující:

```java
import com.aspose.threed.Cylinder;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Vector3;


import java.io.IOException;
```

## Krok 1: Vytvořte scénu

Začněte inicializací scény, kde budete organizovat své 3D prvky.

```java
// Start: 1
// Vytvořte scénu
Scene scene = new Scene();
// Rozšíření: 1
```

## Krok 2: Inicializujte válec s odsazenou horní částí

Dále vytvořte objekt válce s přizpůsobeným odsazeným vrcholem pomocí následujícího kódu:

```java
// Start: 2
// Inicializujte válec
Cylinder cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
// Nastavte OffsetTop
cylinder1.setOffsetTop(new Vector3(5, 3, 0));
// Rozšířit:2
```

## Krok 3: Vytvořte podřízený uzel

Nyní vytvořte podřízený uzel ve scéně a nastavte překlad pro první válec:

```java
// Start: 3
// Vytvořte ChildNode
scene.getRootNode().createChildNode(cylinder1).getTransform().setTranslation(10, 0, 0);
// Rozšířit:3
```

## Krok 4: Inicializujte druhý válec

Pojďme inicializovat druhý válec bez přizpůsobeného ofsetového vrcholu:

```java
// Start: 4
//Inicializujte druhý válec bez přizpůsobeného OffsetTop
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// Rozšíření:4
```

## Krok 5: Vytvořte podřízený uzel pro druhý válec

Vytvořte podřízený uzel pro druhý válec ve scéně:

```java
// Start: 5
// Vytvořte ChildNode
scene.getRootNode().createChildNode(cylinder2);
// Rozšíření:5
```

## Krok 6: Uložte scénu

Nakonec uložte scénu s vytvořenými cylindry jako soubor Wavefront OBJ do adresáře dokumentu:

```java
// Start: 6
// Uložit
scene.save("Your Document Directory" + "CustomizedOffsetTopCylinder.obj", FileFormat.WAVEFRONTOBJ);
// Konec:6
```

Pomocí těchto jednoduchých kroků jste úspěšně vytvořili 3D válce s odsazenými vršky pomocí Aspose.3D for Java!

## Závěr

Aspose.3D for Java umožňuje vývojářům uvést své 3D vize do života bez námahy. V tomto tutoriálu jsme se zaměřili na vytváření válců s odsazenými vršky a ukázali jsme všestrannost a jednoduchost Aspose.3D. Nyní, vyzbrojeni těmito znalostmi, můžete prozkoumat a integrovat pokročilejší funkce do svých 3D projektů založených na Javě.

## FAQ

### Q1: Je Aspose.3D kompatibilní s různými Java IDE?

Odpověď 1: Ano, Aspose.3D se bez problémů integruje s populárními Java Integrated Development Environment (IDE), jako jsou Eclipse, IntelliJ IDEA a NetBeans.

### Q2: Mohu použít textury na vytvořené 3D objekty?

A2: Rozhodně! Aspose.3D poskytuje rozsáhlé možnosti pro aplikaci textur a materiálů pro zvýšení vizuální přitažlivosti vašich 3D modelů.

### Q3: Jsou pro Aspose.3D k dispozici nějaké možnosti licencování?

 A3: Ano, můžete prozkoumat a vybrat možnost licencování, která vyhovuje vašim potřebám[tady](https://purchase.aspose.com/buy).

### Q4: Jak mohu vyhledat pomoc nebo sdílet své zkušenosti s Aspose.3D?

 A4: Připojte se ke komunitnímu fóru Aspose.3D[tady](https://forum.aspose.com/c/3d/18) spojit se s ostatními vývojáři, vyhledat podporu a sdílet své poznatky.

### Q5: Existuje možnost dočasné licence pro účely testování?

 A5: Ano, můžete získat dočasnou licenci pro účely testování a hodnocení[tady](https://purchase.aspose.com/temporary-license/).