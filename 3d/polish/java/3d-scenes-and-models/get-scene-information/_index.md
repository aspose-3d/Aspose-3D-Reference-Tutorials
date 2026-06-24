---
date: 2026-05-04
description: Dowiedz się, jak wyeksportować scenę do formatu FBX i ustawić nazwę aplikacji
  java przy użyciu Aspose.3D for Java. Ten przewodnik krok po kroku pokazuje również,
  jak zdefiniować jednostki miary i pobrać informacje o scenie 3D.
keywords:
- export scene to fbx
- set application name java
- aspose 3d java
linktitle: Jak zapisać FBX i pobrać informacje o scenie 3D w Javie
second_title: Aspose.3D Java API
title: Jak wyeksportować scenę do formatu FBX i pobrać informacje o scenie 3D w Javie
url: /pl/java/3d-scenes-and-models/get-scene-information/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Jak wyeksportować scenę do FBX i pobrać informacje o scenie 3D w Javie

## Wprowadzenie

Jeśli szukasz jasnego, praktycznego przewodnika dotyczącego **jak wyeksportować scenę do FBX**, jednocześnie wyciągając przydatne metadane z Twoich scen 3D, trafiłeś we właściwe miejsce. W tym samouczku przeprowadzimy Cię przez każdy krok przy użyciu biblioteki **Aspose.3D Java**: od utworzenia sceny, **ustawienia nazwy aplikacji**, **definiowania jednostek miary**, po ostateczne **wyeksportowanie sceny do FBX**. Po zakończeniu będziesz mieć gotowy plik FBX, który zawiera informacje o zasobach potrzebne w dalszych etapach przetwarzania.

## Szybkie odpowiedzi

- **Jaki jest główny cel?** Wyeksportować scenę do FBX, która zawiera niestandardowe informacje o zasobach.  
- **Jakiej biblioteki użyto?** Aspose.3D for Java.  
- **Czy potrzebna jest licencja?** Darmowa wersja próbna działa w trakcie rozwoju; licencja komercyjna jest wymagana w produkcji.  
- **Czy mogę zmienić jednostki miary?** Tak – użyj `setUnitName` i `setUnitScaleFactor`.  
- **Gdzie zapisywany jest wynik?** W ścieżce podanej w `scene.save(...)`.  

## Wymagania wstępne

Zanim zaczniemy, upewnij się, że masz:

- Solidną znajomość podstawowej składni Java.  
- **Aspose.3D for Java** pobrany i dodany do projektu (możesz go pobrać z oficjalnej) [Aspose 3D download page](https://releases.aspose.com/3d/java/).  
- Ulubione środowisko IDE Java (IntelliJ IDEA, Eclipse, NetBeans itp.) prawidłowo skonfigurowane.

## Importowanie pakietów

W swoim pliku źródłowym Java zaimportuj klasy Aspose.3D, które zapewniają obsługę scen i formatów plików.

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
```

> **Pro tip:** Trzymaj listę importów minimalną, aby uniknąć niepotrzebnych zależności i przyspieszyć kompilację.

## Jaki jest proces zapisywania pliku FBX?

Poniżej znajduje się zwięzły, krok po kroku przewodnik, który pokazuje **jak dodać informacje o zasobach** do sceny, a następnie **wyeksportować scenę do FBX**.

### Krok 1: Zainicjalizuj scenę 3D

Najpierw utwórz pusty obiekt `Scene`. Będzie on kontenerem dla całej geometrii, świateł, kamer i metadanych zasobów.

```java
// ExStart:AddAssetInformationToScene
Scene scene = new Scene();
```

### Jak ustawić nazwę aplikacji w Javie

Dodanie niestandardowych metadanych pomaga narzędziom downstream zidentyfikować źródło pliku. Użyj obiektu `AssetInfo`, aby **ustawić nazwę aplikacji** (i dostawcę) przed zapisaniem pliku.

```java
scene.getAssetInfo().setApplicationName("Egypt");
scene.getAssetInfo().setApplicationVendor("Manualdesk");
```

> **Dlaczego to ważne:** Wiele pipeline'ów filtruje lub oznacza zasoby na podstawie aplikacji źródłowej, co czyni ten krok niezbędnym w dużych projektach.

### Krok 3: Zdefiniuj jednostki miary

Aspose.3D pozwala określić system jednostek używany w Twojej scenie. W tym przykładzie używamy starożytnej egipskiej jednostki zwanej „pole” z niestandardowym współczynnikiem skali.

```java
scene.getAssetInfo().setUnitName("pole");
scene.getAssetInfo().setUnitScaleFactor(0.6);
```

> **Wskazówka:** Dostosuj `unitScaleFactor`, aby odpowiadał rzeczywistym wymiarom Twoich modeli; 1,0 oznacza odwzorowanie 1‑do‑1 z wybraną jednostką.

### Krok 4: Wyeksportuj scenę do FBX

Teraz, gdy informacje o zasobach są dołączone, zapisujemy scenę jako plik FBX. Opcja `FileFormat.FBX7500ASCII` generuje czytelny dla człowieka plik ASCII FBX, co jest przydatne przy debugowaniu.

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "InformationToScene.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
// ExEnd:AddAssetInformationToScene
```

> **Pamiętaj:** Zastąp `"Your Document Directory"` ścieżką bezwzględną lub ścieżką względną względem katalogu roboczego Twojego projektu.

### Krok 5: Wyświetl komunikat o sukcesie

Proste wyjście w konsoli potwierdza, że operacja zakończyła się sukcesem i informuje, gdzie plik został zapisany.

```java
System.out.println("\nAsset information added successfully to Scene.\nFile saved at " + MyDir);
```

## Dlaczego wyeksportować scenę do FBX przy użyciu Aspose.3D?

Eksport do FBX jest powszechnym wymogiem, ponieważ FBX jest szeroko wspierany przez silniki gier, narzędzia DCC oraz pipeline'y AR/VR. Aspose.3D daje pełną kontrolę nad wyeksportowanym plikiem — metadanymi, jednostkami i geometrią — bez potrzeby używania ciężkiego oprogramowania do tworzenia 3D. Dzięki temu automatyczne generowanie zasobów, przetwarzanie wsadowe i konwersje po stronie serwera są szybkie i niezawodne.

## Typowe przypadki użycia

- **Pipeline'y zasobów gier** – osadź informacje o twórcy bezpośrednio w plikach FBX w celu śledzenia wersji.  
- **Wizualizacja architektoniczna** – przechowuj jednostki specyficzne dla projektu, aby uniknąć błędów skalowania przy importowaniu do silników renderujących.  
- **Automatyczne raportowanie** – generuj pliki FBX w locie z metadanymi, które narzędzia analityczne downstream mogą odczytać.  
- **Usługi 3D w chmurze** – programowo twórz i eksportuj sceny bez interfejsu graficznego, idealne dla platform SaaS.

## Rozwiązywanie problemów i wskazówki

| Problem | Rozwiązanie |
|-------|----------|
| **Plik nie znaleziony po zapisie** | Zweryfikuj, że `MyDir` wskazuje istniejący folder i że aplikacja ma uprawnienia do zapisu. |
| **Jednostki wyglądają niepoprawnie w zewnętrznym podglądzie** | Sprawdź ponownie `unitScaleFactor`; niektóre podglądarki oczekują metrów jako jednostki bazowej. |
| **Brak metadanych zasobu** | Upewnij się, że wywołujesz `scene.getAssetInfo()` **przed** zapisem; zmiany dokonane po `save()` nie zostaną zachowane. |
| **Wąskie gardło wydajności przy dużych scenach** | Użyj `scene.optimize()` przed zapisem, aby zmniejszyć zużycie pamięci. |
| **ASCII FBX jest zbyt duży** | Przełącz się na binarny FBX używając `FileFormat.FBX7500` (zobacz FAQ). |

## Najczęściej zadawane pytania

**P:** Jak zmienić format wyjściowy na binarny FBX?  
O: Zastąp `FileFormat.FBX7500ASCII` przez `FileFormat.FBX7500` przy wywoływaniu `scene.save(...)`.

**P:** Czy mogę dodać niestandardowe metadane definiowane przez użytkownika poza wbudowanymi polami zasobu?  
O: Tak, użyj `scene.getUserData().add("Key", "Value")`, aby osadzić dodatkowe pary klucz‑wartość.

**P:** Czy Aspose.3D obsługuje inne formaty eksportu, takie jak OBJ lub GLTF?  
O: Tak. Po prostu zmień enum `FileFormat` na `OBJ` lub `GLTF2` w zależności od potrzeb.

**P:** Jakiej wersji Javy wymaga?  
O: Aspose.3D for Java obsługuje Javę 8 i nowsze.

**P:** Czy można wczytać istniejący plik FBX, zmodyfikować jego informacje o zasobach i ponownie zapisać?  
O: Oczywiście. Wczytaj plik za pomocą `new Scene("input.fbx")`, zmodyfikuj `scene.getAssetInfo()`, a następnie zapisz.

## Podsumowanie

Masz teraz kompletny, gotowy do produkcji przepływ pracy dla **eksportowania sceny do FBX**, jednocześnie osadzając cenne informacje o zasobach, takie jak nazwa aplikacji, dostawca i niestandardowe jednostki miary. To podejście usprawnia zarządzanie zasobami, redukuje ręczną ewidencję i zapewnia, że narzędzia downstream otrzymują cały potrzebny kontekst. Śmiało eksploruj inne formaty eksportu, dodawaj niestandardowe dane użytkownika lub integruj ten kod w większych pipeline'ach automatyzacji.

---

**Ostatnia aktualizacja:** 2026-05-04  
**Testowano z:** Aspose.3D for Java 24.11  
**Autor:** Aspose

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}