---
date: 2026-05-19
description: Dowiedz się, jak konwertować siatkę do formatu FBX, ustawiając kolor
  materiału i udostępniając dane geometrii siatki w Java 3D przy użyciu Aspose.3D.
keywords:
- convert mesh to fbx
- how to export fbx
- how to set material
- export mesh to fbx
- aspose 3d tutorial
linktitle: Konwertuj siatkę do formatu FBX i ustaw kolor materiału w Java 3D
schemas:
- author: Aspose
  dateModified: '2026-05-19'
  description: Learn how to convert mesh to FBX while setting material color and sharing
    mesh geometry data in Java 3D using Aspose.3D.
  headline: Convert Mesh to FBX and Set Material Color in Java 3D
  type: TechArticle
- questions:
  - answer: Yes, the shared mesh can be animated via skeletal rigs or morph targets
      while each node retains its own material.
    question: Can I reuse the same mesh for animated characters?
  - answer: Absolutely, Aspose.3D writes full UV data, so textures map correctly in
      downstream tools.
    question: Does the FBX export preserve UV coordinates?
  - answer: The library can stream meshes exceeding 2 GB without loading the entire
      file into memory, making it suitable for large scenes.
    question: What is the maximum file size Aspose.3D can handle?
  - answer: Pass a different `FileFormat` enum value, such as `FileFormat.FBX201400ASCII`,
      to `scene.save`.
    question: How do I change the FBX version?
  - answer: Yes, you can create a new `Scene`, add the desired nodes, and then save
      that scene to FBX.
    question: Is it possible to export only a subset of nodes?
  type: FAQPage
second_title: Aspose.3D Java API
title: Konwertuj siatkę do formatu FBX i ustaw kolor materiału w Java 3D
url: /pl/java/geometry/share-mesh-geometry-data/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Konwertuj siatkę do FBX i ustaw kolor materiału w Java 3D

## Wprowadzenie

Jeśli tworzysz aplikację 3D w Javie, często będziesz musiał ponownie używać tej samej geometrii w wielu obiektach, nadając każdej instancji unikalny wygląd. W tym samouczku dowiesz się, **jak konwertować siatkę do FBX**, współdzielić podstawową geometrię siatki pomiędzy kilkoma węzłami oraz **ustawić inny kolor materiału dla każdego węzła**. Po zakończeniu będziesz mieć gotową do eksportu scenę FBX, którą możesz włożyć do dowolnego silnika lub przeglądarki.

## Szybkie odpowiedzi
- **Jaki jest główny cel?** Konwertować siatkę do FBX, współdzielić geometrię siatki i ustawić odrębny kolor materiału dla każdego węzła.  
- **Jakiej biblioteki potrzebujesz?** Aspose.3D for Java.  
- **Jak wyeksportować wynik?** Zapisz scenę jako plik FBX używając `FileFormat.FBX7400ASCII`.  
- **Czy potrzebna jest licencja?** Wymagana jest tymczasowa lub pełna licencja do użytku produkcyjnego.  
- **Jaką wersję Javy obsługuje?** Dowolne środowisko Java 8+.

## Co to jest **konwertować siatkę do FBX**?

Konwertowanie siatki do FBX oznacza pobranie obiektu siatki znajdującego się w pamięci i zapisanie go w formacie pliku FBX, de‑facto standardzie obsługiwanym przez Maya, Blender, Unity i wiele innych narzędzi 3D. Aspose.3D wykonuje ciężką pracę, więc wystarczy wywołać `scene.save(...)` z odpowiednim `FileFormat`.

## Dlaczego współdzielić dane geometrii siatki?

Współdzielenie geometrii zmniejsza zużycie pamięci i przyspiesza renderowanie, ponieważ bufor wierzchołków jest przechowywany tylko raz. Ta technika jest idealna dla scen z wieloma powielonymi obiektami — myśl o lasach, tłumach lub modularnej architekturze — gdzie każda instancja różni się jedynie przekształceniem lub materiałem.

