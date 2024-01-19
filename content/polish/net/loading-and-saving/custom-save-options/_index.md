---
title: Ładowanie i zapisywanie — niestandardowe opcje zapisywania
linktitle: Ładowanie i zapisywanie — niestandardowe opcje zapisywania
second_title: Aspose.3D API .NET
description: Poznaj moc Aspose.3D dla .NET. Dowiedz się, jak dostosować zapisywanie scen 3D, korzystając ze szczegółowych przewodników dotyczących formatów Collada, 3DS, FBX, OBJ, STL, U3D, glTF, DRC i RVM.
type: docs
weight: 21
url: /pl/net/loading-and-saving/custom-save-options/
---
## Wstęp

Witamy w świecie Aspose.3D dla .NET! Jeśli chcesz zwiększyć swoje możliwości w zakresie programowania 3D, jesteś we właściwym miejscu. W tym samouczku omówimy funkcje ładowania i zapisywania, skupiając się szczególnie na niestandardowych opcjach zapisywania. Aspose.3D dla .NET to potężna biblioteka, która umożliwia programistom efektywne manipulowanie i zapisywanie scen 3D.

## Warunki wstępne

Zanim zaczniemy odkrywać ekscytujące funkcje Aspose.3D, upewnij się, że spełniasz następujące wymagania wstępne:

- Podstawowa znajomość programowania w C# i .NET.
-  Zainstalowana biblioteka Aspose.3D dla .NET. Można go pobrać z[strona wydania](https://releases.aspose.com/3d/net/).
- Środowisko programistyczne skonfigurowane w programie Visual Studio lub dowolnym innym preferowanym środowisku C# IDE.

## Importuj przestrzenie nazw

Na początek zaimportujmy niezbędne przestrzenie nazw:

```csharp
using System;
using System.IO;
using System.Collections.Generic;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using Aspose.ThreeD.Shading;
using System.Drawing;
```

Teraz, gdy mamy już przygotowany etap, podzielmy samouczek na kilka kroków.

## Krok 1: Opcja zapisu Collady

Zacznijmy od Collady, popularnego formatu plików 3D. Wykonaj poniższe kroki, aby dostosować opcje zapisywania Collada:

### 1. Skonfiguruj katalog:
   ```csharp
   string dataDir = "Your Document Directory";
   ```

### 2. Zainicjuj opcje zapisywania Collada:
   ```csharp
   ColladaSaveOptions saveColladaOpts = new ColladaSaveOptions();
   ```

### 3. Skonfiguruj opcje:
   ```csharp
   saveColladaOpts.Indented = true;
   saveColladaOpts.TransformStyle = ColladaTransformStyle.Matrix;
   saveColladaOpts.LookupPaths = new List<string>(new string[] { dataDir });
   ```

## Krok 2: Dyskretna opcja zapisu 3DS

Przyjrzyjmy się teraz Discreet 3DS i jego opcjom dostosowywania:

### 1. Skonfiguruj katalog:
   ```csharp
   string dataDir = "Your Document Directory";
   ```

### 2. Zainicjuj opcje zapisu 3DS:
   ```csharp
   Discreet3dsSaveOptions saveOpts = new Discreet3dsSaveOptions();
   ```

### 3. Skonfiguruj opcje:
   ```csharp
   saveOpts.DuplicatedNameCounterBase = 2;
   // Dodatkowe możliwości konfiguracji...
   ```

Kontynuuj to podejście krok po kroku dla opcji zapisywania FBX, OBJ, STL, U3D, glTF i DRC, dostosowując każdą z nich zgodnie z własnymi wymaganiami.

## Krok 3: Opcje zapisu glTF

Skupmy się teraz na glTF, formacie szeroko stosowanym w aplikacjach internetowych i mobilnych. Dostosuj opcje zapisywania glTF, wykonując następujące kroki:

### 1. Zainicjuj obiekt sceny:
   ```csharp
   Scene scene = new Scene();
   scene.RootNode.CreateChildNode("sphere", new Sphere());
   ```

### 2. Ustaw opcje zapisywania glTF:
   ```csharp
   GltfSaveOptions opt = new GltfSaveOptions(FileContentType.ASCII);
   opt.EmbedAssets = true;
   opt.UseCommonMaterials = true;
   opt.BufferFile = "mybuf.bin";
   ```

### 3. Zapisz plik glTF:
   ```csharp
   scene.Save("Your Output Directory" + "glTFSaveOptions_out.gltf", opt);
   ```

Postępuj zgodnie z podobną strukturą dla innych opcji zapisywania, takich jak DRC i RVM.

## Wniosek

Gratulacje! Pomyślnie wypróbowałeś niestandardowe opcje zapisywania w Aspose.3D dla .NET. Ta potężna biblioteka zapewnia mnóstwo opcji umożliwiających dostosowanie procesu zapisywania scen 3D.

## Często zadawane pytania

### P1: Czy mogę używać Aspose.3D dla .NET z innymi frameworkami .NET?

Odpowiedź 1: Tak, Aspose.3D jest kompatybilny z różnymi frameworkami .NET, zapewniając elastyczność w Twoim środowisku programistycznym.

### P2: Czy dostępne są opcje licencjonowania dla Aspose.3D?

 Odpowiedź 2: Tak, możesz zapoznać się z opcjami licencjonowania[Tutaj](https://purchase.aspose.com/buy).

### P3: Gdzie mogę znaleźć pomoc dotyczącą zapytań związanych z Aspose.3D?

 Odpowiedź 3: Możesz szukać wsparcia na stronie[Forum Aspose.3D](https://forum.aspose.com/c/3d/18).

### P4: Czy dostępny jest bezpłatny okres próbny?

 Odpowiedź 4: Tak, możesz uzyskać dostęp do bezpłatnego okresu próbnego[Tutaj](https://releases.aspose.com/).

### P5: Jak mogę uzyskać tymczasową licencję na Aspose.3D?

 A5: Uzyskaj tymczasową licencję[Tutaj](https://purchase.aspose.com/temporary-license/).