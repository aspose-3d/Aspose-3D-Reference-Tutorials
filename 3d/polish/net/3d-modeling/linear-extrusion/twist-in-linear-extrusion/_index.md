---
date: 2026-03-23
description: Dowiedz się, jak tworzyć wyciąg z obrotem przy użyciu Aspose.3D dla .NET.
  Ten przewodnik krok po kroku obejmuje techniki liniowego wyciągu z obrotem.
linktitle: Twist in Linear Extrusion
second_title: Aspose.3D .NET API
title: Jak stworzyć ekstruzję z obrotem w ekstruzji liniowej
url: /pl/net/3d-modeling/linear-extrusion/twist-in-linear-extrusion/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Jak stworzyć ekstruzję z obrotem w ekstruzji liniowej

## Wprowadzenie

Jeśli tworzysz aplikacje .NET, które potrzebują przyciągających wzrok wizualizacji 3D, szybko odkryjesz, że **jak stworzyć ekstruzję** jest podstawową umiejętnością. Aspose.3D for .NET zapewnia czyste, wysokowydajne API, które zamienia proste profile 2‑D w zaawansowane modele 3‑D — szczególnie gdy dodasz obrót. W tym samouczku przejdziemy krok po kroku, od przygotowania sceny po zapis końcowego pliku OBJ, abyś mógł zobaczyć moc efektu obrotu w ekstruzji liniowej w praktyce.

## Szybkie odpowiedzi
- **Jaka jest podstawowa klasa do ekstruzji?** `LinearExtrusion`
- **Która właściwość dodaje obrót?** `Twist`
- **Ile warstw (slices) zapewnia płynny wynik?** Około 100 warstw (dostosuj w razie potrzeby)
- **Czy mogę używać innych kształtów?** Tak, dowolny `IProfile`, np. koła, wielokąty lub własne krzywe
- **Jakiego formatu pliku użyto w przykładzie?** Wavefront OBJ (`.obj`)

## Wymagania wstępne

Zanim zaczniemy, upewnij się, że masz następujące elementy:

