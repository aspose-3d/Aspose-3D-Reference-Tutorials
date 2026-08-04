---
date: 2026-04-12
description: Naučte se, jak vytvořit scény s kostkou a uložit scénu jako FBX pomocí
  Aspose.3D pro .NET – krok‑za‑krokem průvodce, předpoklady a ukázky kódu.
keywords:
- how to create cube
- how to export fbx
- add mesh to node
- export scene as fbx
- save scene as fbx
linktitle: Vytváření scén kostky
second_title: Aspose.3D .NET API
title: Jak vytvořit scény s kostkami pomocí Aspose.3D pro .NET
url: /cs/net/geometry-and-hierarchy/create-cube-scenes/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Jak vytvořit scény s krychlí pomocí Aspose.3D pro .NET

## Úvod

Připraveni oživit jednoduchou 3‑D krychli? V tomto tutoriálu se naučíte **jak vytvořit scény s krychlí** pomocí Aspose.3D pro .NET, exportovat model jako soubor FBX a okamžitě vidět výsledek. Ať už prototypujete herní asset nebo vizualizujete data, níže uvedené kroky vám poskytnou pevný základ, který můžete rozšířit o textury, osvětlení nebo animaci.

## Rychlé odpovědi
- **Co tutoriál pokrývá?** Vytvoření mesh krychle, přidání mesh do uzlu a uložení scény jako souboru FBX.  
- **Která knihovna je vyžadována?** Aspose.3D pro .NET (k dispozici bezplatná zkušební verze).  
- **Potřebuji licenci pro spuštění ukázky?** Dočasná nebo zkušební licence stačí pro vývoj a testování.  
- **Jaké IDE mohu použít?** Jakékoli IDE kompatibilní s .NET (Visual Studio, Rider, VS Code).  
- **Jak dlouho to trvá?** Přibližně 10 minut na napsání, zkompilování a spuštění kódu.

## Jak vytvořit scény s krychlí pomocí Aspose.3D

Scéna s krychlí je „Hello World“ 3‑D grafiky. Umožňuje vám ověřit, že váš pipeline – od vytvoření mesh až po **export scény jako FBX** – funguje správně. Níže projdeme každý krok, vysvětlíme „proč“ a ukážeme vám přesně, kam umístit kód.

## Co je 3D scéna s krychlí?

3D scéna s krychlí je minimální trojrozměrný model sestávající z jedné geometrie krychle umístěné v grafu scény. Slouží jako „Hello World“ 3D grafiky a umožňuje vám ověřit, že váš pipeline – od vytvoření mesh až po export souboru – funguje správně.

## Proč vytvářet scény s krychlí pomocí Aspose.3D?

* **Podpora více formátů:** Export do FBX, STL, OBJ a mnoha dalších formátů bez dalších konvertorů.  
* **Čisté .NET API:** Žádné nativní závislosti, ideální pro vývojáře v C#.  
* **Bohatá sada funkcí:** Vestavěné tvůrce mesh, správa materiálů a hierarchie scény.  
* **Rychlé prototypování:** Napište několik řádků kódu a získáte připravený 3D soubor.  

## Požadavky

