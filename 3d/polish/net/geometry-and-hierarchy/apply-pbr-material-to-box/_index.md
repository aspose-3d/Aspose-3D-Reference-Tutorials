---
date: 2026-04-12
description: Dowiedz się, jak zastosować materiał PBR do pudełka przy użyciu Aspose.3D
  dla .NET, stworzyć materiał PBR i wyeksportować pliki STL w formacie ASCII z fizycznie
  opartym renderowaniem.
keywords:
- how to apply pbr
- create pbr material
- export stl ascii
- physically based rendering
- create box mesh
linktitle: Nakładanie materiału PBR na pudełko
second_title: Aspose.3D .NET API
title: Jak zastosować materiał PBR na pudełku
url: /pl/net/geometry-and-hierarchy/apply-pbr-material-to-box/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Jak zastosować materiał PBR do sześcianu

## Wprowadzenie

Witamy w fascynującym świecie grafiki 3D! W tym samouczku krok po kroku **dowiesz się, jak zastosować materiał pbr** do sześcianu przy użyciu Aspose.3D for .NET. Przejdziemy przez tworzenie materiału PBR, dodawanie go do siatki oraz w końcu **eksportowanie STL ASCII**, abyś mógł używać modelu w dowolnym dalszym procesie. Niezależnie od tego, czy tworzysz prototyp gry, wizualizator produktu, czy szybki prototyp do druku 3D, opanowanie tego przepływu otwiera drzwi do realistycznego renderowania opartego na fizyce (PBR) w Twoich aplikacjach .NET.

## Szybkie odpowiedzi
- **Jaki jest główny cel?** Zastosować materiał PBR do sześcianu i wyeksportować go jako STL ASCII.  
- **Jakiej biblioteki użyto?** Aspose.3D for .NET (how to use aspose).  
- **Czy potrzebna jest licencja?** Tak, wymagana jest tymczasowa lub pełna licencja do produkcji.  
- **Obsługiwany format wyjściowy?** STL ASCII (export stl ascii) oraz wiele innych formatów 3D.  
- **Jak długo to trwa?** Około 10‑15 minut dla podstawowej implementacji.

## Co to jest materiał PBR?

Physically Based Rendering (PBR) to model cieniowania, który symuluje, jak światło oddziałuje z rzeczywistymi powierzchniami. Poprzez dostosowanie właściwości, takich jak czynniki metaliczności i szorstkości, możesz uzyskać bardzo realistyczne wyniki bez ręcznego strojenia złożonych shaderów.

## Dlaczego używać Physically Based Rendering (PBR)?
- **Realizm:** Materiały reagują na oświetlenie w sposób zgodny z rzeczywistą fizyką.  
- **Spójność:** Ten sam materiał wygląda poprawnie w dowolnym środowisku oświetleniowym.  
- **Wydajność:** Nowoczesne GPU są zoptymalizowane pod kątem obliczeń PBR, zapewniając wydajność bez dodatkowych kosztów.

## Wymagania wstępne

Zanim zagłębimy się w kod, upewnij się, że masz następujące elementy:

### Pobierz i zainstaluj Aspose.3D for .NET
Odwiedź [dokumentację Aspose.3D for .NET](https://reference.aspose.com/3d/net/) aby uzyskać szczegółowe instrukcje dotyczące pobierania i instalacji biblioteki.

### Uzyskaj licencję
Aby odblokować pełny potencjał Aspose.3D, uzyskaj ważną licencję. Możesz otrzymać tymczasową licencję [tutaj](https://purchase.aspose.com/temporary-license/) lub zakupić pełną licencję [tutaj](https://purchase.aspose.com/buy).

## Importowanie przestrzeni nazw
Najpierw upewnij się, że zaimportowałeś niezbędne przestrzenie nazw, aby wykorzystać możliwości Aspose.3D for .NET:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Shading;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
```

## Przewodnik krok po kroku

### Krok 1: Inicjalizacja sceny
Rozpocznij od stworzenia pustej sceny 3D. Ten kontener będzie przechowywać całą geometrię, materiały i światła, które dodasz później.

```csharp
Scene scene = new Scene();
```

### Krok 2: Utworzenie materiału PBR
Teraz **tworzymy materiał pbr**, który nada naszemu sześcianowi realistyczny wygląd. Klasa `PbrMaterial` udostępnia wszystkie parametry potrzebne do renderowania opartego na fizyce.

```csharp
PbrMaterial mat = new PbrMaterial();
```

### Krok 3: Ustawienie właściwości materiału
Dopracuj właściwości materiału. W tym przykładzie sprawiamy, że powierzchnia jest prawie metaliczna i bardzo szorstka — idealna dla szczotkowanego metalowego sześcianu.

```csharp
mat.MetallicFactor = 0.9;
mat.RoughnessFactor = 0.9;
```

### Krok 4: Utworzenie siatki sześcianu
Wygeneruj prostą geometrię sześcianu. To jest krok **create box mesh**, do którego odnosi się główne słowo kluczowe.

```csharp
var boxNode = scene.RootNode.CreateChildNode("box", new Box());
```

### Krok 5: Zastosowanie materiału PBR do sześcianu
Przypisz wcześniej skonfigurowany **add pbr material** do węzła sześcianu, który właśnie utworzyliśmy.

```csharp
boxNode.Material = mat;
```

### Krok 6: Eksport STL ASCII (Jak wyeksportować STL)
Na koniec **export stl ascii**, aby model mógł być otwarty w dowolnym standardowym przeglądarce 3D lub slicerze. Użycie `FileFormat.STLASCII` zapewnia plik czytelny dla człowieka.

```csharp
scene.Save("Your Output Directory" + "PBR_Material_Box_Out.stl", FileFormat.STLASCII);
```

## Typowe pułapki i wskazówki
- **Licencja nie znaleziona:** Upewnij się, że plik licencji jest załadowany *przed* jakimikolwiek wywołaniami Aspose; w przeciwnym razie biblioteka działa w trybie ewaluacyjnym.  
- **Nieprawidłowa ścieżka pliku:** Użyj `Path.Combine`, aby uniknąć brakujących separatorów ścieżek w różnych systemach operacyjnych.  
- **Równowaga szorstkości i metaliczności:** Ustawienie obu czynników zbyt wysoko może spowodować, że powierzchnia będzie wyglądać płasko; eksperymentuj z wartościami od `0.5‑0.9`, aby uzyskać zrównoważony wygląd.  
- **Wskazówka dotycząca wydajności:** Użyj jednej instancji `PbrMaterial`, jeśli musisz zastosować ten sam materiał do wielu siatek; zmniejsza to zużycie pamięci.

## Najczęściej zadawane pytania

**Q1: Czy Aspose.3D jest kompatybilny z innymi formatami plików 3D?**  
A1: Tak, Aspose.3D obsługuje szeroką gamę formatów plików 3D, zapewniając elastyczność w Twoich projektach.

**Q2: Czy mogę używać Aspose.3D w aplikacjach komercyjnych?**  
A2: Absolutnie! Aspose.3D oferuje licencje komercyjne umożliwiające płynne włączenie do oprogramowania produkcyjnego.

**Q3: Czy dostępna jest wersja próbna?**  
A3: Tak, możesz zapoznać się z możliwościami Aspose.3D, pobierając darmową wersję próbną [tutaj](https://releases.aspose.com/).

**Q4: Gdzie mogę znaleźć wsparcie społeczności i dyskusje?**  
A4: Dołącz do społeczności Aspose.3D na [Aspose.3D Forums](https://forum.aspose.com/c/3d/18), aby uzyskać wsparcie i uczestniczyć w dyskusjach.

**Q5: Jak uzyskać tymczasową licencję dla Aspose.3D?**  
A5: Możesz uzyskać tymczasową licencję [tutaj](https://purchase.aspose.com/temporary-license/) do celów ewaluacyjnych.

## Podsumowanie
Zanurzenie się w grafikę 3D z Aspose.3D for .NET otwiera drzwi do nieograniczonych możliwości twórczych. Dzięki intuicyjnemu API i solidnym funkcjom, tworzenie wizualnie zachwycających scen staje się przyjemnym doświadczeniem dla programistów. Teraz, gdy wiesz **jak zastosować pbr** materiał do sześcianu i **wyeksportować STL ASCII**, spróbuj zamienić sześcian na bardziej złożoną siatkę lub eksperymentuj z mapami tekstur, aby zobaczyć, jak oświetlenie reaguje w czasie rzeczywistym.

---

**Last Updated:** 2026-04-12  
**Tested With:** Aspose.3D 24.11 for .NET  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}
{{< blocks/products/products-backtop-button >}}