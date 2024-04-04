---
title: Aplikace Twist v lineárním vytlačování s Aspose.3D pro Javu
linktitle: Aplikace Twist v lineárním vytlačování s Aspose.3D pro Javu
second_title: Aspose.3D Java API
description: Naučte se, jak přidat šmrnc svým 3D modelům pomocí Aspose.3D for Java. Postupujte podle našeho podrobného průvodce pro vylepšené efekty lineárního vytlačování.
type: docs
weight: 14
url: /cs/java/linear-extrusion/applying-twist/
---
## Úvod

Vítejte v tomto podrobném návodu na použití zkroucení při lineárním vytlačování pomocí Aspose.3D pro Java. Aspose.3D je výkonná Java knihovna, která umožňuje vývojářům pracovat s 3D formáty souborů a nabízí robustní funkce pro vytváření, manipulaci a renderování 3D scén. V tomto tutoriálu prozkoumáme, jak použít efekt kroucení během procesu lineárního vytlačování pro vylepšení vašich 3D modelů.

## Předpoklady

Než se pustíte do výukového programu, ujistěte se, že máte splněny následující předpoklady:

- Vývojové prostředí Java: Ujistěte se, že máte v systému nainstalovanou Javu.
-  Knihovna Aspose.3D: Stáhněte a nainstalujte knihovnu Aspose.3D pro Javu z[odkaz ke stažení](https://releases.aspose.com/3d/java/).
-  Dokumentace: Viz[Aspose.3D dokumentace](https://reference.aspose.com/3d/java/) za komplexní návod.

## Importujte balíčky

Před zahájením procesu kódování naimportujte potřebné balíčky do svého projektu Java. Zde je příklad, jak to udělat:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Krok 1: Nastavte adresář dokumentů

Začněte nastavením adresáře dokumentů, do kterého bude vaše 3D scéna uložena.

```java
// ExStart:SetDocumentDirectory
String MyDir = "Your Document Directory";
// ExEnd:SetDocumentDirectory
```

## Krok 2: Inicializujte základní profil

Inicializujte základní profil, který má být vysunut. V tomto příkladu používáme tvar obdélníku s poloměrem zaoblení.

```java
// ExStart:InitializeBaseProfile
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
// ExEnd:InitializeBaseProfile
```

## Krok 3: Vytvořte scénu

Vytvořte 3D scénu, která bude hostit vysunuté uzly.

```java
// ExStart:CreateScene
Scene scene = new Scene();
// ExEnd:CreateScene
```

## Krok 4: Vytvořte uzly

Vytvořte levý a pravý uzel ve scéně. Upravte překlad levého uzlu.

```java
// ExStart:CreateNodes
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
// ExEnd:CreateNodes
```

## Krok 5: Proveďte lineární vytlačování pomocí Twist

Proveďte lineární vysunutí na levém i pravém uzlu s použitím vlastností kroucení a řezů.

```java
// ExStart:LinearExtrusionWithTwist
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(0); setSlices(100); }});
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(90); setSlices(100); }});
// ExEnd:LinearExtrusionWithTwist
```

## Krok 6: Uložte 3D scénu

Uložte 3D scénu ve formátu souboru Wavefront OBJ.

```java
// ExStart:Save3DScene
scene.save(MyDir + "TwistInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
//ExEnd:Save3DScene
```

## Závěr

Gratulujeme! Úspěšně jste použili zkroucení v lineárním vytlačování pomocí Aspose.3D pro Java. Tento výukový program poskytuje podrobného průvodce krok za krokem, který vám pomůže vylepšit možnosti 3D modelování.

## FAQ

### Q1: Mohu použít Aspose.3D for Java pro práci s jinými 3D formáty souborů?

Odpověď 1: Ano, Aspose.3D podporuje různé formáty 3D souborů, což vám umožňuje importovat, exportovat a manipulovat s různými typy souborů.

### Q2: Kde najdu podporu pro Aspose.3D pro Java?

 A2: Navštivte[Aspose.3D fórum](https://forum.aspose.com/c/3d/18) za podporu komunity a diskuze.

### Q3: Je k dispozici bezplatná zkušební verze pro Aspose.3D pro Java?

 A3: Ano, máte přístup k bezplatné zkušební verzi z[tady](https://releases.aspose.com/).

### Q4: Jak mohu získat dočasnou licenci pro Aspose.3D for Java?

 A4: Získejte dočasnou licenci od[dočasná licenční stránka](https://purchase.aspose.com/temporary-license/).

### Q5: Kde mohu zakoupit Aspose.3D pro Java?

 A5: Nákup Aspose.3D pro Java z[nákupní stránku](https://purchase.aspose.com/buy).