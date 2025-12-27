---
date: 2025-12-27
description: Naučte se, jak vytvořit 3D krabici v Javě pomocí Aspose.3D, exportovat
  scénu do FBX a prozkoumat knihovnu pro 3D modelování v Javě pro robustní 3D grafiku.
linktitle: Create 3D box Java with Aspose.3D – Primitive Model
second_title: Aspose.3D Java API
title: Vytvořte 3D krabici v Javě s Aspose.3D – Primitivní model
url: /cs/java/primitive-3d-models/building-primitive-3d-models/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Vytvořte 3D krabici v Javě s Aspose.3D – Primitivní model

## Úvod

Pokud chcete rychle **create 3D box Java** programy, Aspose.3D for Java to dělá překvapivě jednoduše. V tomto tutoriálu projdeme celý proces — od nastavení prostředí po export scény jako souboru FBX — abyste mohli s jistotou začít vytvářet 3‑D grafiku. Ať už jste vývojář her, nadšenec AR/VR, nebo jen zkoušíte **java 3d modeling library**, tento průvodce vás provede.

## Rychlé odpovědi
- **Co tutoriál pokrývá?** Vytvoření primitivní krabice a válce, následně export scény do FBX.  
- **Která knihovna je použita?** Aspose.3D for Java, výkonná **java 3d modeling library**.  
- **Potřebuji licenci?** Bezplatná zkušební verze funguje pro vývoj; licence je vyžadována pro produkci.  
- **Mohu exportovat jiné formáty?** Ano, Aspose.3D podporuje OBJ, STL a další, ale tento průvodce se zaměřuje na **export scene FBX**.  
- **Jak dlouho to trvá?** Přibližně 10‑15 minut na vytvoření funkčního příkladu.

## Jak vytvořit 3D krabici v Javě s Aspose.3D
Níže najdete přesné kroky, které je třeba dodržet. Každý krok obsahuje krátké vysvětlení, abyste pochopili *proč* to děláme, ne jen *co* napsat.

## Požadavky

Předtím, než se ponoříte, ujistěte se, že máte následující:

1. **Java Development Kit (JDK)** – jakákoli aktuální verze (8 nebo vyšší) nainstalovaná na vašem počítači.  
2. **Aspose.3D for Java Library** – stáhněte ji ze [download page](https://releases.aspose.com/3d/java/).  
3. IDE nebo textový editor podle vašeho výběru (IntelliJ IDEA, Eclipse, VS Code, atd.).

## Import balíčků

Začněte importováním hlavního balíčku Aspose.3D. To vám poskytne přístup ke všem 3‑D primitivům a třídám pro správu scény.

```java
import com.aspose.threed.*;
```

Nyní, když jsou importy na místě, vytvořme scénu, která bude obsahovat naše modely.

## Vytvoření scény

### Krok 1: Inicializace objektu Scene

```java
// The path to the documents directory.
String myDir = "Your Document Directory";

// Initialize a Scene object
Scene scene = new Scene();
```

Začínáme s čistým **Scene** — kontejnerem pro všechny 3‑D objekty, světla a kamery.

### Krok 2: Vytvoření modelu krabice

```java
// Create a Box model
scene.getRootNode().createChildNode("box", new Box());
```

Primitiv `Box` je středobodem našeho tutoriálu a ukazuje, jak vytvořit objekty ve stylu **create 3d box java**.

### Krok 3: Vytvoření modelu válce

```java
// Create a Cylinder model
scene.getRootNode().createChildNode("cylinder", new Cylinder());
```

Přidání válce ukazuje, jak snadno lze v jedné scéně kombinovat různé primitivy.

### Krok 4: Uložení výkresu ve formátu FBX

```java
// Save drawing in the FBX format
myDir = myDir + "test.fbx";
scene.save(myDir, FileFormat.FBX7500ASCII);
```

Zde **export scene FBX** pomocí ASCII verze formátu FBX 7.5, který je široce podporován 3‑D nástroji.

## Proč používat Aspose.3D pro Java?

- **Jednoduché API** – Není nutné ručně spravovat data sítě na nízké úrovni.  
- **Cross‑platform** – Funguje na Windows, Linuxu i macOS.  
- **Široká podpora formátů** – Kromě FBX můžete exportovat OBJ, STL, 3MF a další.  
- **Optimalizováno pro výkon** – Efektivně zpracovává velké scény, což z něj činí solidní volbu **java 3d modeling library**.

## Časté problémy a tipy

- **Chyby cesty k souboru** – Ujistěte se, že `myDir` ukazuje na existující zapisovatelnou složku.  
- **Upozornění na licenci** – Spuštění zkušební verze bez licence přidá vodoznak do exportovaných souborů.  
- **Kompatibilita verzí** – Použijte nejnovější Aspose.3D JAR, abyste se vyhnuli zastaralým metodám.

## Často kladené otázky

### Q1: Mohu používat Aspose.3D pro Java s jinými programovacími jazyky?

A1: Aspose.3D primárně podporuje Javu, ale jsou k dispozici verze pro jiné jazyky, jako .NET.

### Q2: Je Aspose.3D vhodný pro složité úkoly 3D modelování?

A2: Rozhodně! Aspose.3D poskytuje komplexní sadu funkcí, což ho činí vhodným jak pro jednoduché, tak pro složité úkoly 3D modelování.

### Q3: Kde mohu najít další pomoc a podporu?

A3: Navštivte [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) pro komunitní podporu a diskuse.

### Q4: Mohu vyzkoušet Aspose.3D před nákupem?

A4: Ano, můžete vyzkoušet [free trial](https://releases.aspose.com/) před rozhodnutím o koupi.

### Q5: Jak získám dočasnou licenci pro Aspose.3D?

A5: Dočasnou licenci můžete získat na [temporary license](https://purchase.aspose.com/temporary-license/) pro Aspose.3D na webových stránkách.

## Často kladené otázky

**Q: Podporuje Aspose.3D mapování textur na primitivy?**  
A: Ano, můžete přiřadit materiály a textury jakémukoli primitivu, včetně krabice vytvořené v tomto tutoriálu.

**Q: Mohu exportovat scénu do binárního souboru FBX?**  
A: Rozhodně. Nahraďte `FileFormat.FBX7500ASCII` za `FileFormat.FBX7500Binary` pro získání binárního FBX.

**Q: Existuje způsob, jak animovat krabici po vytvoření?**  
A: Můžete přidat animace klíčových snímků k uzlům pomocí třídy `AnimationController` poskytované Aspose.3D.

**Q: Jak načtu existující soubor FBX pro další úpravy?**  
A: Použijte `Scene scene = new Scene("input.fbx");` k načtení a manipulaci s existujícími soubory.

**Q: Jaká je minimální požadovaná verze Javy?**  
A: Aspose.3D for Java funguje s Java 8 a novějšími.

## Závěr

Právě jste se naučili, jak **create 3D box Java** modely, přidat další primitivy a **export scene FBX** pomocí Aspose.3D. Klidně experimentujte s dalšími tvary, aplikujte materiály nebo prozkoumejte rozsáhlé API pro tvorbu bohatších 3‑D aplikací.

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}
{{< blocks/products/products-backtop-button >}}

---

**Last Updated:** 2025-12-27  
**Tested With:** Aspose.3D for Java 24.12 (latest)  
**Author:** Aspose  

---