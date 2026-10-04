---
date: 2026-10-03
description: Dowiedz się, jak utworzyć sferę java i wyeksportować plik OBJ przy użyciu
  Aspose.3D, wiodącej biblioteki Java 3D do konwersji modeli 3D.
images:
- /java/3d-objects-and-scenes/modify-sphere-radius/og-image.png
keywords:
- create sphere java
- save 3d as obj
- java convert 3d model
- write obj file java
lastmod: 2026-10-03
linktitle: 'Utwórz sferę java: konwersja 3D do OBJ przy użyciu Aspose.3D'
og_description: Dowiedz się, jak utworzyć sferę java i wyeksportować plik OBJ przy
  użyciu Aspose.3D. Ten przewodnik krok po kroku pokazuje, jak dodać sferę, zmienić
  jej promień i zapisać jako OBJ.
og_image_alt: 'Guide: create sphere java and export OBJ using Aspose.3D'
og_title: Utwórz sferę java – eksport OBJ przy użyciu Aspose.3D
schemas:
- author: Aspose
  dateModified: '2026-10-03'
  description: Learn how to create sphere java and export OBJ file using Aspose.3D,
    the leading Java 3D library for converting 3D models.
  headline: 'Create sphere java: Convert 3D to OBJ with Aspose.3D'
  type: TechArticle
- description: Learn how to create sphere java and export OBJ file using Aspose.3D,
    the leading Java 3D library for converting 3D models.
  name: 'Create sphere java: Convert 3D to OBJ with Aspose.3D'
  steps:
  - name: Initialize a Scene
    text: '**Definition anchor:** The `Scene` class is Aspose.3D''s top‑level container
      that holds geometry, lights, and cameras for a 3D model. Creating a `Scene`
      gives you a workspace where you can add and manipulate objects. Creating a `Scene`
      gives you a container for all geometry, lights, and cameras. This'
  - name: Initialize a Sphere
    text: '**Definition anchor:** The `Sphere` class represents a geometric sphere
      primitive with a configurable radius, center, and material. By default it starts
      with a radius of 1.0. A `Sphere` object starts with a default radius of 1.0.
      Think of it as a blank canvas for the shape you want to export.'
  - name: Set the Desired Radius
    text: The `setRadius(double)` method updates the sphere’s size by assigning a
      new radius value in the same units used by the scene. Here we **write obj file
      java**‑style code that sets the exact radius. Replace `10` with any `double`
      value that matches your design requirements.
  - name: Add Sphere to the Scene
    text: This line **adds sphere to scene** by creating a child node under the root
      node. It’s the moment the geometry becomes part of the scene graph.
  - name: Export the Model as OBJ
    text: The `save(String, FileFormat)` method writes the entire scene to the specified
      file using the chosen format, such as OBJ. Calling `scene.save` **exports obj
      file java**‑style, effectively **save scene as obj**. The generated `sphere.obj`
      can be opened in any standard 3D viewer.
  type: HowTo
