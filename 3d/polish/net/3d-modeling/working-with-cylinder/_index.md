---
date: 2026-01-12
description: Dowiedz się, jak stworzyć cylinder ze skośnym dnem i jak wyeksportować
  model 3D w formacie OBJ przy użyciu Aspose.3D dla .NET. Postępuj zgodnie z tym przewodnikiem
  krok po kroku, aby opanować modelowanie 3D.
linktitle: Customized Shear Bottom Cylinder
second_title: Aspose.3D .NET API
title: Jak utworzyć cylinder z pochyłym dnem przy użyciu Aspose.3D dla .NET
url: /pl/net/3d-modeling/working-with-cylinder/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Spersonalizowany Cylinder z Pochyloną Podstawą

## Wprowadzenie
Witamy w naszym kompleksowym przewodniku, w którym **dowiesz się, jak tworzyć modele cylindrów z pochyłą podstawą** przy użyciu Aspose.3D dla .NET. Niezależnie od tego, czy tworzysz zasób do gry, część mechaniczną, czy demonstrację wizualną, ten tutorial pokaże Ci dokładnie, jak ukształtować dolną część cylindra, zastosować pochylenie i w końcu **wyeksportować plik modelu 3D OBJ** do użycia w dowolnym dalszym procesie. Przejdźmy razem przez każdy krok, abyś mógł zacząć produkować niestandardową geometrię w kilka minut.

## Szybkie odpowiedzi
- **Czym jest cylinder z pochyłą podstawą?** Cylinder, którego dolna powierzchnia jest nachylona (przycięta) zamiast płaska.  
- **Jakiej biblioteki użyto?** Aspose.3D dla .NET.  
- **Jak wyeksportować model?** Użyj `scene.Save(..., FileFormat.WavefrontOBJ)`.  
- **Czy potrzebna jest licencja?** Dostępna jest wersja próbna; do produkcji wymagana jest licencja komercyjna.  
- **Jakie są wymagania wstępne?** Środowisko programistyczne .NET oraz pakiet NuGet Aspose.3D.

## Co to jest cylinder z pochyłą podstawą?
Cylinder z pochyłą podstawą to standardowa siatka cylindryczna, której dolna powierzchnia została przekształcona operacją pochylenia. Dzięki temu możesz tworzyć nachylone podstawy, rampy lub niestandardowe łączniki bez ręcznej edycji wierzchołków.

## Dlaczego warto używać Aspose.3D do tego zadania?
- **Pełna kontrola** nad parametrami geometrii (promień, wysokość, segmenty).  
- **Wbudowane wsparcie pochylenia** poprzez właściwość `ShearBottom`, co oszczędza konieczność niskopoziomowej manipulacji siatką.  
- **Jednoklikowy eksport** do popularnych formatów, takich jak OBJ, FBX i STL, co ułatwia integrację z innymi narzędziami.

## Wymagania wstępne
Zanim zaczniemy, upewnij się, że masz:

- Podstawową znajomość C# i .NET.  
- Zainstalowane Aspose.3D dla .NET. Możesz je pobrać **[tutaj](https://releases.aspose.com/3d/net/)**.  
- IDE kompatybilne z .NET (Visual Studio, Rider lub VS Code).

## Importowanie przestrzeni nazw
W swoim pliku C# rozpocznij od zaimportowania niezbędnych przestrzeni nazw:

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

## Krok 1: Utworzenie sceny
Najpierw utwórz nową scenę 3‑D, która będzie przechowywać wszystkie nasze obiekty.

```csharp
Scene scene = new Scene();
```

## Krok 2: Utworzenie Cylinder 1
Utwórz podstawowy cylinder, który następnie dostosujemy, dodając pochylenie podstawy.

```csharp
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```

## Krok 3: Dostosowanie pochylenia podstawy dla Cylinder 1
Zastosuj pochylenie, włącz generowanie wachlarza i dostosuj pozostałe właściwości, aby uzyskać pożądany kształt.

```csharp
// Shear 47.5deg in the xy plane (z‑axis)
cylinder1.ShearBottom = new Vector2(0, 0.83); 

// Set GenerateFanCylinder to true
cylinder1.GenerateFanCylinder = true;
// Set ThetaLength
cylinder1.ThetaLength = MathUtils.ToRadian(270);

// Set OffsetTop
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```

## Krok 4: Dodanie Cylinder 1 do sceny
Umieść dostosowany cylinder w scenie i przesuń go nieco w prawo, abyśmy mogli zobaczyć oba obiekty obok siebie.

```csharp
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```

## Krok 5: Utworzenie Cylinder 2
Utwórz drugi, prosty cylinder do porównania.

```csharp
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```

## Krok 6: Dodanie Cylinder 2 do sceny
Dodaj drugi cylinder bez żadnego pochylenia – to pomoże zobrazować efekt poprzednich kroków.

```csharp
scene.RootNode.CreateChildNode(cylinder2);
```

## Krok 7: Zapisanie sceny
Na koniec wyeksportuj całą scenę jako plik OBJ, aby móc otworzyć go w Blenderze, Mayi lub dowolnym innym przeglądarce 3‑D.

```csharp
scene.Save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WavefrontOBJ);
```

## Typowe problemy i wskazówki
- **Wartości pochylenia**: `Vector2` przyjmuje współczynniki pochylenia X i Y. Wartość `0.83` odpowiada mniej więcej 47,5°, ale możesz ją dostosować, aby uzyskać inne kąty.  
- **Ścieżka eksportu**: Upewnij się, że podany folder istnieje i masz uprawnienia do zapisu; w przeciwnym razie `scene.Save` zgłosi wyjątek.  
- **Wydajność**: Przy bardzo wysokiej liczbie segmentów cylindrów rozważ zmniejszenie liczby segmentów (`20` w przykładzie), aby rozmiar pliku OBJ pozostawał w rozsądnych granicach.

## Najczęściej zadawane pytania

### Czy Aspose.3D dla .NET jest odpowiedni dla początkujących?
Zdecydowanie! Aspose.3D dla .NET oferuje przyjazne API, co czyni go dostępnym zarówno dla początkujących, jak i doświadczonych programistów.

### Czy mogę zastosować różne kąty pochylenia do cylindrów?
Tak, możesz indywidualnie dostosować `ShearBottom` dla każdego cylindra, co pozwala uzyskać unikalne efekty.

### Czy dostępna jest wersja próbna?
Tak, wersję próbną możesz wypróbować **[tutaj](https://releases.aspose.com/)**.

### Gdzie mogę znaleźć dodatkowe wsparcie?
Odwiedź **[forum Aspose.3D](https://forum.aspose.com/c/3d/18)**, aby uzyskać pomoc społeczności i dyskusje.

### Jak mogę uzyskać tymczasową licencję?
Uzyskaj tymczasową licencję **[tutaj](https://purchase.aspose.com/temporary-license/)**.

**Dodatkowe pytania i odpowiedzi**

**Q: Jak zmienić format eksportu na FBX?**  
A: Zamień `FileFormat.WavefrontOBJ` na `FileFormat.FBX` w wywołaniu `scene.Save`.

**Q: Czy mogę animować cylinder po wyeksportowaniu?**  
A: OBJ nie obsługuje animacji; użyj FBX lub GLTF, jeśli potrzebujesz danych animowanych.

**Q: Co zrobić, jeśli potrzebuję większego promienia cylindra?**  
A: Zmień pierwsze dwa parametry konstruktora `Cylinder` (np. `new Cylinder(4, 4, …)`).

## Zakończenie
Teraz opanowałeś, jak **tworzyć modele cylindrów z pochyłą podstawą** i eksportować je jako pliki OBJ przy użyciu Aspose.3D dla .NET. Eksperymentuj z różnymi wartościami pochylenia, liczbą segmentów i formatami eksportu, aby dopasować je do potrzeb swojego projektu. Powodzenia w modelowaniu!

---

**Ostatnia aktualizacja:** 2026-01-12  
**Testowano z:** Aspose.3D dla .NET 24.11 (najnowsza w momencie pisania)  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}