---
title: Dostosowany górny cylinder z przesunięciem
linktitle: Dostosowany górny cylinder z przesunięciem
second_title: Aspose.3D API .NET
description: Odkryj cuda grafiki 3D z Aspose.3D dla .NET. Dowiedz się, jak bez wysiłku tworzyć niestandardowe cylindry z przesunięciem górnym. Popraw swoje doświadczenie w kodowaniu już teraz!
type: docs
weight: 11
url: /pl/net/working-with-cylinder/customized-offset-top-cylinder/
---
## Wstęp
Witamy w świecie manipulacji grafiką 3D za pomocą Aspose.3D dla .NET! W tym samouczku przeprowadzimy Cię przez proces tworzenia dostosowanego górnego cylindra z przesunięciem przy użyciu Aspose.3D, potężnej biblioteki do pracy ze scenami, obiektami i formatami 3D w aplikacjach .NET.
## Warunki wstępne
Zanim przejdziemy do samouczka, upewnij się, że spełniasz następujące wymagania wstępne:
- Podstawowa znajomość języka programowania C#.
- Program Visual Studio zainstalowany na Twoim komputerze.
- Pobrano bibliotekę Aspose.3D dla .NET i odniesiono się do niej w projekcie.
Zacznijmy teraz od przewodnika krok po kroku!
## Importuj przestrzenie nazw
Po pierwsze, pamiętaj o zaimportowaniu niezbędnych przestrzeni nazw do kodu C#:
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
```csharp
// Utwórz scenę
Scene scene = new Scene();
```
Spowoduje to inicjowanie nowej sceny 3D przy użyciu Aspose.3D.
## Krok 2: Zainicjuj cylinder
```csharp
// Zainicjuj cylinder
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```
Tutaj tworzymy cylinder o określonych parametrach, takich jak promień, wysokość i plasterki.
## Krok 3: Ustaw OffsetTop dla pierwszego cylindra
```csharp
// Ustaw odsunięcie od góry
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```
Spowoduje to ustawienie niestandardowego przesunięcia góry dla pierwszego cylindra.
## Krok 4: Utwórz węzeł podrzędny dla pierwszego cylindra
```csharp
// Utwórz węzeł podrzędny
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```
Dodajemy pierwszy cylinder jako węzeł podrzędny do sceny, dostosowując jego położenie.
## Krok 5: Zainicjuj drugi cylinder
```csharp
//Zainicjuj drugi cylinder bez dostosowanego OffsetTop
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```
Drugi cylinder jest inicjowany bez niestandardowej, przesuniętej góry.
## Krok 6: Utwórz węzeł podrzędny dla drugiego cylindra
```csharp
// Utwórz węzeł podrzędny
scene.RootNode.CreateChildNode(cylinder2);
```
Dodajemy drugi cylinder jako węzeł podrzędny do sceny.
## Krok 7: Zapisz scenę
```csharp
// Ratować
scene.Save("Your Document Directory" + "CustomizedOffsetTopCylinder.obj", FileFormat.WavefrontOBJ);
```
Spowoduje to zapisanie sceny 3D, łącznie z dostosowanym górnym cylindrem z przesunięciem, w formacie Wavefront OBJ.
Teraz udało Ci się stworzyć dostosowany górny cylinder z przesunięciem przy użyciu Aspose.3D dla .NET!
## Wniosek
W tym samouczku omówiliśmy podstawy pracy z Aspose.3D dla .NET w celu stworzenia niestandardowego przesuniętego górnego cylindra. Ta biblioteka otwiera nieograniczone możliwości manipulacji grafiką 3D w aplikacjach .NET.
## Często zadawane pytania
### P: Gdzie mogę znaleźć dokumentację Aspose.3D dla .NET?
 Odp.: Dokumentacja jest dostępna[Tutaj](https://reference.aspose.com/3d/net/).
### P: Jak mogę pobrać Aspose.3D dla .NET?
 O: Możesz to pobrać[Tutaj](https://releases.aspose.com/3d/net/).
### P: Czy dostępna jest bezpłatna wersja próbna Aspose.3D dla .NET?
 Odp.: Tak, możesz skorzystać z bezpłatnego okresu próbnego[Tutaj](https://releases.aspose.com/).
### P: Gdzie mogę uzyskać wsparcie dla Aspose.3D dla .NET?
 O: Odwiedź[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) dla wsparcia.
### P: Czy mogę uzyskać tymczasową licencję na Aspose.3D dla .NET?
 Odp.: Tak, możesz uzyskać licencję tymczasową[Tutaj](https://purchase.aspose.com/temporary-license/).