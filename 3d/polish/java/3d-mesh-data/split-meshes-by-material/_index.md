---
date: 2026-01-27
description: Naucz się efektywnie dzielić siatkę według materiału w języku Java przy
  użyciu Aspose.3D. Ten przewodnik pokazuje, jak zmniejszyć liczbę wywołań rysowania
  i poprawić wydajność renderowania, dzieląc siatkę według materiału.
linktitle: How to Split Mesh by Material in Java Using Aspose.3D
second_title: Aspose.3D Java API
title: Jak podzielić siatkę według materiału w Javie przy użyciu Aspose.3D
url: /pl/java/3d-mesh-data/split-meshes-by-material/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Jak umieścić siatkę według materiału w Javie przy użyciu Aspose.3D

## Wstęp

Jeśli pracujesz z grafiką 3D w Javie, szybko odkryjesz, że duży siatek może stać się wydajnością gardłem — szczególnie gdy pojedyncza siatka zawiera wiele materiałów. **Nauka, jak podzielona siatka** według materiału pozwala na wydzielenie każdej grupy wielokątów wyróżnianej dla materiału, umożliwia renderowanie, łatwiejsze odrzucanie (eliminowanie) i bardziej szczegółowe sterowanie nad obsługą tekstury. W tym samouczku przeprowadzimy Cię krok po kroku przez ** podział sieci według materiału** przy użyciu biblioteki Aspose.3D, wraz z praktycznymi narzędziami, pobranie wywołania rysowania oraz poradnictwo na temat wydajności renderowania.

## Szybkie odpowiedzi
- **Co oznacza „podzielić siatkę według materiału”?** Oddziela pojedynczą siatkę na wiele pod‑siatek, z których każda zawiera wielokąty wykorzystujące tego samego materiału.
- **Dlaczego szkodliwego Aspose.3D?** odprowadzanie wysokopoziomowe, wieloplatformowe API, które abstrahuje niskopoziomowe formaty plików, wytwarzac.
- **Jak długo trwa wdrożenie?** Około 10–15 minut kodowania i testowania.
- **Czy istnieje licencjat?** Dostępna jest wersja próbna; licencjat komercyjny jest wymagany do użytku produkcyjnego.
- **Która wersja Javy jest wspierana?** Java8lub wyższy.

## Co to jest dzielenie siatki?

Dzielenie sieci na proces obejmujący sieci 3D na mniejszych, łatwiejszych do zarządzania fragmentami. Gdy podział jest na materiał, każda z nich zawiera tylko wielokąty od głównego materiału do jednego materiału. Takie rozwiązanie powoduje zastosowanie rysowania, usprawnienie renderowania i upraszcza zadań, takie jak zastosowanie shaderów na materiał.

## Dlaczego warto dzielić siatkę według materiału?

- **Wydajność:** Silniki renderujące mogą grupować wywołania rysowania na materiał, zmniejszając zmiany stanu GPU.
- **Elastyczność:** można obliczyć różne efekty postprocessingu lub logiki wyników według materiału.
- **Zarządzanie pamięcią:** Mniejsze sieci umożliwiające strumieniowanie do pamięci, co jest kluczem w aplikacji mobilnej lub VR.
- **Mniej wywołań rysowania:** Mniej zmiany stanu oznacza, że ​​GPU może działać bardziej efektywnie.
- **Poprawiona wydajność renderowania:** Izolowanie materiałów często prowadzi do skuteczniejszego odrzucania (uboju) i wyników cieniowania.

## Warunki wstępne

Zanim przejdziemy do kodu, sprawdź się, że masz dodatkowe elementy:

- Podstawową przyjemność programowania w Javie.
- Zainstalowana bibliotekę Aspose.3D dla Java (pobierz ze [strony Aspose](https://releases.aspose.com/3d/java/)).
- IDE, takie jak IntelliJ IDEA, Eclipse lub VS Code, skonfigurowane do programowania w Javie.

## Importuj pakiety

Najpierw zaimportuj wymagane klasy Aspose.3D oraz wszelkie standardowe utilsy Javy, które będą potrzebne:

```java
import com.aspose.threed.*;

import java.util.Arrays;
```

## Przewodnik krok po kroku

Poniżej znajduje się zwięzły przewodnik po każdym kroku, z wyjaśnieniami poprzedzającymi bloki kodu, abyś dokładnie wiedział, co się dzieje.

### Krok 1: Utwórz siatkę prostopadłościanu

Zaczynamy od prostego prymitywu geometrycznego — sześcianu — abyśmy mogli wyraźnie zobaczyć, jak każda ściana (płaszczyzna) otrzymuje własny materiał później.

```java
// ExStart:SplitMeshbyMaterial

// Create a mesh of a box (composed of 6 planes)
Mesh box = (new Box()).toMesh();
```

### Krok 2: Utwórz element materiału

`VertexElementMaterial` przechowuje indeksy materiałów dla każdego wielokąta. Dołączając go do siatki, możemy kontrolować, którego materiału używa każda ściana.

```java
// Create a material element on the box mesh
VertexElementMaterial mat = (VertexElementMaterial) box.createElement(VertexElementType.MATERIAL, MappingMode.POLYGON, ReferenceMode.INDEX);
```

### Krok 3: Określ różne indeksy materiałów

Tutaj przypisujemy unikalny indeks materiału do każdej z sześciu płaszczyzn sześcianu. kolejność w tablicy odpowiada kolejności wielokątów generowanych przez prymityw `Box`.

```java
// Specify different material indices for each plane
mat.setIndices(new int[]{0, 1, 2, 3, 4, 5});
```

### Krok 4: Podziel siatkę na podsiatki

Wywołanie `PolygonModifier.splitMesh` z `SplitMeshPolicy.CLONE_DATA` tworzy nową pod‑siatkę dla każdego odrębnego indeksu materiału, zachowując pierwotne dane wierzchołków.

```java
// Split the mesh into 6 sub-meshes, each plane becoming a sub-mesh
Mesh[] planes = PolygonModifier.splitMesh(box, SplitMeshPolicy.CLONE_DATA);
```

### Krok 5: Zaktualizuj indeksy materiałów i ponownie podziel

Aby pokazać inną strategię podziału, grupujemy najpierw trzy pierwsze płaszczyzny pod materiał 0, a pozostałe trzy pod materiał 1, a następnie dzielimy używając `COMPACT_DATA`, aby usunąć nieużywane wierzchołki.

```java
// Update material indices and split into 2 sub-meshes
mat.getIndices().clear();
mat.setIndices(new int[]{0, 0, 0, 1, 1, 1});
planes = PolygonModifier.splitMesh(box, SplitMeshPolicy.COMPACT_DATA);
```

### Krok 6: Potwierdź powodzenie

Prosty komunikat w konsoli informuje, że operacja zakończyła się bez błędów.

```java
// Display success message
System.out.println("\nSplitting a mesh by specifying the material successfully.");
// ExEnd:SplitMeshbyMaterial
```

## Zmniejsz liczbę wywołań rysowania i popraw wydajność renderowania

Przekształcając każdy materiał w osobną siatkę, umożliwia potokowi graficznemu jednego, stworzonego przez siebie rysowania na materiał zamiast jednego na wielokąt. Redukcja wywołań rysowania bezpośrednio przekłada się na płynniejsze liczby klatek, szczególnie na słabszym sprzęcie. Poza polityką `COMPACT_DATA` usuwane są nieużywane wierzchołki, co jeszcze bardziej zmniejsza przepustowość pamięci i pomaga GPU renderować wydajniej.

## Typowe problemy i rozwiązania

| Problem | Dlaczego się pojawia | Rozwiązanie |
|--------|----------------------|------------|
| **Pod‑siatki przeznaczone na zduplikowane wierzchołki** | Użycie `CLONE_DATA` kopiuje wszystkie dane wierzchołków dla każdego pod-siatki. | Przejdź na `COMPACT_DATA`, gdy chcesz, aby współdzielone wierzchołki były deduplikowane. |
| **Nieprawidłowe przypisanie materiału** | Długość indeksów nie odpowiada przepisom wielokątów. | Zweryfikuj lokalizację wielokątów (np. sześcian ma 6) i poddaj pasującą tablicę indeksów. |

## Często zadawane pytania

**P: Czy Aspose.3D jest kompatybilny z innymi bibliotekami 3D w Javie?**  
O: Tak, Aspose.3D może współistnieć z takimiami jak Java 3D czy jMonkeyEngine, umożliwiając import/eksport siatek pomiędzy nimi.

**P: Czy tę technikę można zastosować do złożonych modeli z setkami materiałów?**  
O: Zdecydowanie tak. Te same wywołania API działają niezależnie od złożoności siatki; wystarczy, aby tablica indeksów prawidłowo odzwierciedlała układ materiałów.

**P: Gdzie mogę znaleźć pełną dokumentację Aspose.3D dla Javy?**  
O: Odwiedź oficjalną [dokumentację Aspose.3D Java](https://reference.aspose.com/3d/java/), aby uzyskać szczegółowe odniesienia API i dodatkowe przykłady.

**P: Czy dostępna jest darmowa wersja próbna Aspose.3D dla Javy?**  
O: Tak, możesz pobrać wersję próbną ze [strony Aspose Releases](https://releases.aspose.com/).

**P: Jak mogę uzyskać wsparcie, jeśli napotkam problemy?**  
O: Forum społeczności Aspose ([forum Aspose.3D](https://forum.aspose.com/c/3d/18)) to doskonałe miejsce, aby zadawać pytania i otrzymać pomoc zarówno od zespołu Aspose, jak i innych programistów.

---

**Ostatnia aktualizacja:** 2026-01-27  
**Testowano z:** Aspose.3D for Java 24.11  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}