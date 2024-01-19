---
title: Konwersja prymitywnej kuli na siatkę
linktitle: Konwersja prymitywnej kuli na siatkę
second_title: Aspose.3D API .NET
description: Poznaj Aspose.3D dla .NET i bez wysiłku przekonwertuj siatkę sferyczną na siatkę trójkątną z niestandardowym układem pamięci. Postępuj zgodnie z naszym przewodnikiem krok po kroku, aby zapewnić bezproblemową integrację.
type: docs
weight: 16
url: /pl/net/objects/convert-sphere-primitive-to-mesh/
---
## Wstęp
Czy chcesz wykorzystać moc Aspose.3D dla .NET do konwersji siatki sferycznej na siatkę trójkątną z niestandardowym układem pamięci? Ten przewodnik krok po kroku przeprowadzi Cię przez cały proces, dzięki czemu nawet początkujący będą mogli z łatwością go wykonać. Pod koniec tego samouczka będziesz mieć solidną wiedzę, jak to osiągnąć za pomocą Aspose.3D dla .NET.
## Warunki wstępne
Zanim przejdziesz do samouczka, upewnij się, że spełniasz następujące wymagania wstępne:
- Podstawowa znajomość programowania .NET.
-  Zainstalowana biblioteka Aspose.3D dla .NET. Można go pobrać z[Strona pobierania Aspose.3D dla .NET](https://releases.aspose.com/3d/net/).
- Znajomość języka programowania C#.
## Importuj przestrzenie nazw
W swoim projekcie C# pamiętaj o zaimportowaniu niezbędnych przestrzeni nazw, aby wykorzystać funkcjonalność Aspose.3D:
```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
```
## Krok 1: Zainicjuj obiekt sceny
```csharp
// Zainicjuj obiekt sceny
Scene scene = new Scene();
```
## Krok 2: Zainicjuj obiekt klasy węzła
```csharp
// Zainicjuj obiekt klasy Node
Node cubeNode = new Node("sphere");
```
## Krok 3: Konwertuj siatkę sferyczną na wpisaną TriMesh
```csharp
Mesh sphere = (new Sphere()).ToMesh();
var myMesh = TriMesh<MyVertex>.FromMesh(sphere);
```
## Krok 4: Uzyskaj dane wierzchołków w dostosowanej strukturze
```csharp
MyVertex[] vertex = myMesh.VerticesToTypedArray();
```
## Krok 5: Uzyskaj indeksy 32-bitowe i 16-bitowe
```csharp
int[] indices32bit;
ushort[] indices16bit;
myMesh.IndicesToArray(out indices32bit);
myMesh.IndicesToArray(out indices16bit);
```
## Krok 6: Zapisz dane wierzchołków i indeksów w strumieniu pamięci
```csharp
using (MemoryStream ms = new MemoryStream())
{
    myMesh.WriteVerticesTo(ms);
    myMesh.Write16bIndicesTo(ms);
    myMesh.Write32bIndicesTo(ms);
}
```
## Krok 7: Wskaż węzeł na geometrię siatki
```csharp
cubeNode.Entity = sphere;
```
## Krok 8: Dodaj węzeł do sceny
```csharp
scene.RootNode.ChildNodes.Add(cubeNode);
```
## Krok 9: Zapisz scenę 3D
```csharp
string output = "Your Output Directory" + "SphereToTriangleMeshCustomMemoryLayoutScene.fbx";
scene.Save(output, FileFormat.FBX7400ASCII);
```
## Krok 10: Wyświetl wyniki
```csharp
Console.WriteLine("Indices = {0}, Actual vertices = {1}, vertices before merging = {2}", myMesh.IndicesCount, myMesh.VerticesCount, myMesh.UnmergedVerticesCount);
Console.WriteLine("Total bytes of vertices in memory {0}bytes", myMesh.VerticesSizeInBytes);
Console.WriteLine("\nConverted a Sphere mesh to a triangle mesh with a custom memory layout of the vertex successfully.\nFile saved at " + output);
```

## Przykładowy kod źródłowy MyVertex
```csharp
[StructLayout(LayoutKind.Sequential)]
struct MyVertex
{
	[Semantic(VertexFieldSemantic.Position)]
	FVector3 position;
	[Semantic(VertexFieldSemantic.Normal)]
	FVector3 normal;
}
```
## Wniosek
Gratulacje! Pomyślnie przekonwertowałeś siatkę sferyczną na siatkę trójkątną z niestandardowym układem pamięci przy użyciu Aspose.3D dla .NET. Ta potężna biblioteka zapewnia płynny sposób manipulowania obiektami 3D w aplikacjach .NET.
## Często zadawane pytania
### P: Czy mogę używać Aspose.3D dla .NET z innymi frameworkami .NET?
O: Tak, Aspose.3D dla .NET jest kompatybilny z różnymi frameworkami .NET.
### P: Gdzie mogę znaleźć szczegółową dokumentację Aspose.3D dla .NET?
 Odp.: Patrz[Dokumentacja Aspose.3D dla .NET](https://reference.aspose.com/3d/net/) w celu uzyskania szczegółowych informacji.
### P: Jak mogę uzyskać tymczasową licencję na Aspose.3D dla .NET?
 Wizyta[ten link](https://purchase.aspose.com/temporary-license/) w celu uzyskania licencji tymczasowej.
### P: Czy są dostępne jakieś przykładowe projekty dla Aspose.3D dla .NET?
 O: Zapoznaj się z dokumentacją Aspose.3D dla .NET i[Repozytorium GitHuba](https://github.com/aspose-3d/Aspose.3D-for-.NET) dla przykładowych projektów.
### P: Czy istnieje aktywna społeczność obsługująca Aspose.3D dla .NET?
 Odp.: Tak, dołącz do[Forum Aspose.3D dla .NET](https://forum.aspose.com/c/3d/18) aby uzyskać pomoc od społeczności.