1. **Aspose.3D pro .NET knihovna** – stáhněte a nainstalujte z [Aspose dokumentace](https://reference.aspose.com/3d/net/).  
2. **Vývojové prostředí** – Visual Studio 2022, Rider nebo jakýkoli editor podporující .NET 6+.  
3. **Základní znalost C#** – měli byste být obeznámeni s třídami, objekty a konzolovými aplikacemi.

## Importovat jmenné prostory

Nejprve přidejte požadované `using` direktivy, aby kompilátor věděl, kde se nacházejí typy Aspose.3D.

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
```

## Průvodce krok za krokem

### Krok 1: Inicializovat scénu

Vytvořte prázdný objekt `Scene`, který bude obsahovat všechny uzly, mesh, světla a kamery.

```csharp
// ExStart:CreateCubeScene
// Initialize scene object
Scene scene = new Scene();
```

### Krok 2: Vytvořit uzel pro krychli

`Node` funguje jako kontejner pro geometrii. Dejte mu přátelské jméno, abyste jej později v hierarchii snadno našli.

```csharp
// Initialize Node class object
Node cubeNode = new Node("cube");
```

### Krok 3: Vytvořit mesh

Aspose.3D poskytuje pomocníka nazvaného `Common`, který může vygenerovat mesh krychle pomocí polygonového builderu. To vám ušetří ruční definování vrcholů a ploch.

```csharp
// Call Common class create mesh using polygon builder method to set mesh instance 
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
```

### Krok 4: Přidat mesh do uzlu

Přiřaďte právě vytvořený mesh k vlastnosti `Entity` uzlu. Tím propojí geometrii s grafem scény.

```csharp
// Point node to the Mesh geometry
cubeNode.Entity = mesh;
```

### Krok 5: Přidat uzel do scény

Vložte uzel krychle do kořene scény, aby se stal součástí finálního výstupu.

```csharp
// Add Node to a scene
scene.RootNode.ChildNodes.Add(cubeNode);
```

### Krok 6: Jak exportovat FBX (uložit scénu jako FBX)

Zvolte výstupní cestu a exportujte scénu. Zde používáme formát FBX 7400 ASCII, který je široce podporován 3D editory.

```csharp
// The path to the documents directory.
var output = "Your Output Directory" + "CubeScene.fbx";

// Save 3D scene in the supported file formats
scene.Save(output, FileFormat.FBX7400ASCII);
```

### Krok 7: Zobrazit zprávu o úspěchu

Poskytněte uživateli jasné potvrzení, že soubor byl úspěšně zapsán.

```csharp
Console.WriteLine("\nCube Scene created successfully.\nFile saved at " + output);
```

## Časté problémy a řešení

| Problém | Proč se to stane | Řešení |
|-------|----------------|-----|
| **File not found** chyba při spuštění `scene.Save` | Výstupní adresář neexistuje nebo nemáte oprávnění k zápisu. | Nejprve vytvořte adresář (`Directory.CreateDirectory`) nebo použijte absolutní cestu, která vám patří. |
| **Empty file** po exportu | Mesh nebyl připojen k uzlu nebo uzel nebyl přidán do scény. | Ujistěte se, že jsou provedeny `cubeNode.Entity = mesh;` a `scene.RootNode.ChildNodes.Add(cubeNode);`. |
| **Incorrect format** při otevírání ve vieweru | Použití nesprávné hodnoty výčtu `FileFormat`. | Použijte `FileFormat.FBX7400ASCII` pro ASCII FBX nebo `FileFormat.FBX7400Binary` pro binární. |

## Často kladené otázky

**Q: Je Aspose.3D kompatibilní s různými 3D formáty souborů?**  
A: Ano, Aspose.3D podporuje FBX, STL, OBJ, GLTF a mnoho dalších, což vám umožní **uložit scénu jako FBX** nebo jiné formáty jedním řádkem kódu.

**Q: Mohu přizpůsobit vzhled krychle?**  
A: Rozhodně. Můžete přiřadit `Material` k mesh, změnit jeho barvu nebo aplikovat texturu pomocí třídy `Material`.

**Q: Kde mohu najít další podporu a zdroje?**  
A: Navštivte [Aspose.3D fórum](https://forum.aspose.com/c/3d/18) pro komunitní pomoc a diskuse.

**Q: Je k dispozici bezplatná zkušební verze?**  
A: Ano, můžete si vyzkoušet bezplatnou verzi [zde](https://releases.aspose.com/).

**Q: Jak mohu získat dočasnou licenci pro Aspose.3D?**  
A: Získejte dočasnou licenci [zde](https://purchase.aspose.com/temporary-license/).

## Závěr

V tomto průvodci jsme ukázali **jak vytvořit scény s krychlí** krok za krokem, od inicializace `Scene` po **export scény jako FBX**. Nyní máte pevný základ pro experimentování s komplexnějšími geometriemi, přidávání textur, světel a dokonce animaci vašich modelů. Pokračujte v objevování Aspose.3D API – možnosti jsou prakticky neomezené.

---

**Last Updated:** 2026-04-12  
**Tested With:** Aspose.3D for .NET 24.11 (latest at time of writing)  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}