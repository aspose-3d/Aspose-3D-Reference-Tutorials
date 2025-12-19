---
date: 2025-12-19
description: Dowiedz się, jak dostosować ładowanie 3D w Javie przy użyciu Aspose.3D
  LoadOptions. Przewodnik krok po kroku obejmujący pliki 3DS, OBJ, STL, U3D, glTF,
  PLY, X oraz opcjonalnie FBX.
linktitle: Customize 3D Loading Java – How to customize 3d loading java with Aspose.3D
  LoadOptions
second_title: Aspose.3D Java API
title: Dostosuj ładowanie 3D w Javie – Jak dostosować ładowanie 3D w Javie przy użyciu
  Aspose.3D LoadOptions
url: /pl/java/load-and-save/customize-3d-file-loading/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Dostosowywanie ładowania 3D w Javie – Jak dostosować ładowanie 3D w Javie przy użyciu Aspose.3D LoadOptions

## Wprowadzenie

We współczesnych aplikacjach 3D **dostosowywanie ładowania 3D w Javie** jest niezbędne, aby modele wyświetlały się dokładnie tak, jak zamierzono, niezależnie od formatu źródłowego. Niezależnie od tego, czy tworzysz silnik gry, przeglądarkę AR/VR, czy narzędzie do konwersji CAD, możliwość kontrolowania sposobu importu plików 3DS, OBJ, STL, U3D, glTF, PLY, X, a nawet FBX może zaoszczędzić godziny post‑procesingu. Ten samouczek przeprowadzi Cię krok po kroku przez dostosowywanie ładowania plików 3D w Javie przy użyciu elastycznych klas `LoadOptions` Aspose.3D.

## Szybkie odpowiedzi
- **Co oznacza „dostosowywanie ładowania 3d java”?** Oznacza to konfigurowanie `LoadOptions` Aspose.3D w celu kontrolowania zachowania importu, takiego jak odwracanie układu współrzędnych, obsługa materiałów i transformacje animacji.  
- **Jakie formaty mogę dostosować?** 3DS, OBJ, STL, U3D, glTF, PLY, X oraz opcjonalnie FBX.  
- **Czy potrzebna jest licencja, aby to wypróbować?** Wymagana jest tymczasowa licencja dla pełnej funkcjonalności; dostępna jest również darmowa wersja próbna.  
- **Czy potrzebne są dodatkowe dane?** Być może będziesz musiał podać ścieżki wyszukiwania dla zasobów zewnętrznych, takich jak tekstury lub biblioteki materiałów.  
- **Gdzie znaleźć najnowszą wersję Aspose.3D dla Javy?** Na oficjalnej stronie pobierania podanej poniżej.

## Co to jest „dostosowywanie ładowania 3d java”?

Dostosowywanie ładowania 3D w Javie pozwala określić, jak silnik Aspose.3D interpretuje przychodzące pliki. Modyfikując właściwości różnych klas `*LoadOptions`, możesz:

* Odwrócić układ współrzędnych, aby pasował do Twojego potoku renderowania.  
* Włączyć lub wyłączyć ładowanie materiałów w scenariuszach krytycznych pod względem wydajności.  
* Zastosować korekcję gamma, transformacje animacji lub zachować wbudowane ustawienia globalne dla plików FBX.  

## Dlaczego warto używać Aspose.3D LoadOptions?

* **Precyzyjna kontrola** – Dostosuj każdy format niezależnie.  
* **Spójność między formatami** – Stosuj te same zasady układu współrzędnych we wszystkich obsługiwanych typach plików.  
* **Optymalizacja wydajności** – Pomijaj niepotrzebne dane (np. materiały), gdy nie są potrzebne.  

## Wymagania wstępne

Zanim rozpoczniesz, upewnij się, że masz:

- Solidną znajomość podstaw Javy.  
- Zainstalowane JDK 8 lub nowsze.  
- Bibliotekę Aspose.3D dla Javy pobraną z oficjalnej strony — możesz ją uzyskać [tutaj](https://releases.aspose.com/3d/java/).  
- Podstawową znajomość formatów plików 3D, z którymi zamierzasz pracować (3DS, OBJ, STL, U3D, glTF, PLY, X, FBX).

## Importowanie pakietów

W swoim projekcie Java zaimportuj podstawowe klasy Aspose.3D oraz standardowy pakiet I/O:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Dostosowywanie ładowania plików 3D

Poniżej znajdziesz dedykowaną metodę dla każdego obsługiwanego formatu. Każdy fragment kodu pokazuje najczęstsze dostosowania; śmiało modyfikuj właściwości, aby dopasować je do swojego potoku.

### Krok 1: Dostosowywanie ładowania pliku 3DS  

```java
public static void discreet3DSLoadOption() {
    String MyDir = "Your Document Directory";
    Discreet3dsLoadOptions loadOpts = new Discreet3dsLoadOptions();
    loadOpts.setApplyAnimationTransform(true);
    loadOpts.setFlipCoordinateSystem(true);
    loadOpts.setGammaCorrectedColor(true);
    loadOpts.getLookupPaths().add(MyDir);
}
```

*Dlaczego to ważne:* Włączenie `ApplyAnimationTransform` zapewnia, że wszelkie osadzone dane animacji respektują docelowy układ współrzędnych, a `GammaCorrectedColor` naprawia problemy z intensywnością kolorów, które często pojawiają się przy przechodzeniu między różnymi silnikami renderującymi.

### Krok 2: Dostosowywanie ładowania pliku OBJ  

```java
public static void objLoadOption() {
    String MyDir = "Your Document Directory";
    ObjLoadOptions loadObjOpts = new ObjLoadOptions();
    loadObjOpts.setEnableMaterials(true);
    loadObjOpts.setFlipCoordinateSystem(true);
    loadObjOpts.getLookupPaths().add(MyDir);
}
```

*Wskazówka:* Jeśli ładujesz pliki OBJ, które odwołują się do zewnętrznych plików materiałów `.mtl`, pozostaw `EnableMaterials` ustawione na `true` i upewnij się, że ścieżka wyszukiwania wskazuje na folder zawierający te pliki.

### Krok 3: Dostosowywanie ładowania pliku STL  

```java
public static void stlLoadOption() {
    String MyDir = "Your Document Directory";
    StlLoadOptions loadSTLOpts = new StlLoadOptions();
    loadSTLOpts.setFlipCoordinateSystem(true);
    loadSTLOpts.getLookupPaths().add(MyDir);
}
```

*Pro tip:* Pliki STL zawierają wyłącznie geometrię, więc odwrócenie układu współrzędnych jest zazwyczaj jedyną wymaganą modyfikacją.

### Krok 4: Dostosowywanie ładowania pliku U3D  

```java
public static void u3dLoadOption() {
    String MyDir = "Your Document Directory";
    U3dLoadOptions loadU3DOpts = new U3dLoadOptions();
    loadU3DOpts.setFlipCoordinateSystem(true);
    loadU3DOpts.getLookupPaths().add(MyDir);
}
```

### Krok 5: Dostosowywanie ładowania pliku glTF  

```java
public static void gltfLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    GltfLoadOptions loadOpt = new GltfLoadOptions();
    loadOpt.setFlipTexCoordV(true);
    scene.open(MyDir + "Duck.gltf", loadOpt);
}
```

*Dlaczego odwraca się współrzędne V tekstury?* Wiele eksporterów glTF używa innego pochodzenia UV niż tradycyjne potoki DirectX; odwrócenie `TexCoordV` wyrównuje tekstury prawidłowo.

### Krok 6: Dostosowywanie ładowania pliku PLY  

```java
public static void plyLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    PlyLoadOptions loadPLYOpts = new PlyLoadOptions();
    loadPLYOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "vase-v2.ply", loadPLYOpts);
}
```

### Krok 7: Dostosowywanie ładowania pliku X  

```java
public static void xLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    XLoadOptions loadXOpts = new XLoadOptions(FileContentType.ASCII);
    loadXOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "warrior.x", loadXOpts);
}
```

### Krok 8: Dostosowywanie ładowania pliku FBX (Opcjonalnie)  

```java
private static void FBXLoadOptions() throws IOException {
    String dataDir = "Your Document Directory";
    Scene scene = new Scene();
    FbxLoadOptions opt = new FbxLoadOptions();
    opt.setKeepBuiltinGlobalSettings(true);
    scene.open(dataDir + "test.FBX", opt);
    for(Property property:scene.getRootNode().getAssetInfo().getProperties()) {
        System.out.println(property);
    }
}
```

*Kiedy to stosować:* Pliki FBX często zawierają ustawienia globalne (jednostki, oś góry). Zachowanie ich zapewnia, że zaimportowana scena odpowiada zamierzeniom autora.

## Typowe problemy i rozwiązania

| Problem | Prawdopodobna przyczyna | Rozwiązanie |
|---------|--------------------------|-------------|
| Tekstury nie wyświetlają się | Ścieżka wyszukiwania nie ustawiona lub nieprawidłowa wielkość liter | Dodaj właściwy katalog do `loadOpts.getLookupPaths()` i sprawdź nazwy plików |
| Model jest odwrócony do góry nogami | `FlipCoordinateSystem` nie włączony dla danego formatu | Ustaw `setFlipCoordinateSystem(true)` dla odpowiedniego `*LoadOptions` |
| Kolory wyglądają wyblakłe | Korekcja gamma wyłączona dla 3DS | Wywołaj `setGammaCorrectedColor(true)` na `Discreet3dsLoadOptions` |
| Animacja FBX wygląda niepoprawnie | Nadpisane ustawienia globalne | Użyj `setKeepBuiltinGlobalSettings(true)` |

## Najczęściej zadawane pytania

### P1: Gdzie mogę znaleźć dokumentację Aspose.3D dla Javy?  
O1: Dokumentacja jest dostępna [tutaj](https://reference.aspose.com/3d/java/).

### P2: Jak mogę pobrać Aspose.3D dla Javy?  
O2: Możesz pobrać go [tutaj](https://releases.aspose.com/3d/java/).

### P3: Czy dostępna jest darmowa wersja próbna?  
O3: Tak, darmową wersję próbną znajdziesz [tutaj](https://releases.aspose.com/).

### P4: Gdzie mogę uzyskać wsparcie dla Aspose.3D dla Javy?  
O4: Odwiedź forum wsparcia [tutaj](https://forum.aspose.com/c/3d/18).

### P5: Czy potrzebna jest tymczasowa licencja do testów?  
O5: Tak, tymczasową licencję można uzyskać [tutaj](https://purchase.aspose.com/temporary-license/).

### P6: Czy mogę ładować wiele formatów w jednej scenie?  
O6: Oczywiście. Utwórz osobne `LoadOptions` dla każdego formatu i wywołaj `scene.open()` dla każdego pliku; scena połączy geometrię.

### P7: Jak poprawić wydajność ładowania dużych plików?  
O7: Wyłącz niepotrzebne funkcje (np. ładowanie materiałów dla STL) i używaj `LookupPaths`, aby uniknąć powtarzających się operacji I/O.

### P8: Czy można programowo zmienić układ współrzędnych po załadowaniu?  
O8: Tak, możesz wywołać `scene.getRootNode().rotate()` lub `scene.getRootNode().scale()` po otwarciu pliku.

---

**Ostatnia aktualizacja:** 2025-12-19  
**Testowano z:** Aspose.3D for Java 24.11 (najnowsza w momencie pisania)  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}