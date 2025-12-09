---
date: 2025-12-09
description: Naučte se, jak provádět UV mapování 3D modelů přidáním UV souřadnic do
  sítě a mapovat textury v Javě pomocí Aspose.3D. Postupujte podle tohoto krok‑za‑krokem
  průvodce a aplikujte textury na své 3D objekty.
language: cs
linktitle: 'UV Mapping 3D Models: UV Coordinates in Java with Aspose.3D'
second_title: Aspose.3D Java API
title: 'UV mapování 3D modelů: UV souřadnice v Javě s Aspose.3D'
url: /java/geometry/apply-uv-coordinates-to-3d-objects/
weight: 18
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# UV mapování 3D modelů: UV souřadnice v Javě s Aspose.3D

## Introduction

Vítejte! V tomto komplexním tutoriálu se naučíte **uv mapping 3d models** pomocí Javy a výkonné knihovny Aspose.3D. UV mapování je technika, která vám umožní **add uvs to mesh**, takže textury se dokonale zarovnají na vašich 3‑D objektech. Na konci tohoto průvodce budete schopni mapovat textury v Java stylu a vidět, jak vaše modely ožívají.

## Quick Answers
- **What does UV mapping do?** Přiřazuje 2‑D texturové souřadnice (U & V) každému vrcholu 3‑D meshu.  
- **Which library is used?** Aspose.3D for Java.  
- **How many lines of code?** Přibližně 30 řádků, rozdělených do čtyř bloků kódu.  
- **Do I need a license?** Bezplatná zkušební verze funguje pro vývoj; pro produkci je vyžadována komerční licence.  
- **Can I reuse this for other shapes?** Rozhodně – stejný přístup funguje pro jakýkoli mesh.

## What is UV Mapping 3D Models?

UV mapování 3D modelů je proces projekce 2‑D obrázku (textury) na 3‑D povrch. Každý vrchol získá dvojici souřadnic – U (horizontální) a V (vertikální) – které rendereru říkají, odkud má texturu vzorkovat. Tento krok je nezbytný pro realistické renderování, herní assety a AR/VR zážitky.

## Why Use Aspose.3D for UV Mapping?

- **Cross‑platform Java API** – funguje na Windows, Linuxu a macOS.  
- **High‑performance geometry engine** – snadno zpracovává velké meshe.  
- **Built‑in texture handling** – podporuje difúzní, spekulární, normální mapy atd.  
- **Clear, fluent API** – usnadňuje **add uvs to mesh** bez nízkoúrovňového parsování souborů.

## Prerequisites

- **Java Development Kit (JDK 8 nebo vyšší)** nainstalovaný a nakonfigurovaný.  
- **Aspose.3D for Java** – stáhněte nejnovější JAR z oficiální stránky [here](https://releases.aspose.com/3d/java/).  
- **Základní znalosti 3‑D** – pochopení vrcholů, polygonů a konceptů mapování textur.

## Import Packages

Nejprve musíme importovat třídy Aspose.3D, které nám umožní vytvořit geometrii a přiřadit UV data.

### Step 1: Import Aspose.3D Packages

```java
import com.aspose.threed.*;

import java.util.Arrays;
```

Nyní, když jsou importy připravené, přejdeme k vytvoření UV dat pro jednoduchý krychle.

## Setup UV Coordinates on a 3D Object

Níže projdeme přesné kroky k vygenerování UV souřadnic a jejich přiřazení k mesh.

### Step 2: Create UVs and Indices

```java
// ExStart:SetupUVOnCube
// UVs
Vector4[] uvs = new Vector4[]
{
    new Vector4( 0.0, 1.0,0.0, 1.0),
    new Vector4( 1.0, 0.0,0.0, 1.0),
    new Vector4( 0.0, 0.0,0.0, 1.0),
    new Vector4( 1.0, 1.0,0.0, 1.0)
};

// Indices of the uvs per each polygon
int[] uvsId = new int[]
{
    0,1,3,2,2,3,5,4,4,5,7,6,6,7,9,8,1,10,11,3,12,0,2,13
};
// ExEnd:SetupUVOnCube
```

*Vysvětlení*:  
- **uvs** obsahuje skutečné vektory UV souřadnic (U, V, W, Q).  
- **uvsId** mapuje každý vrchol polygonu na položku v poli `uvs`, což umožňuje pozdější krok **add uvs to mesh**.

### Step 3: Create Mesh and UVset

```java
// Call Common class create mesh using polygon builder method to set mesh instance
Mesh mesh = Common.createMeshUsingPolygonBuilder();

// Create UVset
VertexElementUV elementUV = mesh.createElementUV(TextureMapping.DIFFUSE, MappingMode.POLYGON_VERTEX, ReferenceMode.INDEX_TO_DIRECT);
// Copy the data to the UV vertex element
elementUV.setData(uvs);
elementUV.setIndices(uvsId);
```

*Vysvětlení*:  
- `Common.createMeshUsingPolygonBuilder()` vytvoří mesh ve tvaru krychle.  
- `createElementUV` vytvoří UV element pro **diffuse** texturový kanál.  
- `setData` a `setIndices` skutečně **add uvs to mesh**, propojují UV vektory s polygony krychle.

### Step 4: Print Confirmation

```java
System.out.println("\nUVs have been set up successfully on the cube.");
```

Pokud spustíte program, měli byste v konzoli vidět potvrzovací zprávu, která naznačuje, že krok UV mapování byl dokončen bez chyb.

## Common Issues and Solutions

| Problém | Proč k tomu dochází | Řešení |
|-------|----------------|-----|
| **UVs appear stretched** | Nesprávné pořadí v `uvsId` nebo nesoulad s orientací polygonů. | Ověřte, že pole indexů odpovídá pořadí polygonů mesh. |
| **Texture not visible** | UV sada je přiřazena ke špatnému texturovému kanálu. | Použijte `TextureMapping.DIFFUSE` pro hlavní texturu; ostatní kanály (NORMAL, SPECULAR) vyžadují samostatné UV sady. |
| **Runtime `NullPointerException`** | `Common.createMeshUsingPolygonBuilder()` vrátil `null`. | Ujistěte se, že pomocná třída je správně importována a metoda je implementována. |

## Frequently Asked Questions

**Q: Můžu použít UV souřadnice na složité 3D modely?**  
A: Ano. Stejný postup funguje pro jakýkoli mesh – stačí poskytnout větší UV pole a odpovídající seznam indexů.

**Q: Kde najdu další zdroje a podporu pro Aspose.3D?**  
A: Navštivte [Aspose.3D documentation](https://reference.aspose.com/3d/java/) pro podrobné reference API a [Aspose.3D forum](https://forum.aspose.com/c/3d/18) pro komunitní pomoc.

**Q: Je k dispozici bezplatná zkušební verze pro Aspose.3D?**  
A: Rozhodně. Můžete si stáhnout plně funkční zkušební verzi ze [Aspose.3D releases page](https://releases.aspose.com/).

**Q: Jak mohu získat dočasnou licenci pro Aspose.3D?**  
A: Dočasné licence jsou k dispozici [zde](https://purchase.aspose.com/temporary-license/).

**Q: Kde mohu zakoupit Aspose.3D?**  
A: Možnosti nákupu jsou uvedeny na oficiální [Aspose.3D buying page](https://purchase.aspose.com/buy).

---

**Poslední aktualizace:** 2025-12-09  
**Testováno s:** Aspose.3D 24.12 for Java  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}