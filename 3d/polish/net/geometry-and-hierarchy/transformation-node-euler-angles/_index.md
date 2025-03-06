---
title: Transformacja węzła według kątów Eulera
linktitle: Transformacja węzła według kątów Eulera
second_title: Aspose.3D API .NET
description: Naucz się bez wysiłku przekształcać węzły 3D za pomocą Aspose.3D dla .NET. Postępuj zgodnie z naszym przewodnikiem krok po kroku, aby uzyskać oszałamiające rezultaty w swoich projektach.
weight: 19
url: /pl/net/geometry-and-hierarchy/transformation-node-euler-angles/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Transformacja węzła według kątów Eulera

## Wstęp

Witamy w tym kompleksowym samouczku na temat przekształcania węzłów według kątów Eulera w scenach 3D przy użyciu Aspose.3D dla .NET. W tym przewodniku zagłębimy się w ekscytujący świat grafiki 3D i zbadamy proces dodawania transformacji do węzła za pomocą kątów Eulera. Aspose.3D dla .NET zapewnia potężne narzędzia do pracy ze scenami i siatkami 3D, co czyni go doskonałym wyborem dla programistów poszukujących wszechstronności i wydajności w swoich projektach.

## Warunki wstępne

Zanim przejdziemy do samouczka, upewnij się, że spełniasz następujące wymagania wstępne:

-  Biblioteka Aspose.3D dla .NET: Upewnij się, że masz zainstalowaną bibliotekę Aspose.3D. Możesz go pobrać[Tutaj](https://releases.aspose.com/3d/net/).

- Środowisko programistyczne: skonfiguruj preferowane środowisko programistyczne .NET, takie jak Visual Studio.

## Importuj przestrzenie nazw

Rozpocznij od zaimportowania niezbędnych przestrzeni nazw, aby uzyskać dostęp do funkcjonalności zapewnianej przez Aspose.3D dla .NET:

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

Podzielmy teraz przykład na wiele kroków, aby ułatwić zrozumienie.

## Krok 1: Zainicjuj obiekt sceny

```csharp
// ExStart: Dodaj transformację do węzła według kątów Eulera
// Zainicjuj obiekt sceny
Scene scene = new Scene();
```

 Zacznij od utworzenia nowej sceny 3D za pomocą narzędzia`Scene` klasa.


## Krok 2: Utwórz siatkę za pomocą prymitywnego pudełka

```csharp
// Wywołaj klasę Common, aby utworzyć siatkę przy użyciu metody konstruktora wielokątów, aby ustawić instancję siatki
Mesh mesh = (new Box()).ToMesh();
```

 Wywołaj metodę (w tym przypadku`CreateMeshUsingPolygonBuilder` ze zwyczaju`Common`class) w celu wygenerowania siatki dla obiektu 3D.

## Krok 3: Utwórz węzeł kontenerowy dla siatki

```csharp
// Wskaż węzeł na geometrię siatki
Node cubeNode = scene.RootNode.CreateChildNode(mesh);
```

 Utwórz węzeł w scenie za pomocą`Node` klasa. Węzeł ten będzie służył jako kontener dla naszego obiektu 3D.

## Krok 4: Ustaw kąty Eulera i przesunięcie

```csharp
// Kąty Eulera
cubeNode.Transform.EulerAngles = new Vector3(0.3, 0.1, -0.5);            
// Ustaw tłumaczenie
cubeNode.Transform.Translation = new Vector3(0, 0, 20);
```

Zdefiniuj kąty Eulera i translację węzła, aby ustawić go w przestrzeni 3D.

## Krok 5: Zapisz scenę 3D

```csharp
// Ścieżka do katalogu dokumentów.
var output = "TransformationToNode.fbx";

// Zapisz scenę 3D w obsługiwanych formatach plików
scene.Save(output);
// ExEnd:AddTransformationToNodeByEulerAngles
Console.WriteLine("\nTransformation added successfully to node.\nFile saved at " + output);
```

Określ katalog wyjściowy i zapisz scenę 3D, łącznie z przekształconym węzłem, w żądanym formacie pliku (w tym przypadku FBX7500ASCII).

## Wniosek

Gratulacje! Pomyślnie nauczyłeś się przekształcać węzeł według kątów Eulera w scenach 3D przy użyciu Aspose.3D dla .NET. Ta potężna biblioteka otwiera drzwi do nieskończonych możliwości rozwoju grafiki 3D.

## Często zadawane pytania

### P1: Czy Aspose.3D jest kompatybilny z innymi narzędziami do modelowania 3D?

Odpowiedź 1: Aspose.3D obsługuje różne formaty plików 3D, zwiększając kompatybilność z popularnymi narzędziami do modelowania.

### P2: Czy mogę zastosować wiele transformacji do jednego węzła?

Odpowiedź 2: Tak, możesz łączyć i stosować wiele transformacji, aby uzyskać złożone efekty.

### P3: Gdzie mogę znaleźć dodatkową dokumentację Aspose.3D?

 A3: Patrz[dokumentacja](https://reference.aspose.com/3d/net/) szczegółowe informacje i przykłady.

### P4: Czy potrzebuję licencji na używanie Aspose.3D dla .NET?

 A4: Tak, możesz uzyskać licencję[Tutaj](https://purchase.aspose.com/buy) lub odkryj A[bezpłatna wersja próbna](https://releases.aspose.com/).

### P5: Potrzebujesz pomocy lub masz konkretne pytania?

 A5: Odwiedź[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) za wsparcie społeczności.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
