---
title: Węzeł przekształcający według macierzy transformacji
linktitle: Węzeł przekształcający według macierzy transformacji
second_title: Aspose.3D API .NET
description: Bez wysiłku przekształcaj węzły w scenach 3D za pomocą Aspose.3D dla .NET. Dowiedz się, jak krok po kroku przekształcać węzły, korzystając z samouczka.
weight: 21
url: /pl/net/geometry-and-hierarchy/transformation-node-matrix/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Węzeł przekształcający według macierzy transformacji

## Wstęp

W dynamicznej dziedzinie grafiki i wizualizacji 3D możliwość manipulowania obiektami w scenie jest kluczowym aspektem. Aspose.3D dla .NET umożliwia programistom płynne przekształcanie węzłów przy użyciu macierzy transformacji, dodając warstwę kreatywności i kontroli do scen 3D. Ten samouczek przeprowadzi Cię krok po kroku przez proces przekształcania węzła w scenie 3D.

## Warunki wstępne

Zanim przejdziesz do samouczka, upewnij się, że spełniasz następujące wymagania wstępne:

1.  Biblioteka Aspose.3D dla .NET: Upewnij się, że masz zainstalowaną bibliotekę Aspose.3D w projekcie .NET. Możesz go pobrać[Tutaj](https://releases.aspose.com/3d/net/).

2. Środowisko programistyczne: Skonfiguruj działające środowisko programistyczne .NET, a jeśli jeszcze tego nie zrobiłeś, utwórz nowy projekt, w którym będziesz wdrażać transformacje.

## Importuj przestrzenie nazw

Rozpocznij od zaimportowania niezbędnych przestrzeni nazw do projektu .NET. Te przestrzenie nazw zapewniają podstawowe klasy i metody manipulacji scenami 3D.

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

Teraz, gdy omówiliśmy podstawy, podzielmy proces transformacji na przewodnik krok po kroku.

## Krok 1: Zainicjuj scenę

```csharp
// ExStart:AddTransformationToNodeByTransformationMatrix
// Zainicjuj obiekt sceny
Scene scene = new Scene();

```

Na tym etapie tworzymy nową, pustą scenę 3D.

## Krok 2: Utwórz siatkę i dołącz do sceny

```csharp
// Wywołaj klasę Common, aby utworzyć siatkę przy użyciu metody konstruktora wielokątów, aby ustawić instancję siatki
Mesh mesh = (new Box()).ToMesh();

// Utwórz węzeł kontenerowy dla siatki.
Node cubeNode = scene.RootNode.CreateChildNode(mesh);
```

Tutaj generujemy siatkę metodą wielokąta i przypisujemy ją do węzła, ustalając geometrię naszej kostki.

## Krok 3: Ustaw niestandardową macierz tłumaczeń

```csharp
// Ustaw niestandardową macierz tłumaczeń
cubeNode.Transform.TransformMatrix = new Matrix4(
    1, -0.3, 0, 0,
    0.4, 1, 0.3, 0,
    0, 0, 1, 0,
    0, 20, 0, 1
);        
```

Zdefiniuj niestandardową macierz translacji, aby określić konkretną transformację zastosowaną do węzła. Dostosuj wartości macierzy zgodnie z potrzebami żądanej transformacji.

Dołącz węzeł sześcianu do sceny, czyniąc go częścią ogólnego środowiska 3D.

## Krok 4: Zapisz scenę

```csharp
// Ścieżka do katalogu dokumentów.
var output = "TransformationToNode.fbx";

// Zapisz scenę 3D w obsługiwanych formatach plików
scene.Save(output);
// ExEnd:AddTransformationToNodeByTransformationMatrix
Console.WriteLine("\nTransformation added successfully to node.\nFile saved at " + output);
```

Określ katalog wyjściowy i nazwę pliku, a następnie zapisz scenę 3D w żądanym formacie pliku. W tym przykładzie zapisujemy go w formacie FBX7500ASCII.

## Wniosek

Gratulacje! Pomyślnie przekształciłeś węzeł przy użyciu macierzy transformacji w scenie 3D za pomocą Aspose.3D dla .NET. Ta możliwość otwiera drzwi do różnorodnych i urzekających wizualnie aplikacji 3D.

## Często zadawane pytania

### P1: Co to jest macierz transformacji w grafice 3D?

A1: Macierz transformacji to reprezentacja matematyczna używana do stosowania różnych transformacji (przesunięcie, obrót, skalowanie) do obiektów w przestrzeni 3D.

### P2: Czy mogę zastosować wiele transformacji do jednego węzła?

Odpowiedź 2: Tak, możesz łączyć wiele transformacji, mnożąc ich odpowiednie macierze i stosując wynik do węzła.

### P3: Czy istnieją inne obsługiwane formaty plików do zapisywania scen 3D?

 O3: Aspose.3D dla .NET obsługuje różne formaty plików, w tym STL, GLTF, OBJ i inne. Patrz[dokumentacja](https://reference.aspose.com/3d/net/) dla pełnej listy.

### P4: Jak mogę uzyskać tymczasową licencję na Aspose.3D dla .NET?

 A4: Odwiedź[strona licencji tymczasowej](https://purchase.aspose.com/temporary-license/)na stronie internetowej Aspose w celu uzyskania tymczasowej licencji do celów ewaluacyjnych.

### P5: Gdzie mogę szukać pomocy lub połączyć się ze społecznością Aspose.3D?

 A5: Odwiedź[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) aby zadawać pytania, dzielić się doświadczeniami i łączyć się z innymi programistami korzystającymi z Aspose.3D.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
