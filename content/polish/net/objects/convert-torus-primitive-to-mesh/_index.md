---
title: Konwersja prymitywu torusa na siatkę
linktitle: Konwersja prymitywu torusa na siatkę
second_title: Aspose.3D API .NET
description: Odkryj moc Aspose.3D dla .NET dzięki naszemu przewodnikowi krok po kroku na temat konwersji prymitywów Torusa na siatki. Ulepsz swój rozwój 3D bez wysiłku!
type: docs
weight: 17
url: /pl/net/objects/convert-torus-primitive-to-mesh/
---
## Wstęp
Czy chcesz wykorzystać moc Aspose.3D dla .NET, aby bezproblemowo przekonwertować prymityw Torusa na siatkę? Nie szukaj dalej! W tym samouczku przeprowadzimy Cię przez ten proces, dzieląc każdy krok, aby zapewnić płynną podróż. Aspose.3D dla .NET zapewnia solidną platformę do manipulowania scenami 3D, co czyni go idealnym narzędziem dla programistów poszukujących wydajności i elastyczności.
## Warunki wstępne
Zanim przejdziesz do samouczka, upewnij się, że spełniasz następujące wymagania wstępne:
-  Aspose.3D dla .NET: Pobierz i zainstaluj bibliotekę. Możesz znaleźć link do pobrania[Tutaj](https://releases.aspose.com/3d/net/).
-  Plik 3D: Przygotuj przykładowy plik 3D w obsługiwanym formacie. Jeśli go nie masz, możesz skorzystać z[test.fbx](https://reference.aspose.com/3d/net/) plik z dokumentacji Aspose.3D.
## Importuj przestrzenie nazw
W swoim projekcie .NET zaimportuj niezbędne przestrzenie nazw, aby zapewnić płynną integrację z Aspose.3D. Dodaj następujący tekst na początku swojego kodu:
```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
```
## Krok 1: Załaduj plik 3D
```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("test.fbx"));
```
Załaduj plik 3D do sceny. Zastępować`"test.fbx"` ze ścieżką do pliku.
## Krok 2: Zainicjuj obiekt klasy węzła
```csharp
Node torusNode = new Node("torus");
```
Utwórz nowy obiekt węzła dla prymitywu Torus.
## Krok 3: Konwertuj torus na siatkę
```csharp
IMeshConvertible convertible = new Torus();
Mesh mesh = convertible.ToMesh();
```
Wykorzystaj możliwości Aspose.3D, aby przekonwertować prymityw Torusa na siatkę.
## Krok 4: Wskaż węzeł na geometrię siatki
```csharp
torusNode.Entity = mesh;
```
Powiąż geometrię siatki z węzłem.
## Krok 5: Dodaj węzeł do sceny
```csharp
scene.RootNode.ChildNodes.Add(torusNode);
```
Zintegruj węzeł torusa ze sceną.
## Krok 6: Zapisz scenę 3D
```csharp
var output = "Your Output Directory" + "TorusToMeshScene.fbx";
scene.Save(output, FileFormat.FBX7400ASCII);
Console.WriteLine("\nConverted the primitive Torus to a mesh successfully.\nFile saved at " + output);
```
Zapisz zmodyfikowaną scenę 3D w żądanym formacie pliku i lokalizacji.
## Wniosek
Gratulacje! Pomyślnie przekształciłeś prymityw Torusa w siatkę przy użyciu Aspose.3D dla .NET. Ta potężna biblioteka otwiera świat możliwości manipulacji 3D w projektach .NET.
## Często zadawane pytania
### Czy Aspose.3D jest kompatybilny ze wszystkimi formatami plików 3D?
Aspose.3D obsługuje szeroką gamę formatów plików 3D. Pełną listę znajdziesz w dokumentacji.
### Czy mogę używać Aspose.3D w projektach komercyjnych?
 Tak, Aspose.3D oferuje licencje komercyjne. Odwiedzać[zakup.aspose.com/buy](https://purchase.aspose.com/buy) dla szczegółów.
### Czy są dostępne licencje tymczasowe do celów testowych?
 Tak, możesz uzyskać licencję tymczasową[Tutaj](https://purchase.aspose.com/temporary-license/) dla testów.
### Gdzie mogę znaleźć wsparcie dla Aspose.3D?
 Odwiedzić[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) za wsparcie i pomoc społeczną.
### Czy mogę zapoznać się z większą liczbą samouczków i przykładów?
 Tak, patrz[dokumentacja](https://reference.aspose.com/3d/net/) obszerne tutoriale i przykłady.