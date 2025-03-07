---
title: Controlling Center v Linear Extrusion s Aspose.3D for Java
linktitle: Controlling Center v Linear Extrusion s Aspose.3D for Java
second_title: Aspose.3D Java API
description: Prozkoumejte svět 3D grafiky v Javě s Aspose.3D. Ovládejte střed v lineárním vytlačování bez námahy.
weight: 11
url: /cs/java/linear-extrusion/controlling-center/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Controlling Center v Linear Extrusion s Aspose.3D for Java

## Úvod

Ve světě 3D grafiky a programování v jazyce Java hraje ovládání centra v lineárním vytlačování zásadní roli pro dosažení požadovaných efektů ve vašich projektech. Aspose.3D for Java poskytuje výkonnou sadu nástrojů pro bezproblémové zvládnutí takových úkolů. V tomto tutoriálu se ponoříme do procesu ovládání centra v lineárním vytlačování pomocí Aspose.3D pro Java, přičemž rozebereme každý krok, abychom zajistili hladké a komplexní porozumění.

## Předpoklady

Než se pustíme do této výukové cesty, ujistěte se, že máte splněny následující předpoklady:

1. Vývojové prostředí Java: Ujistěte se, že máte na svém počítači nastavené vývojové prostředí Java.

2.  Aspose.3D for Java: Stáhněte a nainstalujte knihovnu Aspose.3D. Knihovnu a její dokumentaci najdete[tady](https://reference.aspose.com/3d/java/).

3. Adresář dokumentů: Vytvořte adresář pro ukládání dokumentů Java. Říkejme tomu „Adresář vašich dokumentů“.

## Importujte balíčky

Ve vývojovém prostředí Java naimportujte potřebné balíčky pro Aspose.3D. Tím zajistíte, že váš kód bude mít přístup k funkcím poskytovaným knihovnou.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Krok 1: Nastavte základní profil

Inicializujte základní profil, který má být vysunut. V tomto příkladu použijeme tvar obdélníku s poloměrem zaoblení 0,3.

```java
// Cesta k adresáři dokumentů.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Krok 2: Vytvořte 3D scénu

Postavte základy svého 3D světa vytvořením scény.

```java
Scene scene = new Scene();
```

## Krok 3: Vytvořte levý a pravý uzel

Vytvořte ve své scéně levý a pravý uzel. Tyto uzly slouží jako plátno pro vaše 3D objekty.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Krok 4: Lineární vytlačování s vlastností středu

Proveďte lineární vysunutí na levém uzlu bez centrování a nastavte počet řezů na 3.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

## Krok 5: Nastavte základní rovinu jako referenční

Vylepšete vizuální reprezentaci přidáním základní roviny do levého uzlu.

```java
left.createChildNode(new Box(0.01, 3, 3));
```

## Krok 6: Lineární vytlačování s vlastností středu (pravý uzel)

Proveďte lineární vysunutí na pravém uzlu, tentokrát vycentrujte vysunutí a znovu nastavte počet řezů na 3.

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

## Krok 7: Nastavte základní rovinu jako referenční (pravý uzel)

Podobně jako u levého uzlu přidejte základní rovinu k pravému uzlu pro referenci.

```java
right.createChildNode(new Box(0.01, 3, 3));
```

## Krok 8: Uložte 3D scénu

Uložte svou 3D scénu ve formátu Wavefront OBJ.

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Závěr

Ovládání centra v lineárním vytlačování pomocí Aspose.3D for Java otevírá vzrušující možnosti ve vývoji 3D grafiky. Podle tohoto podrobného průvodce jste se naučili, jak manipulovat s vlastností centra, což vám umožní dosáhnout požadovaných vizuálních efektů ve vašich projektech Java.

## FAQ

### Q1: Mohu použít Aspose.3D for Java v komerčních projektech?

 Odpověď 1: Ano, Aspose.3D for Java je k dispozici pro komerční použití. Podrobnosti o licencích naleznete na adrese[tady](https://purchase.aspose.com/buy).

### Q2: Je k dispozici bezplatná zkušební verze?

 Odpověď 2: Ano, můžete prozkoumat bezplatnou zkušební verzi Aspose.3D pro Javu[tady](https://releases.aspose.com/).

### Q3: Kde najdu podporu pro Aspose.3D pro Java?

 Odpověď 3: Komunitní fórum Aspose.3D je skvělé místo, kde můžete hledat podporu a sdílet své zkušenosti. Navštivte fórum[tady](https://forum.aspose.com/c/3d/18).

### Q4: Potřebuji pro testování dočasnou licenci?

A4: Ano, pokud požadujete dočasnou licenci pro testovací účely, můžete ji získat[tady](https://purchase.aspose.com/temporary-license/).

### Q5: Kde najdu dokumentaci?

 A5: Dokumentace pro Aspose.3D pro Java je k dispozici[tady](https://reference.aspose.com/3d/java/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
