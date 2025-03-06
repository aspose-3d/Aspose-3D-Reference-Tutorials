---
title: Łączenie kwaternionów
linktitle: Łączenie kwaternionów
second_title: Aspose.3D API .NET
description: Odkryj moc manipulacji kwaternionami w scenach 3D za pomocą Aspose.3D dla .NET. Naucz się krok po kroku łączyć kwaterniony, aby uzyskać wciągające transformacje.
weight: 11
url: /pl/net/geometry-and-hierarchy/concatenate-quaternions/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Łączenie kwaternionów

## Wstęp

Witamy w tym kompleksowym samouczku na temat łączenia kwaternionów w scenach 3D przy użyciu Aspose.3D dla .NET! Jeśli jesteś programistą lub entuzjastą 3D i chcesz udoskonalić swoje umiejętności w zakresie manipulacji kwaternionami, jesteś we właściwym miejscu. Ten samouczek poprowadzi Cię krok po kroku przez proces, zapewniając płynną naukę.

## Warunki wstępne

Zanim przejdziesz do samouczka, upewnij się, że spełniasz następujące wymagania wstępne:

-  Biblioteka Aspose.3D dla .NET: Pobierz i zainstaluj bibliotekę z[Strona Aspose](https://releases.aspose.com/3d/net/).
- Środowisko programistyczne: Upewnij się, że masz działające środowisko programistyczne dla platformy .NET.

## Importuj przestrzenie nazw

W swoim projekcie .NET uwzględnij niezbędne przestrzenie nazw, aby wykorzystać moc Aspose.3D:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Utilities;
```

## Krok 1: Utwórz scenę

Rozpocznij od stworzenia sceny 3D przy użyciu biblioteki Aspose.3D. Scena posłuży jako płótno do manipulacji kwaternionami.

```csharp
Scene scene = new Scene();
```

## Krok 2: Zdefiniuj kwaterniony

 Zdefiniuj trzy kwaterniony,`q1`, `q2` , I`q3`, z których każdy reprezentuje określony obrót.

```csharp
Quaternion q1 = Quaternion.FromEulerAngle(Math.PI * 0.5, 0, 0);
Quaternion q2 = Quaternion.FromAngleAxis(-Math.PI * 0.5, Vector3.XAxis);
Quaternion q3 = q1.Concat(q2);
```

## Krok 3: Utwórz cylindry

Utwórz trzy cylindry, każdy reprezentujący kwaternion. Ustaw właściwości obrotu i translacji w oparciu o zdefiniowane kwaterniony.

```csharp
Node cylinder = scene.RootNode.CreateChildNode("cylinder-q1", new Cylinder(0.1, 1, 2));
cylinder.Transform.Rotation = q1;
cylinder.Transform.Translation = new Vector3(-5, 2, 0);

// Powtórz dla q2 i q3
```

## Krok 4: Zapisz do pliku

Zapisz scenę do pliku, określając format wyjściowy i nazwę pliku.

```csharp
var output = "Your Output Directory" + "test_out.fbx";
scene.Save(output, FileFormat.FBX7400ASCII);
```

## Krok 5: Wyświetl komunikat o powodzeniu

Po połączeniu kwaternionów i zapisaniu pliku wydrukuj komunikat o powodzeniu wraz ze ścieżką pliku.

```csharp
Console.WriteLine("\nQuaternions concatenated successfully.\nFile saved at " + output);
```

## Wniosek

Gratulacje! Pomyślnie nauczyłeś się łączenia kwaternionów w scenach 3D przy użyciu Aspose.3D dla .NET. Eksperymentuj z różnymi kombinacjami kwaternionów, aby uzyskać unikalne transformacje w swoich projektach.

## Często zadawane pytania

### P1: Czym są kwaterniony w grafice 3D?

Odpowiedź 1: Kwaterniony to jednostki matematyczne używane do reprezentowania obrotów w przestrzeni 3D, zapewniające przewagę nad innymi reprezentacjami rotacji.

### P2: Czy mogę używać Aspose.3D dla .NET z innymi bibliotekami .NET?

Odpowiedź 2: Tak, Aspose.3D dla .NET został zaprojektowany tak, aby bezproblemowo współpracować z innymi bibliotekami .NET.

### P3: Czy dostępna jest bezpłatna wersja próbna Aspose.3D dla .NET?

Odpowiedź 3: Tak, możesz uzyskać dostęp do bezpłatnego okresu próbnego[Tutaj](https://releases.aspose.com/).

### P4: Jak mogę uzyskać wsparcie dla Aspose.3D dla .NET?

 A4: Odwiedź[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) za wsparcie społeczności i dyskusje.

### P5: Czy mogę skorzystać z tymczasowej licencji na Aspose.3D dla .NET?

 Odpowiedź 5: Tak, możesz uzyskać licencję tymczasową[Tutaj](https://purchase.aspose.com/temporary-license/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
