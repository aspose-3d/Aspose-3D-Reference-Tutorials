---
date: 2026-04-29
description: Naučte se, jak zmenšit velikost 3D modelu vytvořením sférické sítě v
  Javě a kompresí pomocí Google Draco s využitím Aspose.3D – nezbytné pro export Aspose
  3D.
keywords:
- reduce 3d model size
- aspose 3d export
- compress 3d mesh java
linktitle: Jak vytvořit sférovou síť v Javě – Komprimovat 3D sítě pomocí Google Draco
second_title: Aspose.3D Java API
title: 'Snižte velikost 3D modelu: Vytvořte sférickou síť v Javě s Dracem'
url: /cs/java/3d-mesh-data/compress-meshes-google-draco/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Zmenšení velikosti 3D modelu: Vytvoření sférické sítě v Javě s Dracem

## Úvod

Pokud hledáte rychlý způsob, jak **zmenšit velikost 3D modelu** a přitom zachovat vysoce kvalitní geometrii, jste na správném místě. V tomto tutoriálu vás provedeme generováním sférické sítě pomocí **Aspose.3D for Java** a následnou kompresí této sítě pomocí **Google Draco**. Na konci budete mít připravený soubor `.drc`, který je dramaticky menší než originál, což je ideální pro webové prohlížeče, mobilní hry nebo jakoukoli Java aplikaci s omezenou šířkou pásma.

## Rychlé odpovědi
- **Co tento tutoriál pokrývá?** Vytvoření sférické sítě v Javě a komprese pomocí Google Draco přes Aspose.3D.  
- **Primární knihovna?** Aspose.3D for Java (používá se jak pro tvorbu sítě, tak pro export do Draco).  
- **Typický čas implementace?** Přibližně 10‑15 minut pro základní kouli.  
- **Klíčová podmínka?** Vývojové prostředí Java s JAR soubory Aspose.3D na classpathu.  
- **Výsledek?** Soubor `.drc`, který **zmenšuje velikost 3D modelu** až o 90 % ve srovnání s nekomprimovanou sítí.

## Co znamená „zmenšení velikosti 3D modelu“ v kontextu 3D vývoje?

Zmenšení velikosti 3D modelu znamená snížení objemu geometrických dat, která je potřeba přenést nebo uložit, aniž by došlo k výraznému zhoršení vizuální kvality. Draco toho dosahuje kódováním pozic vrcholů, normál a dalších atributů do vysoce kompaktního binárního formátu. Ve spojení s Aspose.3D zůstává celý workflow uvnitř Javy, takže nemusíte manipulovat s nativními binárními soubory.

## Proč použít kompresi sítě Google Draco s Aspose.3D?

- **Obrovské zmenšení velikosti:** Draco může snížit data sítě až o 90 % ve srovnání s formáty jako OBJ nebo STL.  
- **Rychlé dekódování za běhu:** Enginy jako Unity, Unreal a three.js dekódují Draco nativně, což vede k rychlejším načítacím časům.  
- **Bezproblémová integrace s Javou:** Aspose.3D abstrahuje nativní knihovnu Draco, takže můžete zůstat v ekosystému Java.  
- **Jednoduchý export z Aspose 3D:** Stejné API, které používáte k tvorbě geometrie, také zvládá export, což zjednodušuje celý pipeline.

## Požadavky

