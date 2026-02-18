---
date: 2026-02-17
description: Dowiedz się, jak przekonwertować siatkę na FBX, ustawiając kolor materiału
  i udostępniając dane geometrii siatki w Java 3D przy użyciu Aspose.3D.
linktitle: Convert Mesh to FBX and Set Material Color in Java 3D
second_title: Aspose.3D Java API
title: Konwertuj siatkę do FBX i ustaw kolor materiału w Java 3D
url: /pl/java/geometry/share-mesh-geometry-data/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Konwertowanie siatki do FBX i ustawianie koloru materiału w Java 3D

## Wprowadzenie

Jeśli tworzysz aplikację 3D opartą na Javie, często będziesz musiał ponownie używać tej samej geometrii w wielu obiektach, jednocześnie nadając każdej instancji unikalny wygląd. W tym samouczku nauczysz się **jak konwertować siatkę do FBX**, udostępniać podstawową geometrię siatki pomiędzy kilkoma węzłami oraz **ustawiać inny kolor materiału dla każdego węzła**. Po zakończeniu będziesz mieć gotową do eksportu scenę FBX, którą możesz wstawić do dowolnego silnika lub przeglądarki.

## Szybkie odpowiedzi
- **Jaki jest główny cel?** Konwertowanie siatki do FBX, udostępnianie geometrii siatki i ustawianie odrębnego koloru materiału dla każdego węzła.  
- **Jakiej biblioteki wymaga?** Aspose.3D for Java.  
- **Jak wyeksportować wynik?** Zapisz scenę jako plik FBX używając `FileFormat.FBX7400ASCII`.  
- **Czy potrzebna jest licencja?** Wymagana jest tymczasowa lub pełna licencja do użytku produkcyjnego.  
- **Jaką wersję Javy obsługuje?** Każde środowisko Java 8+.

## Czym jest **convert mesh to FBX**?

`convert mesh to fbx` to proces pobierania obiektu siatki utworzonego lub modyfikowanego w pamięci i zapisywania go w formacie pliku FBX, który jest szeroko wspierany przez narzędzia 3D takie jak Maya, Blender i Unity. Aspose.3D zajmuje się ciężką pracą, więc wystarczy wywołać `scene.save(...)` z odpowiednim `FileFormat`.

## Dlaczego udostępniać dane geometrii siatki?

Udostępnianie geometrii zmniejsza zużycie pamięci i przyspiesza renderowanie, ponieważ podstawowe bufory wierzchołków są przechowywane tylko raz. Ta technika jest idealna dla scen z wieloma powielonymi obiektami — myśl o lasach, tłumach lub modularnej architekturze — gdzie każda instancja różni się jedynie przekształceniem lub materiałem.

## Wymagania wstępne

Zanim przejdziemy do samouczka, upewnij się, że masz spełnione następujące wymagania:

- **Java Development Environment** – dowolne IDE lub środowisko wiersza poleceń z Javą 8 lub nowszą.  
- **Aspose.3D Library** – pobierz najnowszy plik JAR z oficjalnej strony: [here](https://releases.aspose.com/3d/java/).

## Importowanie pakietów

Rozpocznij od zaimportowania niezbędnych pakietów do swojego projektu Java. Ten krok jest kluczowy, aby uzyskać dostęp do funkcjonalności udostępnianych przez bibliotekę Aspose.3D.

```java
import com.aspose.threed.*;
```

## Krok 1: Inicjalizacja obiektu sceny (initialize scene java)

Rozpocznijmy proces od zainicjowania obiektu sceny. Będzie on pełnił rolę płótna, na którym rozegra się nasza magia 3D.

```java
// Initialize scene object
Scene scene = new Scene();
```

## Krok 2: Definiowanie wektorów kolorów

W tym kroku definiujemy tablicę wektorów kolorów, które zostaną zastosowane do różnych elementów naszej sceny 3D.

```java
// Define color vectors
Vector3[] colors = new Vector3[] {
    new Vector3(1, 0, 0),
    new Vector3(0, 1, 0),
    new Vector3(0, 0, 1)
};
```

## Krok 3: Tworzenie siatki 3D w Javie przy użyciu Polygon Builder (create 3d mesh java)

Wykorzystaj klasę Common do stworzenia siatki przy użyciu metody polygon builder. Ta siatka będzie podstawą naszych elementów 3D.

```java
// Call Common class create mesh using polygon builder method to set mesh instance
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

## Jak ustawić kolor materiału dla każdego węzła?

Iteruj po wektorach kolorów, twórz węzły sześcianów i ustawiaj atrybuty takie jak materiał, **set material color** oraz translację. To jest sedno kontrolowania wyglądu każdej instancji siatki.

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

Określ katalog i nazwę pliku, w którym zostanie zapisana scena 3D w obsługiwanym formacie, w tym przypadku FBX7400ASCII. Ten krok również demonstruje **convert mesh to FBX**.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
MyDir = MyDir + "MeshGeometryData.fbx";

// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7400ASCII);
```

## Typowe pułapki i wskazówki

- **Problemy ze ścieżką** – Upewnij się, że ścieżka katalogu kończy się separatorem plików (`/` lub `\\`) przed dołączeniem nazwy pliku.  
- **Inicjalizacja licencji** – Jeśli zapomnisz ustawić licencję Aspose.3D przed wywołaniem `scene.save`, biblioteka będzie działać w trybie próbnym i może dodać znak wodny.  
- **Nadpisywanie materiału** – Ponowne użycie tej samej instancji `LambertMaterial` dla wielu węzłów spowoduje, że wszystkie węzły będą dzielić ten sam kolor. Zawsze twórz nowy materiał w każdej iteracji, jak pokazano powyżej.  
- **Duże siatki** – Dla siatek z milionami wierzchołków rozważ użycie `MeshBuilder` z indeksowanymi wielokątami, aby utrzymać rozmiar pliku FBX w rozsądnych granicach.

## Dodatkowe najczęściej zadawane pytania

**Q1: Czy mogę używać Aspose.3D z innymi frameworkami Java?**  
A1: Tak, Aspose.3D jest zaprojektowane tak, aby współpracować płynnie z różnymi frameworkami Java.

**Q2: Czy dostępne są opcje licencjonowania Aspose.3D?**  
A2: Tak, możesz zapoznać się z opcjami licencjonowania [here](https://purchase.aspose.com/buy).

**Q3: Jak mogę uzyskać wsparcie dla Aspose.3D?**  
A3: Odwiedź forum Aspose.3D [forum](https://forum.aspose.com/c/3d/18) w celu uzyskania pomocy i dyskusji.

**Q4: Czy dostępna jest darmowa wersja próbna?**  
A4: Tak, darmową wersję próbną możesz pobrać [here](https://releases.aspose.com/).

**Q5: Jak uzyskać tymczasową licencję dla Aspose.3D?**  
A5: Tymczasową licencję możesz uzyskać [here](https://purchase.aspose.com/temporary-license/).

## Podsumowanie

Gratulacje! Pomyślnie **przekonwertowałeś siatkę do FBX**, udostępniłeś dane geometrii siatki pomiędzy wieloma węzłami i ustawiłeś indywidualne kolory materiałów przy użyciu Aspose.3D dla Javy. Ten przepływ pracy zapewnia lekką, wielokrotnego użytku architekturę siatki, którą można wyeksportować do dowolnego potoku kompatybilnego z FBX.

---

**Last Updated:** 2026-02-17  
**Tested With:** Aspose.3D 24.11 for Java  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}