## Wymagania wstępne

Zanim przejdziesz do samouczka, upewnij się, że masz następujące elementy:

- **Środowisko programistyczne Java** – dowolne IDE lub konfiguracja wiersza poleceń z Java 8 lub nowszą.  
- **Biblioteka Aspose.3D** – pobierz najnowszy plik JAR z oficjalnej strony: [here](https://releases.aspose.com/3d/java/).

## Importowanie pakietów

Namespace `com.aspose.threed` zawiera wszystkie klasy potrzebne do budowania scen, siatek i materiałów. Zaimportuj te pakiety na początku pliku Java, aby kompilator mógł rozpoznać typy.

```java
import com.aspose.threed.*;
```

## Krok 1: Inicjalizacja obiektu sceny (initialize scene java)

Klasa `Scene` jest kontenerem najwyższego poziomu Aspose.3D, który reprezentuje cały świat 3D. Inicjalizacja `Scene` daje czyste płótno, na którym można dodawać siatki, światła i kamery.

```java
// Initialize scene object
Scene scene = new Scene();
```

## Krok 2: Definicja wektorów kolorów

`Vector3` reprezentuje wektor trójskładnikowy (X, Y, Z) używany do pozycji, kierunków lub kolorów.  
Utwórz tablicę obiektów `Vector3` przechowujących wartości RGB. Każdy wektor zostanie później przypisany do osobnego węzła, dając każdej instancji własny odcień materiału.

```java
// Define color vectors
Vector3[] colors = new Vector3[] {
    new Vector3(1, 0, 0),
    new Vector3(0, 1, 0),
    new Vector3(0, 0, 1)
};
```

## Krok 3: Tworzenie siatki 3D w Javie przy użyciu Polygon Builder (create 3d mesh java)

Klasa `PolygonBuilder` pozwala zbudować siatkę, definiując wierzchołki i ściany ręcznie. Ta siatka będzie ponownie używana we wszystkich węzłach, demonstrując w praktyce działanie współdzielenia geometrii.

```java
// Call Common class create mesh using polygon builder method to set mesh instance
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

## Jak ustawić kolor materiału dla każdego węzła?

`LambertMaterial` to prosty typ materiału definiujący kolor rozpraszony dla siatki.  
Iteruj po wektorach kolorów, twórz węzeł sześcianu dla każdego wpisu, przypisz nowy `LambertMaterial` z bieżącym kolorem i pozycjonuj węzeł przy użyciu macierzy translacji. Ten wzorzec zapewnia, że każdy węzeł wyświetla unikalny kolor, jednocześnie odwołując się do tej samej podstawowej siatki.

```java
int idx = 0;
for(Vector3 color : colors) {
    // Initialize cube node object
    Node cube = new Node("cube");
    cube.setEntity(mesh);
    LambertMaterial mat = new LambertMaterial();
    // Set color
    mat.setDiffuseColor(color);
    // Set material
    cube.setMaterial(mat);
    // Set translation
    cube.getTransform().setTranslation(new Vector3(idx++ * 20, 0, 0));
    // Add cube node
    scene.getRootNode().addChildNode(cube);
}
```

## Krok 5: Zapis sceny 3D (save scene fbx, convert mesh to fbx)

Określ katalog i nazwę pliku, w którym zostanie zapisana scena 3D w obsługiwanym formacie, w tym przypadku FBX7400ASCII. Ten krok również demonstruje **konwertowanie siatki do FBX** poprzez zapis współdzielonej sceny na dysku.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
MyDir = MyDir + "MeshGeometryData.fbx";

// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7400ASCII);
```

## Częste problemy i wskazówki

- **Problemy ze ścieżkami** – Upewnij się, że ścieżka katalogu kończy się separatorem plików (`/` lub `\\`) przed dodaniem nazwy pliku.  
- **Inicjalizacja licencji** – Jeśli zapomnisz ustawić licencję Aspose.3D przed wywołaniem `scene.save`, biblioteka będzie działać w trybie trial i może dodać znak wodny.  
- **Nadpisywanie materiałów** – Ponowne użycie tego samego obiektu `LambertMaterial` dla wielu węzłów spowoduje, że wszystkie węzły będą miały ten sam kolor. Zawsze twórz nowy materiał w każdej iteracji, jak pokazano powyżej.  
- **Duże siatki** – Dla siatek z milionami wierzchołków rozważ użycie `MeshBuilder` z indeksowanymi wielokątami, aby utrzymać rozmiar pliku FBX w rozsądnych granicach.

## Dodatkowe najczęściej zadawane pytania

**Q1: Czy mogę używać Aspose.3D z innymi frameworkami Java?**  
A1: Tak, Aspose.3D jest zaprojektowany tak, aby współpracować bezproblemowo z różnymi frameworkami Java.

**Q2: Czy dostępne są opcje licencjonowania Aspose.3D?**  
A2: Tak, możesz zapoznać się z opcjami licencjonowania [here](https://purchase.aspose.com/buy).

**Q3: Jak mogę uzyskać wsparcie dla Aspose.3D?**  
A3: Odwiedź forum Aspose.3D [forum](https://forum.aspose.com/c/3d/18) w celu uzyskania pomocy i dyskusji.

**Q4: Czy dostępna jest darmowa wersja próbna?**  
A4: Tak, darmową wersję próbną możesz pobrać [here](https://releases.aspose.com/).

**Q5: Jak uzyskać tymczasową licencję dla Aspose.3D?**  
A5: Tymczasową licencję możesz uzyskać [here](https://purchase.aspose.com/temporary-license/).

## Najczęściej zadawane pytania

**Q: Czy mogę ponownie używać tej samej siatki dla animowanych postaci?**  
A: Tak, współdzielona siatka może być animowana za pomocą szkieletów lub morph targetów, przy czym każdy węzeł zachowuje własny materiał.

**Q: Czy eksport FBX zachowuje współrzędne UV?**  
A: Absolutnie, Aspose.3D zapisuje pełne dane UV, więc tekstury mapują się poprawnie w narzędziach downstream.

**Q: Jaki jest maksymalny rozmiar pliku, który Aspose.3D może obsłużyć?**  
A: Biblioteka może strumieniować siatki przekraczające 2 GB bez ładowania całego pliku do pamięci, co czyni ją odpowiednią dla dużych scen.

**Q: Jak zmienić wersję FBX?**  
A: Przekaż inny enum `FileFormat`, np. `FileFormat.FBX201400ASCII`, do metody `scene.save`.

**Q: Czy można wyeksportować tylko podzbiór węzłów?**  
A: Tak, możesz utworzyć nową `Scene`, dodać wybrane węzły i zapisać tę scenę do FBX.

## Zakończenie

Gratulacje! Pomyślnie **skonwertowałeś siatkę do FBX**, współdzieliłeś dane geometrii siatki pomiędzy wieloma węzłami i ustawiłeś indywidualne kolory materiałów przy użyciu Aspose.3D for Java. Ten przepływ pracy zapewnia lekką, wielokrotnego użytku architekturę siatki, którą można wyeksportować do dowolnego potoku obsługującego FBX.

---

**Ostatnia aktualizacja:** 2026-05-19  
**Testowano z:** Aspose.3D 24.11 for Java  
**Autor:** Aspose  

{{< blocks/products/products-backtop-button >}}

## Powiązane samouczki

- [How to Split Mesh by Material in Java Using Aspose.3D](/3d/java/3d-mesh-data/split-meshes-by-material/)
- [Embed Texture FBX in Java – Apply Materials to 3D Objects with Aspose.3D](/3d/java/geometry/apply-materials-to-3d-objects/)
- [How to Export Scene to FBX and Retrieve 3D Scene Info in Java](/3d/java/3d-scenes-and-models/get-scene-information/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}