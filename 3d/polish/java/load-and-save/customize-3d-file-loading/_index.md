---
date: 2026-02-25
description: Dowiedz się, jak odwrócić układ współrzędnych i dostosować import 3D
  przy użyciu Aspose.3D LoadOptions w Javie. Przewodnik krok po kroku dla formatów
  3DS, OBJ, STL, U3D, glTF, PLY, X oraz opcjonalnie FBX.
linktitle: Customize 3D File Loading in Java with Aspose.3D LoadOptions
second_title: Aspose.3D Java API
title: Odwróć układ współrzędnych – Dostosuj ładowanie plików 3D w Javie z Aspose.3D
url: /pl/java/load-and-save/customize-3d-file-loading/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Odwrócenie systemu współrzędnych – Dostosowanie ładowania plików 3D w Javie przy użyciu Aspose.3D

W ciągle rozwijającym się świecie projektowania i tworzenia 3D, **odwracanie systemu współrzędnych** podczas importu modeli jest powszechnym wymogiem. Niezależnie od tego, czy konwertujesz zasoby z systemu praworęcznego na leworęczny, czy musisz dopasować modele do konwencji osi w swoim silniku, Aspose.3D dla Javy zapewnia precyzyjną kontrolę. Ten samouczek pokaże Ci, jak **dostosować import 3D** przy użyciu `LoadOptions` z Aspose.3D, obejmując najpopularniejsze formaty, takie jak 3DS, OBJ, STL, U3D, glTF, PLY, X oraz opcjonalny FBX.

## Szybkie odpowiedzi
- **Co robi opcja „flip coordinate system”?** Zamienia osie X/Y/Z, aby dopasować je do docelowej konwencji współrzędnych.  
- **Które formaty obsługują odwracanie?** Wszystkie główne formaty (3DS, OBJ, STL, U3D, glTF, PLY, X, FBX) udostępniają opcję `setFlipCoordinateSystem`.  
- **Czy potrzebuję dodatkowych bibliotek?** Tylko plik JAR Aspose.3D dla Javy; nie są wymagane zewnętrzne konwertery.  
- **Czy mogę jednocześnie ładować materiały?** Tak — użyj `setEnableMaterials(true)` dla plików OBJ.  
- **Czy licencja jest wymagana w produkcji?** Wymagana jest ważna licencja Aspose.3D dla wdrożeń nie‑testowych.

## Co to jest „flip coordinate system”?
Odwracanie systemu współrzędnych zmienia orientację osi używanych przez importowany model. Jest to niezbędne, gdy plik źródłowy używa innej ręczności (praworęcznej vs. leworęcznej) niż Twój silnik renderujący, zapobiegając wyświetlaniu modeli jako lustrzanych lub odwróconych.

## Dlaczego dostosowywać import 3D?
- Zachowaj przekształcenia animacji (`setApplyAnimationTransform`).  
- Poprawne przetwarzanie kolorów (`setGammaCorrectedColor`).  
- Rozwiąż ścieżki zasobów zewnętrznych za pomocą `getLookupPaths()`.  
- Optymalizuj zużycie pamięci, ładując tylko to, co jest potrzebne.

## Wymagania wstępne

