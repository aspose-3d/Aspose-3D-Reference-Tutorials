---
date: 2026-01-17
description: Dowiedz się, jak wyświetlać właściwości materiału, zmieniać kolor rozpraszający
  i modyfikować atrybuty materiału 3D przy użyciu Aspose.3D dla .NET. Dołączone przykłady
  kodu krok po kroku.
linktitle: List Material Properties in 3D Scenes with Aspose.3D
second_title: Aspose.3D .NET API
title: Wypisz właściwości materiałów w scenach 3D przy użyciu Aspose.3D
url: /pl/net/3d-scene/set-3d-properties/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Lista właściwości materiałów w scenach 3D z Aspose.3D

## Wprowadzenie

Jeśli potrzebujesz **wyświetlić listę właściwości materiału** modelu 3D i następnie dostosować takie elementy jak kolor dyfuzyjny, jesteś we właściwym miejscu. Aspose.3D for .NET oferuje czyste, obiektowo‑zorientowane API, które pozwala przeglądać, pobierać i modyfikować atrybuty materiału bez opuszczania kodu C#. W tym samouczku przeprowadzimy Cię przez ładowanie sceny, wyliczanie jej właściwości materiałów oraz zmianę wartości, takich jak komponent dyfuzyjny — abyś mógł nadać swoim modelom dokładnie taki wygląd, jaki chcesz.

## Szybkie odpowiedzi
- **Jaki jest główny cel?** Wyświetlić listę właściwości materiału i zmodyfikować je (np. kolor dyfuzyjny).  
- **Jakiej biblioteki wymaga?** Aspose.3D for .NET.  
- **Czy potrzebna jest licencja?** Wymagana jest tymczasowa lub pełna licencja do użytku produkcyjnego.  
- **Obsługiwane formaty plików?** FBX, OBJ, STL, STL‑ASCII, 3MF i inne.  
- **Typowy czas implementacji?** Około 10‑15 minut dla podstawowego skryptu wyświetlającego właściwości.

## Co to jest **list material properties**?
Wyświetlanie listy właściwości materiału oznacza iterację po `PropertyCollection` materiału w celu odczytania każdej nazwy właściwości i jej bieżącej wartości. Jest to przydatne przy debugowaniu, wizualnej inspekcji lub budowaniu kontrolek UI, które pozwalają użytkownikom dostosowywać ustawienia materiału w czasie rzeczywistym.

## Dlaczego warto używać Aspose.3D do **access material properties**?
- **Brak zewnętrznych konwerterów** – pracuj bezpośrednio z natywnymi obiektami .NET.  
- **Bogaty model właściwości** – obsługuje niestandardowe atrybuty specyficzne dla FBX oprócz standardowych wartości PBR.  
- **Cross‑platform** – działa na .NET Framework, .NET Core oraz .NET 5/6+.  

## Wymagania wstępne

