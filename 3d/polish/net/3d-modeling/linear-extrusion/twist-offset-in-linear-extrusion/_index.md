---
date: 2026-01-09
description: Dowiedz się, jak tworzyć scenę 3D przy użyciu Aspose.3D dla .NET, w tym
  eksportować plik Wavefront OBJ oraz jak zastosować skręt offsetu w ekstruzji liniowej.
linktitle: Twist Offset in Linear Extrusion
second_title: Aspose.3D .NET API
title: Jak stworzyć scenę 3D z przesunięciem skrętu w ekstruzji liniowej
url: /pl/net/3d-modeling/linear-extrusion/twist-offset-in-linear-extrusion/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Tworzenie sceny 3D: Offset skrętu w liniowej ekstruzji

## Wprowadzenie

Jeśli potrzebujesz szybko **tworzyć sceny 3d** i dodawać dynamiczną geometrię, Aspose.3D for .NET dostarcza dokładnie narzędzia, których potrzebujesz. W tym **samouczku Aspose 3D** przeprowadzimy Cię przez technikę *jak zastosować offset skrętu* podczas wykonywania **skrętu przy liniowej ekstruzji** i na końcu **wyeksportujemy pliki Wavefront OBJ**. Po zakończeniu będziesz mieć w pełni funkcjonalny model 3‑D gotowy do renderowania lub dalszego przetwarzania.

## Szybkie odpowiedzi
- **Co robi „twist offset”?** Przesuwa punkt początkowy skrętu wzdłuż osi ekstruzji.  
- **Która metoda eksportuje Wavefront OBJ?** `scene.Save(..., FileFormat.WavefrontOBJ)`.  
- **Czy potrzebna jest licencja do uruchomienia przykładu?** Licencja tymczasowa działa w testach; pełna licencja jest wymagana w produkcji.  
- **Jakie wersje .NET są obsługiwane?** .NET Framework 4.5+, .NET Core 3.1+, .NET 5/6+.  
- **Ile warstw (slices) jest zalecane dla płynnych skrętów?** Około 100 warstw zapewnia dobrą równowagę między jakością a wydajnością.

## Co to jest **create 3d scene**?

Tworzenie sceny 3‑D oznacza budowanie hierarchicznej struktury, która przechowuje geometrię, światła, kamery i przekształcenia. Aspose.3D udostępnia klasę `Scene`, która działa jako główny kontener dla wszystkich dodawanych węzłów.

## Dlaczego używać **linear extrusion twist**?

Liniowa ekstruzja ze skrętem pozwala przekształcić profil 2‑D w spiralny obiekt 3‑D — idealny do śrub, sprężyn lub ozdobnych kolumn. Dodanie offsetu skrętu daje jeszcze większą kontrolę nad początkiem obrotu, umożliwiając asymetryczne projekty.

## Wymagania wstępne

- Biblioteka Aspose.3D for .NET: Pobierz i zainstaluj bibliotekę ze [strony wydania](https://releases.aspose.com/3d/net/).  
- Twoje środowisko programistyczne: Visual Studio 2022 (lub dowolne IDE C#) gotowe do programowania w .NET.

## Importowanie przestrzeni nazw

Start by importing the necessary namespaces to access Aspose.3D functionality.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Przewodnik krok po kroku

### Krok 1: Inicjalizacja profilu bazowego  

Użyjemy prostokąta z małym promieniem zaokrąglenia jako profilu, który zostanie wyekstruzowany.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

### Krok 2: Utworzenie sceny  

To jest kontener, w którym **tworzymy węzły create 3d scene**.

```csharp
Scene scene = new Scene();
```

### Krok 3: Tworzenie węzłów  

Do korzenia dodawane są dwa węzły siostrzane — jeden dla zwykłej ekstruzji, a drugi dla wersji z offsetem.

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(18, 0, 0);
```

### Krok 4: Liniowa ekstruzja w lewym węźle (podstawowy skręt)  

Tutaj demonstrujemy klasyczny **linear extrusion twist** bez żadnego offsetu.

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100 });
```

### Krok 5: Liniowa ekstruzja w prawym węźle z **Twist Offset**  

Teraz stosujemy technikę **how to twist offset**, podając wektor `TwistOffset`.

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100, TwistOffset = new Vector3(3, 0, 0) });
```

### Krok 6: **Export Wavefront OBJ**  

Na koniec zapisz złożoną scenę do pliku OBJ, aby móc ją wyświetlić w dowolnym standardowym przeglądarce 3‑D.

```csharp
scene.Save("Your Output Directory" + "TwistOffsetInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## Typowe problemy i wskazówki

- **Skręt wygląda płasko?** Zwiększ wartość `Slices`, aby uzyskać gładszą geometrię.  
- **Offset niewidoczny?** Upewnij się, że wektor `TwistOffset` jest niezerowy i jest zgodny z kierunkiem ekstruzji.  
- **Plik OBJ nie zawiera tekstur?** OBJ przechowuje tylko geometrię; w razie potrzeby użyj plików MTL do definicji materiałów.

## Najczęściej zadawane pytania

**Q: Czy mogę używać Aspose.3D for .NET z innymi językami programowania?**  
A: Aspose.3D głównie celuje w języki .NET, ale istnieją równoważne biblioteki dla Javy i innych platform.

**Q: Jak uzyskać tymczasową licencję dla Aspose.3D for .NET?**  
A: Odwiedź [ten link](https://purchase.aspose.com/temporary-license/), aby uzyskać tymczasową licencję do celów testowych.

**Q: Czy istnieje forum społecznościowe dla Aspose.3D for .NET?**  
A: Oczywiście! Dołącz do społeczności na [Aspose.3D Forum](https://forum.aspose.com/c/3d/18), aby wymieniać się doświadczeniami z innymi deweloperami i uzyskać pomoc.

**Q: Czy dostępne są dodatkowe przykłady i dokumentacja?**  
A: Zapoznaj się z [documentation](https://reference.aspose.com/3d/net/), aby znaleźć obszerne przewodniki i przykłady.

**Q: Gdzie mogę kupić Aspose.3D for .NET?**  
A: Przejdź do [this link](https://purchase.aspose.com/buy), aby dokonać zakupu i odblokować pełny potencjał Aspose.3D.

## Zakończenie

W tym **samouczku aspose 3d** nauczyłeś się, jak **create 3d scene**, zastosować **linear extrusion twist**, kontrolować **twist offset** oraz **export Wavefront OBJ**. Te techniki pozwalają dodać zaawansowaną, skręconą geometrię do dowolnego projektu 3‑D przy użyciu kilku linijek kodu.

---

**Ostatnia aktualizacja:** 2026-01-09  
**Testowano z:** Aspose.3D 24.11 for .NET  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}