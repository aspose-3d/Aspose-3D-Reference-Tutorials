---
date: 2026-09-08
description: Dowiedz się, jak definiować units i eksportować scene do FBX w Java przy
  użyciu Aspose.3D. Ten przewodnik krok po kroku pokazuje, jak ustawić application
  name, measurement units oraz jak pobrać 3D scene information.
keywords:
- how to define units
- export scene to fbx
- how to set application name
- define measurement units
lastmod: 2026-09-08
linktitle: Jak zapisać FBX i pobrać 3D Scene Info w Java
og_description: Dowiedz się, jak definiować units i eksportować scene do FBX w Java
  z Aspose.3D. Przewodnik obejmuje ustawienie application name, measurement units
  oraz pobieranie 3D scene info w kilku krokach.
og_image_alt: Guide showing how to define units and export a 3D scene to FBX using
  Aspose.3D Java
og_title: Jak definiować units i eksportować scene do FBX w Java
schemas:
- author: Aspose
  dateModified: '2026-09-08'
  description: Learn how to define units and export a scene to FBX in Java using Aspose.3D.
    This step‑by‑step guide shows setting the application name, measurement units,
    and retrieving 3D scene information.
  headline: How to define units and export scene to FBX in Java
  type: TechArticle
- description: Learn how to define units and export a scene to FBX in Java using Aspose.3D.
    This step‑by‑step guide shows setting the application name, measurement units,
    and retrieving 3D scene information.
  name: How to define units and export scene to FBX in Java
  steps:
  - name: initialize a 3D scene
    text: The `Scene` class is Aspose.3D's top‑level container that represents an
      entire 3D scene, including geometry, lights, cameras, and metadata. First, create
      an empty `Scene` object. This will be the container for all geometry, lights,
      cameras, and asset metadata.
  - name: define measurement units
    text: The unit system determines the real‑world scale of the scene; Aspose.3D
      lets you specify a unit name and a scale factor relative to meters. In this
      example we use an ancient Egyptian unit called “pole” with a custom scale factor.
      > **Tip:** Adjust `unitScaleFactor` to match the real‑world size of yo
  - name: export scene to FBX
    text: Now that the asset information is attached, we save the scene as an FBX
      file. The `FileFormat.FBX7500ASCII` option produces a human‑readable ASCII FBX,
      which is handy for debugging. > **Remember:** Replace `"Your Document Directory"`
      with an absolute path or a path relative to your project's working
  type: HowTo
- questions:
  - answer: Replace `FileFormat.FBX7500ASCII` with `FileFormat.FBX7500` when calling
      `scene.save(...)`.
    question: How do I change the output format to binary FBX?
  - answer: Yes, use `scene.getUserData().add("Key", "Value")` to embed additional
      key‑value pairs.
    question: Can I add custom user‑defined metadata beyond the built‑in asset fields?
  - answer: It does. Simply change the `FileFormat` enum to `OBJ` or `GLTF2` as needed.
    question: Does Aspose.3D support other export formats like OBJ or GLTF?
  - answer: Aspose.3D for Java supports Java 8 and later.
    question: What version of Java is required?
  - answer: Absolutely. Load the file with `new Scene("input.fbx")`, modify `scene.getAssetInfo()`,
      then save.
    question: Is it possible to load an existing FBX, modify its asset info, and resave?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- export scene to fbx
- Aspose.3D
- Java 3D
- define units
- 3D asset metadata
title: Jak definiować units i eksportować scene do FBX w Java
url: /pl/java/3d-scenes-and-models/get-scene-information/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Jak definiować jednostki i eksportować scenę do FBX w Javie

## Wprowadzenie

Jeśli szukasz jasnego, praktycznego przewodnika, jak **definiować jednostki** i **eksportować scenę do FBX**, jednocześnie wyciągając przydatne metadane z Twoich scen 3D, trafiłeś we właściwe miejsce. W tym tutorialu przeprowadzimy Cię przez każdy krok przy użyciu biblioteki **Aspose.3D for Java**: od tworzenia sceny, **ustawiania nazwy aplikacji**, **definiowania jednostek miary**, po ostateczny **eksport sceny do FBX**. Po zakończeniu będziesz mieć gotowy plik FBX, który zawiera informacje o zasobach potrzebne w dalszych procesach.

