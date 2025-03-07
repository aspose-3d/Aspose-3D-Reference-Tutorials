---
title: Provádění lineárního vytlačování v Aspose.3D pro Javu
linktitle: Provádění lineárního vytlačování v Aspose.3D pro Javu
second_title: Aspose.3D Java API
description: Prozkoumejte svět 3D modelování s Aspose.3D pro Java. Naučte se provádět lineární vytlačování bez námahy.
weight: 10
url: /cs/java/linear-extrusion/performing-linear-extrusion/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Provádění lineárního vytlačování v Aspose.3D pro Javu

## Úvod

Vítejte v tomto komplexním tutoriálu o provádění lineárního vytlačování v Aspose.3D pro Java! Pokud chcete zlepšit své dovednosti v oblasti 3D modelování pomocí Javy, jste na správném místě. V tomto tutoriálu vás provedeme procesem provádění lineárního vytlačování pomocí Aspose.3D, výkonné Java knihovny pro 3D modelování.

## Předpoklady

Než se pustíte do výukového programu, ujistěte se, že máte splněny následující předpoklady:

1. Vývojové prostředí Java: Ujistěte se, že máte na svém počítači nastavené vývojové prostředí Java.

2.  Knihovna Aspose.3D: Stáhněte a nainstalujte knihovnu Aspose.3D. Knihovnu najdete[tady](https://releases.aspose.com/3d/java/).

## Importujte balíčky

Jakmile nastavíte vývojové prostředí a nainstalujete knihovnu Aspose.3D, je čas naimportovat potřebné balíčky. Do kódu Java zahrňte následující:

```java
import com.aspose.threed.*;
```

Pojďme si jednotlivé kroky rozebrat, abychom zajistili jasné porozumění.

## Krok 1: Nastavte adresář dokumentů

Definujte cestu k adresáři dokumentů:

```java
String MyDir = "Your Document Directory";
```

Tím je zajištěno, že vygenerovaný 3D model bude uložen do zadaného adresáře.

## Krok 2: Inicializujte základní tvar

Vytvořte obdélníkový tvar jako základní profil pro vytlačování:

```java
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

Upravte poloměr zaoblení podle potřeby pro přizpůsobení tvaru.

## Krok 3: Proveďte lineární vytlačování

Proveďte lineární vytlačování na základním profilu:

```java
LinearExtrusion extrusion = new LinearExtrusion(profile, 10) {{ setSlices(100); setCenter(true); setTwist(360); setTwistOffset(new Vector3(10, 0, 0));}};
```

Zde vytlačíme tvar o 10 jednotek, nastavíme počet řezů, povolíme centrování a použijeme ofset kroucení a kroucení.

## Krok 4: Vytvořte 3D scénu

Vytvořte 3D scénu a přidejte vysunutí jako podřízený uzel:

```java
Scene scene = new Scene();
scene.getRootNode().createChildNode(extrusion);
```

## Krok 5: Uložte 3D scénu

Uložte vygenerovanou 3D scénu jako soubor Wavefront OBJ:

```java
scene.save(MyDir +  "LinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

Nyní jste úspěšně provedli lineární vytlačování pomocí Aspose.3D pro Java!

## Závěr

Gratulujeme! Naučili jste se, jak využít Aspose.3D pro Java k provádění lineárního vytlačování. Tato výkonná knihovna otevírá svět možností pro vaše projekty 3D modelování.

## FAQ

### Q1: Je Aspose.3D kompatibilní se všemi verzemi Java?

A1: Aspose.3D je navržen pro práci s Java 1.6 a novějšími verzemi.

### Q2: Mohu použít Aspose.3D pro komerční projekty?

A2: Ano, Aspose.3D lze použít pro osobní i komerční projekty. Zkontrolujte podrobnosti o licenci[tady](https://purchase.aspose.com/buy).

### Q3: Jak mohu získat podporu pro Aspose.3D?

 A3: Navštivte[Aspose.3D fórum](https://forum.aspose.com/c/3d/18) pro podporu komunity nebo zvažte nákup a[dočasná licence](https://purchase.aspose.com/temporary-license/) za prémiovou podporu.

### Q4: Existují v Aspose.3D další funkce 3D modelování?

 A4: Rozhodně! Prozkoumejte rozsáhlou dokumentaci[tady](https://reference.aspose.com/3d/java/) pro úplný seznam funkcí a příkladů.

### Q5: Je k dispozici bezplatná zkušební verze pro Aspose.3D?

 A5: Ano, máte přístup k bezplatné zkušební verzi[tady](https://releases.aspose.com/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
