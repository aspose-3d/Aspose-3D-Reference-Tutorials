---
date: 2025-12-06
description: „Dowiedz się, jak zapisywać pliki FBX i pobierać informacje o scenie
  przy użyciu Aspose.3D dla Javy. Ten przewodnik krok po kroku obejmuje ustawianie
  nazwy aplikacji, definiowanie jednostek miary oraz eksportowanie sceny do formatu
  FBX.”
language: pl
linktitle: How to Save FBX and Retrieve 3D Scene Info in Java
second_title: Aspose.3D Java API
title: Jak zapisać FBX i odczytać informacje o scenie 3D w Javie
url: /java/3d-scenes-and-models/get-scene-information/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Jak zapisać plik FBX i pobrać informacje o scenie 3D w Javie

## Introduction

Jeśli szukasz jasnego, praktycznego przewodnika, **jak zapisać fbx** pliki jednocześnie wyodrębniając przydatne metadane ze swoich scen 3D, trafiłeś we właściwe miejsce. W tym tutorialu przejdziemy przez każdy krok używając biblioteki **Aspose.3D Java**: od tworzenia sceny, **ustawiania nazwy aplikacji**, **definiowania jednostek miary**, po ostateczne **eksportowanie sceny do FBX**. Po zakończeniu będziesz mieć gotowy‑do‑użycia plik FBX, który niesie informacje o zasobach potrzebne w dalszych pipeline'ach.

## Quick Answers
- **Jaki jest główny cel?** Zapisanie pliku FBX, który zawiera niestandardowe informacje o zasobach.  
- **Jakiej biblioteki użyto?** Aspose.3D for Java.  
- **Czy potrzebna jest licencja?** Darmowa wersja próbna działa w środowisku deweloperskim; licencja komercyjna jest wymagana w produkcji.  
- **Czy mogę zmienić jednostki miary?** Tak – użyj `setUnitName` i `setUnitScaleFactor`.  
- **Gdzie zapisywany jest wynik?** W ścieżce, którą podasz w `scene.save(...)`.

## Prerequisites

Zanim zaczniemy, upewnij się, że masz:

- Solidną znajomość podstawowej składni Javy.  
- **Aspose.3D for Java** pobraną i dodaną do projektu (możesz ją pobrać z oficjalnej) [strony pobierania Aspose 3D](https://releases.aspose.com/3d/java/).  
- Twojego ulubionego IDE Javy (IntelliJ IDEA, Eclipse, NetBeans, itp.) poprawnie skonfigurowanego.

## Import Packages

W swoim pliku źródłowym Java zaimportuj klasy Aspose.3D, które zapewniają obsługę scen i formatów plików.

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
```

> **Wskazówka:** Trzymaj listę importów minimalną, aby uniknąć niepotrzebnych zależności i przyspieszyć kompilację.

## What is the process for saving an FBX file?

Poniżej znajduje się zwięzły, krok po kroku przewodnik, który pokazuje **jak dodać informacje o zasobach** do sceny i następnie **wyeksportować scenę do FBX**.

### Step 1: Initialize a 3D Scene

Najpierw utwórz pusty obiekt `Scene`. Będzie on kontenerem dla całej geometrii, świateł, kamer i metadanych zasobów.

```java
// ExStart:AddAssetInformationToScene
Scene scene = new Scene();
```

### Step 2: Set Application and Vendor Information

Dodanie niestandardowych metadanych pomaga narzędziom downstream zidentyfikować źródło pliku. Tutaj **ustawiamy nazwę aplikacji** i dostawcę przy użyciu obiektu `AssetInfo`.

```java
scene.getAssetInfo().setApplicationName("Egypt");
scene.getAssetInfo().setApplicationVendor("Manualdesk");
```

> **Dlaczego to ważne:** Wiele pipeline'ów filtruje lub taguje zasoby na podstawie aplikacji pochodzenia, co czyni ten krok niezbędnym w dużych projektach.

### Step 3: Define Measurement Units

Aspose.3D pozwala określić system jednostek używany w scenie. W tym przykładzie używamy starożytnej egipskiej jednostki zwanej „pole” z niestandardowym współczynnikiem skali.

```java
scene.getAssetInfo().setUnitName("pole");
scene.getAssetInfo().setUnitScaleFactor(0.6);
```

> **Wskazówka:** Dostosuj `unitScaleFactor`, aby odpowiadał rzeczywistym wymiarom Twoich modeli; 1.0 oznacza odwzorowanie 1‑do‑1 z wybraną jednostką.

### Step 4: Export Scene to FBX

Teraz, gdy informacje o zasobach są dołączone, zapisujemy scenę jako plik FBX. Opcja `FileFormat.FBX7500ASCII` generuje czytelny dla człowieka plik ASCII FBX, co jest przydatne przy debugowaniu.

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "InformationToScene.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
// ExEnd:AddAssetInformationToScene
```

> **Pamiętaj:** Zastąp `"Your Document Directory"` ścieżką bezwzględną lub ścieżką względną względem katalogu roboczego projektu.

### Step 5: Print Success Message

Prosty komunikat w konsoli potwierdza, że operacja zakończyła się sukcesem i informuje, gdzie zapisano plik.

```java
System.out.println("\nAsset information added successfully to Scene.\nFile saved at " + MyDir);
```

## Common Use Cases

- **Pipeline'y zasobów gier** – osadzają informacje o twórcy bezpośrednio w plikach FBX w celu śledzenia wersji.  
- **Wizualizacja architektoniczna** – przechowują jednostki specyficzne dla projektu, aby uniknąć błędów skalowania przy importowaniu do silników renderujących.  
- **Automatyczne raportowanie** – generują pliki FBX w locie z metadanymi, które narzędzia analityczne downstream mogą odczytać.

## Troubleshooting & Tips

| Problem | Rozwiązanie |
|-------|----------|
| **Plik nie znaleziony po zapisie** | Sprawdź, czy `MyDir` wskazuje istniejący folder i czy aplikacja ma uprawnienia do zapisu. |
| **Jednostki wyglądają niepoprawnie w zewnętrznym podglądzie** | Sprawdź ponownie `unitScaleFactor`; niektóre przeglądarki oczekują metrów jako jednostki bazowej. |
| **Brak metadanych zasobu** | Upewnij się, że wywołujesz `scene.getAssetInfo()` **przed** zapisem; zmiany wprowadzone po `save()` nie zostaną zachowane. |

## FAQ's

### Q1: Is Aspose.3D compatible with all Java IDEs?

A1: Tak, Aspose.3D jest zaprojektowane tak, aby działało płynnie ze wszystkimi głównymi IDE Javy.

### Q2: Can I use Aspose.3D for commercial projects?

A2: Absolutnie. Aspose.3D oferuje licencje komercyjne dla deweloperów, zapewniając zgodność z wymaganiami licencyjnymi.

### Q3: Where can I find additional support for Aspose.3D?

A3: W razie pytań lub potrzebnej pomocy, odwiedź [forum Aspose.3D](https://forum.aspose.com/c/3d/18).

### Q4: Is there a free trial available for Aspose.3D?

A4: Tak, możesz przetestować funkcje korzystając z darmowej wersji próbnej dostępnej [tutaj](https://releases.aspose.com/).

### Q5: How can I obtain a temporary license for Aspose.3D?

A5: Uzyskaj tymczasową licencję do celów testowych [tutaj](https://purchase.aspose.com/temporary-license/).

## Frequently Asked Questions

**P:** Jak zmienić format wyjściowy na binarny FBX?  
**O:** Zastąp `FileFormat.FBX7500ASCII` przez `FileFormat.FBX7500` przy wywołaniu `scene.save(...)`.

**P:** Czy mogę dodać niestandardowe metadane definiowane przez użytkownika poza wbudowanymi polami zasobu?  
**O:** Tak, użyj `scene.getUserData().add("Key", "Value")`, aby osadzić dodatkowe pary klucz‑wartość.

**P:** Czy Aspose.3D obsługuje inne formaty eksportu, takie jak OBJ lub GLTF?  
**O:** Tak. Po prostu zmień enum `FileFormat` na `OBJ` lub `GLTF2` w zależności od potrzeb.

**P:** Jaka wersja Javy jest wymagana?  
**O:** Aspose.3D for Java obsługuje Javę 8 i nowsze.

**P:** Czy można wczytać istniejący plik FBX, zmodyfikować jego informacje o zasobach i ponownie zapisać?  
**O:** Absolutnie. Wczytaj plik przy pomocy `new Scene("input.fbx")`, zmodyfikuj `scene.getAssetInfo()`, a następnie zapisz.

---

**Ostatnia aktualizacja:** 2025-12-06  
**Testowano z:** Aspose.3D for Java 24.11  
**Autor:** Aspose

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