## Szybkie odpowiedzi
- **Jaki jest główny cel?** Eksport sceny do FBX, która zawiera niestandardowe informacje o zasobach.  
- **Jakiej biblioteki użyto?** Aspose.3D for Java.  
- **Czy potrzebna jest licencja?** Darmowa wersja próbna działa w trakcie rozwoju; licencja komercyjna jest wymagana w produkcji.  
- **Czy mogę zmienić jednostki miary?** Tak – użyj `setUnitName` i `setUnitScaleFactor`.  
- **Gdzie zapisywany jest wynik?** W ścieżce, którą określisz w `scene.save(...)`.  

## Wymagania wstępne

Zanim zaczniemy, upewnij się, że masz:

- Solidną znajomość podstawowej składni Javy.  
- **Aspose.3D for Java** pobraną i dodaną do swojego projektu (możesz ją pobrać z oficjalnej) [Aspose 3D download page](https://releases.aspose.com/3d/java/).  
- Ulubione IDE Javy (IntelliJ IDEA, Eclipse, NetBeans itp.) poprawnie skonfigurowane.

## Importowanie pakietów

W swoim pliku źródłowym Javy zaimportuj klasy Aspose.3D, które zapewniają obsługę scen i formatów plików.

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
```

> **Wskazówka:** Trzymaj listę importów w minimalnym zakresie, aby uniknąć niepotrzebnych zależności i przyspieszyć kompilację.

## Jaki jest proces zapisywania pliku FBX?

Aby zapisać scenę jako plik FBX, tworzysz `Scene`, ustawiasz dowolne żądane metadane zasobu, definiujesz jednostkę miary, a następnie wywołujesz `scene.save(path, FileFormat.FBX7500ASCII)`. Ta sekwencja zapisuje geometrię, materiały i metadane do pliku ASCII FBX, który można przeglądać lub importować w dalszych narzędziach.

### Krok 1: zainicjalizuj scenę 3D

Klasa `Scene` jest najwyższym kontenerem Aspose.3D, który reprezentuje całą scenę 3D, w tym geometrię, światła, kamery i metadane. Najpierw utwórz pusty obiekt `Scene`. Będzie on kontenerem dla całej geometrii, świateł, kamer i metadanych zasobu.

```java
// ExStart:AddAssetInformationToScene
Scene scene = new Scene();
```

### Jak ustawić nazwę aplikacji w Javie

Obiekt `AssetInfo` przechowuje metadane, takie jak nazwa aplikacji, dostawca i wersja sceny. Dodanie własnych metadanych pomaga narzędziom downstream zidentyfikować źródło pliku. Użyj obiektu `AssetInfo`, aby **ustawić nazwę aplikacji** (i dostawcę) przed zapisaniem pliku.

```java
scene.getAssetInfo().setApplicationName("Egypt");
scene.getAssetInfo().setApplicationVendor("Manualdesk");
```

> **Dlaczego to ważne:** Wiele pipeline'ów filtruje lub taguje zasoby na podstawie aplikacji pochodzenia, co czyni ten krok niezbędnym w dużych projektach.

### Krok 3: zdefiniuj jednostki miary

System jednostek określa rzeczywistą skalę sceny; Aspose.3D pozwala określić nazwę jednostki i współczynnik skali względem metrów. W tym przykładzie używamy starożytnej egipskiej jednostki zwanej „pole” z niestandardowym współczynnikiem skali.

```java
scene.getAssetInfo().setUnitName("pole");
scene.getAssetInfo().setUnitScaleFactor(0.6);
```

> **Wskazówka:** Dostosuj `unitScaleFactor` do rzeczywistego rozmiaru Twoich modeli; 1.0 oznacza odwzorowanie 1‑do‑1 z wybraną jednostką.

### Krok 4: wyeksportuj scenę do FBX

Teraz, gdy informacje o zasobie są dołączone, zapisujemy scenę jako plik FBX. Opcja `FileFormat.FBX7500ASCII` tworzy czytelny dla człowieka plik ASCII FBX, co jest przydatne przy debugowaniu.

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "InformationToScene.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
System.out.println("\nAsset information added successfully to Scene.\nFile saved at " + MyDir);
// ExEnd:AddAssetInformationToScene
```

> **Pamiętaj:** Zastąp `"Your Document Directory"` ścieżką bezwzględną lub ścieżką względną względem katalogu roboczego Twojego projektu.

## Dlaczego eksportować scenę do FBX z Aspose.3D?

Aspose.3D obsługuje **ponad 50 formatów wejściowych i wyjściowych** i może przetwarzać sceny liczące setki stron bez ładowania całego pliku do pamięci, dając pełną kontrolę nad wyeksportowanym plikiem — metadanymi, jednostkami i geometrią — bez potrzeby używania ciężkiego oprogramowania do tworzenia 3D. Dzięki temu automatyczne generowanie zasobów, przetwarzanie wsadowe i konwersje po stronie serwera są szybkie i niezawodne.

## Typowe przypadki użycia

- **Pipeline'y zasobów gier** – osadzaj informacje o twórcy bezpośrednio w plikach FBX w celu śledzenia wersji.  
- **Wizualizacja architektoniczna** – przechowuj jednostki specyficzne dla projektu, aby uniknąć błędów skalowania przy importowaniu do silników renderujących.  
- **Automatyczne raportowanie** – generuj pliki FBX w locie z metadanymi, które narzędzia analityczne downstream mogą odczytać.  
- **Usługi 3D w chmurze** – programowo twórz i eksportuj sceny bez interfejsu graficznego, idealne dla platform SaaS.

## Rozwiązywanie problemów i wskazówki

| Issue | Solution |
|-------|----------|
| **Plik nie znaleziony po zapisaniu** | Sprawdź, czy `MyDir` wskazuje istniejący folder i czy aplikacja ma uprawnienia do zapisu. |
| **Jednostki wyglądają niepoprawnie w zewnętrznym podglądzie** | Sprawdź ponownie `unitScaleFactor`; niektóre przeglądarki oczekują metrów jako jednostki bazowej. |
| **Brak metadanych zasobu** | Upewnij się, że wywołujesz `scene.getAssetInfo()` **przed** zapisaniem; zmiany wprowadzone po `save()` nie zostaną zachowane. |
| **Wąskie gardło wydajności przy dużych scenach** | Użyj `scene.optimize()` przed zapisem, aby zmniejszyć zużycie pamięci. |
| **ASCII FBX jest za duży** | Przejdź na binarny FBX, używając `FileFormat.FBX7500` (zobacz FAQ). |

## Najczęściej zadawane pytania

**P: Jak zmienić format wyjściowy na binarny FBX?**  
A: Zastąp `FileFormat.FBX7500ASCII` przez `FileFormat.FBX7500` przy wywoływaniu `scene.save(...)`.

**P: Czy mogę dodać własne metadane definiowane przez użytkownika poza wbudowanymi polami zasobu?**  
A: Tak, użyj `scene.getUserData().add("Key", "Value")`, aby osadzić dodatkowe pary klucz‑wartość.

**P: Czy Aspose.3D obsługuje inne formaty eksportu, takie jak OBJ lub GLTF?**  
A: Tak. Po prostu zmień enum `FileFormat` na `OBJ` lub `GLTF2` w zależności od potrzeb.

**P: Jaka wersja Javy jest wymagana?**  
A: Aspose.3D for Java obsługuje Javę 8 i nowsze.

**P: Czy można wczytać istniejący FBX, zmodyfikować jego informacje o zasobie i ponownie zapisać?**  
A: Oczywiście. Wczytaj plik za pomocą `new Scene("input.fbx")`, zmodyfikuj `scene.getAssetInfo()`, a następnie zapisz.

---

**Ostatnia aktualizacja:** 2026-09-08  
**Testowano z:** Aspose.3D for Java 24.11  
**Autor:** Aspose

## Powiązane tutoriale

- [Reduce 3D File Size – Compress Scenes with Aspose.3D for Java](/3d/java/3d-scenes-and-models/compress-3d-scenes/)
- [How to set vector3 color java: Change Diffuse Color and Manage 3D Properties in Java Scenes using Aspose.3D](/3d/java/3d-scenes-and-models/managing-3d-properties-scenes/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}