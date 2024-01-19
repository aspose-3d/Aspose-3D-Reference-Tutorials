---
title: Dostosowany cylinder dolny ścinany
linktitle: Dostosowany cylinder dolny ścinany
second_title: Aspose.3D API .NET
description: Dowiedz się, jak tworzyć niestandardowe cylindry ze ścinanym dolnym dnem przy użyciu Aspose.3D dla .NET, korzystając z naszego szczegółowego przewodnika krok po kroku. Podnieś swoje umiejętności modelowania 3D już dziś!
type: docs
weight: 12
url: /pl/net/working-with-cylinder/customized-shear-bottom-cylinder/
---
## Wstęp
Witamy w naszym obszernym przewodniku na temat tworzenia niestandardowego cylindra z dolnym ścinaniem przy użyciu Aspose.3D dla .NET. Jeśli chcesz udoskonalić swoje umiejętności modelowania 3D i dodać unikalne funkcje do swoich projektów, jesteś we właściwym miejscu. W tym samouczku przeprowadzimy Cię krok po kroku przez proces, korzystając z jasnych wyjaśnień i fragmentów kodu.
## Warunki wstępne
Zanim przejdziemy do samouczka, upewnij się, że posiadasz następujące elementy:
- Podstawowa znajomość programowania w C# i .NET.
-  Zainstalowana biblioteka Aspose.3D dla .NET. Możesz go pobrać[Tutaj](https://releases.aspose.com/3d/net/).
- Środowisko programistyczne skonfigurowane do programowania w .NET.
## Importuj przestrzenie nazw
kodzie C# zacznij od zaimportowania niezbędnych przestrzeni nazw:
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```
## Krok 1: Utwórz scenę
Rozpocznij od stworzenia sceny 3D za pomocą Aspose.3D:
```csharp
Scene scene = new Scene();
```
## Krok 2: Utwórz cylinder 1
Wygeneruj pierwszy cylinder i ustaw jego właściwości:
```csharp
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```
## Krok 3: Dostosuj dno ścinane dla cylindra 1
Zastosuj dostosowane dno ścinane do pierwszego cylindra:
```csharp
cylinder1.ShearBottom = new Vector2(0, 0.83); // Ścinanie 47,5 stopnia w płaszczyźnie xy (oś z)
```
## Krok 4: Dodaj cylinder 1 do sceny
Dodaj pierwszy cylinder do sceny i ustaw jego tłumaczenie:
```csharp
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```
## Krok 5: Utwórz cylinder 2
Wygeneruj drugi cylinder o podobnych właściwościach:
```csharp
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```
## Krok 6: Dodaj cylinder 2 do sceny
Dodaj drugi cylinder do sceny bez ścinanego dna:
```csharp
scene.RootNode.CreateChildNode(cylinder2);
```
## Krok 7: Zapisz scenę
Zapisz scenę jako plik Wavefront OBJ w katalogu dokumentów:
```csharp
scene.Save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WavefrontOBJ);
```
## Wniosek
Gratulacje! Pomyślnie utworzyłeś niestandardowy cylinder z dolnym ścinaniem przy użyciu Aspose.3D dla .NET. Celem tego samouczka było zapewnienie przewodnika krok po kroku dla użytkowników o różnym poziomie wiedzy specjalistycznej w zakresie modelowania i programowania 3D.
## Często Zadawane Pytania
### Czy Aspose.3D dla .NET jest odpowiedni dla początkujących?
Absolutnie! Aspose.3D dla .NET oferuje przyjazny dla użytkownika interfejs, dzięki czemu jest dostępny zarówno dla początkujących, jak i doświadczonych programistów.
### Czy mogę zastosować różne kąty ścinania do cylindrów?
Tak, istnieje możliwość dostosowania dna ścinacza do każdego cylindra indywidualnie, co pozwala uzyskać niepowtarzalne efekty.
### Czy dostępna jest wersja próbna?
 Tak, możesz skorzystać z bezpłatnej wersji próbnej[Tutaj](https://releases.aspose.com/).
### Gdzie mogę znaleźć dodatkowe wsparcie?
 Odwiedzić[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) za wsparcie społeczności i dyskusje.
### Jak mogę uzyskać licencję tymczasową?
 Zdobądź tymczasową licencję[Tutaj](https://purchase.aspose.com/temporary-license/).