---
date: 2026-01-20
description: Naučte se, jak vytvořit 3D scény s kostkou a uložit scénu jako FBX pomocí
  Aspose.3D pro .NET – krok za krokem průvodce, předpoklady a ukázky kódu.
linktitle: Creating Cube Scenes
second_title: Aspose.3D .NET API
title: Jak vytvořit 3D kostkové scény pomocí Aspose.3D pro .NET
url: /cs/net/geometry-and-hierarchy/create-cube-scenes/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Jak vytvořit 3D kostkové scény pomocí Aspose.3D pro .NET

## Úvod

Jste připý  cube** scény pomocí Aspose.3D pro .NET, exportovat model jako soubor FBX a okamžitě vidět výsledek. Ať už prototypujete herní asset nebo vizualizujete data, níže uvedené kroky vám poskytnou pevný základ, který můžete rozšířit o textury, osvětlení nebo animaci.

## Rychlé odpovědi
- **Co tutoriál pokrývá?** Vytvoření mesh kostky, přidání do scény a uložení scény jako soubor FBX.  
- **Která knihovna je vyžadována?** Aspose.3D pro .NET (k dispozici bezplatná zkušební verze).  
- **Potřebuji licenci pro spuštění vzorku?** Dočasná nebo zkušební licence stačí pro vývoj a testování.  
- **Jaké IDE mohu použít?** Jakékoli IDE kompatibilní s .NET (Visual Studio, Rider, VS Code).  
- **Jak dlouho to trvá?** Přibližně 10 minut na napsání, zkompilování a spuštění kódu.

## Co je to 3D kostková scéna?

3D kostková scéna je minimální trojrozměrný model sestávající z jedné geometrie kostky umístěné uvnitř grafu scény. Slouží jako „Hello World“ 3ěřit, že váš pipeline – od tvorby mesh po export souboru – funguje správně.

## Proč vytvářet 3d cube scény s Aspose.3D?

* **Podporaů bez dalších konvertorů.  
* **Čisté .NET API:**ování:**dků kódu a získáte připravený 3D soubor.

## Předpoklady

1. **Aspose.3D pro .NET Library** – stáhněte a nainstalujte z [Aspose documentation](https://reference.aspose.com/3d/net/).  
2. **Vývojové prostředí** – Visual Studio 2022, Rider nebo jakýkoli editor podporující .NET 6+.  
3. **Základní znalosti C#** – měli byste být obeznámeni s třídami, objekty a konzolovými aplikacemi.

## Import Namespaces

Nejprve přidejte požadované `using` direktivy, aby kompilátor věděl, kde se nacházejí typy Aspose.3D.

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
```

## Průvodce krok za krokem

### Krok 1: Inicializace scény

Vytvořte prázdný objekt `Scene`, který bude obsahovat všechny uzly, mesh, světla a kamery.

```csharp
// ExStart:CreateCubeScene
// Initialize scene object
Scene scene = new Scene();
```

### Krok 2: Vytvoření uzlu pro kostku

`Node` funguje jako kontejner pro geometrii. Dejte mu přátelské jméno, abyste jej později mohli snadno najít v hierarchii.

```csharp
// Initialize Node class object
Node cubeNode = new Node("cube");
```

### Krok 3: Sestavení mesh

Aspose.3D poskytuje pomocníka `Common`, který dokáže vygenerovat mesh kostky pomocí polygonového builderu. Tím se vyhnete ručnímu definování vrcholů a ploch.

```csharp
// Call Common class create mesh using polygon builder method to set mesh instance 
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
```

### Krok 4: Připojení uzlu k mesh geometrii

Přiřaďte právě vytvořený mesh k vlastnosti `Entity` uzlu. Tím spojíte geometrii s grafem scény.

```csharp
// Point node to the Mesh geometry
cubeNode.Entity = mesh;
```

### Krok 5: Přidání uzlu do scény

Vložte uzel kostky do kořenového uzlu scény, aby se stal součástí finálního výstupu.

```csharp
// Add Node to a scene
scene.RootNode.ChildNodes.Add(cubeNode);
```

### Krok 6: Uložení 3D scény (save scene as fbx)

Zvolte výstupní cestu a exportujte scénu. Zde používáme formát FBX 7400 ASCII, který je široce podporován 3D editory.

```csharp
// The path to the documents directory.
var output = "Your Output Directory" + "CubeScene.fbx";

// Save 3D scene in the supported file formats
scene.Save(output, FileFormat.FBX7400ASCII);
```

### Krok 7: Zobrazení úspěšné zprávy

Dejte uživateli jasné potvrzení, že soubor byl úspěšně zapsán.

```csharp
Console.WriteLine("\nCube Scene created successfully.\nFile saved at " + output);
```

## Časté problémy a řešení

| Problém | Proč se vyskytuje | Řešení |
|-------|----------------|-----|
| **File not found** chyba při volání `scene.Save` | Výstupní adresář neexistuje nebo nemáte oprávnění k zápisu. | Nejprve vytvořte adresář (`Directory.CreateDirectory`) nebo použijte absolutní cestu, ke které máte přístup. |
| **Empty file** po exportu | Mesh nebyl připojen k uzlu nebo uzel nebyl přidán do scény. | Ujistěte se, že jsou provedeny `cubeNode.Entity = mesh;` a `scene.RootNode.ChildNodes.Add(cubeNode);`. |
| **Incorrect format** při otevírání ve vieweru | Použitá špatná hodnota enumu `FileFormat`. | Použijte `FileFormat.FBX7400ASCII` pro ASCII FBX nebo `FileFormat.FBX7400Binary` pro binární. |

## Často kladené otázky

**Q: Je Aspose.3D kompatibilní s různými 3D formáty?**  
A: Ano, Aspose.3D podporuje FBX, mnoho dalších, což k** další podporu a zdroje?**  
A: Navštivte [Aspose.3D forum](https://forum.aspose.com/c/3d/18) pro komunitní pomoc a diskuse.

**Q: Je k dispozici bezplatná zkušební verze?**  
A: Ano, bezplatnou zkušební verzi můžete vyzkoušet [zde](https://releases.aspose.com/).

**Q: Jak získatáte [zde](https://purchase.aspose.com/. PokDováno s:** Aspose.3D pro .NET 24.11 (nejnovější v době psaní)  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}