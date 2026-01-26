---
date: 2026-01-22
description: Dowiedz się, jak zastosować rotację kwaternionową do węzła 3D i przekonwertować
  scenę na FBX przy użyciu Aspose.3D dla .NET. Przewodnik krok po kroku.
linktitle: Apply Quaternion Rotation to Transform Node
second_title: Aspose.3D .NET API
title: Zastosuj rotację kwaternionową do węzła Transform w Aspose.3D dla .NET
url: /pl/net/geometry-and-hierarchy/transformation-node-quaternion/
weight: 20
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Zastosuj rotację kwaternionową do węzła Transform w Aspose.3D dla .NET

## Wstęp

W tym obszernej samouczku **zastosujesz rotację kwaternionową** do węzła, ustawisz rotację węzła i w końcu wyeksportujesz scenę jako plik FBX przy użyciu Aspose.3D dla .NET. Niezależnie od tego, czy tworzysz silnik gry, przeglądarkę CAD, czy wizualizator naukowy, rotacja kwaternionowa zapewnia płynną kontrolę orientacji bez problemu gimbal lock. Przejdźmy krok po kroku przez cały proces.

## Szybkie odpowiedzi
- **Jaki jest główny interfejs API?** Aspose.3D for .NET  
- **Jak zastosować rotację kwaternionową?** Użyj `Quaternion.FromRotation` na `Transform.Rotation` węzła.  
- **Do którego formatu pliku mogę eksportować?** FBX (np. `FileFormat.FBX7500ASCII`).  
- **Czy potrzebna jest licencja?** Wymagana jest tymczasowa lub pełna licencja do użytku produkcyjnego.  
iarowąą,D, zastosowanie rotacji kwaternionowej do węzła pozwala płynnie obracać obiekty wokół dowolnej osi.

## Dlaczego używać **quaternion rotation C#** z Aspose.3D?

- **Brak gimbal lock:** W przeciwieństwie do kątów Eulera, nagłej utraty stopnia swobody.  
- **Płynna interpolacja:** Ideal w czasie rzeczywistym.  
- **Wydajność:** Obliczenia kwaternionowe są obliczeniowo efektyw for . że masz zainstalowaną bibliotekę Aspose.3D. Możesz ją pobrać ze [strony wydania](https://releases.aspose.com/3d/net/).  
- Środowisko programistyczne: Skonfiguruj swoje środowisko .NET Aspose.3D:

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

## Przewodnik krok po kroku

### Krok 1: Inicjalizacja obiektu Scene

Najpierw utwórz nowy `Scene`, który będzie zawierał całą geometrię i transformacje.

```csharp
// ExStart:AddTransformationToNodeByQuaternion            
// Initialize scene object
Scene scene = new Scene();
```

### Krok 2: Inicjalizacja obiektu klasy Node

Utwórz `Node`, który będzie reprezentował sześcian w hierarchii.

```csharp
// Initialize Node class object
Node cubeNode = new Node("cube");
```

### Krok 3: Tworzenie siatki przy użyciu Polygon Builder

Tutaj generujemy prostą siatkę sześcianu przy użyciu metody pomocniczej (logika **create mesh polygon** jest zawarta w `Common.CreateMeshUsingPolygonBuilder()`).

```csharp
// Call Common class create mesh using polygon builder method to set mesh instance 
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
```

### Krok 4: Powiązanie węzła z geometrią siatki

Przypisz siatkę do właściwości `Entity` węzła, aby węzeł wiedział, jaką geometrię renderować.

```csharp
// Point node to the Mesh geometry
cubeNode.Entity = mesh;
```

### Krok 5: Ustawienie rotacji przy użyciu kwaternionu (apply quaternion rotation)

Teraz **zastosujemy rotację kwaternionową** do węzła. Metoda `FromRotation` tworzy kwaternion, który obraca z osi Y do wektora kierunku.

```csharp
// Set rotation
cubeNode.Transform.Rotation = Quaternion.FromRotation(new Vector3(0, 1, 0), new Vector3(0.3, 0.5, 0.1));            
```

### Krok 6: Ustawienie translacji (set node rotation & position)

Ustaw pozycję sześcianu 20 jednostek do przodu wzdłuż osi Z.

```csharp
// Set translation
cubeNode.Transform.Translation = new Vector3(0, 0, 20);            
```

### Krok 7: Dodanie sześcianu do sceny

Dołącz węzeł do korzenia sceny, aby stał się częścią hierarchii.

```csharp
// Add cube to the scene
scene.RootNode.ChildNodes.Add(cubeNode);
```

### Krok 8: Zapis sceny 3D (convert scene FBX)

Na koniec wyeksportuj scenę do pliku FBX. To demonstruje **convert scene fbx** przy użyciu Aspose.3D.

```csharp
// The path to the documents directory.
var output = "Your Output Directory" + "TransformationToNode.fbx";

// Save 3D scene in the supported file formats
scene.Save(output, FileFormat.FBX7500ASCII);
// ExEnd:AddTransformationToNodeByQuaternion
Console.WriteLine("\nTransformation added successfully to node.\nFile saved at " + output);
```

## Typowe problemy i rozwiązania

| Problem | Rozwiązanie |
|---------|-------------|
| **Kwaternion nie wywiera żadnego efektu** | Sprawdź, czy wektory osi nie są zerowe i nie są współliniowe. |
| **Wyeksportowany FBX jest pusty** | Upewnij się, że węzeł jest podłączony do `scene.RootNode` oraz że ścieżka wyjściowa jest zapisywalna. |
| **Wyjątek licencyjny** | Zastosuj tymczasową lub pełną licencję przed wywołaniem jakichkolwiek metod API. |

## Najczęściej zadawane pytania

### Q1: Co to jest kwaternion w grafice 3D?

Kwaterniony są jednostkami matematycznymi używanymi do reprezentacji rotacji w przestrzeni 3D.

### Q2: Jak mogę pobrać Aspose.3D dla .NET?

Możesz pobrać bibliotekę ze [strony wydania](https://releases.aspose.com/3d/net/).

### Q3: Czy dostępna jest darmowa wersja próbna Aspose.3D dla .NET?

Tak, darmową wersję próbną możesz uzyskać [tutaj](https://releases.aspose.com/).

### Q4: Gdzie mogę znaleźć wsparcie dla Aspose.3D dla .NET?

Odwiedź [forum Aspose.3D](https://forum.aspose.com/c/3d/18) w celu uzyskania pomocy i dyskusji.

### Q5: Jak uzyskać tymczasową licencję dla Aspose.3D?

Uzyskaj tymczasową licencję [tutaj](https://purchase.aspose.com/temporary-license/).

## Zakończenie

Gratulacje! Nauczyłeś się **jak zastosować rotację kwaternionową**, **ustawić rotację węzła**, **utworzyć siatkę wielokąta**, i **przekonwertować scenę do FBX** przy użyciu Aspose.3D dla .NET. Eksperymentuj z różnymi wektorami rotacji i formatami eksportu, aby odblokować więcej możliwości Aspose.3D. Po głębsze zanurzenie się, zapoznaj się z oficjalną [dokumentacją](https://reference.aspose.com/3d/net/).

---

**Ostatnia aktualizacja:** 2026-01-22  
**Testowano z:** Aspose.3D 24.11 for .NET  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}