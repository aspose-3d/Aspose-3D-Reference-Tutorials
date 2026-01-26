---
date: 2026-01-22
description: Naučte se, jak vytvořit podřízený uzel a přidat transformační uzel pomocí
  Eulerových úhlů s Aspose.3D pro .NET. Postupujte podle našeho krok‑za‑krokem průvodce
  a dosáhněte úžasných výsledků.
linktitle: Create Child Node and Transform by Euler Angles
second_title: Aspose.3D .NET API
title: Vytvořit podřízený uzel a transformovat pomocí Eulerových úhlů
url: /cs/net/geometry-and-hierarchy/transformation-node-euler-angles/
weight: 19
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Transformace uzlu pomocí Eulerových úhlů

## Úvod

Vítejte v tomto komplexním tutoriálu o **jak vytvořit podřízený uzel** a transformovat uzly pomocí Eulerových úhlů ve 3D scénách pomocí Aspose.3D pro .NET. V tomto průvodci prozkoumáme, proč je důležité přidat transformační uzel, projdeme jednotlivé kroky a ukážeme vám, jak **uložit scénu jako FBX** pro použití v jiných nástrojích.

## Rychlé odpovědi
- **Co znamená „vytvořit podřízený uzel“?** Vytvoří nový uzel pod existujícím rodičem v grafu scény.  
- **Do jakého formátu mohu exportovat?** Použijte `scene.Save` k **uložení scény jako FBX** (nebo jiných podporovaných formátů).  
- **Potřebuji licenci?** Ano, pro produkční použití je vyžadována platná licence Aspose.3D.  
- **Mohu kombinovat více transformací?** Rozhodně – můžete na stejném uzlu vrstvit rotace, škálování a translaci.  
- **Jaké verze .NET jsou podporovány?** .NET Framework 4.5+, .NET Core 3.1+, .NET 5/6/7.

## Co je „vytvořit podřízený uzel“?
Vytvoření podřízeného uzlu znamená přidání nového objektu `Node` do hierarchie existující scény. Tento podřízený uzel dědí transformace od svého rodiče, což vám umožní stavět složité struktury jako robotické paže, sestavy vozidel nebo UI překryvy.

## Proč přidat transformační uzel?
Aplikace Eulerových úhlů nebo jiných transformací přímo na uzel vám poskytuje přesnou kontrolu nad orientací, pozicí a měřítkem. Je to nejužitečnější způsob, jak animovat nebo přemístit objekty, aniž byste měnili podkladová data mesh.

## Předpoklady

- Aspose.3D pro .NET knihovna: Ujistěte se, že máte nainstalovanou knihovnu Aspose.3D. Můžete si ji stáhnout [zde](https://releases.aspose.com/3d/net/).
- Vývojové prostředí: Nastavte si preferované .NET vývojové prostředí, například Visual Studio.

## Import Namespaces

Začněte importováním potřebných jmenných prostorů pro přístup k funkcionalitě poskytované Aspose.3D pro .NET:

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

Nyní rozdělíme příklad do několika kroků pro lepší pochopení.

## Jak vytvořit podřízený uzel

### Krok 1: Inicializace objektu Scene

```csharp
// ExStart:AddTransformationToNodeByEulerAngles
// Initialize scene object
Scene scene = new Scene();
```

Začněte vytvořením nové 3D scény pomocí třídy `Scene`.

### Krok 2: Vytvoření Mesh pomocí primitivní krabice

```csharp
// Call Common class create mesh using polygon builder method to set mesh instance 
Mesh mesh = (new Box()).ToMesh();
```

Zavolejte metodu (v tomto případě `CreateMeshUsingPolygonBuilder` z vlastní třídy `Common`) pro vygenerování mesh pro 3D objekt.

### Krok 3: Vytvoření kontejnerového uzlu pro mesh

```csharp
// Point node to the Mesh geometry
Node cubeNode = scene.RootNode.CreateChildNode(mesh);
```

Vytvořte uzel ve scéně pomocí třídy `Node`. Tento uzel bude sloužit jako kontejner pro náš 3D objekt.

### Krok 4: Nastavení Eulerových úhlů a translace (přidání transformačního uzlu)

```csharp
// Euler angles
cubeNode.Transform.EulerAngles = new Vector3(0.3, 0.1, -0.5);            
// Set translation
cubeNode.Transform.Translation = new Vector3(0, 0, 20);
```

Definujte Eulerovy úhly a translaci pro uzel, aby byl prostoru. Zde **přidáváme data transformačního uzlu**.

### Krok 5: Uložení 3D scény (uložit scénu jako FBX)

```csharp
// The path to the documents directory.
var output = "TransformationToNode.fbx";

// Save 3D scene in the supported file formats
scene.Save(output);
// ExEnd:AddTransformationToNodeByEulerAngles
Console.WriteLine("\nTransformation added successfully to node.\nFile saved at " + output);
```

Zadejte výstupní adresář a **uložte scénu jako FBX** (nebo jakýkoli jiný podporné pořadí rot přelo `Translation = new Vector3(0,0,20)` ho posune dopředu).
- **Soubor se neukládá:** Ověřte oprávnění pro zápis do cílové otázky

**Q: Je Aspose.3D kompatibilní s jinými 3D modelovacími nástroji?**  
A: Aspose.3D podporuje různé 3D formáty souborů, čímž zvyšuje kompatibilitu s populárními modelovacími nástroji.

**Q: Mohu na jeden uzel aplikovat více transformací?**  
A: Ano, můžete kombinovat a aplikovat více transformací pro dosažení složitých efektů.

**Q: Kde najdu další dokumentaci k Aspose.3D?**  
A: Viz [dokumentace](https://reference.aspose.com/3d/net/) pro podrobné informace a příklady.

**Q: Potřebuji licenci pro používání Aspose.3D pro .NET?**  
A: Ano, licenci můžete získat [zde](https://purchase.aspose.com/buy) nebo vyzkoušet [bezplatnou verzi](https://releases.aspose.com/).

**Q: Potřebujete pomoc nebo máte konkrétní otázky?**  
A: Navštivte [forum Aspose.3D](https://forum.aspose.com/c/3d/18) pro podporu komunity.

## Závěr

Gratulujeme! Úspěšně jste se naučili, jak **vytvořit podřízený uzel** a **přidat transformační uzel** pomocí Eulerových úhlů a následně **uložit scénu jako FBX** s Aspose.3D pro .NET. Tato výkonná knihovna otevírá dveře k neomezeným možnostem ve vývoji 3D grafiky.

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Poslední aktualizace:** 2026-01-22  
**Testováno s:** Aspose.3D 24.12 pro .NET  
**Autor:** Asp