- Aspose.3D for .NET zainstalowane w projekcie. Pobierz je [tutaj](https://releases.aspose.com/3d/net/).  
- Folder na dysku przechowujący pliki źródłowe 3‑D (np. plik FBX z osadzonymi teksturami).

Teraz, gdy podstawy są już gotowe, przejdźmy do kodu.

## Import Namespaces

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

## Krok 1: Ładowanie sceny 3D

```csharp
//ExStart: Load3DScene
string dataDir = "Your Document Directory";
Scene scene = new Scene(dataDir + "EmbeddedTexture.fbx");
//ExEnd: Load3DScene
```

## Krok 2: **Access material properties** pierwszego węzła

```csharp
//ExStart: AccessMaterialProperties
Material material = scene.RootNode.ChildNodes[0].Material;
PropertyCollection props = material.Properties;
//ExEnd: AccessMaterialProperties
```

## Krok 3: **List material properties** – zobacz każdy para nazwa/wartość

```csharp
//ExStart: ListAllProperties
foreach (var prop in props)
{
    Console.WriteLine("{0} = {1}", prop.Name, prop.Value);
}

//or using ordinal for loop
for (int i = 0; i < props.Count; i++)
{
    var prop = props[i];
    Console.WriteLine("{0} = {1}", prop.Name, prop.Value);
}
//ExEnd: ListAllProperties
```

## Krok 4: **How to change diffuse** – modyfikacja właściwości Diffuse

```csharp
//ExStart: GetModifyPropertyByName
var diffuse = props["Diffuse"];
Console.WriteLine(diffuse);

//modify property value by name
props["Diffuse"] = new Vector3(1, 0, 1); // sets a magenta diffuse color
//ExEnd: GetModifyPropertyByName
```

## Krok 5: **Retrieve property by name** – uzyskaj silnie typowaną instancję

```csharp
//ExStart: GetPropertyInstanceByName
Property pdiffuse = props.FindProperty("Diffuse");
Console.WriteLine(pdiffuse);
//ExEnd: GetPropertyInstanceByName
```

## Krok 6: Przeglądanie własnych właściwości właściwości (zaawansowane)

```csharp
//ExStart: TraversePropertyProperties
Console.WriteLine("Property flags = {0}", pdiffuse.GetProperty("flags"));

//and some properties that only defined in FBX file:
Console.WriteLine("Label = {0}", pdiffuse.GetProperty("label"));
Console.WriteLine("Type Name = {0}", pdiffuse.GetProperty("typeName"));

//traversal on property's property is possible
foreach (var pp in pdiffuse.Properties)
{
    Console.WriteLine("Diffuse.{0} = {1}", pp.Name, pp.Value);
}
//ExEnd: TraversePropertyProperties
```

## Jak **change 3d material color** poza dyfuzją
Jeśli musisz wpłynąć na kolory specular, ambient lub emissive, po prostu zamień `"Diffuse"` na `"Specular"` lub `"Ambient"` w przypisaniu `props["..."]` powyżej. Stosuje się te same struktury `Vector3` lub `Vector4`.

## Typowe pułapki i wskazówki
- **Wrażliwość na wielkość liter w nazwach właściwości** – klucze właściwości Aspose.3D rozróżniają wielkość liter; używaj dokładnie takiej nazwy, jaka pojawia się w wynikowym wykazie.  
- **Brak właściwości** – nie wszystkie materiały udostępniają każdą cechę PBR. Sprawdź `props.ContainsKey("Specular")` przed dostępem.  
- **Zapisywanie zmian** – po modyfikacji właściwości wywołaj `scene.Save("output.fbx");`, aby utrwalić zmiany.

## Zakończenie

Nauczyłeś się teraz **wyświetlać listę właściwości materiału**, **pobierać właściwość po nazwie** oraz **zmieniać kolor dyfuzyjny** (lub dowolny inny atrybut materiału) przy użyciu Aspose.3D for .NET. Eksperymentuj z różnymi typami właściwości, aby precyzyjnie dopasować wygląd swoich zasobów 3‑D.

## FAQ's

### Q1: Czy mogę używać Aspose.3D for .NET z innymi formatami plików 3D?

A1: Tak, Aspose.3D obsługuje różne formaty plików 3D, w tym FBX, STL i wiele innych.

### Q2: Jak mogę uzyskać tymczasową licencję dla Aspose.3D for .NET?

A2: Odwiedź [tutaj](https://purchase.aspose.com/temporary-license/), aby uzyskać tymczasową licencję.

### Q3: Czy istnieje forum społecznościowe dla użytkowników Aspose.3D?

A3: Tak, wsparcie i dyskusje znajdziesz na [forum Aspose.3D](https://forum.aspose.com/c/3d/18).

### Q4: Gdzie mogę znaleźć szczegółową dokumentację dla Aspose.3D for .NET?

A4: Zapoznaj się z [dokumentacją](https://reference.aspose.com/3d/net/), aby uzyskać kompleksowe wskazówki.

### Q5: Czy mogę wypróbować Aspose.3D for .NET za darmo przed zakupem?

A5: Oczywiście! Pobierz [bezpłatną wersję próbną](https://releases.aspose.com/), aby przetestować jej funkcje.

## Frequently Asked Questions

**Q: Co reprezentuje `Vector3(1, 0, 1)`?**  
A: Ustawia kolor dyfuzyjny na magentę (czerwony = 1, zielony = 0, niebieski = 1) w liniowej przestrzeni kolorów.

**Q: Czy muszę wywołać `scene.Save` po zmianie właściwości?**  
A: Tak, zapis sceny zapisuje Twoje modyfikacje na dysku; w przeciwnym razie zmiany pozostają tylko w pamięci.

**Q: Czy mogę wyliczyć niestandardowe atrybuty FBX?**  
A: Oczywiście. `PropertyCollection` będzie zawierać wszystkie niestandardowe atrybuty, które możesz odczytać za pomocą `GetProperty("customName")`.

**Q: Czy istnieje sposób na masową aktualizację wielu materiałów?**  
A: Przejdź pętlą przez `scene.RootNode.ChildNodes` i powtórz kroki modyfikacji właściwości dla każdego materiału.

**Q: Czy Aspose.3D obsługuje .NET 6?**  
A: Tak, biblioteka jest w pełni kompatybilna z .NET 6 i nowszymi wersjami.

---

**Ostatnia aktualizacja:** 2026-01-17  
**Testowano z:** Aspose.3D 24.11 for .NET  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}