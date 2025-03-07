---
title: Ukládání 3D sítí ve vlastním binárním formátu
linktitle: Ukládání 3D sítí ve vlastním binárním formátu
second_title: Aspose.3D .NET API
description: Prozkoumejte svět 3D s Aspose.3D pro .NET. Naučte se ukládat sítě ve vlastním binárním formátu.
weight: 13
url: /cs/net/3d-scene/save-3d-meshes-binary-format/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Ukládání 3D sítí ve vlastním binárním formátu

## Úvod

Vítejte ve světě Aspose.3D for .NET, výkonné knihovny, která umožňuje vývojářům pracovat s 3D soubory bez námahy. V tomto tutoriálu se ponoříme do procesu ukládání 3D sítí ve vlastním binárním formátu pomocí Aspose.3D for .NET. Tato příručka předpokládá, že máte základní znalosti jazyka C# a jste obeznámeni s knihovnou Aspose.3D.

## Předpoklady

Než se pustíme do výukového programu, ujistěte se, že máte na svém místě následující:

-  Aspose.3D for .NET: Ujistěte se, že máte nainstalovanou knihovnu Aspose.3D. Můžete si jej stáhnout z[tady](https://releases.aspose.com/3d/net/).

- Vývojové prostředí: Nastavte si preferované vývojové prostředí C#, jako je Visual Studio.

- Vstupní 3D soubor: Mějte 3D soubor (např. test.fbx), který chcete převést do vlastního binárního formátu.

## Importovat jmenné prostory

Do kódu C# zahrňte potřebné jmenné prostory pro přístup k funkcím Aspose.3D:

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

Načtěte svůj 3D soubor pomocí Aspose.3D. V tomto příkladu načteme soubor s názvem „test.fbx“:

```csharp
Scene scene = Scene.FromFile("test.fbx");
```

## Krok 2: Definujte vlastní binární formát

Definujte strukturu vlastního binárního formátu, do kterého chcete uložit své 3D sítě. Příklad používá strukturu s MeshBlock, Vertex a Triangle jako komponenty.

```csharp
// Rozložení paměti vrcholu je
// plovoucí[3] poloha;
// plovoucí[3] normální;
// plovák[3] uv;
var vertexDeclaration = new VertexDeclaration();
vertexDeclaration.AddField(VertexFieldDataType.FVector3, VertexFieldSemantic.Position);
vertexDeclaration.AddField(VertexFieldDataType.FVector3, VertexFieldSemantic.Normal);
vertexDeclaration.AddField(VertexFieldDataType.FVector3, VertexFieldSemantic.UV);

```

## Krok 3: Otevřete soubor pro zápis

Otevřete binární soubor pro zápis, kam se uloží převedené 3D sítě:

```csharp
using (var writer = new BinaryWriter(new FileStream("Your Output Directory" + "Save3DMeshesInCustomBinaryFormat_out", FileMode.Create, FileAccess.Write)))
```

## Krok 4: Iterujte přes uzly a entity

Navštivte každý uzel ve 3D scéně a převeďte síťové entity do vlastního binárního formátu. Ignorujte světla, kamery a další entity bez sítě:

```csharp
scene.RootNode.Accept(delegate(Node node)
{
    foreach (Entity entity in node.Entities)
    {
        if (!(entity is IMeshConvertible))
            continue;
        // ... (pokračovat ve zpracování)
    }
    return true;
});
```

## Krok 5: Převeďte a zapište kontrolní body a trojúhelníky

Pro každou entitu sítě převeďte řídicí body na světový prostor a zapište je do binárního souboru spolu s indexy trojúhelníků:

```csharp
Mesh m = ((IMeshConvertible)entity).ToMesh();

var triMesh = TriMesh.FromMesh(vertexDeclaration, m);


//Rozložení paměti sítě je:
// float[16] transform_matrix;
// int vertices_count;
// int počet_indexů;
// vertex[vertices_count] vertexy;
// ushort[index_count] indexy;


//napsat transformovat
var transform = node.GlobalTransform.TransformMatrix.ToArray();
for(int i = 0; i < transform.Length; i++)
    writer.Write((float)transform[i]);
//napište počet vrcholů/indexů
writer.Write(triMesh.VerticesCount);
writer.Write(triMesh.IndicesCount);
//zapisovat vrcholy a indexy
writer.Flush();
triMesh.WriteVerticesTo(writer.BaseStream);
triMesh.Write16bIndicesTo(writer.BaseStream);

```

## Závěr

V tomto tutoriálu jsme se zabývali procesem ukládání 3D sítí ve vlastním binárním formátu pomocí Aspose.3D for .NET. Tato výkonná knihovna poskytuje vývojářům nástroje potřebné k bezproblémové manipulaci s 3D soubory. Experimentujte s různými formáty a nastaveními, abyste ve svých projektech odemkli plný potenciál Aspose.3D.

## Nejčastější dotazy

### Q1: Mohu používat Aspose.3D pro .NET s jinými programovacími jazyky?

Odpověď 1: Aspose.3D primárně podporuje jazyky .NET, ale můžete prozkoumat možnosti kompatibility pro jiné jazyky.

### Q2: Kde najdu další příklady a zdroje?

 A2:[Aspose.3D fórum](https://forum.aspose.com/c/3d/18)je skvělým místem k nalezení podpory, příkladů a zapojení do komunity.

### Q3: Je k dispozici zkušební verze pro Aspose.3D?

 A3: Ano, můžete získat bezplatnou zkušební verzi[tady](https://releases.aspose.com/).

### Q4: Jak získám dočasnou licenci pro Aspose.3D?

 A4: Návštěva[tento odkaz](https://purchase.aspose.com/temporary-license/) získat dočasnou licenci pro testovací účely.

### Q5: Mohu zakoupit Aspose.3D pro .NET?

 A5: Ano, můžete si koupit Aspose.3D z[nákupní stránku](https://purchase.aspose.com/buy).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
