---
date: 2026-01-12
description: Naučte se, jak definovat síť a exportovat 3D síť do vlastního binárního
  formátu pomocí Aspose.3D pro .NET. Efektivně uložte 3D síť.
linktitle: How to Define Mesh and Save 3D Meshes in Binary Format
second_title: Aspose.3D .NET API
title: Jak definovat síť a uložit 3D sítě v binárním formátu
url: /cs/net/3d-scene/save-3d-meshes-binary-format/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Jak definovat síť a uložit 3D sítě v binárním formátu

## Úvod

Vítejte ve světě Aspose.3D pro .NET! V tomto tutoriálu se naučíte **jak definovat síť** a poté **uložit data 3D sítě** do vlastního binárního formátu. Ať už potřebujete **exportovat 3D síť** pro herní engine, simulaci nebo proprietární pipeline, níže uvedené kroky vás provedou celým procesem pomocí C#. Předpokládá se základní znalost C# a knihovny Aspose.3D.

## Rychlé odpovědi
- **Jaký je hlavní cíl?** Definovat síť a exportovat ji do vlastního binárního souboru.  
- **Která knihovna je použita?** Aspose.3D pro .NET.  
- **Potřebuji licenci?** Zkušební verze funguje pro vývoj; pro produkci je vyžadována komerční licence.  
- **Podporovaný vstupní formát?** Jakýkoli formát, který Aspose.3D dokáže číst, např. FBX, OBJ, 3MF.  
- **Typický případ použití?** Převod modelu FBX na lehkou binární reprezentaci pro renderování v reálném čase.

## Co znamená „definování sítě“ v Aspose.3D?

Definování sítě znamená popsat rozložení vrcholů (pozice, normály, UV) a jak jsou tyto vrcholy propojeny do trojúhelníků. Aspose.3D vám umožňuje vytvořit **VertexDeclaration**, která říká enginu, jaká data každý vrchol obsahuje, což je první krok před tím, než můžete **převést FBX do binárního formátu**.

## Proč exportovat 3D síť do vlastního binárního formátu?

- **Výkon:** Binární soubory jsou rychlejší na čtení a vyžadují méně úložiště než textové formáty.  
- **Kontrola:** Rozhodujete přesně, které atributy (normály, UV, vlastní data) jsou uloženy.  
- **Přenositelnost:** Jednoduché binární rozložení může být použito na jakékoli platformě bez dalších knihoven pro parsování.

## Požadavky

- **Aspose.3D pro .NET** – stáhněte jej z [zde](https://releases.aspose.com/3d/net/).  
- **Vývojové prostředí** – Visual Studio (jakákoli recentní verze) nebo jiné C# IDE.  
- **Vstupní 3D soubor** – FBX, OBJ nebo jakýkoli formát podporovaný Aspose.3D (např. `test.fbx`).  

## Importujte jmenné prostory

Zahrňte požadované jmenné prostory, abyste mohli pracovat se scénami, sítěmi a binárními proudy:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
```

## Krok 1: Načtěte 3D soubor

Nejprve načtěte zdrojový model. V tomto příkladu používáme FBX soubor s názvem `test.fbx`:

```csharp
Scene scene = Scene.FromFile("test.fbx");
```

## Krok 2: Definujte vlastní binární formát (Jak definovat síť)

Vytvořte **VertexDeclaration**, která odpovídá datům, která chcete uložit. Níže uvedený příklad definuje pozici, normálu a UV souřadnice pro každý vrchol:

```csharp
//The memory layout of a vertex is 
// float[3] position;
// float[3] normal;
// float[3] uv;
var vertexDeclaration = new VertexDeclaration();
vertexDeclaration.AddField(VertexFieldDataType.FVector3, VertexFieldSemantic.Position);
vertexDeclaration.AddField(VertexFieldDataType.FVector3, VertexFieldSemantic.Normal);
vertexDeclaration.AddField(VertexFieldDataType.FVector3, VertexFieldSemantic.UV);
```

## Krok 3: Otevřete binární soubor pro zápis (uložit 3D síť)

Otevřete `BinaryWriter`, který přijme převedená data sítě. Upravte cestu tak, aby ukazovala na místo, kde chcete mít výstupní soubor:

```csharp
using (var writer = new BinaryWriter(new FileStream("Your Output Directory" + "Save3DMeshesInCustomBinaryFormat_out", FileMode.Create, FileAccess.Write)))
```

## Krok 4: Procházejte uzly a entity (převést fbx do binárního formátu)

Procházejte graf scény, vybírejte pouze entity typu mesh a ignorujte světla, kamery atd.:

```csharp
scene.RootNode.Accept(delegate(Node node)
{
    foreach (Entity entity in node.Entities)
    {
        if (!(entity is IMeshConvertible))
            continue;
        // ... (continue processing)
    }
    return true;
});
```

## Krok 5: Převést kontrolní body a trojúhelníky a poté je zapsat

Pro každou síť transformujte vrcholy do světového prostoru, zapište transformační matici, počet vrcholů, počet indexů a poté surové buffery vrcholů a indexů:

```csharp
Mesh m = ((IMeshConvertible)entity).ToMesh();

var triMesh = TriMesh.FromMesh(vertexDeclaration, m);


//The mesh's memory layout is:
// float[16] transform_matrix;
// int vertices_count;
// int indices_count;
// vertex[vertices_count] vertices;
// ushort[indices_count] indices;


//write transform
var transform = node.GlobalTransform.TransformMatrix.ToArray();
for(int i = 0; i < transform.Length; i++)
    writer.Write((float)transform[i]);
//write number of vertices/indices
writer.Write(triMesh.VerticesCount);
writer.Write(triMesh.IndicesCount);
//write vertices and indices
writer.Flush();
triMesh.WriteVerticesTo(writer.BaseStream);
triMesh.Write16bIndicesTo(writer.BaseStream);
```

## Časté problémy a řešení

| Problém | Důvod | Řešení |
|-------|--------|-----|
| Výstupní soubor je prázdný | Writer nebyl uvolněn | Zajistěte, aby se blok `using` dokončil, nebo zavolejte `writer.Close()` |
| Síť vypadá deformovaně | Zapomněli jste aplikovat globální transformaci uzlu | Zapište transformační matici před vrcholy (jak je ukázáno) |
| Chybějící UV | Zdrojová síť postrádá UV kanál | Ověřte, že zdrojový soubor obsahuje UV, nebo podle toho upravte `VertexDeclaration` |

## Často kladené otázky

### Q1: Mohu použít Aspose.3D pro .NET s jinými programovacími jazyky?

A1: Aspose.3D primárně podporuje .NET jazyky, ale můžete prozkoumat možnosti kompatibility s jinými jazyky.

### Q2: Kde mohu najít další příklady a zdroje?

A2: [Fórum Aspose.3D](https://forum.aspose.com/c/3d/18) je skvělé místo, kde najdete podporu, příklady a můžete se zapojit do komunity.

### Q3: Je k dispozici zkušební verze Aspose.3D?

A3: Ano, můžete získat bezplatnou zkušební verzi [zde](https://releases.aspose.com/).

### Q4: Jak získám dočasnou licenci pro Aspose.3D?

A4: Navštivte [tento odkaz](https://purchase.aspose.com/temporary-license/), abyste získali dočasnou licenci pro testovací účely.

### Q5: Mohu zakoupit Aspose.3D pro .NET?

A5: Ano, můžete zakoupit Aspose.3D na [stránce nákupu](https://purchase.aspose.com/buy).

---

**Last Updated:** 2026-01-12  
**Testováno s:** Aspose.3D pro .NET (nejnovější stabilní verze)  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}