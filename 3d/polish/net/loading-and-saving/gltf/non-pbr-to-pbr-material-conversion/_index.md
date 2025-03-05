---
title: Konwersja materiału innego niż PBR na PBR
linktitle: Konwersja materiału innego niż PBR na PBR
second_title: Aspose.3D API .NET
description: Poznaj Aspose.3D dla .NET - Konwertuj materiały inne niż PBR na PBR bez wysiłku. Kompleksowy samouczek i potężne API.
type: docs
weight: 16
url: /pl/net/loading-and-saving/gltf/non-pbr-to-pbr-material-conversion/
---
## Wstęp

Witamy w tym przewodniku krok po kroku dotyczącym używania Aspose.3D dla .NET do konwersji materiałów innych niż PBR (renderowanie oparte na fizyce) na materiały PBR. Aspose.3D to potężny interfejs API, który umożliwia programistom bezproblemową pracę z formatami plików 3D w aplikacjach .NET.

## Warunki wstępne

Zanim przejdziemy do samouczka, upewnij się, że spełniasz następujące wymagania wstępne:

-  Aspose.3D dla .NET: Upewnij się, że masz zainstalowaną bibliotekę Aspose.3D dla .NET. Możesz znaleźć link do pobrania[Tutaj](https://releases.aspose.com/3d/net/).

- Podstawowa znajomość języka C#: W tym samouczku założono, że masz podstawową wiedzę na temat programowania w języku C#.

- IDE (zintegrowane środowisko programistyczne): wybierz preferowane środowisko IDE do programowania w środowisku .NET, takie jak Visual Studio.

## Importuj przestrzenie nazw

W kodzie C# zacznij od zaimportowania niezbędnych przestrzeni nazw:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
```

## Krok 1: Zainicjuj nową scenę 3D

Rozpocznij od utworzenia nowej sceny 3D przy użyciu następującego kodu:

```csharp
// ExStart:Non_PBRtoPBRMaterial
// zainicjuj nową scenę 3D
var scene = new Scene();
```

## Krok 2: Utwórz obiekt 3D

Następnie utwórz obiekt 3D, na przykład pudełko:

```csharp
var box = new Box();
scene.RootNode.CreateChildNode("box1", box).Material = new PhongMaterial() { DiffuseColor = new Vector3(1, 0, 1) };
```

## Krok 3: Skonfiguruj konwersję materiałów

Skonfiguruj opcje konwersji materiałów dla konwersji innych niż PBR na PBR:

```csharp
GltfSaveOptions options = new GltfSaveOptions(FileFormat.GLTF2);
options.MaterialConverter = delegate (Material material)
{
    PhongMaterial phongMaterial = (PhongMaterial)material;
    return new PbrMaterial() { Albedo = new Vector3(phongMaterial.DiffuseColor.x, phongMaterial.DiffuseColor.y, phongMaterial.DiffuseColor.z) };
};
```

## Krok 4: Zapisz w formacie GLTF 2.0

Zapisz przekonwertowaną scenę w formacie GLTF 2.0:

```csharp
scene.Save("Your Output Directory" + "Non_PBRtoPBRMaterial_Out.gltf", options);
// ExEnd:Non_PBRtoPBRMaterial
```

Powtórz te kroki, jeśli jest to konieczne w konkretnym przypadku użycia, upewniając się, że każdy szczegół jest poprawnie skonfigurowany.

## Wniosek

Gratulacje! Pomyślnie nauczyłeś się konwertować materiały inne niż PBR na PBR przy użyciu Aspose.3D dla .NET. To potężne narzędzie otwiera nieograniczone możliwości manipulacji grafiką 3D w aplikacjach .NET.

## Często zadawane pytania

### P1: Czy Aspose.3D jest kompatybilny ze wszystkimi formatami plików 3D?

Odpowiedź 1: Tak, Aspose.3D obsługuje szeroką gamę formatów plików 3D, zapewniając elastyczność w Twoich projektach.

### P2: Czy mogę używać Aspose.3D do zastosowań komercyjnych?

 A2: Absolutnie! Aspose.3D jest produktem komercyjnym i można go kupić[Tutaj](https://purchase.aspose.com/buy).

### P3: Czy potrzebuję tymczasowej licencji do testowania?

 Odpowiedź 3: Tak, możesz uzyskać tymczasową licencję do celów testowych[Tutaj](https://purchase.aspose.com/temporary-license/).

### P4: Gdzie mogę znaleźć wsparcie dla Aspose.3D?

 A4: Odwiedź[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) za wsparcie społeczności i dyskusje.

### P5: Czy dostępny jest bezpłatny okres próbny?

 Odpowiedź 5: Tak, możesz skorzystać z bezpłatnej wersji próbnej[Tutaj](https://releases.aspose.com/).