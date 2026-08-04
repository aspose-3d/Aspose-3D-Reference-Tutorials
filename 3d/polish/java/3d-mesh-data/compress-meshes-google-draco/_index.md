---
date: 2026-04-29
description: Dowiedz się, jak zmniejszyć rozmiar modelu 3D, tworząc siatkę kuli w
  Javie i kompresując ją przy użyciu Google Draco oraz Aspose.3D – niezbędne przy
  eksporcie Aspose 3D.
keywords:
- reduce 3d model size
- aspose 3d export
- compress 3d mesh java
linktitle: Jak stworzyć siatkę sfery w Javie – kompresja siatek 3D za pomocą Google
  Draco
second_title: Aspose.3D Java API
title: 'Zmniejsz rozmiar modelu 3D: Stwórz siatkę sfery w Javie z Draco'
url: /pl/java/3d-mesh-data/compress-meshes-google-draco/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Zmniejsz rozmiar modelu 3D: Utwórz siatkę sfery w Javie z Draco

## Wprowadzenie

Jeśli szukasz szybkiego sposobu na **zmniejszenie rozmiaru modelu 3D**, jednocześnie zachowując wysoką jakość geometrii, trafiłeś we właściwe miejsce. W tym samouczku przeprowadzimy Cię przez generowanie siatki sfery przy użyciu **Aspose.3D for Java**, a następnie kompresję tej siatki za pomocą **Google Draco**. Po zakończeniu będziesz mieć gotowy do użycia plik `.drc`, który jest dramatycznie mniejszy niż oryginał, co czyni go idealnym dla przeglądarek internetowych, gier mobilnych lub dowolnej aplikacji Java z ograniczoną przepustowością.

## Szybkie odpowiedzi
- **Co obejmuje ten samouczek?** Tworzenie siatki sfery w Javie i kompresja jej przy użyciu Google Draco poprzez Aspose.3D.  
- **Podstawowa biblioteka?** Aspose.3D for Java (używany zarówno do tworzenia siatki, jak i eksportu Draco).  
- **Typowy czas implementacji?** Około 10‑15 minut dla podstawowej sfery.  
- **Kluczowy warunek wstępny?** Środowisko programistyczne Java z plikami JAR Aspose.3D na ścieżce klas.  
- **Rezultat?** Plik `.drc`, który **zmniejsza rozmiar modelu 3D** nawet o 90 % w porównaniu z nieskompresowaną siatką.

## Co oznacza „zmniejszenie rozmiaru modelu 3D” w kontekście tworzenia 3D?

Zmniejszanie rozmiaru modelu 3D oznacza redukcję ilości danych geometrycznych, które muszą być przesyłane lub przechowywane, bez zauważalnego pogorszenia jakości wizualnej. Draco osiąga to poprzez kodowanie pozycji wierzchołków, normalnych i innych atrybutów w wysoce skompaktowanym formacie binarnym. W połączeniu z Aspose.3D cały proces pozostaje w Javie, więc nie musisz operować natywnymi bibliotekami.

## Dlaczego używać kompresji siatek Google Draco z Aspose.3D?

- **Ogromna redukcja rozmiaru:** Draco może zmniejszyć dane siatki nawet o 90 % w porównaniu z formatami takimi jak OBJ lub STL.  
- **Szybkie dekodowanie w czasie działania:** Silniki takie jak Unity, Unreal i three.js dekodują Draco natywnie, co prowadzi do szybszych czasów ładowania.  
- **Bezproblemowa integracja z Javą:** Aspose.3D abstrahuje natywną bibliotekę Draco, pozwalając pozostać w ekosystemie Javy.  
- **Jedno‑stopniowy eksport Aspose 3D:** To samo API, którego używasz do tworzenia geometrii, obsługuje również eksport, upraszczając pipeline.

## Wymagania wstępne

