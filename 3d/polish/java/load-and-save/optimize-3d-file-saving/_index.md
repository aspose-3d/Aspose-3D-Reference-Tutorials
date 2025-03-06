---
title: Zoptymalizuj zapisywanie plików 3D w Javie za pomocą opcji Aspose.3D SaveOptions
linktitle: Zoptymalizuj zapisywanie plików 3D w Javie za pomocą opcji Aspose.3D SaveOptions
second_title: Aspose.3D API Java
description: Dowiedz się, jak zoptymalizować zapisywanie plików 3D w Javie za pomocą Aspose.3D SaveOptions. Zwiększ wydajność i dostosuj wyniki bez wysiłku.
weight: 16
url: /pl/java/load-and-save/optimize-3d-file-saving/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Zoptymalizuj zapisywanie plików 3D w Javie za pomocą opcji Aspose.3D SaveOptions

## Wstęp

Aspose.3D to bogata w funkcje biblioteka Java, która umożliwia programistom płynną pracę z modelami 3D. Jeśli chodzi o zapisywanie plików 3D, klasa SaveOptions oferuje mnóstwo ustawień pozwalających dostosować dane wyjściowe do własnych wymagań. W tym samouczku omówimy różne opcje zapisywania i sposoby ich wykorzystania w celu optymalizacji procesu.

## Warunki wstępne

Zanim przejdziemy do samouczka, upewnij się, że spełniasz następujące wymagania wstępne:

-  Aspose.3D dla Java: Upewnij się, że biblioteka Aspose.3D jest zintegrowana z projektem Java. Możesz go pobrać[Tutaj](https://releases.aspose.com/3d/java/).

- Środowisko programistyczne Java: skonfiguruj na swoim komputerze funkcjonalne środowisko programistyczne Java.

- Katalog dokumentów: Utwórz katalog, w którym chcesz zapisać pliki 3D i zanotuj jego ścieżkę do późniejszego wykorzystania.

## Importuj pakiety

 W swoim projekcie Java zaimportuj pakiety niezbędne do pracy z Aspose.3D. Obejmuje to`Scene` class i różne klasy SaveOptions. Poniżej znajduje się podstawowy przykład:

```java
import com.aspose.threed.*;


import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
```

Teraz podzielmy każdy przykład na wiele kroków, aby zademonstrować użycie różnych opcji SaveOptions.

## Krok 1: Ładny wydruk w opcji GLTF SaveOption

 The`prettyPrintInGltfSaveOption` Metoda umożliwia wygenerowanie pliku GLTF z wciętą treścią JSON w celu zapewnienia czytelności dla człowieka.

```java
public static void prettyPrintInGltfSaveOption() throws IOException {
    // Zainicjuj scenę 3D
    Scene scene = new Scene(new Sphere());
    
    // Zainicjuj opcje GLTFSaveOptions
    GltfSaveOptions opt = new GltfSaveOptions(FileFormat.GLTF2);
    
    // Włącz ładny druk dla lepszej czytelności
    opt.setPrettyPrint(true);
    
    // Zapisz scenę 3D
    scene.save("Your Document Directory" + "prettyPrintInGltfSaveOption.gltf", opt);
}
```

## Krok 2: Opcja zapisu HTML5

 The`html5SaveOption` Metoda pokazuje, jak zapisać scenę 3D jako plik HTML5, łącznie z opcjami dostosowywania.

```java
public static void html5SaveOption() throws IOException {
    // Zainicjuj scenę
    Scene scene = new Scene();
    
    // Utwórz węzeł podrzędny z cylindrem
    Node node = scene.getRootNode().createChildNode(new Cylinder());
    
    //Ustaw właściwości węzła podrzędnego
    LambertMaterial mat = new LambertMaterial();
    mat.setDiffuseColor(new Vector3(0.34, 0.59, 0.41));
    node.setMaterial(mat);
    
    // Dodaj światło do sceny
    Light light = new Light();
    light.setLightType(LightType.POINT);
    scene.getRootNode().createChildNode(light).getTransform().setTranslation(10, 0, 10);
    
    // Zainicjuj opcje HTML5SaveOptions
    Html5SaveOptions opt = new Html5SaveOptions();
    
    // Dostosuj opcje (np. wyłącz siatkę i interfejs użytkownika)
    opt.setShowGrid(false);
    opt.setShowUI(false);
    
    // Zapisz scenę jako plik HTML5
    scene.save("Your Document Directory" + "html5SaveOption.html", FileFormat.HTML5);
}
```

 Kontynuuj podobne podziały dla innych metod SaveOptions, takich jak`colladaSaveOption`, `discreet3DSSaveOption`, `fbxSaveOption`, `objSaveOption`, `STLSaveOption`, `U3DSaveOption`, `glTFSaveOptions` , I`drcSaveOptions`.

## Wniosek

Wykonując ten obszerny samouczek, nauczyłeś się optymalizować zapisywanie plików 3D w Javie przy użyciu Aspose.3D SaveOptions. Niezależnie od tego, czy interesuje Cię ładne drukowanie plików GLTF, czy dostosowywanie wyników HTML5, Aspose.3D wyposaża Cię w narzędzia usprawniające przepływ pracy z grafiką 3D.

## Często zadawane pytania

### P1: Jak mogę osadzić zasoby w pliku glTF?

 Odpowiedź 1: Aby osadzić zasoby, użyj`setEmbedAssets(true)` metoda w`GltfSaveOptions` klasa.

###  Pytanie 2: Jaki jest cel`setPositionBits` method in `DracoSaveOptions`?

 A2:`setPositionBits` Metoda ustawia bity kwantyzacji dla pozycji w algorytmie kompresji Draco.

### P3: Czy mogę wyeksportować normalne dane w pliku U3D?

 A3: Tak, możesz eksportować normalne dane, ustawiając`setExportNormals(true)` w`U3dSaveOptions` klasa.

### P4: Jak odrzucić zapisywanie plików materiałów w eksporcie OBJ?

A4: Wykorzystaj`setFileSystem(new DummyFileSystem())` metoda w`ObjSaveOptions` class, aby odrzucić pliki materiałów.

### P5: Czy istnieje sposób na zapisanie zależności w katalogu lokalnym w pliku OBJ?

 O5: Tak, użyj`setFileSystem(new LocalFileSystem(MyDir))` metoda w`ObjSaveOptions` class, aby lokalnie zapisać zależności.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