- **Java Development Kit (JDK)** – verze 8 nebo novější.  
- **Aspose.3D for Java** – stáhněte nejnovější JAR soubory z oficiální stránky [zde](https://releases.aspose.com/3d/java/).  
- **Základní znalost Google Draco** – budete používat obal Aspose.3D, takže není potřeba nastavení nativního Draco.

## Import balíčků

```java
import com.aspose.threed.DracoCompressionLevel;
import com.aspose.threed.DracoSaveOptions;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Sphere;


import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
```

## Průvodce krok za krokem

### Krok 1: Nastavení projektu

Vytvořte nový Java projekt (libovolné IDE funguje) a přidejte všechny JAR soubory Aspose.3D do classpathu. Pro přehlednost uložte své zdrojové soubory do balíčku například `com.example.draco`.

### Krok 2: Jak vytvořit sférickou síť v Javě

```java
// ExStart:Encode3DMeshinGoogleDraco
// The path to the documents directory.
String MyDir = "Your Document Directory";

// Create a sphere
Sphere sphere = new Sphere();
```

> **Pro tip:** Třída `Sphere` generuje triangulovanou síť s výchozím poloměrem 1.0. Můžete předat vlastní poloměr, tessellaci nebo materiálové parametry, pokud potřebujete jinou úroveň detailu před kompresí.

### Krok 3: Jak komprimovat síť pomocí Google Draco

```java
// Encode the sphere to Google Draco raw data using optimal compression level.
DracoSaveOptions opt = new DracoSaveOptions();
opt.setCompressionLevel(DracoCompressionLevel.OPTIMAL);
byte[] b = FileFormat.DRACO.encode(sphere.toMesh(), opt);
```

Nastavení úrovně komprese na `OPTIMAL` poskytuje největší zmenšení velikosti při zachování vizuální věrnosti, což přímo pomáhá **zmenšit velikost 3D modelu**.

### Krok 4: Uložení komprimované sítě

```java
// Save the raw bytes to file
Files.write(Paths.get(MyDir, "SphereMeshtoDRC_Out.drc"), b);
// ExEnd:Encode3DMeshinGoogleDraco
```

Výsledný soubor `SphereMeshtoDRC_Out.drc` lze streamovat klientům, uložit do CDN nebo načíst přímo jakýmkoli enginem podporujícím Draco.

## Běžné případy použití

| Scénář | Proč zmenšit velikost modelu? | Jak tento návod pomáhá |
|----------|-------------------------------|------------------------|
| Webové konfigurátory produktů | Rychlejší načítání stránek při pomalých připojeních | Draco‑komprimované `.drc` soubory se načtou během sekund |
| Mobilní AR/VR aplikace | Nižší paměťová náročnost na zařízeních | Menší sítě udržují aplikaci responzivní |
| Scény renderované v cloudu | Snížení nákladů na šířku pásma | Export jedním kliknutím z Aspose.3D do Draco |

## Běžné problémy a řešení

| Problém | Důvod | Řešení |
|---------|-------|--------|
| **`NoClassDefFoundError` for Draco classes** | Aspose.3D JARs not on classpath | Verify that *all* Aspose.3D JAR files are included and that the version matches the documentation. |
| **Output file is empty** | `MyDir` points to a non‑existent folder | Create the directory programmatically (`Files.createDirectories(Paths.get(MyDir))`) before writing the file. |
| **Compressed mesh looks distorted** | Using a low compression level or insufficient tessellation | Switch to `DracoCompressionLevel.OPTIMAL` and increase the sphere’s tessellation (e.g., `new Sphere(1.0, 64, 64)`). |

## Často kladené otázky

**Q: Je Aspose.3D kompatibilní s různými 3D formáty souborů?**  
A: Ano, Aspose.3D podporuje OBJ, FBX, STL, GLTF a mnoho dalších, což z něj činí univerzální volbu pro **Aspose 3D export** pipeline.

**Q: Mohu použít Google Draco pro kompresi v jiných programovacích jazycích?**  
A: Rozhodně. Draco nabízí nativní knihovny pro C++, Python a JavaScript. Tento tutoriál se zaměřuje na Javu, ale koncepty platí napříč jazyky.

**Q: Kde najdu další dokumentaci k Aspose.3D?**  
A: Navštivte [Aspose.3D Java documentation](https://reference.aspose.com/3d/java/) pro kompletní API reference a další příklady.

**Q: Jak získám dočasnou licenci pro Aspose.3D?**  
A: Prozkoumejte možnosti dočasného licencování [zde](https://purchase.aspose.com/temporary-license/).

**Q: Existuje komunitní fórum pro podporu Aspose.3D?**  
A: Ano, připojte se k diskusi na [Aspose.3D Forum](https://forum.aspose.com/c/3d/18).

## Závěr

V tomto průvodci jsme ukázali, jak **zmenšit velikost 3D modelu** vytvořením sférické sítě v Javě a následnou kompresí pomocí Google Draco přes Aspose.3D. Dodržením těchto stručných kroků můžete dramaticky zmenšit soubory sítí, zlepšit načítací časy a udržet své Java‑based 3D aplikace responzivní a šetrné k šířce pásma.

---

**Poslední aktualizace:** 2026-04-29  
**Testováno s:** Aspose.3D for Java 24.12 (latest)  
**Autor:** Aspose

---

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}