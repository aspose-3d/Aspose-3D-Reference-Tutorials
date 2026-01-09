---
date: 2026-01-09
description: Naucz się tworzyć sceny 3D w .NET przy użyciu Aspose.3D i odkryj, jak
  stosować skręcanie ekstruzji techniką skrętu liniowego.
linktitle: Twist in Linear Extrusion
second_title: Aspose.3D .NET API
title: Utwórz scenę 3D .NET – skręt w ekstruzji liniowej
url: /pl/net/3d-modeling/linear-extrusion/twist-in-linear-extrusion/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Utwórz scenę 3D .NET – Skręt w ekstruzji liniowej

## Wprowadzenie

W ciągle rozwijającym się świecie programowania .NET wykorzystanie mocy grafiki 3D jest ekscytującym przedsięwzięciem. **Aspose.3D for .NET** pojawia się jako cenne narzędzie, umożliwiając programistom **tworzenie scen 3D .NET** aplikacji, które są zarówno immersyjne, jak i wizualnie zachwycające. W tym kompleksowym przewodniku przyjrzymy się fascynującej funkcji — Ekstruzja liniowa z obrotem — i przeprowadzimy Cię krok po kroku, abyś mógł z pewnością dodawać dynamiczne skręty do swoich modeli.

## Szybkie odpowiedzi
- **Co oznacza „create 3d scene .net”?** Odnosi się do programowego budowania sceny 3‑D przy użyciu biblioteki Aspose.3D w środowisku .NET.  
- **Jak dodać skręt do ekstruzji?** Ustaw właściwość `Twist` w obiekcie `LinearExtrusion`; wartość to kąt obrotu w stopniach.  
- **Czy potrzebna jest licencja na Aspose.3D?** Darmowa wersja próbna wystarcza do oceny; licencja komercyjna jest wymagana do użytku produkcyjnego.  
- **Jakie wersje .NET są obsługiwane?** .NET Framework 4.5+, .NET Core 3.1+, .NET 5/6 i późniejsze.  
- **Jaki wpływ ma wartość `Slices`?** Więcej warstw (slices) zapewnia płynniejszy skręt, ale zwiększa zużycie pamięci i czas przetwarzania.

## Czym jest ekstruzja liniowa z obrotem?

Ekstruzja liniowa przemieszcza profil 2‑D wzdłuż prostej ścieżki, podczas gdy właściwość **twist** stopniowo obraca profil, tworząc efekt helisy. Technika ta jest idealna do modelowania sprężyn, skręconych kolumn lub elementów dekoracyjnych.

## Dlaczego warto używać Aspose.3D do tego zadania?

- **Proste API** – intuicyjne klasy takie jak `LinearExtrusion` i `RectangleShape`.  
- **Pełna integracja z .NET** – działa bezproblemowo z C#, VB.NET i F#.  
- **Wynik wieloplatformowy** – eksport do OBJ, STL, FBX i wielu innych formatów.

## Wymagania wstępne

Zanim wyruszymy w tę 3‑D podróż, upewnij się, że spełniasz następujące wymagania:

