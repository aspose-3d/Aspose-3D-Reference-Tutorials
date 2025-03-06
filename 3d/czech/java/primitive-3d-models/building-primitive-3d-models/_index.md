---
title: Vytváření primitivních 3D modelů pomocí Aspose.3D pro Javu
linktitle: Vytváření primitivních 3D modelů pomocí Aspose.3D pro Javu
second_title: Aspose.3D Java API
description: Objevte umění 3D modelování s Aspose.3D pro Javu. Naučte se bez námahy stavět primitivní 3D modely a popusťte uzdu své kreativitě.
weight: 10
url: /cs/java/primitive-3d-models/building-primitive-3d-models/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Vytváření primitivních 3D modelů pomocí Aspose.3D pro Javu

## Úvod

Programové vytváření 3D modelů může být skličující úkol, ale s Aspose.3D pro Java se z toho stává příjemný a přímočarý proces. Tento tutoriál vám pomůže začít s vytvářením primitivních 3D modelů se zaměřením na jednoduchost a efektivitu.

## Předpoklady

Než se ponoříte do světa 3D modelování s Aspose.3D pro Java, ujistěte se, že máte splněny následující předpoklady:

1. Java Development Kit (JDK): Ujistěte se, že máte na svém počítači nainstalovaný JDK.
2.  Knihovna Aspose.3D for Java: Stáhněte a nainstalujte knihovnu Aspose.3D for Java z[stránka ke stažení](https://releases.aspose.com/3d/java/).

## Importujte balíčky

Začněte importováním potřebných balíčků do vašeho projektu Java. Tento krok je zásadní pro přístup k funkcím poskytovaným Aspose.3D pro Javu.

```java

import com.aspose.threed.*;
```

Nyní, když máte vše nastaveno, přejděme k jádru tohoto tutoriálu – vytváření primitivních 3D modelů.

## Vytvoření scény

### Krok 1: Inicializujte objekt scény

```java
// Cesta k adresáři dokumentů.
String myDir = "Your Document Directory";

//Inicializujte objekt Scene
Scene scene = new Scene();
```

### Krok 2: Vytvořte krabicový model

```java
// Vytvořte model krabice
scene.getRootNode().createChildNode("box", new Box());
```

### Krok 3: Vytvořte model válce

```java
// Vytvořte model válce
scene.getRootNode().createChildNode("cylinder", new Cylinder());
```

### Krok 4: Uložte výkres ve formátu FBX

```java
// Uložte výkres ve formátu FBX
myDir = myDir + "test.fbx";
scene.save(myDir, FileFormat.FBX7500ASCII);
```

## Závěr

Gratulujeme! Úspěšně jste vytvořili scénu z primitivních 3D modelů pomocí Aspose.3D for Java. Soubor je nyní uložen v určeném adresáři.

## FAQ

### Q1: Mohu použít Aspose.3D pro Java s jinými programovacími jazyky?

A1: Aspose.3D primárně podporuje Javu, ale jsou dostupné verze pro jiné jazyky, jako je .NET.

### Q2: Je Aspose.3D vhodný pro komplexní úlohy 3D modelování?

A2: Rozhodně! Aspose.3D poskytuje komplexní sadu funkcí, takže je vhodný pro jednoduché i složité úlohy 3D modelování.

### Otázka 3: Kde najdu další pomoc a podporu?

 A3: Navštivte[Aspose.3D fórum](https://forum.aspose.com/c/3d/18) za podporu komunity a diskuze.

### Q4: Mohu vyzkoušet Aspose.3D před nákupem?

 A4: Ano, můžete prozkoumat a[zkušební verze zdarma](https://releases.aspose.com/) před rozhodnutím o koupi.

### Q5: Jak získám dočasnou licenci pro Aspose.3D?

 A5: Můžete získat a[dočasná licence](https://purchase.aspose.com/temporary-license/) pro Aspose.3D prostřednictvím webové stránky.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
