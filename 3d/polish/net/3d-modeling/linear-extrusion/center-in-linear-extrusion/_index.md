---
title: Centrum w wytłaczaniu liniowym
linktitle: Centrum w wytłaczaniu liniowym
second_title: Aspose.3D API .NET
description: Poznaj świat modelowania 3D z Aspose.3D dla .NET. Wyśrodkuj techniki wytłaczania liniowego, twórz oszałamiające projekty i uwolnij swoją kreatywność.
weight: 10
url: /pl/net/3d-modeling/linear-extrusion/center-in-linear-extrusion/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Centrum w wytłaczaniu liniowym

## Wstęp

Witamy w tym kompleksowym przewodniku na temat opanowania wytłaczania liniowego przy użyciu Aspose.3D dla .NET. Jeśli chcesz udoskonalić swoje umiejętności modelowania 3D i tworzyć wspaniałe profile, jesteś we właściwym miejscu. W tym samouczku zagłębimy się w technikę wytłaczania liniowego, koncentrując się szczególnie na aspekcie centrowania, aby przenieść Twoje projekty na zupełnie nowy poziom.

## Warunki wstępne

Zanim wyruszymy w tę ekscytującą podróż, upewnij się, że spełniasz następujące wymagania wstępne:

- Podstawowa znajomość języka programowania C#.
- Program Visual Studio zainstalowany na Twoim komputerze.
-  Biblioteka Aspose.3D dla .NET, którą można pobrać z witryny[Dokumentacja Aspose.3D .NET](https://reference.aspose.com/3d/net/).
-  Upewnij się, że masz dostęp do[Dokumentacja Aspose.3D .NET](https://reference.aspose.com/3d/net/) w celach informacyjnych w całym samouczku.

## Importuj przestrzenie nazw

Na początek zaimportujmy niezbędne przestrzenie nazw. Położą one podwaliny pod nasze arcydzieło modelowania 3D.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Krok 1: Zainicjuj profil podstawowy

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## Krok 2: Utwórz scenę 3D

```csharp
Scene scene = new Scene();
```

## Krok 3: Utwórz lewy i prawy węzeł

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(5, 0, 0);
```

## Krok 4: Wykonaj wytłaczanie liniowe na lewym węźle

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 2) { Center = false, Slices = 3 });
```

## Krok 5: Ustaw płaszczyznę podłoża jako odniesienie

```csharp
left.CreateChildNode(new Box(0.01, 3, 3));
```

## Krok 6: Wykonaj wytłaczanie liniowe na prawym węźle

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 2) { Center = true, Slices = 3 });
```

## Krok 7: Ustaw płaszczyznę podłoża jako odniesienie (prawy węzeł)

```csharp
right.CreateChildNode(new Box(0.01, 3, 3));
```

## Krok 8: Zapisz scenę 3D

```csharp
scene.Save("Your Output Directory" + "CenterInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## Wniosek

Gratulacje! Udało Ci się opanować sztukę wytłaczania liniowego z centrowaniem przy użyciu Aspose.3D dla .NET. Możesz eksperymentować z różnymi parametrami i odkrywać ogromne możliwości, jakie oferuje ta technika.

## Często zadawane pytania

### P1: Czy mogę używać Aspose.3D dla .NET z innymi językami programowania?

O1: Aspose.3D obsługuje przede wszystkim języki .NET, takie jak C# i VB.NET.

### P2: Gdzie mogę znaleźć pomoc dotyczącą zapytań związanych z Aspose.3D?

 A2: Odwiedź[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) za dedykowane wsparcie i dyskusje.

### P3: Czy dostępna jest bezpłatna wersja próbna Aspose.3D dla .NET?

 Odpowiedź 3: Tak, możesz uzyskać dostęp do bezpłatnego okresu próbnego[Tutaj](https://releases.aspose.com/).

### P4: Jak mogę uzyskać tymczasową licencję na Aspose.3D dla .NET?

 Odpowiedź 4: Możesz nabyć licencję tymczasową[Tutaj](https://purchase.aspose.com/temporary-license/).

### P5: Gdzie mogę kupić licencję Aspose.3D for .NET?

 A5: Kup licencję[Tutaj](https://purchase.aspose.com/buy).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