- Podstawowa znajomość programowania w języku Java.  
- Zainstalowany Java Development Kit (JDK).  
- Pobraną bibliotekę Aspose.3D dla Javy. Możesz ją uzyskać [tutaj](https://releases.aspose.com/3d/java/).  
- Znajomość formatów plików 3D, takich jak 3DS, OBJ, STL, U3D, glTF, PLY, X oraz FBX.

## Importowanie pakietów

W swoim projekcie Java upewnij się, że importujesz niezbędne pakiety Aspose.3D:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Jak dostosować import 3D przy użyciu LoadOptions

Poniżej znajdują się fragmenty kodu krok po kroku, które pokazują, jak włączyć opcję **odwrócenia systemu współrzędnych** dla każdego obsługiwanego formatu. Fragmenty są gotowe do skopiowania do Twojego projektu; wystarczy zamienić `"Your Document Directory"` na rzeczywistą ścieżkę do Twoich zasobów.

### Krok 1: Dostosowanie ładowania pliku 3DS

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

### Krok 2: Dostosowanie ładowania pliku OBJ

```java
public static void objLoadOption() {
    String MyDir = "Your Document Directory";
    ObjLoadOptions loadObjOpts = new ObjLoadOptions();
    loadObjOpts.setEnableMaterials(true);
    loadObjOpts.setFlipCoordinateSystem(true);
    loadObjOpts.getLookupPaths().add(MyDir);
}
```

### Krok 3: Dostosowanie ładowania pliku STL

```java
public static void stlLoadOption() {
    String MyDir = "Your Document Directory";
    StlLoadOptions loadSTLOpts = new StlLoadOptions();
    loadSTLOpts.setFlipCoordinateSystem(true);
    loadSTLOpts.getLookupPaths().add(MyDir);
}
```

### Krok 4: Dostosowanie ładowania pliku U3D

```java
public static void u3dLoadOption() {
    String MyDir = "Your Document Directory";
    U3dLoadOptions loadU3DOpts = new U3dLoadOptions();
    loadU3DOpts.setFlipCoordinateSystem(true);
    loadU3DOpts.getLookupPaths().add(MyDir);
}
```

### Krok 5: Dostosowanie ładowania pliku glTF

```java
public static void gltfLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    GltfLoadOptions loadOpt = new GltfLoadOptions();
    loadOpt.setFlipTexCoordV(true);
    scene.open(MyDir + "Duck.gltf", loadOpt);
}
```

### Krok 6: Dostosowanie ładowania pliku PLY

```java
public static void plyLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    PlyLoadOptions loadPLYOpts = new PlyLoadOptions();
    loadPLYOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "vase-v2.ply", loadPLYOpts);
}
```

### Krok 7: Dostosowanie ładowania pliku X

```java
public static void xLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    XLoadOptions loadXOpts = new XLoadOptions(FileContentType.ASCII);
    loadXOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "warrior.x", loadXOpts);
}
```

### Krok 8: Dostosowanie ładowania pliku FBX (Opcjonalnie)

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

## Typowe problemy i rozwiązania
- **Model jest odbity lustrzanie po załadowaniu** – sprawdź, czy `setFlipCoordinateSystem(true)` jest ustawione dla właściwego formatu.  
- **Brak materiałów** – dla plików OBJ upewnij się, że `setEnableMaterials(true)` jest włączone oraz że pliki materiałów (.mtl) znajdują się w jednej ze ścieżek wyszukiwania.  
- **Współrzędne tekstury są odwrócone** – dla glTF może być potrzebne `setFlipTexCoordV(true)` oprócz odwrócenia osi.  
- **Błędy pliku nie znaleziono** – dodaj katalog zawierający zasoby zewnętrzne (tekstury, pliki pomocnicze) do `loadOpts.getLookupPaths()`.

## Zakończenie

Korzystając z `LoadOptions` Aspose.3D, możesz **odwrócić system współrzędnych** i **dostosować import 3D** dla praktycznie każdego głównego formatu. Ten poziom kontroli eliminuje potrzebę skryptów post‑procesowych i zapewnia, że Twoje zasoby będą renderowane poprawnie za pierwszym razem.

## Najczęściej zadawane pytania

### P1: Gdzie mogę znaleźć dokumentację Aspose.3D dla Javy?
O1: Dokumentacja jest dostępna [tutaj](https://reference.aspose.com/3d/java/).

### P2: Jak mogę pobrać Aspose.3D dla Javy?
O2: Możesz go pobrać [tutaj](https://releases.aspose.com/3d/java/).

### P3: Czy dostępna jest darmowa wersja próbna?
O3: Tak, możesz uzyskać darmową wersję próbną [tutaj](https://releases.aspose.com/).

### P4: Gdzie mogę uzyskać wsparcie dla Aspose.3D dla Javy?
O4: Odwiedź forum wsparcia [tutaj](https://forum.aspose.com/c/3d/18).

### P5: Czy potrzebuję tymczasowej licencji do testów?
O5: Tak, uzyskaj tymczasową licencję [tutaj](https://purchase.aspose.com/temporary-license/).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Ostatnia aktualizacja:** 2026-02-25  
**Testowano z:** Aspose.3D for Java 24.11 (latest)  
**Autor:** Aspose