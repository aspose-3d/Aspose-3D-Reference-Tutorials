---
date: 2026-02-20
description: Dowiedz się, jak tworzyć siatkę w Aspose Java i przekształcać węzły 3D
  przy użyciu kątów Eulera, dodać obrót 3D oraz ustawić translację w Javie.
linktitle: Create Mesh Aspose Java – Transform 3D Nodes with Euler Angles
second_title: Aspose.3D Java API
title: Utwórz siatkę Aspose Java – Transformuj węzły 3D za pomocą kątów Eulera
url: /pl/java/geometry/transform-3d-nodes-with-euler-angles/
weight: 19
---

 (keep)

**Author:** Aspose (keep)

Then closing shortcodes.

Now ensure we keep all markdown formatting, code block placeholders unchanged.

Also note "All URLs and file paths (never translate these)" we kept them unchanged.

Now produce final content with translations.

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Transformuj węzły 3D za pomocą kątów Eulera w Javie z użyciem Aspose.3D

## Wstęp

W tym samouczku dowiesz się, jak **create mesh aspose java** i przekształcać węzły 3D, stosując kąty Eulera. Po zakończeniu przewodnika będziesz w stanie dodać rotację 3D, ustawić translation java oraz tworzyć dynamiczne sceny reagujące na dane w czasie rzeczywistym.

## Szybkie odpowiedzi
- **Jaką bibliotekę obsługuje transformacje 3D w Javie?** Aspose 3D for Java.  
- **Która metoda ustawia rotację przy użyciu kątów Eulera?** `setEulerAngles()` on the node’s transform.  
- **Jak przesunąć węzeł w przestrzeni?** Use `setTranslation()` with a `Vector3`.  
- **Czy potrzebna jest licencja do produkcji?** Yes, a commercial Aspose 3D license is required.  
- **Czy mogę eksportować do FBX?** Absolutely – `scene.save(..., FileFormat.FBX7500ASCII)` works out of the box.

## Wymagania wstępne

Zanim przejdziemy do samouczka, upewnij się, że spełniasz następujące wymagania:

- Podstawowa znajomość programowania w Javie.  
- Zainstalowany Java Development Kit (JDK) na Twoim komputerze.  
- Biblioteka Aspose.3D, którą możesz pobrać z [Aspose.3D Java Documentation](https://reference.aspose.com/3d/java/).

## Importowanie pakietów

Rozpocznij od zaimportowania niezbędnych pakietów do swojego projektu w Javie. Upewnij się, że biblioteka Aspose.3D została poprawnie dodana do classpath. Jeśli jeszcze jej nie pobrałeś, znajdziesz link do pobrania [tutaj](https://releases.aspose.com/3d/java/).

```java
import com.aspose.threed.*;
```

## Utwórz siatkę Aspose Java

Pierwszym krokiem w każdym przepływie pracy 3D jest **create mesh aspose java** – czyli zbudowanie danych geometrycznych, które później zostaną przekształcone. W tym przykładzie wygenerujemy prostą siatkę sześcianu przy użyciu metod pomocniczych Aspose i dołączymy ją do węzła.

### aspose 3d java – Praca z kątami Eulera

#### Krok 1. Inicjalizacja sceny i węzła

Najpierw utwórz scenę i węzeł, które będą przechowywać geometrię, którą chcesz przekształcić.

```java
// ExStart:AddTransformationToNodeByEulerAngles
// Initialize scene object
Scene scene = new Scene();

// Initialize Node class object
Node cubeNode = new Node("cube");
```

#### Krok 2. Utwórz siatkę i ustaw geometrię

Następnie wygeneruj prostą siatkę (w tym przypadku sześcian) i dołącz ją do węzła.

```java
// Call Common class create mesh using polygon builder method to set mesh instance
Mesh mesh = Common.createMeshUsingPolygonBuilder();

// Point node to the Mesh geometry
cubeNode.setEntity(mesh);
```

## Dodaj rotację 3D do węzła

#### Krok 3. Ustaw kąty Eulera i translację

Teraz stosujemy rotację przy użyciu kątów Eulera oraz przesuwamy węzeł do widocznej pozycji.

```java
// Euler angles
cubeNode.getTransform().setEulerAngles(new Vector3(0.3, 0.1, -0.5));

// Set translation
cubeNode.getTransform().setTranslation(new Vector3(0, 0, 20));
```

## Ustaw translację Java – pozycjonowanie węzła

Powyższy krok translacji demonstruje **set translation java** w praktyce: węzeł jest przesunięty o 20 jednostek wzdłuż osi Z, aby był widoczny po renderowaniu.

## Krok 4. Dodaj węzeł do sceny

Dołącz przekształcony węzeł do głównego węzła sceny.

```java
// Add cube to the scene
scene.getRootNode().getChildNodes().add(cubeNode);
```

## Krok 5. Zapisz scenę 3D

Na koniec wyeksportuj scenę do pliku FBX (lub innego obsługiwanego formatu).

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
MyDir = MyDir + "TransformationToNode.fbx";

// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7500ASCII);
// ExEnd:AddTransformationToNodeByEulerAngles
System.out.println("\nTransformation added successfully to node.\nFile saved at " + MyDir);
```

Upewnij się, że zamienisz `"Your Document Directory"` na odpowiednią ścieżkę na swoim komputerze.

## Dlaczego używać kątów Eulera z Aspose 3D?

Kąty Eulera zapewniają intuicyjny sposób myślenia o rotacjach — pitch, yaw i roll — co czyni je idealnymi do szybkiego prototypowania lub gdy trzeba udostępnić kontrolki rotacji użytkownikom końcowym. Aspose 3D abstrahuje skomplikowaną matematykę macierzy, dzięki czemu możesz skupić się na efekcie wizualnym, a nie na matematyce.

## Typowe przypadki użycia

- **Wizualizacja danych w czasie rzeczywistym:** Obracaj model na podstawie danych z czujników.  
- **Rig kamery w stylu gry:** Zastosuj yaw‑pitch‑roll, aby zasymulować kamerę.  
- **Konfiguratory produktów:** Pozwól klientom obracać model 3D produktu za pomocą prostych suwaków.  

## Rozwiązywanie problemów i wskazówki

- **Gimbal lock:** Jeśli zauważysz nieoczekiwane przeskoki przy rotacji, rozważ przejście na rotację opartą na kwaternionach (`setRotationQuaternion()`).  
- **Spójność jednostek:** Aspose 3D działa w tych samych jednostkach, które podajesz; utrzymuj wartości translacji zgodne ze skalą modelu.  
- **Wydajność:** W przypadku dużych scen wywołaj `scene.dispose()` po zapisaniu, aby zwolnić zasoby natywne.  

## Najczęściej zadawane pytania

**Q: Jaka jest różnica między kątami Eulera a rotacją kwaternionową?**  
A: Kąty Eulera są intuicyjne (pitch, yaw, roll), ale mogą cierpieć na gimbal lock, podczas gdy kwaterniony unikają tego problemu i są lepsze do płynnych interpolacji.

**Q: Czy mogę łączyć wiele transformacji na tym samym węźle?**  
A: Tak. Wywołaj `setEulerAngles`, `setTranslation` i `setScale` w dowolnej kolejności; biblioteka łączy je w jedną macierz transformacji.

**Q: Czy można eksportować do innych formatów, takich jak OBJ lub STL?**  
A: Oczywiście. Zastąp `FileFormat.FBX7500ASCII` przez `FileFormat.OBJ` lub `FileFormat.STL` w wywołaniu `scene.save`.

**Q: Jak zastosować tę samą rotację do kilku węzłów jednocześnie?**  
A: Utwórz węzeł nadrzędny, zastosuj rotację do niego, a następnie dodaj węzły podrzędne. Wszystkie podrzędne dziedziczą transformację.

**Q: Czy muszę wywoływać jakiekolwiek metody czyszczenia po zapisaniu?**  
A: Garbage collector Javy obsługuje większość zasobów, ale możesz jawnie wywołać `scene.dispose()`, jeśli pracujesz z dużymi scenami w długotrwałej aplikacji.

## Podsumowanie

Gratulacje! Pomyślnie **created mesh aspose java** i przekształciłeś węzły 3D przy użyciu kątów Eulera w Javie z Aspose 3D. Eksperymentuj z różnymi kątami, translacjami i nawet rotacjami kwaternionowymi, aby tworzyć dynamiczne i angażujące doświadczenia 3D.

---

**Last Updated:** 2026-02-20  
**Tested With:** Aspose.3D 23.12 for Java  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}