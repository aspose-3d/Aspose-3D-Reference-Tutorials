---
title: Dzielenie wszystkich siatek sceny według materiału
linktitle: Dzielenie wszystkich siatek sceny według materiału
second_title: Aspose.3D API .NET
description: Dowiedz się, jak dzielić siatki 3D według materiału za pomocą Aspose.3D dla .NET. Postępuj zgodnie z naszym przewodnikiem krok po kroku, aby efektywnie organizować modele 3D i zarządzać nimi.
type: docs
weight: 21
url: /pl/net/objects/split-all-meshes-by-material/
---
## Wstęp
Witamy w tym przewodniku krok po kroku dotyczącym dzielenia wszystkich siatek sceny 3D według materiału przy użyciu Aspose.3D dla .NET. Jeśli pracujesz z modelami 3D i chcesz efektywnie organizować swoje siatki w oparciu o materiały, ten poradnik jest dla Ciebie. Aspose.3D to potężna biblioteka .NET, która zapewnia szereg funkcji do pracy z plikami 3D, co czyni ją doskonałym wyborem dla programistów.
## Warunki wstępne
Zanim przejdziesz do samouczka, upewnij się, że spełniasz następujące wymagania wstępne:
- Podstawowa znajomość języka programowania C#.
- Program Visual Studio zainstalowany na Twoim komputerze.
-  Biblioteka Aspose.3D dla .NET. Można go pobrać z[Tutaj](https://releases.aspose.com/3d/net/).
- Wejściowy plik 3D (na przykład „test.fbx”), który chcesz podzielić.
## Importuj przestrzenie nazw
Zacznij od zaimportowania niezbędnych przestrzeni nazw do projektu C#:
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
// Ścieżka do katalogu dokumentów.
string input = RunExamples.GetDataFilePath("test.fbx");
// Załaduj plik 3D
Scene scene = new Scene(input);
```
 W tym kroku ładujemy plik 3D przy użyciu Aspose.3D`Scene` klasa.
## Krok 2: Podziel wszystkie siatki
```csharp
// Podziel wszystkie siatki
PolygonModifier.SplitMesh(scene, SplitMeshPolicy.CloneData);
```
 Tutaj używamy`SplitMesh` metoda z`PolygonModifier` klasa do podziału wszystkich siatek w oparciu o materiał.
## Krok 3: Zapisz podzieloną scenę
```csharp
// Zapisz plik
var output = "Your Output Directory" + "test-splitted.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```
Zapisz zmodyfikowaną scenę w nowym pliku, aby zachować zmiany.
## Krok 4: Wyświetl komunikat o powodzeniu
```csharp
// Wyświetl komunikat o powodzeniu
Console.WriteLine("\nSplitting all meshes of a scene per material successfully.\nFile saved at " + output);
```
Wydrukuj komunikat o powodzeniu wskazujący, że operacja została pomyślnie ukończona.
## Wniosek
Gratulacje! Pomyślnie nauczyłeś się, jak dzielić wszystkie siatki sceny 3D według materiału, używając Aspose.3D dla .NET. Może to być cenna technika organizowania i zarządzania złożonymi modelami 3D.
## Często zadawane pytania
### 1. Czy mogę używać Aspose.3D dla .NET z innymi językami programowania?
Aspose.3D jest przeznaczony głównie dla .NET, ale zapewnia interoperacyjność z innymi językami poprzez powiązania językowe .NET.
### 2. Czy dostępna jest wersja próbna?
 Tak, możesz uzyskać dostęp do bezpłatnej wersji próbnej[Tutaj](https://releases.aspose.com/).
### 3. Gdzie mogę znaleźć więcej przykładów i dokumentacji?
 Zapoznaj się z obszerną dokumentacją pod adresem[Dokumentacja Aspose.3D](https://reference.aspose.com/3d/net/).
### 4. Jak mogę uzyskać wsparcie dla Aspose.3D?
 Odwiedzić[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) za wsparcie społeczności i dyskusje.
### 5. Czy mogę uzyskać licencję tymczasową?
 Tak, możesz uzyskać licencję tymczasową[Tutaj](https://purchase.aspose.com/temporary-license/).