---
date: 2025-12-13
description: Dowiedz się, jak używać Aspose 3D Java do przekształcania węzłów 3D.
  Ten przewodnik pokazuje, jak używać kątów Eulera, dodać obrót 3D i ustawić translację
  w Javie.
linktitle: Aspose 3D Java – Transform 3D Nodes with Euler Angles
second_title: Aspose.3D Java API
title: Aspose 3D Java – Transformacja węzłów 3D za pomocą kątów Eulera
url: /pl/java/geometry/transform-3d-nodes-with-euler-angles/
weight: 19
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Transformuj węzły 3D za pomocą kątów Eulera w Javie przy użyciu Aspose.3D

## Wstęp

W tym samouczku odkryjesz **jak używać aspose 3d java**, aby przekształcać węzły 3D poprzez zastosowanie kątów Eulera. Po zakończeniu przewodnika będziesz w stanie dodać rotację 3d, ustawić translację java i tworzyć dynamiczne sceny reagujące na dane w czasie rzeczywistym.

## Szybkie odpowiedzi
- **Jaką bibliotekę obsługuje transformacje 3D w Javie?** Aspose 3D for Java.  
- **Która metoda ustawia rotację przy użyciu kątów Eulera?** `setEulerAngles()` na transformacji węzła.  
- **Jak przesunąć węzeł w przestrzeni?** Użyj `setTranslation()` z `Vector3`.  
- **Czy potrzebna jest licencja do produkcji?** Tak, wymagana jest komercyjna licencja Aspose 3D.  
- **Czy mogę eksportować do FBX?** Absolutnie – `scene.save(..., FileFormat.FBX7500ASCII)` działa od razu.

## Wymagania wstępne

Zanim zagłębimy się w samouczek, upewnij się, że spełniasz następujące wymagania:

- Podstawowa znajomość programowania w Javie.  
- Zainstalowany Java Development Kit (JDK) na twoim komputerze.  
- Biblioteka Aspose.3D, którą możesz pobrać z [Aspose.3D Java Documentation](https://reference.aspose.com/3d/java/).

## Importowanie pakietów

Rozpocznij od zaimportowania niezbędnych pakietów do swojego projektu Java. Upewnij się, że biblioteka Aspose.3D jest poprawnie dodana do classpath. Jeśli jeszcze jej nie pobrałeś, link do pobrania znajdziesz [tutaj](https://releases.aspose.com/3d/java/).

```java
import com.aspose.threed.*;
```

aspose 3d java – Praca z kątami Eulera

### Krok 1. Inicjalizacja sceny i węzła

Najpierw utwórz scenę i węzeł, który będzie zawierał geometrię, którą chcesz przekształcić.

```java
// ExStart:AddTransformationToNodeByEulerAngles
// Initialize scene object
Scene scene = new Scene();

// Initialize Node class object
Node cubeNode = new Node("cube");
```

### Krok 2. Utwórz siatkę i ustaw geometrię

Następnie wygeneruj prostą siatkę (w tym przypadku sześcian) i dołącz ją do węzła.

```java
// Call Common class create mesh using polygon builder method to set mesh instance
Mesh mesh = Common.createMeshUsingPolygonBuilder();

// Point node to the Mesh geometry
cubeNode.setEntity(mesh);
```

## Dodaj rotację 3D do węzła

### Krok 3. Ustaw kąty Eulera i translację

Teraz zastosujemy rotację przy użyciu kątów Eulera oraz przemieścimy węzeł do widocznej pozycji.

```java
// Euler angles
cubeNode.getTransform().setEulerAngles(new Vector3(0.3, 0.1, -0.5));

// Set translation
cubeNode.getTransform().setTranslation(new Vector3(0, 0, 20));
```

## Ustaw translację Java – pozycjonowanie węzła

Powyższy krok translacji demonstruje **set translation java** w praktyce: węzeł jest przesunięty o 20 jednostek wzdłuż osi Z, aby można go było zobaczyć po renderowaniu.

### Krok 4. Dodaj węzeł do sceny

Dołącz przekształcony węzeł do głównego węzła sceny.

```java
// Add cube to the scene
scene.getRootNode().getChildNodes().add(cubeNode);
```

### Krok 5. Zapisz scenę 3D

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

Upewnij się, że zamieniłeś `"Your Document Directory"` na odpowiednią ścieżkę na swoim komputerze.

## Podsumowanie

Gratulacje! Pomyślnie przekształciłeś węzły 3D przy użyciu kątów Eulera w Javie z **aspose 3d java**. Eksperymentuj z różnymi kątami i translacjami, aby tworzyć dynamiczne i angażujące sceny 3D.

## Najczęściej zadawane pytania

**Q:** Jaka jest różnica między kątami Eulera a rotacją kwaternionową?  
**A:** Kąty Eulera są intuicyjne (pitch, yaw, roll), ale mogą cierpieć na zjawisko blokady gimbal, podczas gdy kwaterniony unikają tego problemu i są lepsze do płynnych interpolacji.

**Q:** Czy mogę łączyć wiele transformacji na tym samym węźle?  
**A:** Tak. Wywołaj `setEulerAngles`, `setTranslation` i `setScale` w dowolnej kolejności; biblioteka łączy je w jedną macierz transformacji.

**Q:** Czy można eksportować do innych formatów, takich jak OBJ lub STL?  
**A:** Absolutnie. Zastąp `FileFormat.FBX7500ASCII` przez `FileFormat.OBJ` lub `FileFormat.STL` w wywołaniu `scene.save`.

**Q:** Jak zastosować tę samą rotację do kilku węzłów jednocześnie?  
**A:** Utwórz węzeł nadrzędny, zastosuj rotację do niego i dodaj węzły podrzędne. Wszystkie podrzędne dziedziczą transformację.

**Q:** Czy muszę wywoływać jakiekolwiek metody czyszczenia po zapisaniu?  
**A:** Zbieracz śmieci Javy obsługuje większość zasobów, ale możesz jawnie wywołać `scene.dispose()`, jeśli pracujesz z dużymi scenami w długotrwałej aplikacji.

---

**Last Updated:** 2025-12-13  
**Tested With:** Aspose.3D 23.12 for Java  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}