- **Java Development Kit (JDK)** – wersja 8 lub nowsza.  
- **Aspose.3D for Java** – pobierz najnowsze pliki JAR ze strony oficjalnej [tutaj](https://releases.aspose.com/3d/java/).  
- **Basic familiarity with Google Draco** – będziesz używać wrappera Aspose.3D, więc nie jest wymagana natywna instalacja Draco.

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

### Krok 1: Konfiguracja projektu

Utwórz nowy projekt Java (dowolne IDE działa) i dodaj wszystkie pliki JAR Aspose.3D do ścieżki klas. Umieść pliki źródłowe w pakiecie, np. `com.example.draco`, dla przejrzystości.

### Krok 2: Jak utworzyć siatkę sfery w Javie

```java
// ExStart:Encode3DMeshinGoogleDraco
// The path to the documents directory.
String MyDir = "Your Document Directory";

// Create a sphere
Sphere sphere = new Sphere();
```

> **Wskazówka:** Klasa `Sphere` generuje siatkę triangulowaną o domyślnym promieniu 1.0. Możesz podać własny promień, tessellację lub parametry materiału, jeśli potrzebujesz innego poziomu szczegółowości przed kompresją.

### Krok 3: Jak skompresować siatkę przy użyciu Google Draco

```java
// Encode the sphere to Google Draco raw data using optimal compression level.
DracoSaveOptions opt = new DracoSaveOptions();
opt.setCompressionLevel(DracoCompressionLevel.OPTIMAL);
byte[] b = FileFormat.DRACO.encode(sphere.toMesh(), opt);
```

Ustawienie poziomu kompresji na `OPTIMAL` zapewnia największą redukcję rozmiaru przy zachowaniu wierności wizualnej, bezpośrednio pomagając **zmniejszyć rozmiar modelu 3D**.

### Krok 4: Zapisz skompresowaną siatkę

```java
// Save the raw bytes to file
Files.write(Paths.get(MyDir, "SphereMeshtoDRC_Out.drc"), b);
// ExEnd:Encode3DMeshinGoogleDraco
```

Wynikowy plik `SphereMeshtoDRC_Out.drc` może być przesyłany do klientów, przechowywany w CDN lub ładowany bezpośrednio przez dowolny silnik kompatybilny z Draco.

## Typowe przypadki użycia

| Scenariusz | Dlaczego zmniejszyć rozmiar modelu? | Jak ten samouczek pomaga |
|------------|------------------------------------|--------------------------|
| Konfiguratory produktów w sieci | Szybsze ładowanie stron przy wolnych połączeniach | Pliki `.drc` skompresowane przez Draco ładują się w ciągu kilku sekund |
| Aplikacje mobilne AR/VR | Mniejszy ślad pamięciowy na urządzeniach | Mniejsze siatki utrzymują responsywność aplikacji |
| Sceny renderowane w chmurze | Zmniejszenie kosztów przepustowości | Eksport jednym kliknięciem z Aspose.3D do Draco |

## Typowe problemy i rozwiązania

| Problem | Powód | Rozwiązanie |
|---------|-------|-------------|
| **`NoClassDefFoundError` for Draco classes** | Pliki JAR Aspose.3D nie znajdują się na ścieżce klas | Sprawdź, czy *wszystkie* pliki JAR Aspose.3D są dołączone i czy wersja odpowiada dokumentacji. |
| **Output file is empty** | `MyDir` wskazuje na nieistniejący folder | Utwórz katalog programowo (`Files.createDirectories(Paths.get(MyDir))`) przed zapisem pliku. |
| **Compressed mesh looks distorted** | Użycie niskiego poziomu kompresji lub niewystarczającej tessellacji | Przejdź na `DracoCompressionLevel.OPTIMAL` i zwiększ tessellację sfery (np. `new Sphere(1.0, 64, 64)`). |

## Najczęściej zadawane pytania

**Q: Czy Aspose.3D jest kompatybilny z różnymi formatami plików 3D?**  
A: Tak, Aspose.3D obsługuje OBJ, FBX, STL, GLTF i wiele innych, co czyni go wszechstronnym wyborem dla **pipeline'ów eksportu Aspose 3D**.

**Q: Czy mogę używać Google Draco do kompresji w innych językach programowania?**  
A: Oczywiście. Draco oferuje natywne biblioteki dla C++, Pythona i JavaScript. Ten samouczek koncentruje się na Javie, ale koncepcje mają zastosowanie w różnych językach.

**Q: Gdzie mogę znaleźć dodatkową dokumentację Aspose.3D?**  
A: Odwiedź [dokumentację Aspose.3D Java](https://reference.aspose.com/3d/java/) aby uzyskać pełne odniesienia API i więcej przykładów.

**Q: Jak uzyskać tymczasową licencję na Aspose.3D?**  
A: Zapoznaj się z opcjami tymczasowego licencjonowania [tutaj](https://purchase.aspose.com/temporary-license/).

**Q: Czy istnieje forum społecznościowe wsparcia Aspose.3D?**  
A: Tak, dołącz do dyskusji na [forum Aspose.3D](https://forum.aspose.com/c/3d/18).

## Podsumowanie

W tym przewodniku pokazaliśmy, jak **zmniejszyć rozmiar modelu 3D** poprzez utworzenie siatki sfery w Javie, a następnie skompresowanie jej przy użyciu Google Draco poprzez Aspose.3D. Postępując zgodnie z tymi zwięzłymi krokami, możesz drastycznie zmniejszyć pliki siatek, poprawić czasy ładowania i utrzymać swoje aplikacje 3D oparte na Javie responsywne oraz przyjazne dla przepustowości.

---

**Ostatnia aktualizacja:** 2026-04-29  
**Testowano z:** Aspose.3D for Java 24.12 (latest)  
**Autor:** Aspose

---

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}