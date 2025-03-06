---
title: Dostosuj ładowanie plików 3D w Javie za pomocą Aspose.3D LoadOptions
linktitle: Dostosuj ładowanie plików 3D w Javie za pomocą Aspose.3D LoadOptions
second_title: Aspose.3D API Java
description: Ulepsz ładowanie plików 3D w Javie dzięki konfigurowalnym modułom LoadOptions Aspose.3D. Naucz się krok po kroku dostosowywania dla 3DS, OBJ, STL, U3D, glTF, PLY, X i opcjonalnego FBX.
weight: 12
url: /pl/java/load-and-save/customize-3d-file-loading/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Dostosuj ładowanie plików 3D w Javie za pomocą Aspose.3D LoadOptions

## Wstęp

stale zmieniającym się środowisku projektowania i rozwoju 3D, wydajna obsługa formatów plików 3D ma kluczowe znaczenie. Aspose.3D dla Java zapewnia potężne rozwiązanie umożliwiające dostosowanie ładowania różnych formatów plików 3D. Ten samouczek poprowadzi Cię przez proces dostosowywania ładowania plików 3D w Javie przy użyciu opcji LoadOptions Aspose.3D.

## Warunki wstępne

Zanim przystąpisz do procesu dostosowywania, upewnij się, że posiadasz następujące elementy:

- Podstawowa znajomość programowania w języku Java.
- Zainstalowany zestaw Java Development Kit (JDK).
-  Pobrano bibliotekę Aspose.3D dla Java. Możesz to uzyskać[Tutaj](https://releases.aspose.com/3d/java/).
- Znajomość formatów plików 3D, takich jak 3DS, OBJ, STL, U3D, glTF, PLY, X i FBX.

## Importuj pakiety

W swoim projekcie Java pamiętaj o zaimportowaniu niezbędnych pakietów Aspose.3D:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Dostosuj ładowanie plików 3D

### Krok 1: Dostosuj ładowanie plików 3DS

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

### Krok 2: Dostosuj ładowanie pliku OBJ

```java
public static void objLoadOption() {
    String MyDir = "Your Document Directory";
    ObjLoadOptions loadObjOpts = new ObjLoadOptions();
    loadObjOpts.setEnableMaterials(true);
    loadObjOpts.setFlipCoordinateSystem(true);
    loadObjOpts.getLookupPaths().add(MyDir);
}
```

### Krok 3: Dostosuj ładowanie pliku STL

```java
public static void stlLoadOption() {
    String MyDir = "Your Document Directory";
    StlLoadOptions loadSTLOpts = new StlLoadOptions();
    loadSTLOpts.setFlipCoordinateSystem(true);
    loadSTLOpts.getLookupPaths().add(MyDir);
}
```

### Krok 4: Dostosuj ładowanie pliku U3D

```java
public static void u3dLoadOption() {
    String MyDir = "Your Document Directory";
    U3dLoadOptions loadU3DOpts = new U3dLoadOptions();
    loadU3DOpts.setFlipCoordinateSystem(true);
    loadU3DOpts.getLookupPaths().add(MyDir);
}
```

### Krok 5: Dostosuj ładowanie pliku glTF

```java
public static void gltfLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    GltfLoadOptions loadOpt = new GltfLoadOptions();
    loadOpt.setFlipTexCoordV(true);
    scene.open(MyDir + "Duck.gltf", loadOpt);
}
```

### Krok 6: Dostosuj ładowanie pliku PLY

```java
public static void plyLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    PlyLoadOptions loadPLYOpts = new PlyLoadOptions();
    loadPLYOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "vase-v2.ply", loadPLYOpts);
}
```

### Krok 7: Dostosuj ładowanie pliku X

```java
public static void xLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    XLoadOptions loadXOpts = new XLoadOptions(FileContentType.ASCII);
    loadXOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "warrior.x", loadXOpts);
}
```

### Krok 8: Dostosuj ładowanie pliku FBX (opcjonalnie)

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

## Wniosek

Dostosowywanie ładowania plików 3D w Javie za pomocą opcji LoadOptions Aspose.3D umożliwia programistom dostosowanie procesu importowania do konkretnych wymagań. Niezależnie od tego, czy chodzi o dostosowywanie transformacji animacji, odwracanie układów współrzędnych, czy obsługę zewnętrznych zależności, Aspose.3D zapewnia elastyczność potrzebną do bezproblemowej integracji.

## Często zadawane pytania

### P1: Gdzie mogę znaleźć dokumentację Aspose.3D for Java?

 Odpowiedź 1: Dokumentacja jest dostępna[Tutaj](https://reference.aspose.com/3d/java/).

### P2: Jak mogę pobrać Aspose.3D dla Java?

 A2: Możesz go pobrać[Tutaj](https://releases.aspose.com/3d/java/).

### P3: Czy dostępny jest bezpłatny okres próbny?

 Odpowiedź 3: Tak, możesz uzyskać dostęp do bezpłatnego okresu próbnego[Tutaj](https://releases.aspose.com/).

### P4: Gdzie mogę uzyskać wsparcie dla Aspose.3D dla Java?

 Odpowiedź 4: Odwiedź forum pomocy technicznej[Tutaj](https://forum.aspose.com/c/3d/18).

### P5: Czy potrzebuję tymczasowej licencji do testowania?

 Odpowiedź 5: Tak, uzyskaj licencję tymczasową[Tutaj](https://purchase.aspose.com/temporary-license/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
