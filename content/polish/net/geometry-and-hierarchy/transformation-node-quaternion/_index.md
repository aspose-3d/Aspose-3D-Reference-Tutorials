---
title: Transformacja węzła przez kwaternion w scenach 3D
linktitle: Transformacja węzła przez kwaternion w scenach 3D
second_title: Aspose.3D API .NET
description: Naucz się przekształcać węzły 3D za pomocą kwaternionów przy użyciu Aspose.3D dla .NET. Przewodnik krok po kroku dla początkujących.
type: docs
weight: 20
url: /pl/net/geometry-and-hierarchy/transformation-node-quaternion/
---
## Wstęp

Witamy w przewodniku krok po kroku dotyczącym przekształcania węzła przez kwaternion w scenach 3D przy użyciu Aspose.3D dla .NET. W tym samouczku odkryjemy potężne możliwości Aspose.3D dla .NET i przejdziemy przez proces dodawania transformacji do węzła 3D za pomocą kwaternionów.

## Warunki wstępne

Zanim przejdziemy do samouczka, upewnij się, że spełniasz następujące wymagania wstępne:

-  Aspose.3D dla .NET: Upewnij się, że masz zainstalowaną bibliotekę Aspose.3D. Można go pobrać z[strona wydania](https://releases.aspose.com/3d/net/).

- Środowisko programistyczne: Skonfiguruj środowisko programistyczne .NET za pomocą niezbędnych narzędzi i konfiguracji.

- Podstawowe zrozumienie koncepcji 3D: Pomocna będzie znajomość grafiki 3D i koncepcji.

## Importuj przestrzenie nazw

W projekcie .NET uwzględnij wymagane przestrzenie nazw dla Aspose.3D:

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

## Krok 1: Zainicjuj obiekt sceny

```csharp
// ExStart:AddTransformationToNodeByQuaternion
// Zainicjuj obiekt sceny
Scene scene = new Scene();
```

## Krok 2: Zainicjuj obiekt klasy węzła

```csharp
// Zainicjuj obiekt klasy Node
Node cubeNode = new Node("cube");
```

## Krok 3: Utwórz siatkę za pomocą narzędzia Polygon Builder

```csharp
// Wywołaj klasę Common, aby utworzyć siatkę przy użyciu metody konstruktora wielokątów, aby ustawić instancję siatki
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
```

## Krok 4: Skieruj węzeł na geometrię siatki

```csharp
// Wskaż węzeł na geometrię siatki
cubeNode.Entity = mesh;
```

## Krok 5: Ustaw obrót za pomocą kwaternionu

```csharp
// Ustaw obrót
cubeNode.Transform.Rotation = Quaternion.FromRotation(new Vector3(0, 1, 0), new Vector3(0.3, 0.5, 0.1));            
```

## Krok 6: Ustaw tłumaczenie

```csharp
// Ustaw tłumaczenie
cubeNode.Transform.Translation = new Vector3(0, 0, 20);            
```

## Krok 7: Dodaj kostkę do sceny

```csharp
// Dodaj kostkę do sceny
scene.RootNode.ChildNodes.Add(cubeNode);
```

## Krok 8: Zapisz scenę 3D

```csharp
// Ścieżka do katalogu dokumentów.
var output = "Your Output Directory" + "TransformationToNode.fbx";

//Zapisz scenę 3D w obsługiwanych formatach plików
scene.Save(output, FileFormat.FBX7500ASCII);
// ExEnd:AddTransformationToNodeByQuaternion
Console.WriteLine("\nTransformation added successfully to node.\nFile saved at " + output);
```

## Wniosek

Gratulacje! Pomyślnie nauczyłeś się, jak przekształcać węzeł za pomocą kwaternionów w scenach 3D przy użyciu Aspose.3D dla .NET. Odkryj więcej funkcji i możliwości, korzystając z[dokumentacja](https://reference.aspose.com/3d/net/).

## Często zadawane pytania

### P1: Co to jest kwaternion w grafice 3D?

Odpowiedź 1: Kwaterniony to jednostki matematyczne używane do reprezentowania obrotów w przestrzeni 3D.

### P2: Jak mogę pobrać Aspose.3D dla .NET?

 O2: Możesz pobrać bibliotekę z[strona wydania](https://releases.aspose.com/3d/net/).

### P3: Czy dostępna jest bezpłatna wersja próbna Aspose.3D dla .NET?

 A3: Tak, możesz uzyskać bezpłatną wersję próbną[Tutaj](https://releases.aspose.com/).

### P4: Gdzie mogę znaleźć wsparcie dla Aspose.3D dla .NET?

 A4: Odwiedź[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) za wsparcie i dyskusje.

### P5: Jak uzyskać tymczasową licencję na Aspose.3D?

 A5: Uzyskaj tymczasową licencję[Tutaj](https://purchase.aspose.com/temporary-license/).
