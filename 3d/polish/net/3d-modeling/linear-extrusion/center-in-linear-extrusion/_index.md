---
date: 2026-01-07
description: Dowiedz się, jak dodać płaszczyznę podłoża podczas wykonywania ekstruzji
  liniowej przy użyciu Aspose.3D dla .NET i eksportować pliki Wavefront OBJ. Opanuj
  techniki centrowania i umieszczania w podłożu w modelowaniu 3‑D.
linktitle: Add Ground Plane and Center in Linear Extrusion
second_title: Aspose.3D .NET API
title: Dodaj płaszczyznę podłoża i środek w ekstruzji liniowej
url: /pl/net/3d-modeling/linear-extrusion/center-in-linear-extrusion/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Dodaj płaszczyznę podłoża i wyśrodkuj w ekstruzji liniowej

## Wprowadzenie

Witamy w tym kompleksowym przewodniku po opanowaniu ekstruzji liniowej przy użyciu Aspose.3D dla .NET. Jeśli chcesz **dodać płaszczyznę podłoża** do swoich modeli i **eksportować pliki Wavefront OBJ**, jednocześnie utrzymując ekstruzję wyśrodkowaną, jesteś we właściwym miejscu. W tym samouczku zagłębimy się w technikę ekstruzji liniowej, ze szczególnym uwzględnieniem aspektu wyśrodkowania oraz tego, jak płaszczyzna podłoża pomaga lepiej zwizualizować wynik.

## Szybkie odpowiedzi
- **Co osiąga „dodanie płaszczyzny podłoża”?** Zapewnia wizualne odniesienie, które ułatwia zobaczenie, gdzie ekstruzja znajduje się na płaszczyźnie X‑Z.  
- **Jakiego formatu użyto do eksportu modelu?** Scena jest zapisywana jako plik Wavefront OBJ (`FileFormat.WavefrontOBJ`).  
- **Czy potrzebna jest licencja do uruchomienia kodu?** Darmowa wersja próbna wystarcza do rozwoju; stała licencja jest wymagana w produkcji.  
- **Czy mogę zmienić długość ekstruzji?** Tak – zmodyfikuj drugi parametr `LinearExtrusion`.  
- **Czy wyśrodkowanie jest opcjonalne?** Ustawienie `Center = true` wyśrodkowuje ekstruzję wokół profilu; `false` ustawia ją po jednej stronie.

## Wymagania wstępne

Zanim wyruszymy w tę ekscytującą podróż, upewnij się, że masz spełnione następujące wymagania:

- Podstawowa znajomość języka programowania C#.  
- Zainstalowane Visual Studio na Twoim komputerze.  
- Biblioteka Aspose.3D dla .NET, którą możesz pobrać z [Aspose.3D .NET Documentation](https://reference.aspose.com/3d/net/).  
- Zapewnij dostęp do [Aspose.3D .NET Documentation](https://reference.aspose.com/3d/net/) jako odniesienia podczas całego samouczka.

## Importowanie przestrzeni nazw

Na początek zaimportujmy niezbędne przestrzenie nazw. Utworzą one fundament naszej mistrzowskiej pracy modelowania 3D.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Krok 1: Inicjalizacja profilu bazowego

Zaczynamy od zdefiniowania prostokątnego profilu, który zostanie wyekstruzowany. `RoundingRadius` dodaje subtelną zaokrąglenie narożników.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## Krok 2: Utworzenie sceny 3D

Obiekt `Scene` pełni rolę kontenera dla całej geometrii, świateł i kamer.

```csharp
Scene scene = new Scene();
```

## Krok 3: Utworzenie węzłów lewego i prawego

Dwa węzły rodzeństwa są tworzone pod korzeniem. Jeden pokaże ekstruzję **bez** wyśrodkowania, drugi **z** wyśrodkowaniem. Przesuwamy także lewy węzeł, aby dwa przykłady się nie nakładały.

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(5, 0, 0);
```

## Krok 4: Wykonanie ekstruzji liniowej na lewym węźle (bez wyśrodkowania)

Tutaj ekstruzujemy profil bez wyśrodkowania. Zwróć uwagę na flagę `Center = false`.

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 2) { Center = false, Slices = 3 });
```

## Krok 5: Dodanie płaszczyzny podłoża jako odniesienia (lewy węzeł)

Dodanie cienkiego pudełka pełni rolę **płaszczyzny podłoża**, dzięki czemu wyraźnie widać, jak ekstruzja leży na podstawie.

```csharp
left.CreateChildNode(new Box(0.01, 3, 3));
```

## Krok 6: Wykonanie ekstruzji liniowej na prawym węźle (z wyśrodkowaniem)

Teraz ekstruzujemy ten sam profil, ale włączamy wyśrodkowanie. Geometria zostanie symetrycznie rozmieszczona wokół początku profilu.

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 2) { Center = true, Slices = 3 });
```

## Krok 7: Dodanie płaszczyzny podłoża jako odniesienia (prawy węzeł)

Druga płaszczyzna podłoża jest dodawana do prawego węzła, aby zachować spójność wizualnego porównania.

```csharp
right.CreateChildNode(new Box(0.01, 3, 3));
```

## Krok 8: Eksport pliku Wavefront OBJ

Na koniec **eksportujemy Wavefront OBJ**, aby wynik mógł być otwarty w dowolnym standardowym przeglądarce 3‑D.

```csharp
scene.Save("Your Output Directory" + "CenterInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## Dlaczego dodawać płaszczyznę podłoża?

Dodanie płaszczyzny podłoża daje natychmiastową wskazówkę wizualną o wysokości i wyrównaniu ekstruzji. Jest to szczególnie pomocne, gdy trzeba porównać wyniki wyśrodkowane i nie‑wyśrodkowane, jak pokazano w tym samouczku.

## Typowe problemy i wskazówki

- **Płaszczyzna podłoża niewidoczna:** Upewnij się, że grubość płaszczyzny (`0.01` w konstruktorze `Box`) jest wystarczająco mała, aby nie zasłaniać ekstruzji, ale jednocześnie na tyle duża, aby była renderowana.  
- **Eksport nie powiódł się:** Sprawdź, czy katalog wyjściowy istnieje i masz uprawnienia do zapisu.  
- **Wyśrodkowana ekstruzja wydaje się przesunięta:** Ponownie sprawdź właściwość `Center`; `true` wyśrodkowuje profil, `false` ustawia go po jednej stronie.

## Najczęściej zadawane pytania

### Q1: Czy mogę używać Aspose.3D dla .NET w innych językach programowania?

A1: Aspose.3D głównie obsługuje języki .NET, takie jak C# i VB.NET.

### Q2: Gdzie mogę znaleźć wsparcie w sprawach związanych z Aspose.3D?

A2: Odwiedź [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) w celu uzyskania dedykowanego wsparcia i dyskusji.

### Q3: Czy dostępna jest darmowa wersja próbna Aspose.3D dla .NET?

A3: Tak, darmową wersję próbną znajdziesz [tutaj](https://releases.aspose.com/).

### Q4: Jak mogę uzyskać tymczasową licencję dla Aspose.3D dla .NET?

A4: Tymczasową licencję możesz nabyć [tutaj](https://purchase.aspose.com/temporary-license/).

### Q5: Gdzie mogę kupić licencję Aspose.3D dla .NET?

A5: Licencję możesz zakupić [tutaj](https://purchase.aspose.com/buy).

### Q6: Czy mogę eksportować scenę do innych formatów niż OBJ?

A6: Tak, Aspose.3D obsługuje wiele formatów, takich jak STL, FBX i GLTF. Wystarczy zmienić wartość enum `FileFormat` w metodzie `Save`.

### Q7: Jak zmienić liczbę przekrojów (slices) ekstruzji?

A7: Dostosuj właściwość `Slices` w konstruktorze `LinearExtrusion`, aby kontrolować gęstość siatki.

---

**Ostatnia aktualizacja:** 2026-01-07  
**Testowane z:** najnowsza wersja Aspose.3D dla .NET  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}