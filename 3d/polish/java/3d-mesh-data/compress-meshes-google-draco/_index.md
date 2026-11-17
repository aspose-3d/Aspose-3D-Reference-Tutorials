---
date: 2026-11-17
description: Jak zmniejszyć rozmiar modelu 3D, generując siatkę sfery w Javie i kompresując
  ją za pomocą Google Draco poprzez Aspose.3D. Poznaj pełny przepływ pracy w kilka
  minut.
images:
- /java/3d-mesh-data/compress-meshes-google-draco/og-image.png
keywords:
- create sphere mesh
- how to compress 3d
- reduce 3d model size
- aspose 3d java
- compress 3d mesh
lastmod: 2026-11-17
linktitle: Jak zmniejszyć rozmiar modelu 3D – Utwórz siatkę sfery w Javie przy użyciu
  Google Draco
og_description: Utwórz siatkę sfery i skompresuj model 3D przy użyciu Java, Aspose.3D
  i Google Draco. Ten samouczek pokazuje, jak wygenerować sferę, wyeksportować do
  .drc i osiągnąć redukcję rozmiaru do 95% w ciągu kilku minut.
og_image_alt: 'Developer guide: Reduce 3d model size with Java sphere mesh and Draco
  compression'
og_title: Utwórz siatkę sfery i skompresuj model 3D przy użyciu Java i Draco
schemas:
- author: Aspose
  dateModified: '2026-11-17'
  description: How to reduce 3d model size by generating a sphere mesh in Java and
    compressing it with Google Draco via Aspose.3D. Learn the full workflow in minutes.
  headline: How to reduce 3d model size with a Java sphere mesh and Draco
  type: TechArticle
- description: How to reduce 3d model size by generating a sphere mesh in Java and
    compressing it with Google Draco via Aspose.3D. Learn the full workflow in minutes.
  name: How to reduce 3d model size with a Java sphere mesh and Draco
  steps:
  - name: set up the project
    text: Create a new Java project (any IDE works) and add all Aspose.3D JARs to
      the classpath. Keep your source files in a package such as `com.example.draco`
      for clarity.
  - name: how to create sphere mesh in Java
    text: 'The `Sphere` class is Aspose.3D''s built‑in geometry generator that produces
      a triangulated mesh with a configurable radius and tessellation. > **Pro tip:**
      The `Sphere` class generates a triangulated mesh with a default radius of 1.0.
      You can pass custom radius, tessellation, or material parameters '
  - name: export the mesh to Draco format
    text: After the sphere is added to a `Scene` object, call `scene.save("sphere.drc",
      SaveFormat.Draco)`. Aspose.3D automatically selects optimal compression settings,
      but you can fine‑tune them by adjusting `DracoCompressionOptions` if you need
      the smallest possible file. `DracoCompressionOptions` lets you
  - name: verify the output
    text: Open the generated `.drc` file with a Draco viewer (e.g., three.js `DRACOLoader`)
      to ensure the geometry renders correctly. You’ll notice a dramatic reduction
      in file size—often a factor of ten or more.
  type: HowTo
