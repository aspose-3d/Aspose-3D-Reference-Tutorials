---
date: 2026-03-23
description: Dowiedz się, jak wykonać liniową ekstruzję z przekrojami przy użyciu
  Aspose.3D dla .NET. Twórz szczegółowe modele 3D z przykładami kodu krok po kroku.
linktitle: How to Linear Extrusion with Slices
second_title: Aspose.3D .NET API
title: Jak wykonać ekstruzję liniową z przekrojami przy użyciu Aspose.3D dla .NET
url: /pl/net/3d-modeling/linear-extrusion/slices-in-linear-extrusion/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Jak wykonać liniową ekstruzję z przekrojami przy użyciu Aspose.3D dla .NET

## Wprowadzenie

Witamy w świecie projektowania 3D przy użyciu Aspose.3D dla .NET! W tym samouczku odkryjesz **jak wykonać liniową ekstruzję** z przekrojami, technikę pozwalającą kontrolować poziom szczegółowości modeli. Niezależnie od tego, czy jesteś doświadczonym programistą, czy dopiero zaczynasz, przeprowadzimy Cię przez każdy krok, wyjaśnimy, dlaczego wykonujemy poszczególne czynności, i podamy praktyczne wskazówki, które możesz od razu zastosować.

## Szybkie odpowiedzi
- **Co to jest liniowa ekstruzja z przekrojami?** To metoda rozszerzania 2‑D profilu do 3‑D przy określaniu liczby pośrednich przekrojów (slices).  
- **Dlaczego używać przekrojów?** Więcej przekrojów daje płynniejszą krzywiznę; mniej przekrojów utrzymuje siatkę lekką.  
- **Wymagania wstępne?** Aspose.3D dla .NET, środowisko IDE kompatybilne z .NET oraz podstawowa znajomość C#.  
- **Typowy czas wykonania?** Przykład działa w mniej niż sekundę na nowoczesnym komputerze.  
- **Format wyjściowy?** Przykład zapisuje do Wavefront OBJ, ale Aspose.3D obsługuje wiele formatów.

## Co to jest liniowa ekstruzja z przekrojami?

Liniowa ekstruzja przyjmuje kształt 2‑D (profil) i rozciąga go wzdłuż prostej linii, tworząc bryłę 3‑D. Właściwość **Slices** określa, ile pośrednich przekrojów zostanie wstawionych pomiędzy początkiem a końcem ekstruzji, wpływając na gładkość i liczbę wielokątów.

## Dlaczego używać przekrojów w liniowej ekstruzji?

- **Kontrola gęstości siatki:** Precyzyjnie dopasuj równowagę między jakością wizualną a rozmiarem pliku.  
- **Optymalizacja wydajności:** Używaj mniej przekrojów w aplikacjach czasu rzeczywistego, więcej w renderach wysokiej rozdzielczości.  
- **Kreatywna elastyczność:** Łącz różne liczby przekrojów na oddzielnych obiektach, aby podkreślić zamierzenie projektowe.

## Wymagania wstępne

Zanim zanurzysz się w kod, upewnij się, że masz:

- Aspose.3D for .NET Library – pobierz ją z [tutaj](https://releases.aspose.com/3d/net/).  
- Środowisko IDE obsługujące C# (Visual Studio, Rider, VS Code, itp.).  
- Podstawową znajomość składni C# i koncepcji programowania obiektowego.  
- Ciekawość do eksperymentowania z geometrią 3‑D!

## Importowanie przestrzeni nazw

Najpierw zaimportuj przestrzenie nazw, które dają dostęp do podstawowych klas Aspose.3D.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Przewodnik krok po kroku

### Krok 1: Inicjalizacja podstawowego profilu

Zaczynamy od prostego prostokątnego kształtu i nadajemy mu mały promień zaokrąglenia, aby krawędzie nie były idealnie ostre.

```csharp
// ExStart:InitializeBaseProfile
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
// ExEnd:InitializeBaseProfile
```

### Krok 2: Utworzenie sceny 3D

`Scene` pełni rolę kontenera dla wszystkich węzłów, siatek, świateł i kamer.

```csharp
// ExStart:Create3DScene
Scene scene = new Scene();
// ExEnd:Create3DScene
```

### Krok 3: Dodanie węzłów lewego i prawego

Utworzymy dwa węzły siostrzane pod korzeniem sceny. Lewy węzeł otrzyma niską liczbę przekrojów, prawy wysoką, abyś mógł porównać różnicę wizualną.

```csharp
// ExStart:CreateLeftRightNodes
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(15, 0, 0);
// ExEnd:CreateLeftRightNodes
```

### Krok 4: Wykonanie liniowej ekstruzji na lewym węźle (niska szczegółowość)

Tutaj ekstruzujemy prostokąt przy użyciu tylko **2 przekrojów**. Powoduje to grubą siatkę — idealną do szybkich podglądów.

```csharp
// ExStart:LinearExtrusionLeftNode
left.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 2 });
// ExEnd:LinearExtrusionLeftNode
```

### Krok 5: Wykonanie liniowej ekstruzji na prawym węźle (wysoka szczegółowość)

Teraz używamy **10 przekrojów** dla znacznie płynniejszego wyniku. Zauważ, jak geometria staje się bardziej szczegółowa.

```csharp
// ExStart:LinearExtrusionRightNode
right.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 10 });
// ExEnd:LinearExtrusionRightNode
```

### Krok 6: Zapisanie sceny 3D

Na koniec zapisz scenę do pliku OBJ. Zastąp `"Your Output Directory"` prawidłową ścieżką na swoim komputerze.

```csharp
// ExStart:Save3DScene
scene.Save("Your Output Directory" + "SlicesInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
// ExEnd:Save3DScene
```

## Typowe problemy i rozwiązania

| Problem | Dlaczego się pojawia | Rozwiązanie |
|---------|----------------------|-------------|
| **Nie utworzono pliku** | Ścieżka wyjściowa jest nieprawidłowa lub brakuje uprawnień do zapisu. | Użyj ścieżki bezwzględnej i upewnij się, że folder istnieje. |
| **Obiekt wygląda płasko** | `Slices` ustawione na 1 lub 0. | Ustaw `Slices` na co najmniej 2, aby ekstruzja była widoczna. |
| **Nieoczekiwana geometria** | Zbyt duży promień zaokrąglenia w stosunku do rozmiaru prostokąta. | Dostosuj `RoundingRadius` do wartości mniejszej niż połowa krótszego boku prostokąta. |

## Najczęściej zadawane pytania

**P: Czy mogę zmienić kierunek ekstruzji?**  
O: Tak. Użyj właściwości `Transform` na węźle, aby obrócić lub przemieścić ekstruzowaną geometrię przed zapisem.

**P: Czy Aspose.3D obsługuje inne typy ekstruzji?**  
O: Zdecydowanie. Oprócz `LinearExtrusion` możesz używać `RevolveExtrusion`, `SweepExtrusion` i innych.

**P: Do jakich formatów plików mogę eksportować?**  
O: Aspose.3D obsługuje OBJ, STL, FBX, 3MF, Collada i wiele innych. Wystarczy zmienić wartość enum `FileFormat`.

**P: Czy istnieje sposób na programowe ustawienie materiału?**  
O: Tak. Po utworzeniu węzła przypisz `Material` do jego kolekcji `Entity`.

**P: Jak liczba przekrojów wpływa na zużycie pamięci?**  
O: Więcej przekrojów zwiększa liczbę wierzchołków i ścian, co proporcjonalnie podnosi zużycie pamięci. Użyj profilowania, aby znaleźć optymalny punkt dla docelowej platformy.

## Oryginalne FAQ

### P1: Czy mogę używać Aspose.3D dla .NET z innymi językami programowania?

O1: Aspose.3D jest przede wszystkim przeznaczony dla .NET, ale możesz badać opcje interoperacyjności z językami takimi jak Python przy użyciu powiązań .NET.

### P2: Gdzie mogę znaleźć szczegółową dokumentację Aspose.3D dla .NET?

O2: Odwołaj się do dokumentacji [tutaj](https://reference.aspose.com/3d/net/) po szczegółowe informacje o możliwościach i użyciu Aspose.3D.

### P3: Czy dostępna jest darmowa wersja próbna Aspose.3D dla .NET?

O3: Tak, możesz pobrać darmową wersję próbną [tutaj](https://releases.aspose.com/) , aby przetestować funkcje biblioteki przed zakupem.

### P4: Jak mogę uzyskać wsparcie techniczne dla Aspose.3D dla .NET?

O4: Odwiedź forum Aspose.3D [tutaj](https://forum.aspose.com/c/3d/18), aby uzyskać pomoc i skontaktować się ze społecznością.

### P5: Czy mogę używać tymczasowej licencji dla Aspose.3D dla .NET?

O5: Tak, uzyskaj tymczasową licencję [tutaj](https://purchase.aspose.com/temporary-license/) do celów ewaluacji.

## Podsumowanie

Teraz zobaczyłeś **jak wykonać liniową ekstruzję** z przekrojami przy użyciu Aspose.3D dla .NET, zbadałeś wpływ różnych liczby przekrojów i nauczyłeś się eksportować swoją pracę. Eksperymentuj z innymi profilami, baw się wartością `Slices` i integruj materiały lub światła, aby tworzyć gotowe do produkcji zasoby 3‑D.

---

**Last Updated:** 2026-03-23  
**Tested With:** Aspose.3D 24.11 for .NET (latest at time of writing)  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}