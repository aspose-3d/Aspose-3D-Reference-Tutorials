---
title: Tworzenie cylindra wentylatora
linktitle: Tworzenie cylindra wentylatora
second_title: Aspose.3D API .NET
description: Odblokuj świat projektowania 3D dzięki Aspose.3D dla .NET! Bez wysiłku twórz wspaniałe cylindry z wentylatorami i bez wentylatorów. Pobierz teraz wersję próbną.
type: docs
weight: 10
url: /pl/net/working-with-cylinder/create-fan-cylinder/
---
## Wstęp
Witamy w świecie modelowania i wizualizacji 3D z Aspose.3D dla .NET! W tym przewodniku krok po kroku odkryjemy, jak stworzyć urzekający cylinder wentylatora za pomocą Aspose.3D dla .NET. Aspose.3D to potężna biblioteka zapewniająca szerokie możliwości pracy z treścią 3D w aplikacjach .NET.
## Warunki wstępne
Zanim zagłębimy się w ekscytujący świat modelowania 3D, upewnij się, że spełniasz następujące wymagania wstępne:
- Podstawowa znajomość programowania .NET.
- Program Visual Studio zainstalowany na Twoim komputerze.
-  Biblioteka Aspose.3D dla .NET, którą możesz pobrać[Tutaj](https://releases.aspose.com/3d/net/).
- Prawdziwe zainteresowanie uwolnieniem swojej kreatywności poprzez projektowanie 3D.
## Importuj przestrzenie nazw
Zacznijmy od zaimportowania niezbędnych przestrzeni nazw, aby udostępnić funkcjonalność Aspose.3D w Twoim projekcie .NET.
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
// Importuj przestrzenie nazw Aspose.3D
```
Teraz, gdy już wszystko skonfigurowaliśmy, podzielmy proces tworzenia cylindra wentylatora na łatwe do wykonania etapy.
## Krok 1: Utwórz scenę
```csharp
// Utwórz scenę
Scene scene = new Scene();
```
Rozpocznij od zainicjowania nowej sceny 3D. Służy to jako płótno, na którym ożyje cylinder naszego wentylatora.
## Krok 2: Utwórz cylinder wentylatora
```csharp
// Utwórz cylinder
var fan = new Cylinder(2, 2, 10, 20, 1, false);
```
Zdefiniuj charakterystykę cylindra wentylatora, określając parametry, takie jak promień, wysokość i rozdzielczość.
## Krok 3: Dostosuj właściwości cylindra wentylatora
```csharp
// Ustaw GenerateFanCylinder na true
fan.GenerateFanCylinder = true;
// Ustaw długość Theta
fan.ThetaLength = MathUtils.ToRadian(270);
```
Dostosuj cylinder wentylatora, umożliwiając wygenerowanie części wentylatora i dostosowując kąt odchylenia za pomocą ThetaLength.
## Krok 4: Umieść cylinder wentylatora na scenie
```csharp
// Utwórz węzeł podrzędny
scene.RootNode.CreateChildNode(fan).Transform.Translation = new Vector3(10, 0, 0);
```
Dodaj cylinder wentylatora jako węzeł podrzędny do węzła głównego sceny i umieść go w przestrzeni 3D.
## Krok 5: Utwórz cylinder bez wentylatora
```csharp
// Utwórz cylinder bez wentylatora
var nonfan = new Cylinder(2, 2, 10, 20, 1, false);
```
Odkryj elastyczność Aspose.3D, tworząc cylinder bez części wentylatora.
## Krok 6: Dostosuj właściwości cylindra innego niż wentylator
```csharp
// Ustaw GenerateFanCylinder na false
nonfan.GenerateFanCylinder = false;
// Ustaw długość Theta
nonfan.ThetaLength = MathUtils.ToRadian(270);
```
Rozróżnij cylinder inny niż wentylator, wyłączając generowanie części wentylatora.
## Krok 7: Umieść cylinder bez wentylatora na scenie
```csharp
// Utwórz węzeł podrzędny
scene.RootNode.CreateChildNode(nonfan);
```
Podobnie dodaj cylinder inny niż wentylator jako węzeł podrzędny do węzła głównego sceny.
## Krok 8: Zapisz scenę
```csharp
// Zapisz scenę
scene.Save("Your Document Directory" + "CreateFanCylinder.obj", FileFormat.WavefrontOBJ);
```
Zapisz swoje arcydzieło w żądanym formacie i lokalizacji. Teraz pomyślnie utworzyłeś cylinder z wentylatorem i bez wentylatora, używając Aspose.3D dla .NET!
## Wniosek
Gratulujemy ukończenia tego praktycznego przewodnika po modelowaniu 3D za pomocą Aspose.3D dla .NET! Uwolniłeś swoją kreatywność w świecie cyfrowym, z łatwością tworząc cylindry z wentylatorami i bez wentylatorów.
## Często Zadawane Pytania
### Czy mogę używać Aspose.3D dla .NET z innymi frameworkami .NET?
Tak, Aspose.3D jest kompatybilny z różnymi frameworkami .NET, zapewniając wszechstronność w twoich projektach programistycznych.
### Czy dostępna jest bezpłatna wersja próbna Aspose.3D dla .NET?
 Tak, możesz skorzystać z bezpłatnego okresu próbnego[Tutaj](https://releases.aspose.com/).
### Gdzie mogę znaleźć szczegółową dokumentację Aspose.3D dla .NET?
 Dokumentacja jest dostępna[Tutaj](https://reference.aspose.com/3d/net/).
### Jak mogę uzyskać wsparcie dla Aspose.3D dla .NET?
 Odwiedź forum pomocy[Tutaj](https://forum.aspose.com/c/3d/18) pomoc od społeczności i ekspertów Aspose.
### Czy dostępne są licencje tymczasowe dla Aspose.3D dla .NET?
 Tak, można uzyskać licencje tymczasowe[Tutaj](https://purchase.aspose.com/temporary-license/).