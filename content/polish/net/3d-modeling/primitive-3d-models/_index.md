---
title: Tworzenie prymitywnych modeli 3D
linktitle: Tworzenie prymitywnych modeli 3D
second_title: Aspose.3D API .NET
description: Poznaj świat modelowania 3D z Aspose.3D dla .NET. Twórz oszałamiające, prymitywne modele bez wysiłku.
type: docs
weight: 10
url: /pl/net/3d-modeling/primitive-3d-models/
---
## Wstęp

Witamy w ekscytującym świecie modelowania 3D z Aspose.3D dla .NET! W tym kompleksowym samouczku będziemy krok po kroku badać proces tworzenia prymitywnych modeli 3D przy użyciu Aspose.3D. Niezależnie od tego, czy jesteś doświadczonym programistą, czy ciekawskim początkującym, ten przewodnik pomoże Ci wykorzystać moc Aspose.3D do tworzenia oszałamiających wizualnie elementów 3D dla Twoich projektów.

## Warunki wstępne

Zanim zagłębimy się w fascynującą dziedzinę modelowania 3D, upewnij się, że spełniasz następujące wymagania wstępne:

- Aspose.3D dla .NET: Pobierz i zainstaluj bibliotekę Aspose.3D dla .NET z[link do pobrania](https://releases.aspose.com/3d/net/).

- Środowisko programistyczne: Skonfiguruj środowisko programistyczne .NET, zapewniając kompatybilność z Aspose.3D.

Teraz, gdy masz już wszystko, co niezbędne, wyruszmy w podróż polegającą na tworzeniu krok po kroku prymitywnych modeli 3D.

## Importuj przestrzenie nazw

Rozpocznij od zaimportowania niezbędnych przestrzeni nazw, aby uzyskać dostęp do funkcjonalności zapewnianej przez Aspose.3D:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
```

Mając te przestrzenie nazw, możesz uwolnić moc Aspose.3D w swojej aplikacji .NET.

## Krok 1: Zainicjuj obiekt sceny

```csharp
//Zainicjuj obiekt Scene
Scene scene = new Scene();
```

Utwórz nowy obiekt sceny, który posłuży jako płótno dla Twojego arcydzieła 3D.

## Krok 2: Utwórz model pudełka

```csharp
// Utwórz model pudełkowy
scene.RootNode.CreateChildNode("box", new Box());
```

Dodaj model pudełkowy do katalogu głównego swojej sceny. Dostosuj wymiary i właściwości pudełka do swojej kreatywnej wizji.

## Krok 3: Utwórz model cylindra

```csharp
// Utwórz model cylindra
scene.RootNode.CreateChildNode("cylinder", new Cylinder());
```

Wzbogać swoją scenę, wprowadzając model cylindryczny. Dostosuj jego parametry, aby uzyskać pożądany kształt i rozmiar.

## Krok 4: Zapisz rysunek w formacie FBX

```csharp
// Zapisz rysunek w formacie FBX
var output = "Your Output Directory" + "test.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

Zapisz swoje arcydzieło 3D w formacie FBX. Wybierz odpowiedni katalog wyjściowy i nazwę pliku dla swojego dzieła.

## Krok 5: Wyświetl komunikat o powodzeniu

```csharp
// Wyświetl komunikat o powodzeniu
Console.WriteLine("\nBuilding a scene from primitive 3D models successfully.\nFile saved at " + output);
```

Świętuj swoje osiągnięcie! Scena została pomyślnie zbudowana z prymitywnych modeli 3D, a plik został zapisany.

## Wniosek

 Gratulacje! Udało Ci się stworzyć wspaniałe modele 3D przy użyciu Aspose.3D dla .NET. W tym przewodniku omówiono podstawy, ale możliwości są nieograniczone. Poznaj[dokumentacja](https://reference.aspose.com/3d/net/) dla bardziej zaawansowanych funkcji i technik.

## Często zadawane pytania

### P1: Czy mogę używać Aspose.3D dla .NET z innymi językami programowania?

Odpowiedź 1: Aspose.3D obsługuje przede wszystkim .NET, ale dostępne są inne wersje dla Java i innych platform.

### P2: Czy dostępny jest bezpłatny okres próbny?

 Odpowiedź 2: Tak, możesz poznać możliwości Aspose.3D za pomocą[bezpłatna wersja próbna](https://releases.aspose.com/).

### P3: Gdzie mogę znaleźć wsparcie dla Aspose.3D dla .NET?

 A3: Odwiedź[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) za wsparcie społeczności i dyskusje.

### P4: Jak mogę uzyskać licencję tymczasową?

 A4: Możesz uzyskać licencję tymczasową[Tutaj](https://purchase.aspose.com/temporary-license/).

### P5: Czy dostępne są przykładowe samouczki?

 Odpowiedź 5: Tak, przejrzyj więcej samouczków i przykładów w[dokumentacja](https://reference.aspose.com/3d/net/).