- questions:
  - answer: Yes, Aspose.3D supports OBJ, FBX, STL, GLTF, and many others, making it
      a versatile choice for **Aspose 3d export** pipelines.
    question: Is Aspose.3D compatible with different 3d file formats?
  - answer: Absolutely. Draco offers native libraries for C++, Python, and JavaScript.
      This tutorial focuses on Java, but the concepts apply across languages.
    question: Can I use Google Draco for compression in other programming languages?
  - answer: Visit the **[Aspose.3D Java documentation](https://reference.aspose.com/3d/java/)**
      for full API references and more examples.
    question: Where can I find additional Aspose.3D documentation?
  - answer: Explore temporary licensing options on the **[Aspose temporary license
      page](https://purchase.aspose.com/temporary-license/)**.
    question: How do I obtain a temporary license for Aspose.3D?
  - answer: Yes, join the discussion at the **[Aspose.3D Forum](https://forum.aspose.com/c/3d/18)**.
    question: Is there a community forum for Aspose.3D support?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- reduce 3d model size
- Aspose.3D
- Java 3D compression
- Google Draco
- sphere mesh
title: Jak zmniejszyć rozmiar modelu 3D przy użyciu siatki sfery w Javie i Draco
url: /pl/java/3d-mesh-data/compress-meshes-google-draco/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Jak zmniejszyć rozmiar modelu 3d przy użyciu siatki sfery w Javie i Draco

## Wprowadzenie

Aspose.3D for Java to biblioteka umożliwiająca tworzenie, manipulację i konwersję modeli 3‑D bezpośrednio z kodu Java. Jeśli szukasz szybkiego sposobu na **zmniejszenie rozmiaru modelu 3d**, zachowując jednocześnie wysoką jakość geometrii, trafiłeś we właściwe miejsce. W tym samouczku przeprowadzimy Cię przez generowanie siatki sfery przy użyciu **Aspose.3D for Java**, a następnie kompresję tej siatki za pomocą **Google Draco**. Na końcu będziesz mieć gotowy plik `.drc`, który jest dramatycznie mniejszy niż oryginał, co czyni go idealnym dla przeglądarek internetowych, gier mobilnych lub każdej aplikacji Java z ograniczoną przepustowością.

## Szybkie odpowiedzi
- **Co obejmuje ten samouczek?** Tworzenie siatki sfery w Javie i kompresja jej przy użyciu Google Draco poprzez Aspose.3D.  
- **Główna biblioteka?** Aspose.3D for Java (used for both mesh creation and Draco export).  
- **Typowy czas implementacji?** Około 10‑15 minut dla podstawowej sfery.  
- **Kluczowy warunek wstępny?** Środowisko programistyczne Java z JAR‑ami Aspose.3D na classpath.  
- **Wynik?** Plik `.drc`, który **zmniejsza rozmiar modelu 3d** nawet o 95 % w porównaniu z nieskompresowaną siatką.

## Jak zmniejszyć rozmiar modelu 3d?

Załaduj swoją sferę i skompresuj ją w dwóch prostych krokach. Najpierw **tworzysz siatkę sfery** przy użyciu `new Sphere(1.0, 32, 32)`. Następnie eksportujesz scenę bezpośrednio do Draco używając `scene.save("sphere.drc", SaveFormat.Draco)`. Aspose.3D automatycznie obsługuje kwantyzację geometrii i deduplikację wierzchołków, dostarczając pliki, które są zazwyczaj o 80‑95 % mniejsze, zachowując jednocześnie wierność wizualną.

Klasa `Sphere` jest wbudowanym generatorem geometrii Aspose.3D, który tworzy trójkątną siatkę sfery. Akceptuje promień oraz parametry teselacji, pozwalając kontrolować poziom szczegółowości przed kompresją.

## Co oznacza „zmniejszenie rozmiaru modelu 3d” w kontekście rozwoju 3d?

**Zmniejszanie rozmiaru modelu 3d** oznacza redukcję ilości danych geometrycznych, które muszą być przesłane lub przechowywane, bez zauważalnego pogorszenia jakości wizualnej. Draco osiąga to poprzez kodowanie pozycji wierzchołków, normalnych i innych atrybutów w wysoce skompaktowanym formacie binarnym. W połączeniu z Aspose.3D cały proces pozostaje w środowisku Java, więc nie musisz zarządzać natywnymi binariami.

## Dlaczego używać kompresji siatek Google Draco z Aspose.3D?

Google Draco w połączeniu z Aspose.3D zapewnia wydajny potok, który dramatycznie zmniejsza pliki siatek, jednocześnie pozostając łatwym do integracji w projektach Java. Biblioteka obsługuje całe niskopoziomowe kodowanie, dzięki czemu programiści mogą skupić się na tworzeniu geometrii, nie zajmując się natywnymi binariami Draco, co skutkuje szybszym rozwojem i mniejszymi zasobami dla sieci i urządzeń mobilnych.

- **Ogromna redukcja rozmiaru:** Draco może zredukować dane siatki nawet o 95 % dla typowych modeli, zamieniając 5 MB OBJ na 0,3 MB `.drc`.  
- **Szybkie dekodowanie w czasie wykonywania:** Silniki takie jak Unity, Unreal i three.js dekodują Draco natywnie, co prowadzi do szybszych czasów ładowania.  
- **Bezproblemowa integracja z Java:** Aspose.3D abstrahuje natywną bibliotekę Draco, pozwalając pozostać w ekosystemie Java.  
- **Jednoetapowy eksport Aspose 3D:** To samo API, którego używasz do tworzenia geometrii, obsługuje także eksport, upraszczając potok.

Aspose.3D obsługuje **ponad 50 formatów wejściowych i wyjściowych** — w tym OBJ, FBX, STL, GLTF i wiele innych — i może przetwarzać modele liczące setki stron bez ładowania całego pliku do pamięci.

## Wymagania wstępne

- **Java Development Kit (JDK)** – wersja 8 lub nowsza.  
- **Aspose.3D for Java** – pobierz najnowsze JAR‑y ze **[strony wydań Aspose 3D Java](https://releases.aspose.com/3d/java/)**.  
- **Podstawowa znajomość Google Draco** – użyjesz wrappera Aspose.3D, więc nie jest wymagana natywna konfiguracja Draco.

## Importowanie pakietów

```java
import com.aspose.threed.DracoCompressionLevel;
import com.aspose.threed.DracoSaveOptions;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Sphere;


import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
```

## Przewodnik krok po kroku

### Krok 1: skonfiguruj projekt

Utwórz nowy projekt Java (dowolne IDE będzie działać) i dodaj wszystkie JAR‑y Aspose.3D do classpath. Trzymaj pliki źródłowe w pakiecie takim jak `com.example.draco` dla przejrzystości.

### Krok 2: jak stworzyć siatkę sfery w Javie

Klasa `Sphere` jest wbudowanym generatorem geometrii Aspose.3D, który tworzy trójkątną siatkę sfery.  

```java
import java.nio.file.Files;
import java.nio.file.Paths;
import com.aspose.threed.Sphere;
import com.aspose.threed.DracoSaveOptions;
import com.aspose.threed.DracoCompressionLevel;
import com.aspose.threed.FileFormat;

// ExStart:Encode3DMeshinGoogleDraco
// The path to the documents directory.
String MyDir = "Your Document Directory";

// Create a sphere
Sphere sphere = new Sphere();

// Encode the sphere to Google Draco raw data using optimal compression level.
DracoSaveOptions opt = new DracoSaveOptions();
opt.setCompressionLevel(DracoCompressionLevel.OPTIMAL);
byte[] b = FileFormat.DRACO.encode(sphere.toMesh(), opt);

// Save the raw bytes to file
Files.write(Paths.get(MyDir, "SphereMeshtoDRC_Out.drc"), b);
// ExEnd:Encode3DMeshinGoogleDraco
```

> **Pro tip:** Klasa `Sphere` generuje trójkątną siatkę z domyślnym promieniem 1.0. Możesz podać własny promień, teselację lub parametry materiału, jeśli potrzebujesz innego poziomu szczegółowości przed kompresją.

### Krok 3: eksportuj siatkę do formatu Draco

Klasa `Scene` reprezentuje kompletną scenę 3‑D, która może zawierać siatki, światła i kamery. Klasa `DracoCompressionOptions` pozwala dostosować ustawienia kompresji Draco, takie jak kwantyzacja i poziom kompresji. Po dodaniu sfery do obiektu `Scene`, wywołaj `scene.save("sphere.drc", SaveFormat.Draco)`. Aspose.3D automatycznie wybiera optymalne ustawienia kompresji, ale możesz je precyzyjnie dostroić, modyfikując `DracoCompressionOptions`, jeśli potrzebujesz najmniejszego możliwego pliku. `DracoCompressionOptions` pozwala

### Krok 4: zweryfikuj wynik

`DRACOLoader` to narzędzie three.js, które ładuje pliki `.drc` skompresowane Draco i konwertuje je na geometrię kompatybilną z WebGL. Otwórz wygenerowany plik `.drc` w przeglądarce Draco (np. three.js `DRACOLoader`), aby upewnić się, że geometria renderuje się poprawnie. Zauważysz dramatyczną redukcję rozmiaru pliku — często dziesięciokrotną lub większą.

## Typowe przypadki użycia

| Scenariusz | Dlaczego zmniejszyć rozmiar modelu? | Jak ten samouczek pomaga |
|------------|-------------------------------------|--------------------------|
| Konfiguratory produktów w sieci | Szybsze ładowanie stron przy wolnych połączeniach | Pliki skompresowane Draco `.drc` ładują się w ciągu kilku sekund |
| Aplikacje mobilne AR/VR | Mniejsze zużycie pamięci na urządzeniach | Mniejsze siatki utrzymują responsywność aplikacji |
| Sceny renderowane w chmurze | Obniżenie kosztów przepustowości | Eksport jednym kliknięciem z Aspose.3D do Draco |

## Typowe problemy i rozwiązania

| Problem | Powód | Rozwiązanie |
|---------|-------|-------------|
| **`NoClassDefFoundError` for Draco classes** | JAR‑y Aspose.3D nie znajdują się w classpath | Sprawdź, czy *wszystkie* pliki JAR Aspose.3D są dołączone i czy wersja odpowiada dokumentacji. |
| **Output file is empty** | `MyDir` wskazuje na nieistniejący folder | Utwórz katalog programowo (`Files.createDirectories(Paths.get(MyDir))`) przed zapisem pliku. |
| **Compressed mesh looks distorted** | Użycie niskiego poziomu kompresji lub niewystarczającej teselacji | Przejdź na `DracoCompressionLevel.OPTIMAL` i zwiększ teselację sfery (np. `new Sphere(1.0, 64, 64)`). `DracoCompressionLevel.OPTIMAL` wybiera najwyższą jakość kompresji dla wyjścia Draco. |

## Najczęściej zadawane pytania

**Q: Czy Aspose.3D jest kompatybilny z różnymi formatami plików 3d?**  
A: Tak, Aspose.3D obsługuje OBJ, FBX, STL, GLTF i wiele innych, co czyni go wszechstronnym wyborem dla **pipeline'ów eksportu Aspose 3d**.

**Q: Czy mogę używać Google Draco do kompresji w innych językach programowania?**  
A: Oczywiście. Draco oferuje natywne biblioteki dla C++, Pythona i JavaScript. Ten samouczek koncentruje się na Javie, ale koncepcje mają zastosowanie w różnych językach.

**Q: Gdzie mogę znaleźć dodatkową dokumentację Aspose.3D?**  
A: Odwiedź **[dokumentację Aspose.3D Java](https://reference.aspose.com/3d/java/)**, aby uzyskać pełne odniesienia API i więcej przykładów.

**Q: Jak uzyskać tymczasową licencję na Aspose.3D?**  
A: Zapoznaj się z opcjami tymczasowego licencjonowania na **[stronie tymczasowej licencji Aspose](https://purchase.aspose.com/temporary-license/)**.

**Q: Czy istnieje forum społecznościowe wsparcia Aspose.3D?**  
A: Tak, dołącz do dyskusji na **[forum Aspose.3D](https://forum.aspose.com/c/3d/18)**.

## Zakończenie

W tym przewodniku pokazaliśmy, jak **zmniejszyć rozmiar modelu 3d** poprzez stworzenie siatki sfery w Javie i jej kompresję przy użyciu Google Draco za pośrednictwem Aspose.3D. Postępując zgodnie z tymi zwięzłymi krokami, możesz drastycznie zmniejszyć pliki siatek, przyspieszyć czasy ładowania oraz utrzymać aplikacje 3d oparte na Javie responsywne i przyjazne pod względem przepustowości.

---

**Ostatnia aktualizacja:** 2026-11-17  
**Testowano z:** Aspose.3D for Java 24.12 (latest)  
**Autor:** Aspose

## Powiązane samouczki

- [Zmniejsz rozmiar pliku 3D – kompresuj sceny przy użyciu Aspose.3D for Java](/3d/java/3d-scenes-and-models/compress-3d-scenes/)
- [Generuj chmurę punktów Draco z sfer przy użyciu Aspose.3D for Java](/3d/java/point-clouds/generate-point-clouds-spheres-java/)
- [Naucz się triangulować siatki dla zoptymalizowanego renderowania w Javie przy użyciu Aspose.3D](/3d/java/geometry/triangulate-meshes-for-optimized-rendering/)

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}