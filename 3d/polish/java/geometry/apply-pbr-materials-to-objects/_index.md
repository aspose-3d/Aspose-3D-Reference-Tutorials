---
date: 2026-05-14
description: Dowiedz się, jak wyeksportować STL w Javie, tworząc scenę 3D, stosując
  realistyczne materiały PBR przy użyciu Aspose.3D oraz zapisując model do renderowania.
keywords:
- how to export stl
- Aspose 3D PBR materials
- Java 3D scene creation
linktitle: Jak wyeksportować STL w Javie – Tworzenie sceny 3D przy użyciu Aspose.3D
schemas:
- author: Aspose
  dateModified: '2026-05-14'
  description: Learn how to export STL in Java by creating a 3D scene, applying realistic
    PBR materials with Aspose.3D, and saving the model for rendering.
  headline: How to Export STL in Java – Create 3D Scene with Aspose.3D
  type: TechArticle
- description: Learn how to export STL in Java by creating a 3D scene, applying realistic
    PBR materials with Aspose.3D, and saving the model for rendering.
  name: How to Export STL in Java – Create 3D Scene with Aspose.3D
  steps:
  - name: '**Java Development Environment** – JDK 8 or newer installed.'
    text: '**Java Development Environment** – JDK 8 or newer installed.'
  - name: '**Aspose.3D Library** – Download the latest JAR from the [download link](https://releases.aspose.com/3d/java/).'
    text: '**Aspose.3D Library** – Download the latest JAR from the [download link](https://releases.aspose.com/3d/java/).'
  - name: '**Documentation** – Familiarise yourself with the API via the official
      [documentation](https://reference.aspose.com/3d/java/).'
    text: '**Documentation** – Familiarise yourself with the API via the official
      [documentation](https://reference.aspose.com/3d/java/).'
  - name: '**Temporary License (Optional)** – If you don’t have a permanent license,
      obtain a [temporary license](https://purchase.aspose.com/temporary-license/)
      for testing.'
    text: '**Temporary License (Optional)** – If you don’t have a permanent license,
      obtain a [temporary license](https://purchase.aspose.com/temporary-license/)
      for testing.'
  type: HowTo
- questions:
  - answer: It’s the process of building a `Scene` object that holds geometry, lights,
      and cameras in a Java application.
    question: What does “create 3d scene java” mean?
  - answer: Aspose.3D provides a ready‑made `PbrMaterial` class.
    question: Which library handles PBR materials?
  - answer: Yes – the `Scene.save` method supports STL (ASCII and binary).
    question: Can I export the result as STL?
  - answer: A permanent Aspose.3D license is required for commercial use; a temporary
      license works for testing.
    question: Do I need a license for production?
  - answer: Any Java 8+ runtime is supported.
    question: What Java version is required?
  type: FAQPage
second_title: Aspose.3D Java API
title: Jak wyeksportować STL w Javie – Tworzenie sceny 3D przy użyciu Aspose.3D
url: /pl/java/geometry/apply-pbr-materials-to-objects/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Jak wyeksportować STL w Javie – Tworzenie sceny 3D za pomocą Aspose.3D

## Wprowadzenie

W tym praktycznym samouczku nauczysz się **jak wyeksportować STL** z aplikacji Java, budując pełną scenę 3D, stosując materiały Physically Based Rendering (PBR) i zapisując wynik przy użyciu Aspose.3D. Niezależnie od tego, czy celujesz w druk 3‑D, pipeline silnika gry, czy wizualizację produktu, poniższe kroki zapewniają powtarzalny, wersjonowany przepływ pracy, który działa na dowolnym środowisku Java 8+.

## Szybkie odpowiedzi
- **Co oznacza „create 3d scene java”?** To proces budowania obiektu `Scene`, który przechowuje geometrię, światła i kamery w aplikacji Java.  
- **Która biblioteka obsługuje materiały PBR?** Aspose.3D udostępnia gotową klasę `PbrMaterial`.  
- **Czy mogę wyeksportować wynik jako STL?** Tak – metoda `Scene.save` obsługuje STL (ASCII i binarny).  
- **Czy potrzebna jest licencja do produkcji?** Stała licencja Aspose.3D jest wymagana do użytku komercyjnego; licencja tymczasowa działa w testach.  
- **Jaka wersja Javy jest wymagana?** Obsługiwane jest dowolne środowisko Java 8+.

## Jak stworzyć scenę 3D w Javie przy użyciu Aspose.3D

`Scene` jest główną klasą kontenera reprezentującą dokument 3D. Ładuj, konfiguruj i zapisuj scenę w kilku linijkach kodu. Najpierw tworzysz instancję `Scene`, następnie dołączasz geometrię i `PbrMaterial`, a na końcu wywołujesz `Scene.save` w formacie STL. Ten przepływ end‑to‑end pozwala automatyzować generowanie zasobów bez konieczności otwierania edytora 3D.

## Czym jest scena 3D w Javie?

*Scena* jest kontenerem, który przechowuje wszystkie obiekty (węzły), ich geometrię, materiały, światła i kamery. Można ją traktować jako wirtualną scenę, na której umieszczasz modele 3D. Klasa `Scene` w Aspose.3D zapewnia czysty, obiektowo‑zorientowany sposób budowania tej sceny programowo.

## Dlaczego używać materiałów PBR do renderowania obiektów 3D w Javie?

PBR (Physically Based Rendering) naśladuje interakcję światła ze światem rzeczywistym, wykorzystując parametry metaliczności i szorstkości. Efektem jest materiał, który wygląda spójnie przy dowolnym oświetleniu, co jest kluczowe dla realistycznej wizualizacji produktów, AR/VR oraz nowoczesnych silników gier. Kontrolując mapy metaliczności, szorstkości, albedo i normalne, możesz uzyskać szeroką gamę wykończeń powierzchni — od wypolerowanego metalu po matowy plastik — bez ręcznego dostrajania shaderów.

## Wymagania wstępne

1. **Środowisko programistyczne Java** – zainstalowany JDK 8 lub nowszy.  
2. **Biblioteka Aspose.3D** – Pobierz najnowszy plik JAR z [download link](https://releases.aspose.com/3d/java/).  
3. **Dokumentacja** – Zapoznaj się z API poprzez oficjalną [documentation](https://reference.aspose.com/3d/java/).  
4. **Licencja tymczasowa (Opcjonalnie)** – Jeśli nie masz stałej licencji, uzyskaj [temporary license](https://purchase.aspose.com/temporary-license/) do testów.

## Typowe przypadki użycia

| Przypadek użycia | Jak samouczek pomaga |
|------------------|----------------------|
| **3‑D printing** | Eksport do STL pozwala wysłać model bezpośrednio do slicera. |
| **Game asset pipeline** | Parametry materiałów PBR odpowiadają wymaganiom nowoczesnych silników gier. |
| **Product configurator** | Automatyzuj warianty kolorów/wykończeń, dostosowując wartości metaliczności i szorstkości. |

## Importowanie pakietów

Przestrzeń nazw `Aspose.3D` musi zostać zaimportowana, aby kompilator mógł rozwiązać klasy użyte w samouczku.

```java
import com.aspose.threed.*;
```

## Krok 1: Inicjalizacja sceny

`Scene` jest głównym kontenerem dla całej zawartości 3D. Utworzenie nowej instancji daje czyste płótno, do którego możesz dodać geometrię, światła i kamery.

```java
// ExStart:InitializeScene
String MyDir = "Your Document Directory";
Scene scene = new Scene();
// ExEnd:InitializeScene
```

> **Wskazówka:** Upewnij się, że `MyDir` wskazuje na folder z prawem zapisu; w przeciwnym razie wywołanie `save` zakończy się niepowodzeniem.

## Krok 2: Inicjalizacja materiału PBR

`PbrMaterial` definiuje właściwości renderowania fizycznie opartego, takie jak metaliczność i szorstkość. `PbrMaterial` określa metaliczność, szorstkość i inne właściwości powierzchni. Ustawienie wysokiego współczynnika metaliczności (≈ 0.9) i szorstkości 0.9 daje realistyczny wygląd szczotkowanego metalu.

```java
// ExStart:InitializePBRMaterial
PbrMaterial mat = new PbrMaterial();
mat.setMetallicFactor(0.9);
mat.setRoughnessFactor(0.9);
// ExEnd:InitializePBRMaterial
```

> **Dlaczego te wartości?** Wysoki współczynnik metaliczności sprawia, że powierzchnia zachowuje się jak metal, natomiast wysoka szorstkość dodaje subtelną dyfuzję, zapobiegając idealnemu lustrzanemu wykończeniu.

## Krok 3: Utworzenie obiektu 3D i zastosowanie materiału

Tutaj generujemy prostą geometrię sześcianu, dołączamy ją do węzła głównego sceny i przypisujemy `PbrMaterial`, który właśnie stworzyliśmy.

```java
// ExStart:Create3DObject
Node boxNode = scene.getRootNode().createChildNode("box", new Box());
boxNode.setMaterial(mat);
// ExEnd:Create3DObject
```

> **Częsty błąd:** Zapomnienie o ustawieniu materiału na węźle spowoduje, że obiekt będzie miał domyślny (nie‑PBR) wygląd.

## Krok 4: Zapis sceny 3D (eksport STL)

`Scene.save` zapisuje scenę do pliku w określonym formacie. Wyeksportuj całą scenę — w tym sześcian z ulepszonym PBR — do pliku STL. STL jest szeroko wspieranym formatem do druku 3‑D i szybkich kontroli wizualnych.

```java
// ExStart:Save3DScene
scene.save(MyDir + "PBR_Material_Box_Out.stl", FileFormat.STLASCII);
// ExEnd:Save3DScene
```

`FileFormat.STLBINARY` określa wyjście binarne STL, które jest mniejsze niż ASCII. Możesz także wybrać `FileFormat.STLASCII`, jeśli preferujesz plik czytelny dla człowieka.

## Dlaczego to ma znaczenie

Spójne parametry materiałów zapewniają, że każdy wygenerowany model wygląda tak samo w różnych przeglądarkach i warunkach oświetleniowych. Automatyzacja pozwala produkować duże partie wariantów przy minimalnym wysiłku, a wieloplatformowy eksport STL gwarantuje kompatybilność z narzędziami od Blender po slicery drukarek 3‑D. Razem te korzyści przyspieszają pipeline’y rozwojowe i redukują błędy manualne.

## Wskazówki rozwiązywania problemów

| Problem | Prawdopodobna przyczyna | Rozwiązanie |
|---------|--------------------------|-------------|
| **Plik nie zapisany** | `MyDir` wskazuje na nieistniejący folder lub brakuje uprawnień do zapisu | Sprawdź, czy katalog istnieje i czy proces Java ma dostęp do zapisu |
| **Materiał wygląda płasko** | Wartości Metallic/Roughness ustawione na 0 | Zwiększ `setMetallicFactor` i/lub `setRoughnessFactor` |
| **Plik STL nie może zostać otwarty** | Nieprawidłowa flaga formatu pliku (ASCII vs Binary) dla przeglądarki | Użyj odpowiedniego enumu `FileFormat` dla docelowego podglądu |

## Najczęściej zadawane pytania

**Q:** Czy mogę używać Aspose.3D w projektach komercyjnych?  
**A:** Tak. Kup licencję komercyjną na [purchase page](https://purchase.aspose.com/buy).

**Q:** Jak uzyskać wsparcie dla Aspose.3D?  
**A:** Dołącz do społeczności na [Aspose.3D forum](https://forum.aspose.com/c/3d/18) aby uzyskać darmową pomoc, lub otwórz zgłoszenie wsparcia z ważną licencją.

**Q:** Czy dostępna jest darmowa wersja próbna?  
**A:** Oczywiście. Pobierz wersję próbną z [free trial page](https://releases.aspose.com/).

**Q:** Gdzie mogę znaleźć szczegółową dokumentację Aspose.3D?  
**A:** Wszystkie odniesienia API są dostępne w oficjalnej [documentation](https://reference.aspose.com/3d/java/).

**Q:** Jak uzyskać tymczasową licencję do testów?  
**A:** Poproś o nią poprzez [temporary license link](https://purchase.aspose.com/temporary-license/).

**Ostatnia aktualizacja:** 2026-05-14  
**Testowano z:** Aspose.3D 24.12 (latest)  
**Autor:** Aspose  

{{< blocks/products/products-backtop-button >}}

## Powiązane samouczki

- [Utwórz scenę 3D w Javie z Aspose 3D Java](/3d/java/3d-scenes-and-models/)
- [Jak wyeksportować scenę do FBX i pobrać informacje o scenie 3D w Javie](/3d/java/3d-scenes-and-models/get-scene-information/)
- [Jak wyeksportować OBJ – modyfikacja orientacji płaszczyzny dla precyzyjnego pozycjonowania sceny 3D w Javie](/3d/java/3d-scenes-and-models/change-plane-orientation/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}