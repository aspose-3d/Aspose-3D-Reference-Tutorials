---
date: 2026-06-13
description: Dowiedz się, jak łączyć macierze w samouczku grafiki 3D w Javie przy
  użyciu Aspose.3D, obejmując kolejność mnożenia macierzy, przekształcenia węzłów
  oraz eksport sceny.
keywords:
- how to concatenate matrices
- matrix multiplication order 3d
- Aspose.3D node transformation
linktitle: Łączenie macierzy transformacji w samouczku grafiki 3D w Javie z Aspose.3D
schemas:
- author: Aspose
  dateModified: '2026-06-13'
  description: Learn how to concatenate matrices in a Java 3D graphics tutorial using
    Aspose.3D, covering matrix multiplication order, node transformations, and scene
    export.
  headline: How to Concatenate Matrices in Java 3D Graphics – Aspose.3D Tutorial
  type: TechArticle
- description: Learn how to concatenate matrices in a Java 3D graphics tutorial using
    Aspose.3D, covering matrix multiplication order, node transformations, and scene
    export.
  name: How to Concatenate Matrices in Java 3D Graphics – Aspose.3D Tutorial
  steps:
  - name: Initialize the Scene Object
    text: '`Scene` is the top‑level container that holds all nodes, meshes, lights
      and cameras in an Aspose.3D model. The `Scene` class is Aspose.3D''s top‑level
      container that holds all nodes, meshes, lights, and cameras. Create a `Scene`
      which acts as the root container for all 3D elements.'
  - name: Initialize a Node (Cube)
    text: '`Node` represents an element in the scene graph that can contain geometry,
      lights or child nodes. The `Node` class represents a scene graph element that
      can contain geometry, lights, or other nodes. Instantiate a `Node` that will
      hold the geometry of a cube.'
  - name: Create Mesh Using Polygon Builder
    text: The `Common` helper builds a mesh from a list of polygons. Generate a mesh
      for the cube using the helper method in `Common`.
  - name: Attach Mesh to the Node
    text: Link the geometry to the node so the scene knows what to render. The `Node`’s
      `setMesh` method attaches the previously created mesh.
  - name: Set a Custom Translation Matrix (Concatenation Example)
    text: '`Matrix4` defines a 4×4 transformation matrix used for translation, rotation
      and scaling operations. Here we **concatenate transformation matrices** by directly
      providing a custom `Matrix4`. You could first create separate translation, rotation,
      and scaling matrices and multiply them, but for brevit'
  - name: Add the Cube Node to the Scene
    text: Insert the node into the scene hierarchy under the root node. The `Scene`’s
      `getRootNode().getChildren().add` method registers the cube for rendering.
  - name: Save the 3D Scene
    text: '`FileFormat` enum specifies the output file type such as FBX, OBJ, STL
      or glTF. Choose a directory and file name, then export the scene. The example
      saves as FBX ASCII, but you can switch to OBJ, STL, glTF, etc., by changing
      the `FileFormat` enum.'
  type: HowTo
