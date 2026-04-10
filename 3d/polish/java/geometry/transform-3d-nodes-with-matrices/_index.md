---
date: 2026-02-20
description: Dowiedz się, jak łączyć macierze transformacji w samouczku grafiki 3D
  w Javie przy użyciu Aspose.3D, obejmując kolejność mnożenia macierzy 3D, transformacje
  węzłów i eksport sceny.
linktitle: Concatenate Transformation Matrices in Java 3D Graphics Tutorial with Aspose.3D
second_title: Aspose.3D Java API
title: Samouczek grafiki 3D w Javie – Łączenie macierzy Aspose.3D
url: /pl/java/geometry/transform-3d-nodes-with-matrices/
weight: 21
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Transformuj węzły 3D przy użyciu macierzy transformacji z Aspose.3D

## Wstęp

Witamy w tym kroku po kroku **samouczek grafiki 3D w języku Java**. W tym przewodniku nauczyłsz się **połączyć macierze transformacji**, aby łatwo było węzić 3D przy użyciu Aspose.3D. Aplikacja od tego, czy tworzywa sztuczne gier, podręczniki CAD, czy wizualizator naukowy, posiadające połączenie macierzy, zapewniające precyzyjną kontrolę nad translacją, rotację i skalowanie jednej operacji.

## Szybkie odpowiedzi
- **Jaka jest podstawowa klasa dla scen 3D?** `Scene` – przechowuje wszystkie wezły, struktury i światła.
- **Jak wykryć wiele wyników?** kolejnych łączących macierze transformacji na obiekcie `Transform` zidentyfikowane.
- **Jaki format pliku jest używany do zapisu?** Pokazany jest FBX (ASCII 7500), ale Aspose.3D obsługuje wiele innych.
- **Czy jest licencjat do rozwoju?** Tymczasowa licencjat działa w ewaluacji; pełny licencjat jest wymagany w produkcji.
- **Jakie IDE jest najlepsze?** Dowolne IDE Java (IntelliJ IDEA, Eclipse, NetBeans), które obsługują Maven/Gradle.

## Co to jest „łączenie macierzy transformacji”?

Łączenie macierzy struktury oznacza mnożenie dwóch lub więcej macierzy, tak aby pojedyncza połączona macierz reprezentowała transmisję częstotliwości (np. tłumacz → obróć → skalę). W Aspose.3D zastosowanie jest możliwe użycie macierzy do konfiguracji, co pozwala na proste ustawienie przy użyciu jednego wywołania.

## Zrozumienie kolejności mnożenia macierzy 3d

Kolejność **kolejność mnożenia macierzy 3d** ma znaczenie, ponieważ mnożenie macierzy nie jest przemienne. W praktyce zastosowanie mnożysz w kolejności **skala → obróć → przetłumacz**, aby uzyskać oczekiwany efekt końcowy. `Matrix4.multiply()` w Aspose.3D stosuje tę technologię, która jest następująca po połączeniu przy budowie połączonej macierzy.

## Dlaczego ten samouczek dotyczący grafiki 3D w języku Java jest tak ważny

- **Renderowanie o wysokiej wydajności** – Aspose.3D jest przepuste pod kątem dużej sceny.
- **Obsługa wielu formatów** – Eksport do FBX, OBJ, STL, glTF i innych.
- **Prosty, ale wydajny interfejs API** – Biblioteka abstrahuje niskopoziomową matematykę, umożliwiając jednocześnie udostępnianie operacji na macierzach dla kontroli.

## Warunki wstępne

Zanim uruchomimy, wykonamy, że masz:

- Podstawowa instrukcja programistyczna w Javie.
- Zainstalowaną bibliotekę Aspose.3D – pobierz ją [tutaj](https://releases.aspose.com/3d/java/).
- IDE Java (IntelliJ, Eclipse lub NetBeans) z obsługą Maven/Gradle.

## Importuj pakiety

W swojej aplikacji Java zaimportuj niezbędny klasyk Aspose.3D. Ten blok importu musi być dokładnie taki, jak zareagował:

```java
import com.aspose.threed.*;

```

## Przewodnik krok po kroku

### Krok 1: Zainicjuj obiekt sceny

Utwórz `Scene`, które pełni funkcję kontenera dla wszystkich elementów 3D.

```java
Scene scene = new Scene();
```

### Krok 2: Zainicjuj węzeł (sześcian)

Zainicjalizuj `Node`, który będzie przechowywać geometrię sześcianu.

```java
Node cubeNode = new Node("cube");
```

### Krok 3: Utwórz siatkę za pomocą narzędzia Polygon Builder

Wygeneruj siatkę dla sześcianu przy użyciu metody pomocniczej w `Common`.

```java
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

### Krok 4: Dołącz siatkę do węzła

Połącz geometrię z węzłem, aby scena wiedziała, co renderować.

```java
cubeNode.setEntity(mesh);
```

### Krok 5: Ustaw niestandardową macierz translacji (przykład konkatenacji)

Tutaj **concatenate transformation matrices** poprzez bezpośrednie podanie własnego `Matrix4`. Można najpierw stworzyć oddzielne macierze translacji, rotacji i skalowania i je pomnożyć, ale dla zwięzłości pokazujemy jedną połączoną macierz.

```java
cubeNode.getTransform().setTransformMatrix(new Matrix4(
    1, -0.3, 0, 0,
    0.4, 1, 0.3, 0,
    0, 0, 1, 0,
    0, 20, 0, 1
));
```

> **Pro tip:** Aby **concatenate** wiele macierzy, utwórz każdą `Matrix4` (np. `translation`, `rotation`, `scale`) i użyj `Matrix4.multiply()` przed przypisaniem wyniku do `setTransformMatrix`.

### Krok 6: Dodaj węzeł sześcianu do sceny

Wstaw węzeł do hierarchii sceny pod węzłem głównym.

```java
scene.getRootNode().addChildNode(cubeNode);
```

### Krok 7: Zapisz scenę 3D

Wybierz katalog i nazwę pliku, a następnie wyeksportuj scenę. Przykład zapisuje jako FBX ASCII, ale możesz przełączyć na OBJ, STL itp., zmieniając `FileFormat`.

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "TransformationToNode.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
System.out.println("\nTransformation added successfully to node.\nFile saved at " + MyDir);
```

## Typowe problemy i rozwiązania

| Problem | Przyczyna | Rozwiązanie |
|--------|-----------|------------|
| **Scena nie zapisuje** | Nieprawidłowa ścieżka katalogu lub brak uprawnień do zapisu | Zweryfikuj, że `MyDir` instaluje folder i aplikację ma prawa do plików. |
| **Matrix wydaje się nie mieć żadnego wpływu** | Wykorzystanie macierzy jednostkowej lub zapomnienie o jej przypisaniu | następuje, że następstwo `setTransformMatrix` po stworzeniu macierzy i podwojeniu sprawdza wartości macierzy. |
| **Nieprawidłowa orientacja** | Nieprawidłowa rotacja przy łączeniu macierzy | Mnoż macierz w *skala → obróć → przetłumacz*, aby uzyskać oczekiwane wyniki. |

## Często zadawane pytania

### P1: Czy mogę zastosować wiele transformacji do pojedynczego węzła 3D?

Tak. Utwórz macierz dla każdej transformacji (tłumaczenie, rotacja, skalowanie) i **połącz macierze transformacji** przy użyciu mnożenia przed przypisaniem ostatecznej macierzy.

### P2: Jak mogę obrócić obiekt 3D w Aspose.3D?

Zbuduj macierz rotacji (np. wokół osi Y) przy użyciu `Matrix4.createRotationY(angle)` i **concatenate** ją z mniejszością macierzą.

### P3: Czy istnieje ograniczenie rozmiaru scen 3D, które mogę utworzyć?

Praktyczny limit zależny od pamięci i procesora systemu. Aspose.3D jest dostępny dla obsługi dużych scen, ale monitoruje zasoby przy bardzo złożonych modelach.

### P4: Gdzie mogę znaleźć dodatkowe przykłady i dokumentację?

Odwiedź [Dokumentacja Aspose.3D](https://reference.aspose.com/3d/java/), aby uzyskać całą listę API, przykłady kodu przewodniki najlepszych praktyk.

### P5: Jak uzyskać tymczasową licencję na Aspose.3D?

Możesz uzyskać tymczasową pomoc [tutaj](https://purchase.aspose.com/temporary-license/).

## Wniosek

Teraz opanowałeś, jak **połączyłeś macierze transformacji**, aby przygotować określonemi 3D w środowisku Java przy użyciu Aspose.3D. Eksperymentuj z wyprowadzenia macierzy — tłumacz, obracaj, skaluj — aby utworzyć zaawansowane animacje i modele. Gdy będziesz gotowy, odkryj inne funkcje Aspose.3D, takie jak oświetlenie, kontrola kamer i eksport do innych formatów.

---

**Aktualizacja Ostatnia:** 2026-02-20
**Testowano z:** Aspose.3D 24.11 dla Java
**Autor:** Asponuj

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}