- Aspose.3D for .NET zainstalowane. Jeśli jeszcze go nie pobrałeś, pobierz **[tutaj](https://releases.aspose.com/3d/net/)**.
- Działające środowisko programistyczne .NET (Visual Studio, VS Code lub dowolne inne IDE).
- Podstawową znajomość składni C# oraz koncepcji programowania obiektowego.

## Importowanie przestrzeni nazw

W każdym projekcie .NET prawidłowe użycie przestrzeni nazw jest kluczowe. Zacznij od zaimportowania niezbędnych przestrzeni nazw, aby w pełni wykorzystać możliwości Aspose.3D. Oto fragment kodu, który Cię poprowadzi:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Przewodnik krok po kroku

### Krok 1: Inicjalizacja profilu bazowego

Zaczynamy od zdefiniowania kształtu, który zostanie wyekstruzowany. W tym przykładzie używamy prostokąta z małym promieniem zaokrąglenia, aby krawędzie miały delikatną krzywiznę.

```csharp
// Initialize the base profile to be extruded
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

### Krok 2: Utworzenie sceny 3D

Obiekt `Scene` działa jak płótno, na którym żyją wszystkie elementy 3‑D. Pomyśl o nim jako o scenie dla Twojej ekstruzji.

```csharp
// Create a scene 
Scene scene = new Scene();
```

### Krok 3: Dodanie węzłów lewego i prawego

Węzły pozwalają organizować obiekty hierarchicznie. Utworzymy dwa węzły‑rodzeń — jeden dla prostej ekstruzji, a drugi dla wersji z obrotem.

```csharp
// Create left node
var left = scene.RootNode.CreateChildNode();
// Create right node
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(15, 0, 0);
```

### Krok 4: Wykonanie ekstruzji liniowej z obrotem w lewym węźle

Właściwość `Twist` kontroluje, o ile profil obraca się podczas ekstruzji. Ustawienie jej na **0** daje klasyczną prostą ekstruzję.

```csharp
// Twist property defines the degree of the rotation while extruding the profile
// Perform linear extrusion on the left node using twist and slices property
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 0, Slices = 100 });
```

### Krok 5: Wykonanie ekstruzji liniowej z obrotem w prawym węźle

Teraz stosujemy obrót o 90 stopni do tego samego profilu. To wyraźnie pokazuje efekt **obrotu w ekstruzji liniowej**.

```csharp
// Perform linear extrusion on the right node using twist and slices property
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 90, Slices = 100 });
```

### Krok 6: Zapis sceny 3D

Na koniec eksportujemy scenę do formatu, który można otworzyć w dowolnym przeglądarce 3‑D. Przykład używa Wavefront OBJ, ale Aspose.3D obsługuje także wiele innych formatów.

```csharp
// Save 3D scene
scene.Save("Your Output Directory" + "TwistInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## Dlaczego warto używać ekstruzji liniowej z obrotem?

- **Szybkie prototypowanie:** Przekształć szkice 2‑D w części 3‑D bez ręcznego modelowania.
- **Elastyczność projektowania:** Reguluj wartość `Twist`, aby tworzyć spirale, żebrowane elementy helikalne lub ozdobne detale.
- **Przyjazna wydajność:** Parametr `Slices` pozwala zbalansować jakość wizualną i szybkość działania.

## Typowe problemy i wskazówki

- **Zbyt wiele warstw:** Choć 100 warstw wygląda płynnie, bardzo wysokie wartości mogą spowolnić renderowanie. Testuj mniejsze liczby, jeśli wydajność stanie się problemem.
- **Ujemne wartości obrotu:** Ujemny `Twist` obraca w przeciwnym kierunku — przydatne przy projektach lustrzanych.
- **Ścieżki plików:** Upewnij się, że katalog wyjściowy istnieje i masz uprawnienia do zapisu; w przeciwnym razie `scene.Save` zgłosi wyjątek.

## Zakończenie

W tym samouczku pokazaliśmy **jak stworzyć ekstruzję** z obrotem przy użyciu Aspose.3D for .NET. Regulując właściwości `Twist` i `Slices`, możesz generować szeroką gamę kształtów, od prostych skręconych prętów po złożone struktury helikalne, przy użyciu zaledwie kilku linii kodu.

## Najczęściej zadawane pytania

**P: Czy mogę zastosować ekstruzję liniową z obrotem do innych kształtów?**  
O: Oczywiście! Każda klasa implementująca `IProfile` — np. `CircleShape`, `PolygonShape` lub własna krzywa — może być wyekstruzowana z obrotem.

**P: Co właściwie reprezentuje właściwość `Twist`?**  
O: Określa całkowity kąt obrotu (w stopniach) zastosowany do profilu wzdłuż długości ekstruzji.

**P: Czy zwiększenie liczby warstw wpływa na zużycie pamięci?**  
O: Tak, więcej warstw generuje więcej wierzchołków i ścian, co zwiększa zużycie pamięci i może obniżyć wydajność na słabszych urządzeniach.

**P: Czy mogę łączyć ekstruzję liniową z innymi funkcjami Aspose.3D?**  
O: Zdecydowanie. Po ekstruzji możesz dodać materiały, tekstury lub nawet operacje Boolean, aby stworzyć jeszcze bogatsze modele.

**P: Gdzie mogę uzyskać pomoc lub dyskutować pomysły z innymi programistami?**  
O: Dołącz do społeczności Aspose.3D na **[Aspose Forum](https://forum.aspose.com/c/3d/18)**, gdzie znajdziesz wsparcie, przykłady i dyskusje.

---

**Ostatnia aktualizacja:** 2026-03-23  
**Testowano z:** Aspose.3D 24.11 for .NET  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}