- questions:
  - answer: You can refer to the [Aspose.3D for Java documentation](https://reference.aspose.com/3d/java/)
      for comprehensive guidance.
    question: Where can I find the documentation for Aspose.3D for Java?
  - answer: 'Download the library from the releases page: [Download Aspose.3D for
      Java](https://releases.aspose.com/3d/java/).'
    question: How do I download Aspose.3D for Java?
  - answer: Yes, explore the features with a free trial by visiting [Aspose.3D Free
      Trial](https://releases.aspose.com/).
    question: Is there a free trial available for Aspose.3D for Java?
  - answer: Join the Aspose community at [Aspose.3D Support Forum](https://forum.aspose.com/c/3d/18)
      for assistance and discussions.
    question: Where can I get support for Aspose.3D for Java?
  - answer: Get a temporary license by visiting [Temporary License](https://purchase.aspose.com/temporary-license/).
    question: How can I obtain a temporary license for Aspose.3D?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- modify sphere radius
- export OBJ
- aspose.3d
- java 3d
- 3d conversion
title: 'Utwórz sferę java: konwersja 3D do OBJ przy użyciu Aspose.3D'
url: /pl/java/3d-objects-and-scenes/modify-sphere-radius/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Utwórz kulę w Java i wyeksportuj do OBJ

## Wprowadzenie

W tym samouczku nauczysz się, jak **create sphere java**, dostosować jej promień oraz **save 3d as obj** przy użyciu biblioteki Aspose.3D Java. Przejdziemy przez każdy wiersz kodu, wyjaśnimy, dlaczego każdy krok ma znaczenie, i podamy praktyczne wskazówki, abyś mógł z pewnością wbudować ten przepływ pracy w gry, narzędzia CAD lub wizualizacje naukowe.

## Szybkie odpowiedzi
- **What is the main goal of this tutorial?** Aby zademonstrować, jak **create sphere java**, zmodyfikować jej rozmiar i wyeksportować model jako OBJ przy użyciu Javy.  
- **Which library provides the 3D functionality?** Aspose.3D, pełna funkcjonalnie **java 3d library tutorial**.  
- **How do I change the sphere size?** Wywołaj `sphere.setRadius(double)` na instancji `Sphere`.  
- **Can I write the OBJ file directly from Java?** Tak — użyj `scene.save("file.obj", FileFormat.WAVEFRONTOBJ)`.  
- **Do I need a license for production?** Darmowa wersja próbna wystarczy do rozwoju; stała licencja jest wymagana do użytku komercyjnego.

## Co to jest Aspose.3D dla Javy?

Aspose.3D for Java to kompleksowa **java 3d library**, która umożliwia programistom tworzyć, edytować i konwertować pliki 3D bez zewnętrznych zależności. Obsługuje ponad **50 input and output formats** — w tym OBJ, FBX, STL i GLTF — co pozwala na płynną integrację z dowolnym potokiem 3‑D.

## Dlaczego konwertować 3D do OBJ?

Konwersja do OBJ zapewnia uniwersalnie obsługiwaną, tekstową reprezentację geometrii, którą może odczytać każde narzędzie 3D, co czyni ją idealną do szybkiego prototypowania, wymiany zasobów między platformami oraz łatwego debugowania danych wierzchołków. Ponieważ pliki OBJ są lekkie i czytelne dla człowieka, możesz je przeglądać lub modyfikować prostym edytorem tekstu w razie potrzeby.

## Wymagania wstępne

- Podstawowa znajomość programowania w Javie.  
- Biblioteka Aspose.3D zainstalowana – pobierz ją z [Aspose.3D for Java documentation](https://reference.aspose.com/3d/java/).  
- JDK 8 lub nowszy zainstalowany na Twoim komputerze deweloperskim.

## Importowanie pakietów

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Sphere;

import java.io.IOException;
```

## Jak zmodyfikować promień kuli w Java?

`Sphere` jest prymitywem geometrycznym reprezentującym kulę w Aspose.3D.

Załaduj obiekt `Sphere`, wywołaj `setRadius` z żądaną wartością, a następnie zapisz scenę jako OBJ — cały ten przepływ pracy można wykonać w pięciu zwięzłych krokach. Podejście działa dla dowolnego numerycznego promienia i zapewnia, że wyeksportowany OBJ odzwierciedla dokładny rozmiar, który określisz.

### Krok 1: Inicjalizacja sceny

```java
// ExStart:WorkingWithSphereRadius

// initialize a scene
Scene scene = new Scene();
```

**Definition anchor:** Klasa `Scene` jest kontenerem najwyższego poziomu w Aspose.3D, który przechowuje geometrię, światła i kamery dla modelu 3D. Tworzenie `Scene` daje Ci przestrzeń roboczą, w której możesz dodawać i manipulować obiektami.

Tworzenie `Scene` zapewnia kontener dla całej geometrii, świateł i kamer. To jest miejsce, w którym później **add sphere to scene**.

### Krok 2: Inicjalizacja kuli

```java
// initialize a Sphere
Sphere sphere = new Sphere();
```

**Definition anchor:** Klasa `Sphere` reprezentuje geometryczny prymityw kuli z konfigurowalnym promieniem, środkiem i materiałem. Domyślnie zaczyna się z promieniem 1.0.

Obiekt `Sphere` rozpoczyna z domyślnym promieniem 1.0. Traktuj go jako czyste płótno dla kształtu, który chcesz wyeksportować.

### Krok 3: Ustaw żądany promień

**Definition anchor:** Metoda `setRadius(double)` ustawia promień kuli w tych samych jednostkach, które są używane w scenie.  

```java
// set radius
sphere.setRadius(10);
```

Tutaj używamy kodu w stylu **write obj file java**, który ustawia dokładny promień. Zastąp `10` dowolną wartością `double`, która spełnia Twoje wymagania projektowe.

### Krok 4: Dodaj kulę do sceny

```java
// add sphere to the scene
scene.getRootNode().createChildNode(sphere);
```

Ten wiersz **adds sphere to scene** poprzez utworzenie węzła potomnego pod węzłem głównym. To moment, w którym geometria staje się częścią grafu sceny.

### Krok 5: Eksportuj model jako OBJ

```java
// save scene
scene.save("sphere.obj", FileFormat.WAVEFRONTOBJ);
```

Metoda `save(String, FileFormat)` zapisuje całą scenę do określonego pliku przy użyciu wybranego formatu, takiego jak OBJ. Wywołanie `scene.save` **exports obj file java**‑style, skutecznie **save scene as obj**. Wygenerowany `sphere.obj` może być otwarty w dowolnym standardowym przeglądarce 3D.

## Typowe problemy i rozwiązania

| Problem | Rozwiązanie |
|---------|-------------|
| **Sphere appears too small in the viewer** | Sprawdź, czy wartość promienia została ustawiona poprawnie; pamiętaj, że jednostki są arbitralne, chyba że zastosujesz transformację skalowania. |
| **Exported OBJ has no material** | Aspose.3D zapisuje tylko geometrię; dodaj materiał do kuli, jeśli potrzebujesz tekstur (`sphere.setMaterial(...)`). |
| **License exception at runtime** | Upewnij się, że przed utworzeniem `Scene` załadowano plik licencji tymczasowej lub stałej. |

## Frequently asked questions

**Q: Where can I find the documentation for Aspose.3D for Java?**  
A: You can refer to the [Aspose.3D for Java documentation](https://reference.aspose.com/3d/java/) for comprehensive guidance.

**Q: How do I download Aspose.3D for Java?**  
A: Download the library from the releases page: [Download Aspose.3D for Java](https://releases.aspose.com/3d/java/).

**Q: Is there a free trial available for Aspose.3D for Java?**  
A: Yes, explore the features with a free trial by visiting [Aspose.3D Free Trial](https://releases.aspose.com/).

**Q: Where can I get support for Aspose.3D for Java?**  
A: Join the Aspose community at [Aspose.3D Support Forum](https://forum.aspose.com/c/3d/18) for assistance and discussions.

**Q: How can I obtain a temporary license for Aspose.3D?**  
A: Get a temporary license by visiting [Temporary License](https://purchase.aspose.com/temporary-license/).

**Q: Can I use this code with other 3D formats like STL?**  
A: Absolutely – just change the `FileFormat` enum when calling `scene.save`, e.g., `FileFormat.STL`.

---

**Last Updated:** 2026-10-03  
**Tested With:** Aspose.3D for Java 24.11  
**Author:** Aspose

## Related tutorials

- [How to Set Normals on 3D Objects in Java Using Aspose.3D Java API](/3d/java/geometry/set-up-normals-on-3d-objects/)
- [How to Embed Texture in FBX with Java – Apply Materials to 3D Objects using Aspose.3D](/3d/java/geometry/apply-materials-to-3d-objects/)
- [How to Change Plane Orientation and Export OBJ in Java](/3d/java/3d-scenes-and-models/change-plane-orientation/)

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}