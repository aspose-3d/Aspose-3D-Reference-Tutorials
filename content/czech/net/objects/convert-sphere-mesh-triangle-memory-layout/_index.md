---
title: Převod Sphere Mesh na Triangle Mesh s vlastním rozložením paměti
linktitle: Převod Sphere Mesh na Triangle Mesh s vlastním rozložením paměti
second_title: Aspose.3D .NET API
description: Prozkoumejte Aspose.3D for .NET a bez námahy převeďte Sphere Mesh na Triangle Mesh s vlastním rozložením paměti. Postupujte podle našeho podrobného průvodce pro bezproblémovou integraci.
type: docs
weight: 15
url: /cs/net/objects/convert-sphere-mesh-triangle-memory-layout/
---
## Úvod
Chcete využít sílu Aspose.3D pro .NET k převodu Sphere Mesh na Triangle Mesh s vlastním rozložením paměti? Tento průvodce vás krok za krokem provede celým procesem a usnadní ho i začátečníkům. Na konci tohoto tutoriálu budete dobře rozumět tomu, jak toho dosáhnout pomocí Aspose.3D for .NET.
## Předpoklady
Než se pustíte do výukového programu, ujistěte se, že máte splněny následující předpoklady:
- Základní znalost programování .NET.
-  Nainstalovaná knihovna Aspose.3D for .NET. Můžete si jej stáhnout z[Aspose.3D for .NET download page](https://releases.aspose.com/3d/net/).
- Znalost programovacího jazyka C#.
## Importovat jmenné prostory
Ujistěte se, že ve svém projektu C# importujete potřebné jmenné prostory, abyste mohli využít funkce Aspose.3D:
```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD.Utilities;
using System.Runtime.InteropServices;
```
## Krok 1: Inicializujte objekt scény
```csharp
// Inicializujte objekt scény
Scene scene = new Scene();
```
## Krok 2: Inicializujte objekt třídy uzlu
```csharp
// Inicializujte objekt třídy Node
Node cubeNode = new Node("sphere");
```
## Krok 3: Převeďte Sphere Mesh na Typed TriMesh
```csharp
Mesh sphere = (new Sphere()).ToMesh();
var myMesh = TriMesh<MyVertex>.FromMesh(sphere);
```
## Krok 4: Získejte data vertexu v přizpůsobené struktuře
```csharp
MyVertex[] vertex = myMesh.VerticesToTypedArray();
```
## Krok 5: Získejte 32bitové a 16bitové indexy
```csharp
int[] indices32bit;
ushort[] indices16bit;
myMesh.IndicesToArray(out indices32bit);
myMesh.IndicesToArray(out indices16bit);
```
## Krok 6: Zapište data vertexu a indexu do Memory Stream
```csharp
using (MemoryStream ms = new MemoryStream())
{
    myMesh.WriteVerticesTo(ms);
    myMesh.Write16bIndicesTo(ms);
    myMesh.Write32bIndicesTo(ms);
}
```
## Krok 7: Bodový uzel na geometrii sítě
```csharp
cubeNode.Entity = sphere;
```
## Krok 8: Přidejte uzel do scény
```csharp
scene.RootNode.ChildNodes.Add(cubeNode);
```
## Krok 9: Uložte 3D scénu
```csharp
string output = "Your Output Directory" + "SphereToTriangleMeshCustomMemoryLayoutScene.fbx";
scene.Save(output, FileFormat.FBX7400ASCII);
```
## Krok 10: Zobrazení výsledků
```csharp
Console.WriteLine("Indices = {0}, Actual vertices = {1}, vertices before merging = {2}", myMesh.IndicesCount, myMesh.VerticesCount, myMesh.UnmergedVerticesCount);
Console.WriteLine("Total bytes of vertices in memory {0}bytes", myMesh.VerticesSizeInBytes);
Console.WriteLine("\nConverted a Sphere mesh to a triangle mesh with a custom memory layout of the vertex successfully.\nFile saved at " + output);
```
## Závěr
Gratulujeme! Úspěšně jste převedli Sphere Mesh na Triangle Mesh s vlastním rozložením paměti pomocí Aspose.3D for .NET. Tato výkonná knihovna poskytuje bezproblémový způsob manipulace s 3D objekty ve vašich aplikacích .NET.
## Nejčastější dotazy
### Otázka: Mohu používat Aspose.3D pro .NET s jinými frameworky .NET?
Odpověď: Ano, Aspose.3D for .NET je kompatibilní s různými .NET frameworky.
### Otázka: Kde najdu podrobnou dokumentaci k Aspose.3D pro .NET?
 A: Viz[Aspose.3D pro dokumentaci .NET](https://reference.aspose.com/3d/net/) pro podrobné informace.
### Otázka: Jak mohu získat dočasnou licenci pro Aspose.3D pro .NET?
 Návštěva[tento odkaz](https://purchase.aspose.com/temporary-license/) získat dočasnou licenci.
### Otázka: Jsou k dispozici nějaké vzorové projekty pro Aspose.3D pro .NET?
 Odpověď: Prozkoumejte dokumentaci Aspose.3D for .NET a[úložiště GitHub](https://github.com/aspose-3d/Aspose.3D-for-.NET) pro vzorové projekty.
### Otázka: Existuje aktivní komunita pro podporu Aspose.3D pro .NET?
 A: Ano, připojte se[Aspose.3D for .NET fórum](https://forum.aspose.com/c/3d/18) získat pomoc od komunity.