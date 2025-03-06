---
title: Ustawianie właściwości trójwymiarowych w scenach 3D
linktitle: Ustawianie właściwości trójwymiarowych w scenach 3D
second_title: Aspose.3D API .NET
description: Zapoznaj się z samouczkiem Aspose.3D dla .NET dotyczącym ustawiania właściwości 3D. Ucz się krok po kroku z przykładami kodu. Podnieś swoje umiejętności manipulowania scenami 3D.
weight: 14
url: /pl/net/3d-scene/set-3d-properties/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Ustawianie właściwości trójwymiarowych w scenach 3D

## Wstęp

Tworzenie urzekających scen trójwymiarowych często wymaga możliwości manipulowania różnymi właściwościami, dodania głębi i realizmu Twoim projektom. Aspose.3D dla .NET zapewnia potężny zestaw narzędzi do osiągnięcia tego celu, umożliwiając bezproblemowe ustawianie i modyfikowanie właściwości trójwymiarowych w scenach 3D. W tym samouczku przeanalizujemy ten proces krok po kroku, zwiększając Twoją wiedzę na temat skutecznego wykorzystania Aspose.3D dla .NET.

## Warunki wstępne

Zanim przejdziesz do samouczka, upewnij się, że spełniasz następujące wymagania wstępne:

-  Aspose.3D dla .NET: Upewnij się, że masz zainstalowaną bibliotekę w projekcie .NET. Możesz go pobrać[Tutaj](https://releases.aspose.com/3d/net/).

- Katalog dokumentów: Utwórz katalog do przechowywania dokumentów 3D.

Teraz, gdy masz już podstawowe informacje, przyjrzyjmy się procesowi ustawiania właściwości trójwymiarowych w scenach 3D przy użyciu Aspose.3D dla .NET.

## Importuj przestrzenie nazw

Aby rozpocząć, zaimportuj niezbędne przestrzenie nazw do swojego projektu. Te przestrzenie nazw zapewniają klasy i metody wymagane do pracy z właściwościami trójwymiarowymi w Aspose.3D dla .NET.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```

## Krok 1: Załaduj scenę 3D

Rozpocznij od załadowania sceny 3D. W tym przykładzie używamy pliku FBX z osadzoną teksturą.

```csharp
//ExStart: Załaduj3DScene
string dataDir = "Your Document Directory";
Scene scene = new Scene(dataDir + "EmbeddedTexture.fbx");
//Zakończ: Load3DScene
```

## Krok 2: Uzyskaj dostęp do właściwości materiału

Uzyskaj dostęp do właściwości materiału wczytanej sceny 3D, aby manipulować jej charakterystyką.

```csharp
//ExStart: Właściwości materiału dostępu
Material material = scene.RootNode.ChildNodes[0].Material;
PropertyCollection props = material.Properties;
//ExEnd: AccessMaterialProperties
```

## Krok 3: Wyświetl listę wszystkich właściwości

Wypisz wszystkie właściwości materiału, używając pętli foreach lub pętli porządkowej for.

```csharp
//ExStart: ListAllProperties
foreach (var prop in props)
{
    Console.WriteLine("{0} = {1}", prop.Name, prop.Value);
}

//lub używając porządkowej pętli for
for (int i = 0; i < props.Count; i++)
{
    var prop = props[i];
    Console.WriteLine("{0} = {1}", prop.Name, prop.Value);
}
//Rozwiń: ListAllProperties
```

## Krok 4: Uzyskaj i zmodyfikuj właściwość według nazwy

Pobierz i zmodyfikuj określoną właściwość według jej nazwy.

```csharp
//ExStart: GetModifyPropertyByName
var diffuse = props["Diffuse"];
Console.WriteLine(diffuse);

//zmodyfikuj wartość właściwości według nazwy
props["Diffuse"] = new Vector3(1, 0, 1);
//ExEnd: GetModifyPropertyByName
```

## Krok 5: Uzyskaj instancję właściwości według nazwy

Pobierz instancję właściwości według jej nazwy w celu dalszej manipulacji.

```csharp
//ExStart: GetPropertyInstanceByName
Property pdiffuse = props.FindProperty("Diffuse");
Console.WriteLine(pdiffuse);
//ExEnd: GetPropertyInstanceByName
```

## Krok 6: Przejdź przez właściwości właściwości

 Od`Property` jest dziedziczony od`A3DObject`możesz przeglądać właściwości właściwości.

```csharp
//ExStart: TraversePropertyProperties
Console.WriteLine("Property flags = {0}", pdiffuse.GetProperty("flags"));

//i niektóre właściwości zdefiniowane tylko w pliku FBX:
Console.WriteLine("Label = {0}", pdiffuse.GetProperty("label"));
Console.WriteLine("Type Name = {0}", pdiffuse.GetProperty("typeName"));

//możliwe jest poruszanie się po posesji
foreach (var pp in pdiffuse.Properties)
{
    Console.WriteLine("Diffuse.{0} = {1}", pp.Name, pp.Value);
}
//Zakończenie: TraversePropertyProperties
```

## Wniosek

Gratulacje! Opanowałeś teraz sztukę ustawiania właściwości trójwymiarowych w scenach 3D przy użyciu Aspose.3D dla .NET. Eksperymentuj z różnymi właściwościami i wartościami, aby ożywić swoje projekty 3D.

## Często zadawane pytania

### P1: Czy mogę używać Aspose.3D dla .NET z innymi formatami plików 3D?

Odpowiedź 1: Tak, Aspose.3D obsługuje różne formaty plików 3D, w tym FBX, STL i wiele innych.

### P2: Jak mogę uzyskać tymczasową licencję na Aspose.3D dla .NET?

 A2: Odwiedź[Tutaj](https://purchase.aspose.com/temporary-license/) w celu uzyskania licencji tymczasowej.

### P3: Czy istnieje forum społecznościowe dla użytkowników Aspose.3D?

 Odpowiedź 3: Tak, wsparcie i dyskusje można znaleźć na stronie[Forum Aspose.3D](https://forum.aspose.com/c/3d/18).

### P4: Gdzie mogę znaleźć szczegółową dokumentację Aspose.3D dla .NET?

 A4: Patrz[dokumentacja](https://reference.aspose.com/3d/net/) w celu uzyskania kompleksowych wskazówek.

### P5: Czy mogę bezpłatnie wypróbować Aspose.3D dla .NET przed zakupem?

 A5: Oczywiście! Pobierz[bezpłatna wersja próbna](https://releases.aspose.com/) aby poznać jego funkcje.

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