- questions:
  - answer: Yes. Create separate matrices for each transformation (translation, rotation,
      scaling) and **concatenate transformation matrices** using multiplication before
      assigning the final matrix.
    question: Can I apply multiple transformations to a single 3D node?
  - answer: Build a rotation matrix (e.g., around the Y‑axis) with `Matrix4.createRotationY(angle)`
      and concatenate it with any existing matrix.
    question: How can I rotate a 3D object in Aspose.3D?
  - answer: The practical limit is dictated by your system’s memory and CPU. Aspose.3D
      is designed to handle large scenes efficiently, but monitor resource usage for
      extremely complex models.
    question: Is there a limit to the size of the 3D scenes I can create?
  - answer: Visit the [Aspose.3D documentation](https://reference.aspose.com/3d/java/)
      for a full list of APIs, code samples, and best‑practice guides.
    question: Where can I find additional examples and documentation?
  - answer: You can get a temporary license [here](https://purchase.aspose.com/temporary-license/).
    question: How do I obtain a temporary license for Aspose.3D?
  type: FAQPage
second_title: Aspose.3D Java API
title: Jak łączyć macierze w grafice 3D w Javie – samouczek Aspose.3D
url: /pl/java/geometry/transform-3d-nodes-with-matrices/
weight: 21
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Transformuj węzły 3D przy użyciu macierzy transformacji z Aspose.3D

## Wprowadzenie

W tym kompleksowym **java 3d graphics tutorial** odkryjesz **jak konkatenować macierze**, aby kontrolować translację, rotację i skalowanie węzłów 3D przy użyciu Aspose.3D. Niezależnie od tego, czy tworzysz silnik gry, przeglądarkę CAD, czy wizualizator naukowy, opanowanie konkatenacji macierzy zapewnia precyzyjne pozycjonowanie w jednej operacji, oszczędzając zarówno kod, jak i czas przetwarzania.

## Szybkie odpowiedzi
- **Jaka jest podstawowa klasa dla sceny 3D?** `Scene` – przechowuje wszystkie węzły, siatki i światła.  
- **Jak zastosować wiele transformacji?** Poprzez konkatenację macierzy transformacji na obiekcie `Transform` węzła.  
- **Jaki format pliku jest używany do zapisu?** Pokazany jest FBX (ASCII 7500), ale Aspose.3D obsługuje ponad 20 formatów.  
- **Czy potrzebna jest licencja do rozwoju?** Tymczasowa licencja działa w trybie ewaluacyjnym; pełna licencja jest wymagana w produkcji.  
- **Które IDE jest najlepsze?** Dowolne IDE Java (IntelliJ IDEA, Eclipse, NetBeans) obsługujące Maven/Gradle.

## Czym jest „konkatenacja macierzy transformacji”?

Konkatenacja macierzy transformacji oznacza mnożenie dwóch lub więcej macierzy, tak aby pojedyncza połączona macierz reprezentowała sekwencję transformacji (np. translate → rotate → scale). W Aspose.3D stosujesz wynikową macierz do transformacji węzła, co pozwala na złożone pozycjonowanie przy jednym wywołaniu.

## Zrozumienie kolejności mnożenia macierzy 3d

**Kolejność mnożenia macierzy 3d** ma znaczenie, ponieważ mnożenie macierzy nie jest przemienne. W praktyce zwykle mnoży się w kolejności **scale → rotate → translate**, aby uzyskać oczekiwany efekt wizualny. `Matrix4.multiply()` w Aspose.3D stosuje tę samą konwencję, więc pamiętaj o kolejności przy budowie połączonej macierzy.  
`Matrix4.multiply()` mnoży dwie macierze transformacji 4×4 i zwraca macierz połączoną.

## Dlaczego ten tutorial java 3d graphics ma znaczenie

- **Renderowanie wysokiej wydajności** – Aspose.3D potrafi renderować sceny zawierające do 500 000 wielokątów, nie przekraczając 2 GB pamięci RAM.  
- **Obsługa wielu formatów** – Eksport do FBX, OBJ, STL, glTF i **ponad 20 dodatkowych formatów** jednym wywołaniem API.  
- **Proste, a jednocześnie potężne API** – Biblioteka ukrywa niskopoziomową matematykę, jednocześnie udostępniając operacje na macierzach dla precyzyjnej kontroli.

## Wymagania wstępne

Zanim przejdziesz dalej, upewnij się, że masz:

- Podstawową znajomość programowania w Javie.  
- Zainstalowaną bibliotekę Aspose.3D – pobierz ją [tutaj](https://releases.aspose.com/3d/java/).  
- IDE Java (IntelliJ, Eclipse lub NetBeans) z obsługą Maven/Gradle.

## Importowanie pakietów

W swoim projekcie Java zaimportuj niezbędne klasy Aspose.3D. Ten blok importu musi pozostać dokładnie taki, jak podano:

```java
import com.aspose.threed.*;

```

## Przewodnik krok po kroku

### Jak konkatenować macierze?

Wczytaj lub utwórz `Matrix4` dla każdej transformacji (scale, rotate, translate), pomnóż je w kolejności *scale → rotate → translate* i przypisz wynikową macierz do `Transform` węzła. Ta pojedyncza połączona macierz steruje ostateczną pozycją, orientacją i rozmiarem węzła w jednej efektywnej operacji.

### Krok 1: Inicjalizacja obiektu Scene

`Scene` jest kontenerem najwyższego poziomu, który przechowuje wszystkie węzły, siatki, światła i kamery w modelu Aspose.3D.  

Klasa `Scene` jest kontenerem najwyższego poziomu Aspose.3D, który przechowuje wszystkie węzły, siatki, światła i kamery. Utwórz `Scene`, które będzie pełnić rolę korzenia dla wszystkich elementów 3D.

```java
Scene scene = new Scene();
```

### Krok 2: Inicjalizacja węzła (sześcian)

`Node` reprezentuje element w grafie sceny, który może zawierać geometrię, światła lub węzły potomne.  

Klasa `Node` reprezentuje element grafu sceny, który może zawierać geometrię, światła lub inne węzły. Zainstaluj `Node`, który będzie przechowywać geometrię sześcianu.

```java
Node cubeNode = new Node("cube");
```

### Krok 3: Tworzenie siatki przy użyciu Polygon Builder

Pomocnik `Common` buduje siatkę z listy wielokątów. Wygeneruj siatkę dla sześcianu, używając metody pomocniczej w `Common`.

```java
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

### Krok 4: Dołączenie siatki do węzła

Połącz geometrię z węzłem, aby scena wiedziała, co renderować. Metoda `setMesh` węzła dołącza wcześniej utworzoną siatkę.

```java
cubeNode.setEntity(mesh);
```

### Krok 5: Ustawienie własnej macierzy translacji (przykład konkatenacji)

`Matrix4` definiuje 4×4 macierz transformacji używaną do operacji translacji, rotacji i skalowania.  

Tutaj **konkatenujemy macierze transformacji**, podając bezpośrednio własną `Matrix4`. Można najpierw utworzyć osobne macierze translacji, rotacji i skalowania i je pomnożyć, ale dla zwięzłości pokazujemy jedną połączoną macierz.

```java
cubeNode.getTransform().setTransformMatrix(new Matrix4(
    1, -0.3, 0, 0,
    0.4, 1, 0.3, 0,
    0, 0, 1, 0,
    0, 20, 0, 1
));
```

> **Pro tip:** Aby konkatenować wiele macierzy, utwórz każdą `Matrix4` (np. `translation`, `rotation`, `scale`) i użyj `Matrix4.multiply()` przed przypisaniem wyniku do `setTransformMatrix`.

### Krok 6: Dodanie węzła sześcianu do sceny

Wstaw węzeł do hierarchii sceny pod węzłem głównym. Metoda `Scene.getRootNode().getChildren().add` rejestruje sześcian do renderowania.

```java
scene.getRootNode().addChildNode(cubeNode);
```

### Krok 7: Zapis sceny 3D

Enum `FileFormat` określa typ pliku wyjściowego, takiego jak FBX, OBJ, STL lub glTF.  

Wybierz katalog i nazwę pliku, a następnie wyeksportuj scenę. Przykład zapisuje jako FBX ASCII, ale możesz przełączyć się na OBJ, STL, glTF itp., zmieniając enum `FileFormat`.

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "TransformationToNode.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
System.out.println("\nTransformation added successfully to node.\nFile saved at " + MyDir);
```

## Typowe problemy i rozwiązania

| Problem | Przyczyna | Rozwiązanie |
|---------|-----------|--------------|
| **Scena nie zapisuje się** | Nieprawidłowa ścieżka katalogu lub brak uprawnień do zapisu | Sprawdź, czy `MyDir` wskazuje istniejący folder i aplikacja ma prawa do systemu plików. |
| **Macierz nie ma efektu** | Użycie macierzy jednostkowej lub zapomnienie o jej przypisaniu | Upewnij się, że wywołujesz `setTransformMatrix` po stworzeniu macierzy i podwójnie sprawdź jej wartości. |
| **Nieprawidłowa orientacja** | Nieprawidłowa kolejność rotacji przy konkatenacji macierzy | Mnoż macierze w kolejności *scale → rotate → translate*, aby uzyskać oczekiwane wyniki. |

## Najczęściej zadawane pytania

**Q: Czy mogę zastosować wiele transformacji do jednego węzła 3D?**  
A: Tak. Utwórz osobne macierze dla każdej transformacji (translacja, rotacja, skalowanie) i **konkatenuj macierze transformacji** przy użyciu mnożenia przed przypisaniem ostatecznej macierzy.

**Q: Jak mogę obrócić obiekt 3D w Aspose.3D?**  
A: Zbuduj macierz rotacji (np. wokół osi Y) za pomocą `Matrix4.createRotationY(angle)` i konkatenuj ją z istniejącą macierzą.

**Q: Czy istnieje limit rozmiaru scen 3D, które mogę tworzyć?**  
A: Praktyczny limit zależy od pamięci i CPU twojego systemu. Aspose.3D jest zaprojektowane do obsługi dużych scen efektywnie, ale monitoruj zużycie zasobów przy bardzo złożonych modelach.

**Q: Gdzie mogę znaleźć dodatkowe przykłady i dokumentację?**  
A: Odwiedź [dokumentację Aspose.3D](https://reference.aspose.com/3d/java/) aby uzyskać pełną listę API, przykłady kodu i przewodniki najlepszych praktyk.

**Q: Jak uzyskać tymczasową licencję dla Aspose.3D?**  
A: Tymczasową licencję możesz pobrać [tutaj](https://purchase.aspose.com/temporary-license/).

## Zakończenie

Teraz opanowałeś **sposób konkatenacji macierzy** w celu manipulacji węzłami 3D w środowisku Java przy użyciu Aspose.3D. Eksperymentuj z różnymi kombinacjami macierzy — translacja, rotacja, skalowanie — aby tworzyć zaawansowane animacje i modele. Gdy będziesz gotowy, odkryj inne funkcje Aspose.3D, takie jak oświetlenie, kontrola kamery i eksport do dodatkowych formatów.

---

**Ostatnia aktualizacja:** 2026-06-13  
**Testowano z:** Aspose.3D 24.11 for Java  
**Autor:** Aspose

## Powiązane tutoriale

- [Utwórz węzeł Aspose 3D w Javie – Udostępnij transformacje](/3d/java/geometry/expose-geometric-transformations/)
- [Jak eksportować FBX i budować hierarchie węzłów w Javie](/3d/java/geometry/build-node-hierarchies/)
- [Tutorial Java 3D Graphics - Utwórz scenę sześcianu 3D z Aspose.3D](/3d/java/geometry/create-3d-cube-scene/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}