---
date: 2026-01-17
description: Dowiedz się, jak zastosować materiał PBR do pudełka przy użyciu Aspose.3D
  dla .NET, utworzyć materiał PBR i wyeksportować pliki STL w formacie ASCII z renderowaniem
  opartym na fizyce.
linktitle: Applying PBR Material to Box
second_title: Aspose.3D .NET API
title: Jak zastosować materiał PBR do pudełka
url: /pl/net/geometry-and-hierarchy/apply-pbr-material-to-box/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Jak zastosować materiał PBR do sześcianu

## Wprowadzenie

Witamy w fascynującym świecie grafiki 3D! W tym przewodniku krok po kroku nauczysz się **jak zastosować materiał pbr** do sześcianu przy użyciu Aspose.3D for .NET. Przeprowadzimy Cię przez tworzenie materiału PBR, dodawanie go do siatki oraz **eksportowanie STL ASCII**, abyś mógł używać modelu w dowolnym dalszym procesie. Niezależnie od tego, czy tworzysz prototyp gry, czy wizualizację produktu, opanowanie tego przepływu otwiera drzwi do realistycznego renderowania fizycznie opartego (PBR) w aplikacjach .NET.

## Szybkie odpowiedzi
- **Jaki jest główny cel?** Zastosować materiał PBR do sześcianu i wyeksportować go jako STL ASCII.  
- **Jakiej biblioteki używamy?** Aspose.3D for .NET (how to use aspose).  
- **Czy potrzebna jest licencja?** Tak, wymagana jest tymczasowa lub pełna licencja do użytku produkcyjnego.  
- **Obsługiwany format wyjściowy?** STL ASCII (export stl ascii) oraz wiele innych formatów 3D.  
- **Ile to zajmuje?** Około 10‑15 minut dla podstawowej implementacji.

## Co to jest materiał PBR?
Physically Based Rendering (PBR) to model cieniowania, który symuluje, jak światło oddziałuje z rzeczywistymi powierzchniami. Poprzez dostosowanie właściwości takich jak współczynniki metaliczności i szorstkości, możesz uzyskać wysoce realistyczne wyniki bez ręcznego strojenia skomplikowanych shaderów.

## Dlaczego warto używać Physically Based Rendering (PBR)?
- **Realizm:** Materiały reagują na oświetlenie w sposób zgodny z rzeczywistą fizyką.  
- **Spójność:** Ten sam materiał wygląda poprawnie w dowolnym środowisku oświetleniowym.  
- **Wydajność:** Nowoczesne GPU są zoptymalizowane pod kątem obliczeń PBR, co zapewnia wydajność „za darmo”.

## Wymagania wstępne

Zanim przejdziesz do kodu, upewnij się, że masz następujące elementy:

### Pobierz i zainstaluj Aspose.3D for .NET
Odwiedź [dokumentację Aspose.3D for .NET](https://reference.aspose.com/3d/net/), aby uzyskać szczegółowe instrukcje dotyczące pobierania i instalacji biblioteki.

### Uzyskaj licencję
Aby odblokować pełny potencjał Aspose.3D, zdobądź ważną licencję. Tymczasową licencję możesz uzyskać [tutaj](https://purchase.aspose.com/temporary-license/), a pełną licencję – [tutaj](https://purchase.aspose.com/buy).

## Importowanie przestrzeni nazw
Najpierw zaimportuj niezbędne przestrzenie nazw, aby wykorzystać możliwości Aspose.3D for .NET:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Shading;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
```

## Krok 1: Inicjalizacja sceny
Rozpocznij od zainicjowania sceny 3D, używając poniższego fragmentu kodu:

```csharp
Scene scene = new Scene();
```

## Krok 2: Utworzenie materiału PBR
Teraz **tworzymy materiał pbr**, który nada naszemu sześcianowi realistyczny wygląd:

```csharp
PbrMaterial mat = new PbrMaterial();
```

## Krok 3: Ustawienie właściwości materiału
Dostosuj właściwości materiału, czyniąc go prawie metalicznym i bardzo szorstkim — idealnym dla szczotkowanego metalowego sześcianu:

```csharp
mat.MetallicFactor = 0.9;
mat.RoughnessFactor = 0.9;
```

## Krok 4: Utworzenie sześcianu
Wygeneruj sześcian, do którego zostanie zastosowany materiał PBR:

```csharp
var boxNode = scene.RootNode.CreateChildNode("box", new Box());
```

## Krok 5: Dodanie materiału PBR do sześcianu
Przypisz wcześniej skonfigurowany **add pbr material** do utworzonego węzła sześcianu:

```csharp
boxNode.Material = mat;
```

## Krok 6: Zapis sceny 3D jako STL ASCII
Na koniec **export stl ascii**, aby model mógł być otwarty w dowolnym standardowym przeglądarce 3D lub slicerze:

```csharp
scene.Save("Your Output Directory" + "PBR_Material_Box_Out.stl", FileFormat.STLASCII);
```

Gratulacje! Pomyślnie zastosowałeś materiał PBR do sześcianu w scenie 3D przy użyciu Aspose.3D for .NET.

## Typowe pułapki i wskazówki
- **Licencja nie znaleziona:** Upewnij się, że plik licencji jest wczytany przed jakimikolwiek wywołaniami Aspose; w przeciwnym razie biblioteka działa w trybie ewaluacyjnym.  
- **Nieprawidłowa ścieżka pliku:** Używaj `Path.Combine`, aby uniknąć brakujących separatorów ścieżek na różnych systemach operacyjnych.  
- **Roughness vs. Metallic:** Ustawienie obu współczynników na zbyt wysokie wartości może spowodować, że powierzchnia będzie wyglądać płasko; eksperymentuj z wartościami w przedziale 0.5‑0.9, aby uzyskać zrównoważony efekt.

## Zakończenie
Zanurzenie się w grafice 3D z Aspose.3D for .NET otwiera drzwi do nieograniczonych możliwości twórczych. Dzięki intuicyjnemu API i solidnym funkcjom tworzenie wizualnie zachwycających scen staje się przyjemnym doświadczeniem dla programistów. Następnym krokiem może być zamiana sześcianu na bardziej złożoną siatkę lub eksperymentowanie z różnymi teksturami PBR, aby zobaczyć, jak światło reaguje.

## Najczęściej zadawane pytania

**Q1: Czy Aspose.3D jest kompatybilny z innymi formatami plików 3D?**  
A1: Tak, Aspose.3D obsługuje różne formaty plików 3D, zapewniając elastyczność w Twoich projektach.

**Q2: Czy mogę używać Aspose.3D w aplikacjach komercyjnych?**  
A2: Oczywiście! Aspose.3D oferuje licencje komercyjne umożliwiające płynną integrację w Twoich aplikacjach.

**Q3: Czy dostępna jest wersja próbna?**  
A3: Tak, możesz poznać możliwości Aspose.3D, pobierając darmową wersję próbną [tutaj](https://releases.aspose.com/).

**Q4: Gdzie mogę znaleźć wsparcie społeczności i dyskusje?**  
A4: Dołącz do społeczności Aspose.3D na [forum Aspose.3D](https://forum.aspose.com/c/3d/18), aby uzyskać pomoc i wymienić się doświadczeniami.

**Q5: Jak uzyskać tymczasową licencję dla Aspose.3D?**  
A5: Tymczasową licencję możesz pobrać [tutaj](https://purchase.aspose.com/temporary-license/) w celach ewaluacyjnych.

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Ostatnia aktualizacja:** 2026-01-17  
**Testowano z:** Aspose.3D 24.11 for .NET  
**Autor:** Aspose  

---