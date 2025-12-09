---
date: 2025-12-08
description: Poznaj samouczek grafiki 3D w Javie, jak dodać teksturę przy użyciu Aspose.3D.
  Szybko zastosuj realistyczne materiały do obiektów 3D w Javie.
language: pl
linktitle: Apply Materials to 3D Objects in Java with Aspose.3D
second_title: Aspose.3D Java API
title: Samouczek grafiki 3D w Javie – Zastosuj materiały do obiektów 3D w Javie z
  Aspose.3D
url: /java/geometry/apply-materials-to-3d-objects/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Zastosuj materiały do obiektów 3D w Javie z Aspose.3D

## Wprowadzenie

W tym **samouczku grafiki 3D w Javie** pokażemy Ci **jak dodać teksturę w Javie** do prostego sześcianu 3‑D przy użyciu API Aspose.3D Java. Nakładanie materiałów i tekstur to kluczowy krok, który zamienia płaską siatkę w realistyczny obiekt, którego możesz używać w grach, wizualizacjach czy prezentacjach produktów. Po zakończeniu tego przewodnika będziesz mieć w pełni teksturowany plik FBX, który możesz otworzyć w dowolnym przeglądarce 3‑D.

## Szybkie odpowiedzi
- **Jaki jest główny cel?** Zastosować materiał Phonga z teksturą dyfuzyjną do sześcianu.  
- **Która biblioteka?** Aspose.3D for Java (dostępna wersja próbna).  
- **Jak długo to trwa?** Około 10‑15 minut dla działającego przykładu.  
- **Czy potrzebna jest licencja?** Wymagana jest tymczasowa licencja dla wersji nie‑ewaluacyjnych.  
- **Jaki format pliku jest generowany?** FBX 7.4 ASCII (kompatybilny z większością narzędzi 3‑D).

## Czym jest samouczek grafiki 3D w Javie?

**Samouczek grafiki 3D w Javie** prowadzi Cię przez tworzenie, manipulowanie i eksportowanie treści 3‑D przy użyciu bibliotek opartych na Javie. W tym przypadku skupiamy się na obsłudze materiałów — przypisywaniu kolorów, tekstur i właściwości oświetlenia do elementów geometrycznych.

## Dlaczego używać Aspose.3D do dodawania tekstur w Javie?

Aspose.3D oferuje czyste, obiektowo‑zorientowane API, które ukrywa szczegóły niskopoziomowe formatów plików. Obsługuje szeroką gamę formatów (FBX, STL, OBJ, itp.) i pozwala osadzać tekstury bezpośrednio w pliku, co jest idealne, gdy potrzebujesz jednego, przenośnego zasobu.

## Wymagania wstępne

Przed rozpoczęciem upewnij się, że masz:

- Zainstalowany Java Development Kit (JDK 8 lub nowszy).  
- Najnowszy plik JAR Aspose.3D for Java dodany do classpath projektu.  
- Podstawową znajomość składni Javy i programowania obiektowego.

## Importowanie pakietów

```java
import com.aspose.threed.*;


import java.nio.file.Files;
import java.nio.file.Paths;
```

## Krok 1: Inicjalizacja obiektu sceny

```java
// Initialize scene object
Scene scene = new Scene();
```

## Krok 2: Inicjalizacja obiektu węzła sześcianu

```java
// Initialize cube node object
Node cubeNode = new Node("cube");
```

## Krok 3: Tworzenie siatki przy użyciu Polygon Builder

```java
// Call Common class create mesh using polygon builder method to set mesh instance
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

## Krok 4: Powiązanie węzła z siatką

```java
// Point node to the mesh
cubeNode.setEntity(mesh);
```

## Krok 5: Dodanie sześcianu do sceny

```java
// Add cube to the scene
scene.getRootNode().addChildNode(cubeNode);
```

## Krok 6: Inicjalizacja obiektu PhongMaterial

```java
// Initialize PhongMaterial object
PhongMaterial mat = new PhongMaterial();
```

## Krok 7: Inicjalizacja obiektu tekstury

```java
// Initialize Texture object
Texture diffuse = new Texture();
```

## Krok 8: Ustawienie lokalnej ścieżki pliku dla tekstury

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
```

## Krok 9: Ustawienie lokalnej ścieżki pliku dla osadzonej tekstury

```java
// Set local file path for embedded texture
diffuse.setFileName(MyDir + "surface.dds");
```

## Krok 10: Ustawienie tekstury materiału

```java
// Set Texture of the material
mat.setTexture(Material.MAP_DIFFUSE, diffuse);
```

## Krok 11: Osadzenie surowych danych w FBX (opcjonalnie)

```java
// Set file name for embedded texture
diffuse.setFileName("embedded-texture.png");
// Set binary content
diffuse.setContent(Files.readAllBytes(Paths.get(MyDir, "aspose-logo.jpg")));
```

## Krok 12: Ustawienie koloru odbicia

```java
// Set specular color
mat.setSpecularColor(new Vector3(1, 0, 0));
```

## Krok 13: Ustawienie jasności

```java
// Set brightness
mat.setShininess(100);
```

## Krok 14: Ustawienie właściwości materiału obiektu sześcianu

```java
// Set material property of the cube object
cubeNode.setMaterial(mat);
```

## Krok 15: Zapis sceny 3D

```java
// Set the file name
MyDir = MyDir + "MaterialToCube.fbx";
// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7400ASCII);
```

## Typowe problemy i rozwiązania

| Problem | Przyczyna | Rozwiązanie |
|-------|--------|-----|
| **Tekstura niewidoczna** | Nieprawidłowa ścieżka pliku lub nieobsługiwany format tekstury. | Sprawdź, czy `MyDir` wskazuje prawidłowy folder i użyj obsługiwanego formatu, takiego jak `.dds` lub `.png`. |
| **Plik FBX nie ładuje się** | Brak danych wbudowanej tekstury. | Użyj opcjonalnego bloku (Krok 11), aby osadzić bajty tekstury bezpośrednio w FBX. |
| **Materiał jest czarny** | Nie ustawiono wartości specular lub diffuse. | Upewnij się, że `setSpecularColor` i `setTexture` są wywoływane przed zapisem. |

## Najczęściej zadawane pytania

**Q: Czy mogę zastosować wiele materiałów do jednego obiektu 3D?**  
A: Tak, Aspose.3D pozwala przypisać różne materiały do oddzielnych części siatki lub pod‑węzłów.

**Q: Jakie formaty plików Aspose.3D obsługuje przy zapisywaniu scen?**  
A: FBX, STL, OBJ, 3DS i kilka innych. Zobacz pełną listę w oficjalnej [dokumentacji](https://reference.aspose.com/3d/java/).

**Q: Czy dostępna jest tymczasowa licencja dla Aspose.3D for Java?**  
A: Tak, możesz uzyskać [tymczasową licencję](https://purchase.aspose.com/temporary-license/) do oceny.

**Q: Gdzie mogę znaleźć wsparcie dla Aspose.3D?**  
A: Najlepszym miejscem jest [forum Aspose.3D](https://forum.aspose.com/c/3d/18), gdzie pomaga społeczność.

**Q: Czy mogę pobrać bibliotekę Aspose.3D z konkretnego linku?**  
A: Oczywiście — użyj [linku do pobrania](https://releases.aspose.com/3d/java/), aby uzyskać najnowsze pliki JAR.

---

**Ostatnia aktualizacja:** 2025-12-08  
**Testowano z:** Aspose.3D for Java 24.11  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}