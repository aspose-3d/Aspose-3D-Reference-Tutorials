---
date: 2026-03-26
description: Dowiedz się, jak stworzyć cylinder i wyeksportować plik OBJ przy użyciu
  Aspose.3D dla .NET. Ten przyjazny dla początkujących przewodnik obejmuje konfigurację
  sceny 3D oraz eksport OBJ.
linktitle: Customized Shear Bottom Cylinder
second_title: Aspose.3D .NET API
title: Jak stworzyć cylinder z nachylonym dnem – Aspose.3D dla .NET
url: /pl/net/3d-modeling/working-with-cylinder/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Jak utworzyć cylinder z pochyleniem dolnej części – Aspose.3D dla .NET

## Wprowadzenie
Jeśli zastanawiasz się **jak utworzyć obiekty cylinder** z niestandardowym pochyleniem dolnej części w środowisku .NET, trafiłeś we właściwe miejsce. W tym samouczku przeprowadzimy Cię przez każdy krok — od skonfigurowania sceny 3‑D po wyeksportowanie gotowego modelu jako plik OBJ — abyś mógł podnieść swoje *początkowe umiejętności modelowania 3D* przy użyciu **Aspose.3D dla .NET**.

## Szybkie odpowiedzi
- **Jaka jest podstawowa klasa do rozpoczęcia modelu 3D?** `Scene` tworzy główny kontener dla całej geometrii.  
- **Która metoda eksportuje model do OBJ?** `scene.Save(..., FileFormat.WavefrontOBJ)`.  
- **Czy potrzebna jest licencja do testów?** Dostępna jest darmowa wersja próbna — zobacz link do wersji próbnej w FAQ.  
- **Czy mogę zmienić kąt pochylenia?** Tak, zmodyfikuj `ShearBottom` przy pomocy wartości `Vector2`.  
- **Czy to nadaje się dla początkujących?** Zdecydowanie; API ukrywa niskopoziomowe operacje na siatkach.

## Co to jest scena 3D?
*Scena 3D* to hierarchiczny kontener, który przechowuje wszystkie jednostki geometryczne, światła, kamery i przekształcenia. W Aspose.3D klasa `Scene` zapewnia przejrzysty sposób organizacji i późniejszego eksportu Twoich modeli.

## Dlaczego eksportować do OBJ?
OBJ jest szeroko wspieranym, tekstowym formatem, który wiele aplikacji 3‑D (Blender, Maya, Unity) potrafi zaimportować. Eksport do OBJ umożliwia udostępnianie lub dalszą edycję Twoich modeli cylinderów poza .NET.

## Wymagania wstępne
Zanim przejdziesz do kodu, upewnij się, że masz:

- Podstawową wiedzę o C# i programowaniu w .NET.  
- **Aspose.3D dla .NET** zainstalowane – możesz pobrać go **[tutaj](https://releases.aspose.com/3d/net/)**.  
- Środowisko IDE .NET (Visual Studio, Rider lub VS Code) gotowe do kodowania.

## Importowanie przestrzeni nazw
Najpierw wprowadź wymagane przestrzenie nazw, aby typy API były rozpoznawane.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```

## Krok 1: Utwórz scenę 3D
Obiekt `Scene` pełni rolę korzenia hierarchii Twojego modelu.

```csharp
Scene scene = new Scene();
```

## Krok 2: Utwórz Cylinder 1
Generujemy pierwszy cylinder o promieniu 2, wysokości 10 i 20 segmentach radialnych.

```csharp
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```

## Krok 3: Dostosuj pochylenie dolnej części dla Cylinder 1
Zastosuj przekształcenie pochylenia, włącz generowanie cylindra‑wiatraka i dostosuj inne właściwości, aby uzyskać pożądany kształt.

```csharp
// Shear 47.5deg in the xy plane (z-axis)
cylinder1.ShearBottom = new Vector2(0, 0.83); 

// Set GenerateFanCylinder to true
cylinder1.GenerateFanCylinder = true;
// Set ThetaLength
cylinder1.ThetaLength = MathUtils.ToRadian(270);

// Set OffsetTop
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```

## Krok 4: Dodaj Cylinder 1 do sceny
Umieść pierwszy cylinder w dogodnym miejscu przy użyciu przekształcenia translacji.

```csharp
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```

## Krok 5: Utwórz Cylinder 2
Drugi cylinder tworzony jest z tymi samymi wymiarami podstawowymi, ale bez niestandardowego pochylenia — idealny do porównania obok pierwszego.

```csharp
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```

## Krok 6: Dodaj Cylinder 2 do sceny
Po prostu dołącz drugi cylinder do grafu sceny.

```csharp
scene.RootNode.CreateChildNode(cylinder2);
```

## Krok 7: Eksportuj scenę jako plik OBJ
Na koniec zapisujemy całą scenę do pliku OBJ, aby można go było otworzyć w dowolnym standardowym przeglądarce 3‑D.

```csharp
scene.Save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WavefrontOBJ);
```

## Typowe problemy i rozwiązania
| Problem | Dlaczego się pojawia | Rozwiązanie |
|-------|----------------|-----|
| **Plik OBJ jest pusty** | Scena nie ma dołączonej geometrii. | Upewnij się, że oba cylindry zostały dodane do `scene.RootNode`. |
| **Pochylenie wygląda niepoprawnie** | `ShearBottom` oczekuje tangensa kąta. | Użyj `Math.Tan(kątWRadianach)` lub podanej wartości `0.83` dla ~47,5°. |
| **Błędy ścieżki pliku** | Nieprawidłowy lub brakujący katalog. | Użyj `Path.Combine(Environment.CurrentDirectory, "CustomizedShearBottomCylinder.obj")`. |

## Najczęściej zadawane pytania
### Czy Aspose.3D dla .NET jest odpowiedni dla początkujących?
Zdecydowanie! Aspose.3D dla .NET oferuje wysokopoziomowe API, które ukrywa matematycznie intensywne części modelowania 3‑D, co czyni go przystępnym dla programistów o dowolnym poziomie umiejętności.

### Czy mogę zastosować różne kąty pochylenia do cylinderów?
Tak, każda instancja `Cylinder` posiada własną właściwość `ShearBottom`, więc możesz przypisać unikalny kąt do każdego obiektu.

### Czy dostępna jest wersja próbna?
Tak, wersję próbną możesz pobrać **[tutaj](https://releases.aspose.com/)**.

### Gdzie mogę znaleźć dodatkowe wsparcie?
Odwiedź **[forum Aspose.3D](https://forum.aspose.com/c/3d/18)**, aby uzyskać pomoc społeczności, przykłady kodu i dyskusje.

### Jak uzyskać tymczasową licencję?
Uzyskaj tymczasową licencję **[tutaj](https://purchase.aspose.com/temporary-license/)**.

**Dodatkowe pytania i odpowiedzi**

**P: Jak wyeksportować model w innym formacie, np. STL?**  
O: Zastąp `FileFormat.WavefrontOBJ` przez `FileFormat.STL` w wywołaniu `scene.Save`.

**P: Czy mogę animować cylindry po ich utworzeniu?**  
O: Tak, możesz dodać animacje klatek kluczowych do przekształceń węzłów przy użyciu klas `Animation` udostępnionych przez Aspose.3D.

**P: Czy API obsługuje .NET Core?**  
O: Biblioteka jest w pełni kompatybilna z .NET Core, .NET 5+ oraz .NET 6+.

---

**Ostatnia aktualizacja:** 2026-03-26  
**Testowano z:** Aspose.3D dla .NET (najnowsze wydanie)  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}