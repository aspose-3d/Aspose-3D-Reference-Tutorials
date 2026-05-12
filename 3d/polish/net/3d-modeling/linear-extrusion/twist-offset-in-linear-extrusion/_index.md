---
date: 2026-03-23
description: Dowiedz się, jak dodać skręt w liniowej ekstruzji za pomocą Aspose.3D
  dla .NET i odkryj, jak wykorzystać ekstruzję w projektach modelowania 3D w ASP.NET.
linktitle: Twist Offset in Linear Extrusion
second_title: Aspose.3D .NET API
title: Jak dodać skręt w ekstruzji liniowej przy użyciu Aspose.3D dla .NET
url: /pl/net/3d-modeling/linear-extrusion/twist-offset-in-linear-extrusion/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Jak dodać skręt w liniowej ekstruzji przy użyciu Aspose.3D dla .NET

## Wprowadzenie

Jeśli szukasz przejrzystego, krok po kroku przewodnika **jak dodać skręt** do liniowej ekstruzji, jesteś we właściwym miejscu. W tym tutorialu przeprowadzimy Cię przez cały proces z użyciem Aspose.3D dla .NET, pokazując **jak używać ekstruzji** do tworzenia dynamicznych kształtów 3D, które są idealne dla scenariuszy *asp.net 3d modeling*. Po zakończeniu będziesz mieć gotowy przykład, który demonstruje offset skrętu, podziały (slices) oraz zapis wyniku jako plik OBJ.

## Szybkie odpowiedzi
- **Co robi „twist offset”?** Przesuwa punkt początkowy skrętu wzdłuż osi ekstruzji.  
- **Czy potrzebna jest licencja, aby uruchomić przykład?** Licencja tymczasowa wystarczy do testów; pełna licencja jest wymagana w produkcji.  
- **Jakie wersje .NET są wspierane?** .NET Framework 4.5+, .NET Core 3.1+, .NET 5/6+.  
- **Czy mogę zmienić liczbę podziałów?** Tak — dostosuj właściwość `Slices`, aby kontrolować gładkość siatki.  
- **Czy format wyjściowy jest ograniczony do OBJ?** Nie, Aspose.3D obsługuje wiele formatów; OBJ jest używany tutaj dla prostoty.

## Co to jest Twist Offset w liniowej ekstruzji?

Twist offset definiuje translacyjną zmianę stosowaną do operacji skrętu. Zamiast obracać się wokół dokładnego początku ekstruzji, geometria zaczyna się obracać od określonego wektora offsetu, dając większą kontrolę artystyczną nad ostatecznym kształtem.

## Dlaczego warto używać Aspose.3D dla .NET?

- **Pełnoprawne API** – Obsługuje profile, transformacje i szeroką gamę formatów plików.  
- **Cross‑platform** – Działa na Windows, Linux i macOS z .NET Core.  
- **Wydajność zoptymalizowana** – Generuje czyste siatki bez ręcznych obliczeń.  
- **Doskonale udokumentowane** – Mnóstwo przykładów przyspieszających rozwój.

## Wymagania wstępne

Zanim zaczniemy, upewnij się, że masz:

- Bibliotekę Aspose.3D dla .NET: Pobierz i zainstaluj bibliotekę ze [strony wydania](https://releases.aspose.com/3d/net/).  
- Środowisko programistyczne: Visual Studio, Rider lub dowolne IDE obsługujące C#.

## Importowanie przestrzeni nazw

Najpierw zaimportuj przestrzenie nazw, które dają dostęp do podstawowych klas 3D.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

Te instrukcje udostępniają w kodzie typy `Scene`, `LinearExtrusion`, `Vector3` i inne niezbędne elementy.

## Przewodnik krok po kroku

### Krok 1: Inicjalizacja podstawowego profilu

Zaczynamy od prostego prostokątnego profilu i nadajemy mu mały promień zaokrąglenia, aby krawędzie nie były idealnie ostre.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

### Krok 2: Utworzenie sceny

`Scene` działa jako kontener dla wszystkich węzłów, świateł, kamer i geometrii.

```csharp
Scene scene = new Scene();
```

### Krok 3: Utworzenie węzłów

Do korzenia sceny dodawane są dwa węzły potomne — jeden dla zwykłej ekstruzji, a drugi dla wersji ze skrętem. Lewy węzeł jest przesunięty wzdłuż osi X w celu wizualnego oddzielenia.

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(18, 0, 0);
```

### Krok 4: Liniowa ekstruzja w lewym węźle (bez offsetu skrętu)

Tutaj prezentujemy podstawową ekstruzję z pełnym skrętem 360° i 100 podziałami dla płynności.

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100 });
```

### Krok 5: Liniowa ekstruzja w prawym węźle z offsetem skrętu

Teraz stosujemy offset skrętu `(3, 0, 0)`. Przesuwa to początek skrętu o trzy jednostki wzdłuż osi X, tworząc widocznie przesuniętą helisę.

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100, TwistOffset = new Vector3(3, 0, 0) });
```

### Krok 6: Zapis sceny 3D

Na koniec zapisujemy scenę do pliku OBJ. Zmień ścieżkę wyjściową w razie potrzeby, aby pasowała do Twojego środowiska.

```csharp
scene.Save("Your Output Directory" + "TwistOffsetInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## Typowe problemy i rozwiązania

| Problem | Dlaczego się pojawia | Rozwiązanie |
|-------|----------------|-----|
| **Skręt wygląda płasko** | `Slices` jest ustawione zbyt nisko, co skutkuje grubą siatką. | Zwiększ `Slices` (np. do 200) dla płynniejszej rotacji. |
| **Obiekt jest poza środkiem** | `TwistOffset` używa współrzędnych świata; węzeł może już być przetłumaczony. | Zastosuj offset względem lokalnej transformacji węzła lub odpowiednio dostosuj translację węzła. |
| **Plik nie został zapisany** | Nieprawidłowa ścieżka wyjściowa lub brak uprawnień do zapisu. | Sprawdź, czy katalog istnieje i aplikacja ma prawo zapisu. |
| **Wyjątek licencyjny** | Uruchamianie bez ważnej licencji w wersji nie‑trial. | Załaduj tymczasową lub stałą licencję przed utworzeniem sceny. |

## Najczęściej zadawane pytania

### P1: Czy mogę używać Aspose.3D dla .NET z innymi językami programowania?

O1: Aspose.3D głównie wspiera języki .NET, ale Aspose oferuje podobne biblioteki dla Javy i innych platform.

### P2: Jak uzyskać tymczasową licencję dla Aspose.3D dla .NET?

O2: Odwiedź [ten link](https://purchase.aspose.com/temporary-license/), aby uzyskać tymczasową licencję do testów.

### P3: Czy istnieje forum społecznościowe dla Aspose.3D dla .NET?

O3: Oczywiście! Dołącz do społeczności na [forum Aspose.3D](https://forum.aspose.com/c/3d/18), aby wymieniać się doświadczeniami i uzyskać pomoc.

### P4: Czy dostępne są dodatkowe przykłady i dokumentacja?

O4: Przeglądaj [dokumentację](https://reference.aspose.com/3d/net/), aby znaleźć obszerne przewodniki i przykłady.

### P5: Gdzie mogę kupić Aspose.3D dla .NET?

O5: Przejdź do [tego linku](https://purchase.aspose.com/buy), aby dokonać zakupu i odblokować pełny potencjał Aspose.3D.

### P6: Czy mogę eksportować model do formatów innych niż OBJ?

O6: Tak — Aspose.3D obsługuje FBX, STL, 3MF i wiele innych. Wystarczy zmienić wartość enum `FileFormat` w wywołaniu `Save`.

### P7: Jak „dodawanie skrętu” różni się od zwykłej rotacji?

O7: Skręt stopniowo obraca profil wzdłuż długości ekstruzji, podczas gdy zwykła rotacja stosuje jednorazowy, stały kąt. Offset dodaje translacyjną zmianę przed rozpoczęciem rotacji.

---

**Ostatnia aktualizacja:** 2026-03-23  
**Testowano z:** Aspose.3D dla .NET (najnowsze wydanie)  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}