- Aspose.3D for .NET: Upewnij się, że zainstalowałeś bibliotekę Aspose.3D. Jeśli nie, możesz ją pobrać [tutaj](https://releases.aspose.com/3d/net/).
- Podstawowa znajomość programowania w .NET: Ten samouczek zakłada podstawową wiedzę o rozwoju w .NET.

## Importowanie przestrzeni nazw

W każdym projekcie .NET właściwe użycie przestrzeni nazw jest kluczowe. Rozpocznij od zaimportowania niezbędnych przestrzeni nazw, aby efektywnie wykorzystać funkcje Aspose.3D. Oto fragment kodu, który Cię poprowadzi:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Jak utworzyć scenę 3d .net z ekstruzją liniową i skrętem

Poniżej znajduje się krok po kroku przewodnik, który dokładnie pokazuje, jak **utworzyć scenę 3D .NET** i zastosować skręt do ekstruzji liniowej.

### Krok 1: Zainicjalizuj profil bazowy

```csharp
// Initialize the base profile to be extruded
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

Zaczynamy od zdefiniowania profilu prostokątnego. Dostosuj `RoundingRadius`, aby w razie potrzeby zaokrąglić narożniki.

### Krok 2: Utwórz scenę 3D

```csharp
// Create a scene 
Scene scene = new Scene();
```

Obiekt `Scene` pełni rolę płótna, na którym będą znajdować się wszystkie obiekty 3‑D.

### Krok 3: Utwórz węzły lewy i prawy

```csharp
// Create left node
var left = scene.RootNode.CreateChildNode();
// Create right node
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(15, 0, 0);
```

Węzły są kontenerami dla geometrii. Tworzymy dwa węzły, aby móc porównać ekstruzję bez skrętu (lewy) z ekstruzją ze skrętem (prawy). Lewy węzeł jest przesunięty o 15 jednostek wzdłuż osi X w celu wizualnego oddzielenia.

### Krok 4: Wykonaj ekstruzję liniową z obrotem na lewym węźle

```csharp
// Twist property defines the degree of the rotation while extruding the profile
// Perform linear extrusion on the left node using twist and slices property
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 0, Slices = 100 });
```

Tutaj `Twist` jest ustawiony na **0°**, co daje prostą ekstruzję. Wartość `Slices` równa **100** zapewnia gładką powierzchnię.

### Krok 5: Wykonaj ekstruzję liniową z obrotem na prawym węźle

```csharp
// Perform linear extrusion on the right node using twist and slices property
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 90, Slices = 100 });
```

Ustawienie `Twist = 90` obraca profil o pełne 90 stopni wzdłuż długości ekstruzji, tworząc wyraźną helisę.

### Krok 6: Zapisz scenę 3D

```csharp
// Save 3D scene
scene.Save("Your Output Directory" + "TwistInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

Scena jest eksportowana jako plik OBJ, który możesz otworzyć w większości przeglądarek 3‑D lub zaimportować do innych potoków.

## Typowe problemy i rozwiązania

| Problem | Dlaczego się pojawia | Jak naprawić |
|---------|----------------------|--------------|
| **Skręt wygląda płasko** | `Slices` jest za niski, co powoduje szorstką geometrię. | Zwiększ `Slices` (np. do 200), aby uzyskać płynniejsze skręty. |
| **Spadek wydajności przy wysokiej liczbie `Slices`** | Więcej wielokątów wymaga więcej pamięci/CPU. | Użyj najniższej liczby `Slices`, która nadal spełnia wymagania jakości wizualnej, lub włącz uproszczenie geometrii po ekstruzji. |
| **Nie znaleziono pliku podczas zapisu** | Ścieżka katalogu wyjściowego jest nieprawidłowa. | Podaj pełną ścieżkę bezwzględną lub upewnij się, że katalog istnieje przed wywołaniem `Save`. |

## Najczęściej zadawane pytania

**Q: Czy mogę zastosować ekstruzję liniową z obrotem do innych kształtów?**  
A: Oczywiście! Możesz eksperymentować z różnymi profilami bazowymi poza prostokątami, otwierając mnóstwo możliwości projektowych.

**Q: Jaką rolę odgrywa właściwość 'Twist' w ekstruzji liniowej?**  
A: Właściwość 'Twist' określa stopień obrotu podczas procesu ekstruzji, wpływając na ostateczny kształt 3D.

**Q: Czy istnieją kwestie wydajności przy używaniu dużej liczby warstw (slices)?**  
A: Choć większa liczba warstw dodaje detale, może wpływać na wydajność. Znajdź kompromis w zależności od wymagań Twojej aplikacji.

**Q: Czy mogę połączyć ekstruzję liniową z innymi funkcjami Aspose.3D?**  
A: Z pewnością! Aspose.3D oferuje bogaty zestaw funkcji. Śmiało łącz ekstruzję liniową z innymi możliwościami, aby tworzyć bardziej złożone projekty.

**Q: Czy istnieje społeczność wsparcia i dyskusji dotycząca Aspose.3D?**  
A: Tak, dołącz do społeczności Aspose.3D na [Aspose Forum](https://forum.aspose.com/c/3d/18), aby uzyskać wsparcie i uczestniczyć w dyskusjach.

---

**Ostatnia aktualizacja:** 2026-01-09  
**Testowano z:** Aspose.3D 24.11 for .NET  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}