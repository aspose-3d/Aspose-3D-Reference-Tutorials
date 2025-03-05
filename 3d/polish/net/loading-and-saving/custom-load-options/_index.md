---
title: Niestandardowe opcje ładowania
linktitle: Niestandardowe opcje ładowania
second_title: Aspose.3D API .NET
description: Poznaj Aspose.3D dla .NET, najlepsze rozwiązanie do płynnego ładowania i zapisywania modeli 3D.
type: docs
weight: 15
url: /pl/net/loading-and-saving/custom-load-options/
---
## Wstęp

Witamy w świecie Aspose.3D dla .NET – potężnej biblioteki, która umożliwia programistom bezproblemową pracę z plikami 3D. W tym samouczku zagłębimy się w zawiłości ładowania i zapisywania modeli 3D, koncentrując się na niestandardowych opcjach ładowania. Niezależnie od tego, czy jesteś doświadczonym programistą, czy nowicjuszem, ten przewodnik przeprowadzi Cię krok po kroku przez proces, upewniając się, że wykorzystasz pełny potencjał Aspose.3D dla .NET.

## Warunki wstępne

Zanim wyruszymy w tę podróż, upewnijmy się, że spełniamy następujące warunki wstępne:

-  Aspose.3D dla .NET: Upewnij się, że masz zainstalowaną bibliotekę. Możesz go pobrać[Tutaj](https://releases.aspose.com/3d/net/).

- Katalog dokumentów: Utwórz katalog do przechowywania plików modeli 3D.

Teraz, gdy masz już wszystko, co niezbędne, zanurzmy się w ekscytujący świat manipulacji modelami 3D!

## Importuj przestrzenie nazw

Na początek zaimportujmy niezbędne przestrzenie nazw. To przygotuje grunt pod naszą podróż do krainy Aspose.3D.

```csharp
using System;
using System.IO;
using System.Collections.Generic;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Formats;
```

## Ładowanie i zapisywanie — niestandardowe opcje ładowania

### Krok 1: Ładowanie plików Discreet3DS

```csharp
private static void Discreet3DSLoadOption()
{
    Discreet3dsLoadOptions loadOpts = new Discreet3dsLoadOptions();

    //Ustaw opcje niestandardowe
    loadOpts.ApplyAnimationTransform = true;
    loadOpts.FlipCoordinateSystem = true;
    loadOpts.GammaCorrectedColor = true;
    loadOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //Załaduj plik z opcjami ładowania
    var scene = Scene.FromFile("test.3ds", loadOpts);
}
```

### Krok 2: Ładowanie plików OBJ

```csharp
private static void ObjLoadOption()
{
    ObjLoadOptions loadObjOpts = new ObjLoadOptions();

    //Ustaw opcje niestandardowe
    loadObjOpts.EnableMaterials = true;
    loadObjOpts.FlipCoordinateSystem = true;
    loadObjOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //Załaduj plik z opcjami ładowania
    var scene = Scene.FromFile("test.obj", loadObjOpts);

}
```

### Krok 3: Ładowanie plików STL

```csharp
private static void STLLoadOption()
{
    // Ścieżka do katalogu dokumentów.
    StlLoadOptions loadSTLOpts = new StlLoadOptions();

    //Ustaw opcje niestandardowe
    loadSTLOpts.FlipCoordinateSystem = true;
    loadSTLOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //Załaduj plik z opcjami ładowania
    var scene = Scene.FromFile("test.stl", loadSTLOpts);
}
```

### Krok 4: Ładowanie plików U3D

```csharp
private static void U3DLoadOption()
{
    // Ścieżka do katalogu dokumentów.
    string dataDir = "Your Document Directory";
    U3dLoadOptions loadU3DOpts = new U3dLoadOptions();

    //Ustaw opcje niestandardowe
    loadU3DOpts.FlipCoordinateSystem = true;
    loadU3DOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //Załaduj plik z opcjami ładowania
    var scene = Scene.FromFile("test.u3d", loadU3DOpts);
}
```

### Krok 5: Ładowanie plików glTF

```csharp
private static void glTFLoadOptions()
{
    // Ścieżka do katalogu dokumentów.
    Scene scene = new Scene();
    GltfLoadOptions loadOpt = new GltfLoadOptions();

    //Ustaw opcje niestandardowe
    loadOpt.FlipTexCoordV = true;
    scene.Open("Duck.gltf", loadOpt);
}
```

### Krok 6: Ładowanie plików PLY

```csharp
private static void PlyLoadOptions()
{
    // Ścieżka do katalogu dokumentów.
    string dataDir = "Your Document Directory";
    Scene scene = new Scene();
    PlyLoadOptions loadPLYOpts = new PlyLoadOptions();

    //Ustaw opcje niestandardowe
    loadPLYOpts.FlipCoordinateSystem = true;
    scene.Open("vase-v2.ply", loadPLYOpts);
}
```

### Krok 7: Ładowanie plików FBX

```csharp
private static void FBXLoadOptions()
{
    // Ścieżka do katalogu dokumentów.
    Scene scene = new Scene();
    FbxLoadOptions opt = new FbxLoadOptions() { KeepBuiltinGlobalSettings = true };

    //Ustaw opcje niestandardowe
    scene.Open("test.FBX", opt);

    // Właściwości wyjściowe zdefiniowane w GlobalSettings w pliku FBX
    foreach (Property property in scene.RootNode.AssetInfo.Properties)
    {
        Console.WriteLine(property);
    }
}
```

## Wniosek

Gratulacje! Udało Ci się pomyślnie poruszać po skomplikowanym świecie ładowania i zapisywania modeli 3D przy użyciu Aspose.3D dla .NET. W tym samouczku omówiono różne formaty plików i ich niestandardowe opcje ładowania, co umożliwiło łatwe manipulowanie zasobami 3D.

## Często zadawane pytania

### P1: Czy Aspose.3D dla .NET jest odpowiedni dla początkujących?

A1: Absolutnie! Aspose.3D dla .NET zapewnia przyjazny dla użytkownika interfejs, dzięki czemu jest dostępny dla programistów na wszystkich poziomach.

### P2: Czy mogę używać Aspose.3D w projektach komercyjnych?

Odpowiedź 2: Tak, Aspose.3D dla .NET jest dostarczany z licencją komercyjną, która pozwala na wykorzystanie go w Twoich projektach.

### P3: Czy istnieją jakieś ograniczenia dotyczące obsługiwanych formatów plików?

 O3: Aspose.3D dla .NET obsługuje szeroką gamę popularnych formatów plików 3D, w tym OBJ, STL, FBX i inne. Patrz[dokumentacja](https://reference.aspose.com/3d/net/) dla pełnej listy.

### P4: Czy dostępna jest wersja próbna?

O4: Tak, możesz poznać możliwości Aspose.3D dla .NET, pobierając plik[bezpłatna wersja próbna](https://releases.aspose.com/).

### P5: Gdzie mogę szukać wsparcia dla Aspose.3D dla .NET?

 A5: Odwiedź[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) za wsparcie i pomoc społeczną.