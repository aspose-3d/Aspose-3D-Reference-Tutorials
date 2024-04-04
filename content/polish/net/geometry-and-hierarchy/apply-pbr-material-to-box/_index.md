---
title: Nakładanie materiału PBR na pudełko
linktitle: Nakładanie materiału PBR na pudełko
second_title: Aspose.3D API .NET
description: Poznaj świat grafiki 3D dzięki Aspose.3D dla .NET. Twórz wciągające sceny bez wysiłku, korzystając z materiałów do renderowania fizycznego.
type: docs
weight: 10
url: /pl/net/geometry-and-hierarchy/apply-pbr-material-to-box/
---
## Wstęp

Witamy w fascynującym świecie grafiki 3D! W tym przewodniku krok po kroku poznamy potężną bibliotekę Aspose.3D dla .NET i dowiemy się, jak tworzyć wspaniałe sceny 3D przy użyciu materiałów do renderowania opartego na fizyce (PBR). Aspose.3D upraszcza złożony proces grafiki 3D i otwiera pole możliwości dla programistów.

## Warunki wstępne

Zanim zagłębimy się w ekscytujący świat grafiki 3D, upewnijmy się, że mamy wszystko skonfigurowane:

### Pobierz i zainstaluj Aspose.3D dla .NET

 Odwiedzić[Dokumentacja Aspose.3D dla .NET](https://reference.aspose.com/3d/net/) aby uzyskać szczegółowe instrukcje dotyczące pobierania i instalowania biblioteki.

### Zdobądź licencję

Aby odblokować pełny potencjał Aspose.3D, uzyskaj ważną licencję. Możesz uzyskać licencję tymczasową[Tutaj](https://purchase.aspose.com/temporary-license/) lub kup pełną licencję[Tutaj](https://purchase.aspose.com/buy).

## Importuj przestrzenie nazw

Po pierwsze, pamiętaj o zaimportowaniu niezbędnych przestrzeni nazw, aby wykorzystać możliwości Aspose.3D dla .NET:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Shading;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
```

## Krok 1: Zainicjuj scenę

Rozpocznij od zainicjowania sceny 3D przy użyciu następującego fragmentu kodu:

```csharp
Scene scene = new Scene();
```

## Krok 2: Zainicjuj materiał PBR

Utwórz obiekt materialny PBR, aby uzyskać realistyczne renderowanie:

```csharp
PbrMaterial mat = new PbrMaterial();
```

## Krok 3: Ustaw właściwości materiału

Dostosuj właściwości materiału, czyniąc go niemal metalicznym i bardzo szorstkim:

```csharp
mat.MetallicFactor = 0.9;
mat.RoughnessFactor = 0.9;
```

## Krok 4: Utwórz pudełko

Wygeneruj box, do którego zostanie nałożony materiał PBR:

```csharp
var boxNode = scene.RootNode.CreateChildNode("box", new Box());
```

## Krok 5: Nałóż materiał na pudełko

Przypisz materiał PBR do utworzonego węzła boxu:

```csharp
boxNode.Material = mat;
```

## Krok 6: Zapisz scenę 3D

Zapisz scenę 3D w formacie STL z żądanym katalogiem wyjściowym:

```csharp
scene.Save("Your Output Directory" + "PBR_Material_Box_Out.stl", FileFormat.STLASCII);
```

Gratulacje! Pomyślnie zastosowałeś materiał PBR do pudełka w scenie 3D przy użyciu Aspose.3D dla .NET.

## Wniosek

Wyruszenie w grafikę 3D z Aspose.3D dla .NET otwiera drzwi do nieskończonych możliwości twórczych. Dzięki intuicyjnemu interfejsowi API i solidnym funkcjom tworzenie oszałamiających wizualnie scen staje się przyjemnym doświadczeniem dla programistów.

## Często zadawane pytania

### P1: Czy Aspose.3D jest kompatybilny z innymi formatami plików 3D?

Odpowiedź 1: Tak, Aspose.3D obsługuje różne formaty plików 3D, zapewniając elastyczność w Twoich projektach.

### P2: Czy mogę używać Aspose.3D do zastosowań komercyjnych?

A2: Absolutnie! Aspose.3D zapewnia licencje komercyjne umożliwiające bezproblemową integrację z aplikacjami.

### P3: Czy dostępna jest wersja próbna?

 Odpowiedź 3: Tak, możesz poznać możliwości Aspose.3D, pobierając bezpłatną wersję próbną[Tutaj](https://releases.aspose.com/).

### P4: Gdzie mogę znaleźć wsparcie i dyskusje społeczności?

 A4: Dołącz do społeczności Aspose.3D pod adresem[Fora Aspose.3D](https://forum.aspose.com/c/3d/18) za wsparcie i dyskusję.

### P5: Jak uzyskać tymczasową licencję na Aspose.3D?

 Odpowiedź 5: Możesz uzyskać licencję tymczasową[Tutaj](https://purchase.aspose.com/temporary-license/) w celach ewaluacyjnych.