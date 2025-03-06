---
title: Kierunek w wytłaczaniu liniowym
linktitle: Kierunek w wytłaczaniu liniowym
second_title: Aspose.3D API .NET
description: Odblokuj świat modelowania 3D dzięki Aspose.3D dla .NET. Naucz się kierunku wytłaczania liniowego, zwiększ kreatywność i bez wysiłku twórz wciągające aplikacje.
weight: 11
url: /pl/net/3d-modeling/linear-extrusion/direction-in-linear-extrusion/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Kierunek w wytłaczaniu liniowym

## Wstęp

W dynamicznym świecie tworzenia oprogramowania tworzenie wciągających modeli 3D jest umiejętnością niezbędną. Aspose.3D dla .NET zapewnia programistom solidny zestaw narzędzi pozwalających wykorzystać potencjał modelowania 3D w ich aplikacjach. W tym samouczku zagłębimy się w intrygujący świat wytłaczania liniowego i poznamy niuanse funkcji „Kierunek w wytłaczaniu liniowym”.

## Warunki wstępne

Zanim wyruszymy w tę ekscytującą podróż, upewnij się, że spełniasz następujące wymagania wstępne:

-  Aspose.3D dla .NET: Pobierz i zainstaluj bibliotekę z[Dokumentacja Aspose.3D .NET](https://reference.aspose.com/3d/net/).

- Środowisko programistyczne: Upewnij się, że masz skonfigurowane działające środowisko programistyczne .NET.

## Importuj przestrzenie nazw

projekcie .NET zaimportuj niezbędne przestrzenie nazw, aby uzyskać dostęp do funkcjonalności Aspose.3D. Dodaj następujące linie na początku kodu:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Krok 1: Zainicjuj profil podstawowy

Rozpocznij od zainicjowania profilu bazowego, który ma zostać wyciągnięty. W tym przykładzie tworzymy kształt prostokąta o promieniu zaokrąglenia 0,3.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## Krok 2: Utwórz scenę 3D

Zbuduj podstawę dla swojego arcydzieła 3D, tworząc scenę.

```csharp
Scene scene = new Scene();
```

## Krok 3: Utwórz węzły

Wygeneruj węzły w scenie, aby reprezentować różne komponenty środowiska 3D.

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(8, 0, 0);
```

## Krok 4: Wytłaczanie liniowe bez kierunku

 Wykonaj wytłaczanie liniowe w lewym węźle za pomocą`Twist` I`Slices` nieruchomości.

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100 });
```

## Krok 5: Wytłaczanie liniowe z kierunkiem

 Rozszerz możliwości wytłaczania, włączając`Direction` właściwość w prawym węźle.

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100, Direction = new Vector3(0.3, 0.2, 1) });
```

## Krok 6: Zapisz scenę 3D

 Zachowaj swoje dzieło, zapisując scenę 3D. Zastępować`"Your Output Directory"` z żądanym katalogiem.

```csharp
scene.Save("Your Output Directory" + "DirectionInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

Gratulacje! Pomyślnie wdrożyłeś wytłaczanie liniowe w Aspose.3D dla .NET, badając zarówno podejście tradycyjne, jak i kierunkowe.

## Wniosek

tym samouczku poruszaliśmy się po fascynującej dziedzinie modelowania 3D przy użyciu Aspose.3D dla .NET. Wytłaczanie liniowe, z kierunkiem lub bez, otwiera nieograniczone możliwości dla programistów pragnących tworzyć oszałamiające wizualnie aplikacje. Dzięki Aspose.3D moc modelowania 3D jest na wyciągnięcie ręki.

## Często zadawane pytania

### P1: Jak mogę uzyskać tymczasową licencję na Aspose.3D dla .NET?

 Odpowiedź 1: Odwiedź[Aspose licencja tymczasowa](https://purchase.aspose.com/temporary-license/) aby uzyskać licencję tymczasową.

### P2: Gdzie mogę znaleźć wsparcie dla Aspose.3D?

 A2: Dołącz do[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) szukać pomocy i nawiązywać kontakt ze społecznością.

### P3: Czy dostępny jest bezpłatny okres próbny?

 Odpowiedź 3: Tak, poznaj funkcje w bezpłatnej wersji próbnej na stronie[Wydania Aspose.3D](https://releases.aspose.com/).

### P4: Jak kupić Aspose.3D dla .NET?

 A4: Przejdź do[Strona zakupu Aspose](https://purchase.aspose.com/buy) w celu uzyskania informacji o opcjach licencjonowania i szczegółach zakupu.

### P5: Gdzie mogę znaleźć szczegółową dokumentację Aspose.3D dla .NET?

 A5: Zapoznaj się z kompleksowym[Dokumentacja Aspose.3D .NET](https://reference.aspose.com/3d/net/) w celu uzyskania szczegółowych informacji.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
