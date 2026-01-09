---
date: 2026-01-09
description: Dowiedz się, jak tworzyć scenę 3D i zapisywać model 3D przy użyciu Aspose.3D
  dla .NET, w tym eksportować plik Wavefront OBJ oraz wycinki ekstruzji liniowej.
linktitle: Create 3D Scene with Linear Extrusion Slices
second_title: Aspose.3D .NET API
title: Utwórz scenę 3D z liniowymi wycinkami ekstruzji
url: /pl/net/3d-modeling/linear-extrusion/slices-in-linear-extrusion/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Tworzenie sceny 3D z wycinkami liniowej ekstruzji

## Wprowadzenie

Witamy w świecie projektowania 3D przy użyciu Aspose.3D dla .NET! W tym samouczku **utworzysz scenę 3D**, zastosujesz liniową ekstruzję z niestandardową liczbą wycinków oraz w końcu **zapiszesz model 3D** jako plik Wavefront OBJ. Niezależnie od tego, czy tworzysz szybki prototyp, czy gotową do produkcji wizualizację, poniższe kroki pokażą Ci **jak używać Aspose**, aby generować wysokiej jakości geometrie bezpośrednio z C#.

## Szybkie odpowiedzi
- **Co oznacza „create 3d scene”?** Oznacza to utworzenie obiektu Scene, który przechowuje wszystkie elementy 3D (siatki, światła, kamery).  
- **Jaki format jest używany do eksportu?** Przykład eksportuje do **Wavefront OBJ** (`export wavefront obj`).  
- **Ile wycinków mogę ustawić?** Możesz ustawić dowolną liczbę całkowitą; demonstracja pokazuje 2 i 10 wycinków.  
- **Czy potrzebna jest licencja?** Do użytku produkcyjnego wymagana jest tymczasowa lub pełna licencja.  
- **Czy mogę uruchomić to na .NET Core?** Tak, Aspose.3D obsługuje .NET Framework i .NET Core.

## Wymagania wstępne

Zanim zanurzysz się w świat projektowania 3D z Aspose.3D, upewnij się, że spełniasz następujące wymagania:

- Biblioteka Aspose.3D dla .NET: Upewnij się, że masz zainstalowaną bibliotekę Aspose.3D. Możesz ją pobrać [tutaj](https://releases.aspose.com/3d/net/).

- Zintegrowane środowisko programistyczne (IDE): Użyj dowolnego preferowanego IDE kompatybilnego z programowaniem w .NET.

- Podstawowa znajomość C#: Zapoznaj się z podstawami języka programowania C#.

- Chęć eksploracji projektowania 3D: Pasja do tworzenia wizualnie zachwycających modeli 3D!

## Importowanie przestrzeni nazw

Aby rozpocząć przygodę z projektowaniem 3D przy użyciu Aspose.3D, musisz zaimportować niezbędne przestrzenie nazw. Dzięki temu Twój kod będzie miał dostęp do wymaganych klas i funkcjonalności.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Jak utworzyć scenę 3D z liniową ekstruzją

Poniżej przechodzimy krok po kroku przez wszystkie etapy budowy sceny, zastosowania ekstruzji i **zapisania modelu 3D** jako pliku OBJ. Wyjaśnienia są napisane w przyjaznym tonie, abyś mógł łatwo podążać za instrukcją.

### Krok 1: Inicjalizacja profilu bazowego

Najpierw definiujemy kształt 2‑D, który zostanie wyekstruzowany. W tym przypadku prostokąt z zaokrąglonymi narożnikami.

```csharp
// ExStart:InitializeBaseProfile
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
// ExEnd:InitializeBaseProfile
```

### Krok 2: Utworzenie sceny 3D

Obiekt `Scene` jest kontenerem dla całej geometrii, świateł i kamer – rdzeniem **tworzenia sceny 3D**.

```csharp
// ExStart:Create3DScene
Scene scene = new Scene();
// ExEnd:Create3DScene
```

### Krok 3: Utworzenie węzłów lewego i prawego

Dodajemy dwa węzły potomne do korzenia sceny. Jeden będzie używał małej liczby wycinków, drugi większej, abyś mógł zobaczyć różnicę wizualną.

```csharp
// ExStart:CreateLeftRightNodes
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(15, 0, 0);
// ExEnd:CreateLeftRightNodes
```

### Krok 4: Wykonanie liniowej ekstruzji na lewym węźle

Tutaj ekstruzujemy prostokąt z **2 wycinkami**. Mniejsza liczba wycinków daje bardziej szorstki wygląd.

```csharp
// ExStart:LinearExtrusionLeftNode
left.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 2 });
// ExEnd:LinearExtrusionLeftNode
```

### Krok 5: Wykonanie liniowej ekstruzji na prawym węźle

Teraz ekstruzujemy ten sam profil, ale z **10 wycinkami**, co daje gładszą powierzchnię.

```csharp
// ExStart:LinearExtrusionRightNode
right.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 10 });
// ExEnd:LinearExtrusionRightNode
```

### Krok 6: Zapis sceny 3D

Na koniec eksportujemy scenę do pliku Wavefront OBJ. To pokazuje **jak zapisać obj** i **export wavefront obj** przy użyciu Aspose.3D.

```csharp
// ExStart:Save3DScene
scene.Save("Your Output Directory" + "SlicesInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
// ExEnd:Save3DScene
```

## Typowe problemy i rozwiązania

| Problem | Dlaczego się pojawia | Rozwiązanie |
|---------|----------------------|-------------|
| Plik OBJ jest pusty | Ścieżka wyjściowa jest nieprawidłowa lub brakuje uprawnień do zapisu. | Sprawdź, czy katalog istnieje i aplikacja ma dostęp do zapisu. |
| Wycinki nie wpływają na gładkość | Wartość `Slices` jest zbyt niska w stosunku do rozmiaru geometrii. | Zwiększ liczbę wycinków lub dostosuj wymiary profilu. |
| Wyjątek licencyjny | Uruchamianie bez ważnej licencji w wersji nie‑trial. | Zastosuj tymczasową lub stałą licencję używając `License license = new License(); license.SetLicense("Aspose.3D.lic");` |

## Najczęściej zadawane pytania

**P: Czy mogę używać Aspose.3D dla .NET z innymi językami programowania?**  
O: Aspose.3D jest głównie przeznaczony dla .NET, ale możesz badać opcje interoperacyjności z językami takimi jak Python przy użyciu powiązań .NET.

**P: Gdzie znajdę szczegółową dokumentację Aspose.3D dla .NET?**  
O: Zapoznaj się z dokumentacją [tutaj](https://reference.aspose.com/3d/net/) aby uzyskać szczegółowe informacje o możliwościach i użyciu Aspose.3D.

**P: Czy dostępna jest darmowa wersja próbna Aspose.3D dla .NET?**  
O: Tak, możesz pobrać darmową wersję próbną [tutaj](https://releases.aspose.com/) aby wypróbować funkcje biblioteki przed zakupem.

**P: Jak mogę uzyskać wsparcie techniczne dla Aspose.3D dla .NET?**  
O: Odwiedź forum Aspose.3D [tutaj](https://forum.aspose.com/c/3d/18), aby uzyskać pomoc i skontaktować się ze społecznością.

**P: Czy mogę używać tymczasowej licencji dla Aspose.3D dla .NET?**  
O: Tak, tymczasową licencję można uzyskać [tutaj](https://purchase.aspose.com/temporary-license/) w celach ewaluacyjnych.

## Zakończenie

Gratulacje! Pomyślnie nauczyłeś się **tworzyć scenę 3D**, stosować liniową ekstruzję z niestandardową liczbą wycinków oraz **zapisywać model 3D** jako plik Wavefront OBJ przy użyciu Aspose.3D dla .NET. To dopiero początek Twojej przygody z projektowaniem 3D — eksperymentuj z różnymi profilami, wartościami wycinków i formatami eksportu, aby w pełni wykorzystać potencjał **modelowania 3d c#**.

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Ostatnia aktualizacja:** 2026-01-09  
**Testowane z:** Aspose.3D 24.11 dla .NET  
**Autor:** Aspose