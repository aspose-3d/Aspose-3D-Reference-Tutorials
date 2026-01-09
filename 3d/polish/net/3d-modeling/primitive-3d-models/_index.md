---
date: 2026-01-09
description: Dowiedz się, jak tworzyć proste modele 3D w kształcie pudełka i jak zapisywać
  pliki FBX przy użyciu Aspose.3D dla .NET. Eksportuj modele 3D FBX bez wysiłku.
linktitle: How to Create Box Primitive 3D Model with Aspose.3D
second_title: Aspose.3D .NET API
title: Jak utworzyć model 3D sześcianu przy użyciu Aspose.3D
url: /pl/net/3d-modeling/primitive-3d-models/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Tworzenie prymitywnych modeli 3D

## Wprowadzenie

Witamy w ekscytującym świecie modelowania 3D z Aspose.3D dla .NET! W tym kompleksowym samouczku pokażemy Ci **jak stworzyć sześcian** prymitywne modele 3D, przeprowadzimy przez kroki **jak zapisać FBX**, i damy Ci pewność, aby **eksportować model 3D FBX** do użycia w dowolnym pipeline. Niezależnie od tego, czy jesteś doświadczonym programistą, czy dopiero zaczynasz, znajdziesz jasne, praktyczne wskazówki, które możesz od razu zastosować.

## Szybkie odpowiedzi
- **Jaki jest główny cel?** Naucz się, jak tworzyć prymitywne modele 3D typu sześcian z Aspose.3D.  
- **Jaki format jest używany do eksportu?** Format FBX (FileFormat.FBX7500ASCII).  
- **Czy potrzebna jest licencja?** Dostępna jest bezpłatna wersja próbna; licencja jest wymagana w produkcji.  
- **Jakie środowisko jest wymagane?** Dowolne środowisko programistyczne .NET kompatybilne z Aspose.3D.  
- **Jak długo to trwa?** Około 10‑15 minut na wygenerowanie podstawowej sceny.

## Czym jest prymitywny model 3D?

Prymitwy model 3D to podstawowy kształt geometryczny — taki jak sześcian, kula lub cylinder — używany jako element budulcowy bardziej złożonych scen. Aspose.3D udostępnia gotowe klasy, które pozwalają tworzyć te kształty jedną linią kodu.

## Dlaczego używać Aspose.3D dla .NET?

- **Renderowanie bez zależności** – nie wymaga zewnętrznego silnika graficznego.  
- **Bogate wsparcie formatów** – eksport bezpośrednio do FBX, OBJ, STL i innych.  
- **Pełna integracja z .NET** – działa z .NET Framework, .NET Core oraz .NET 5/6+.  

## Prerequisites

Zanim zagłębimy się w fascynujący świat modelowania 3D, upewnij się, że masz spełnione następujące wymagania:

- Aspose.3D for .NET: Pobierz i zainstaluj bibliotekę Aspose.3D dla .NET z [linku do pobrania](https://releases.aspose.com/3d/net/).

- Środowisko programistyczne: Skonfiguruj środowisko programistyczne .NET, zapewniając kompatybilność z Aspose.3D.

Teraz, gdy masz wszystkie niezbędne elementy, rozpocznijmy naszą podróż tworzenia prymitywnych modeli 3D krok po kroku.

## Importowanie przestrzeni nazw

Rozpocznij od zaimportowania niezbędnych przestrzeni nazw, aby uzyskać dostęp do funkcjonalności udostępnianej przez Aspose.3D:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
```

Z tymi przestrzeniami nazw jesteś gotowy, aby uwolnić moc Aspose.3D w swojej aplikacji .NET.

## Jak stworzyć prymitywny model 3D typu sześcian

### Krok 1: Zainicjalizuj obiekt sceny

```csharp
// Initialize a Scene object
Scene scene = new Scene();
```

Utwórz nowy obiekt sceny, który służy jako płótno dla Twojego dzieła 3D.

### Krok 2: Utwórz model sześcianu

```csharp
// Create a Box model
scene.RootNode.CreateChildNode("box", new Box());
```

Dodaj model sześcianu do korzenia sceny. To jest sedno **jak stworzyć sześcian** geometrycznie. Możesz później dostosować jego wymiary w razie potrzeby.

### Krok 3: Utwórz model cylindra

```csharp
// Create a Cylinder model
scene.RootNode.CreateChildNode("cylinder", new Cylinder());
```

Ulepsz scenę, wprowadzając model cylindra. Dostosuj jego parametry, aby uzyskać pożądany kształt i rozmiar.

### Krok 4: Zapisz rysunek w formacie FBX (Jak zapisać FBX)

```csharp
// Save drawing in the FBX format
var output = "Your Output Directory" + "test.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

Tutaj demonstrujemy **jak zapisać FBX** — scena jest eksportowana jako plik FBX, który możesz zaimportować do większości narzędzi 3D. Ten krok pokazuje również, jak **eksportować model 3D FBX** do dalszych przepływów pracy.

### Krok 5: Wyświetl komunikat o sukcesie

```csharp
// Display success message
Console.WriteLine("\nBuilding a scene from primitive 3D models successfully.\nFile saved at " + output);
```

Świętuj swoje osiągnięcie! Scena została pomyślnie zbudowana z prymitywnych modeli 3D, a plik został zapisany.

## Typowe problemy i rozwiązania
- **Ścieżka wyjściowa nie znaleziona** – Upewnij się, że katalog podany w `output` istnieje lub użyj `Path.Combine` z `Environment.CurrentDirectory`.  
- **Wyjątek licencyjny** – Wymagana jest ważna licencja Aspose.3D do użytku produkcyjnego; wersja próbna działa w ocenie.  
- **Nieprawidłowa wersja FBX** – Kod używa `FBX7500ASCII`; przełącz na inną wartość wyliczenia `FileFormat`, jeśli potrzebujesz innej wersji.

## FAQ

### P1: Czy mogę używać Aspose.3D dla .NET z innymi językami programowania?
O1: Aspose.3D głównie wspiera .NET, ale dostępne są inne wersje dla Javy i innych platform.

### P2: Czy dostępna jest bezpłatna wersja próbna?
O2: Tak, możesz przetestować możliwości Aspose.3D korzystając z [bezpłatnej wersji próbnej](https://releases.aspose.com/).

### P3: Gdzie mogę znaleźć wsparcie dla Aspose.3D dla .NET?
O3: Odwiedź [forum Aspose.3D](https://forum.aspose.com/c/3d/18) w celu uzyskania wsparcia społeczności i dyskusji.

### P4: Jak mogę uzyskać tymczasową licencję?
O4: Tymczasową licencję możesz uzyskać [tutaj](https://purchase.aspose.com/temporary-license/).

### P5: Czy dostępne są przykładowe samouczki?
O5: Tak, odkryj więcej samouczków i przykładów w [dokumentacji](https://reference.aspose.com/3d/net/).

## Najczęściej zadawane pytania

**P: Czy mogę wyeksportować scenę do innych formatów oprócz FBX?**  
O: Tak, Aspose.3D obsługuje OBJ, STL, 3MF i wiele innych. Wystarczy zmienić wyliczenie `FileFormat` przy wywołaniu `scene.Save()`.

**P: Czy można dostosować wymiary sześcianu?**  
O: Oczywiście. Użyj konstruktora `Box(double width, double height, double depth)`, aby ustawić własne rozmiary.

**P: Czy potrzebny jest 64‑bitowy system operacyjny, aby uruchomić wyeksportowany plik FBX?**  
O: Nie, plik FBX jest niezależny od platformy; każdy nowoczesny przeglądarka 3D może go otworzyć.

**P: Jak dodać materiały lub tekstury do prymitywów?**  
O: Utwórz obiekt `Material`, przypisz go do właściwości `Material` węzła i opcjonalnie ustaw mapy tekstur.

## Zakończenie

Gratulacje! Pomyślnie nauczyłeś się **jak stworzyć sześcian** prymitywnych modeli 3D, zapisałeś je jako plik FBX i odkryłeś sposoby **eksportowania modelu 3D FBX** do dalszego użycia. Ten przewodnik obejmuje podstawy, ale możliwości są nieograniczone. Zagłęb się w [dokumentację](https://reference.aspose.com/3d/net/), aby odkryć zaawansowane funkcje, takie jak oświetlenie, animacja i skomplikowana manipulacja siatką.

---

**Ostatnia aktualizacja:** 2026-01-09  
**Testowano z:** Aspose.3D 24.11 dla .NET  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}