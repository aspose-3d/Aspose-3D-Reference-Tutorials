---
title: Praca z danymi geometrii siatki
linktitle: Praca z danymi geometrii siatki
second_title: Aspose.3D API .NET
description: Opanuj sztukę programowania grafiki 3D dzięki Aspose.3D dla .NET. Twórz, manipuluj i zapisuj wspaniałe sceny 3D bez wysiłku.
weight: 15
url: /pl/net/geometry-and-hierarchy/mesh-geometry-data/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Praca z danymi geometrii siatki

## Wstęp

Witamy w ekscytującym świecie programowania grafiki 3D z Aspose.3D dla .NET! W tym samouczku zagłębimy się w zawiłości pracy z danymi geometrii siatki w scenach 3D przy użyciu Aspose.3D, potężnej i wszechstronnej biblioteki dla programistów .NET. Niezależnie od tego, czy jesteś doświadczonym programistą, czy dopiero zaczynasz przygodę z grafiką 3D, ten przewodnik krok po kroku pomoże Ci bez wysiłku opanować sztukę obsługi danych geometrii siatki.

## Warunki wstępne

Zanim wyruszymy w tę podróż 3D, upewnij się, że spełniasz następujące wymagania wstępne:

- Praktyczna znajomość programowania w C# i .NET.
- Program Visual Studio zainstalowany na Twoim komputerze.
- Biblioteka Aspose.3D dla .NET, którą możesz pobrać[Tutaj](https://releases.aspose.com/3d/net/).

Teraz, gdy już wszystko gotowe, wskoczmy do fascynującego świata programowania grafiki 3D!

## Importuj przestrzenie nazw

W projekcie C# rozpocznij od zaimportowania niezbędnych przestrzeni nazw:

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using Aspose.ThreeD.Shading;
```

Te przestrzenie nazw zapewniają dostęp do podstawowych klas i metod potrzebnych do pracy ze scenami 3D i danymi geometrii siatki.

## Krok 1: Zainicjuj scenę

```csharp
// Zainicjuj obiekt sceny
Scene scene = new Scene();
```

Spowoduje to utworzenie pustej sceny 3D, w której można budować modele 3D i manipulować nimi.

## Krok 2: Zdefiniuj wektory kolorów

```csharp
// Zdefiniuj wektory kolorów
Vector3[] colors = new Vector3[] {
    new Vector3(1, 0, 0),
    new Vector3(0, 1, 0),
    new Vector3(0, 0, 1)
};
```

Określ tablicę wektorów kolorów, które zostaną zastosowane do różnych części sceny 3D.

## Krok 3: Utwórz siatkę i ustaw kolory

```csharp
// Wywołaj klasę Common, aby utworzyć siatkę przy użyciu metody konstruktora wielokątów, aby ustawić instancję siatki
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();

int idx = 0;
foreach (Vector3 color in colors)
{
    // Zainicjuj obiekt węzła kostki
    Node cube = new Node("cube");
    cube.Entity = mesh;
    LambertMaterial mat = new LambertMaterial();
    
    // Ustaw kolor
    mat.DiffuseColor = color;
    
    // Ustaw materiał
    cube.Material = mat;
    
    // Ustaw tłumaczenie
    cube.Transform.Translation = new Vector3(idx++ * 20, 0, 0);
    
    // Dodaj węzeł kostki
    scene.RootNode.ChildNodes.Add(cube);
}
```

Utwórz siatkę za pomocą metody konstruktora wielokątów i zastosuj kolory do różnych części sceny.

## Krok 4: Zapisz scenę 3D

```csharp
// Ścieżka do katalogu dokumentów.
var output = "Your Output Directory" + "MeshGeometryData.fbx";

// Zapisz scenę 3D w obsługiwanych formatach plików
scene.Save(output, FileFormat.FBX7400ASCII);
```

Określ katalog wyjściowy i zapisz scenę 3D w formacie pliku FBX7400ASCII.

## Wniosek

Gratulacje! Pomyślnie nauczyłeś się pracować z danymi geometrii siatki w scenach 3D przy użyciu Aspose.3D dla .NET. W tym samouczku przedstawiono podstawowe kroki tworzenia modeli 3D i manipulowania nimi. Eksperymentuj, odkrywaj i wynieś swoje umiejętności programowania grafiki 3D na nowy poziom!

## Często zadawane pytania

### P1: Czy mogę używać Aspose.3D dla .NET z innymi językami programowania?

Odpowiedź 1: Aspose.3D jest przeznaczony głównie dla .NET, ale możesz eksplorować inne produkty Aspose, które obsługują różne platformy i języki.

### P2: Czy dostępna jest bezpłatna wersja próbna Aspose.3D?

 Odpowiedź 2: Tak, możesz uzyskać dostęp do bezpłatnego okresu próbnego[Tutaj](https://releases.aspose.com/).

### P3: Gdzie mogę znaleźć dodatkowe wsparcie i zasoby?

 A3: Odwiedź[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) za wsparcie społeczności i dyskusje.

### P4: Jak uzyskać tymczasową licencję na Aspose.3D?

 A4: Możesz uzyskać licencję tymczasową[Tutaj](https://purchase.aspose.com/temporary-license/).

### P5: Jakie formaty plików są obsługiwane przy zapisywaniu scen 3D?

 O5: Aspose.3D obsługuje różne formaty plików, w tym FBX, STL i inne. Patrz[dokumentacja](https://reference.aspose.com/3d/net/) aby uzyskać pełną listę.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
