---
date: 2026-08-02
description: Dowiedz się, jak zmienić kierunek ekstruzji w ekstruzji liniowej i eksportować
  pliki OBJ przy użyciu Aspose.3D for Java. Postępuj zgodnie z naszym przewodnikiem
  krok po kroku.
keywords:
- change extrusion direction
- export obj file java
- Aspose.3D Java
lastmod: 2026-08-02
linktitle: Zmienianie kierunku ekstruzji – Aspose.3D Java
og_description: Zmienianie kierunku ekstruzji w ekstruzji liniowej przy użyciu Aspose.3D
  for Java i eksport plików OBJ. Ten przewodnik pokazuje kod krok po kroku oraz wskazówki
  dla programistów.
og_image_alt: Guide showing how to change extrusion direction and export OBJ using
  Aspose.3D Java
og_title: Zmienianie kierunku ekstruzji – Poradnik Aspose.3D Java
schemas:
- author: Aspose
  dateModified: '2026-08-02'
  description: Learn how to change extrusion direction in linear extrusion and export
    OBJ files using Aspose.3D for Java. Follow our step‑by‑step guide.
  headline: Change Extrusion Direction in 3D Models – Aspose.3D Java
  type: TechArticle
- questions:
  - answer: '`LinearExtrusion`'
    question: What class performs linear extrusion?
  - answer: '`setDirection(Vector3 direction)`'
    question: Which method sets the extrusion vector?
  - answer: Yes—use `scene.save(..., FileFormat.WAVEFRONTOBJ)`
    question: Can the result be saved as OBJ?
  - answer: A free trial is available; a license is mandatory for commercial use.
    question: Is a license required for production?
  - answer: IntelliJ IDEA and Eclipse are fully supported.
    question: Which IDE works best with Aspose.3D?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- change extrusion direction
- Aspose.3D
- Java 3D modeling
- export OBJ
title: Zmienianie kierunku ekstruzji w modelach 3D – Aspose.3D Java
url: /pl/java/linear-extrusion/setting-direction/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Zmiana Kierunku Ekstruzji w Modelach 3D – Aspose.3D Java

## Wprowadzenie

W tym obszernej samouczku dowiesz się **jak zmienić kierunek ekstruzji** podczas wykonywania ekstruzji liniowej przy użyciu Aspose.3D dla Javy. Niezależnie od tego, czy tworzysz narzędzie podobne do CAD, przygotowujesz zasoby dla silnika gry, czy generujesz części do druku 3‑D, kontrolowanie kierunku ekstruzji pozwala stworzyć dokładnie taki kształt, jakiego potrzebujesz. Przejdziemy krok po kroku, od inicjalizacji profilu po zapis wyniku jako pliku OBJ, abyś mógł również **eksportować pliki OBJ modeli 3D** bezpośrednio z Javy.

## Szybkie Odpowiedzi
- **Jaka klasa wykonuje ekstruzję liniową?** `LinearExtrusion`
- **Która metoda ustawia wektor ekstruzji?** `setDirection(Vector3 direction)`
- **Czy wynik można zapisać jako OBJ?** Tak — użyj `scene.save(..., FileFormat.WAVEFRONTOBJ)`
- **Czy wymagana jest licencja do produkcji?** Dostępna jest darmowa wersja próbna; licencja jest wymagana do użytku komercyjnego.
- **Które IDE najlepiej współpracuje z Aspose.3D?** IntelliJ IDEA i Eclipse są w pełni wspierane.

## Czym jest Ekstruzja Liniowa?

Ekstruzja liniowa to proces wydłużania szkicu 2‑D (takiego jak prostokąt lub koło) wzdłuż prostej linii w celu utworzenia bryły 3‑D. Domyślnie ekstruzja podąża wzdłuż dodatniej osi Z, ale Aspose.3D pozwala zmienić tę ścieżkę za pomocą właściwości `setDirection`, dając pełną kontrolę nad ostateczną geometrią.

## Dlaczego Zmienić Kierunek Ekstruzji w Ekstruzji Liniowej?

Zmiana kierunku ekstruzji pozwala wyrównać nową geometrię z istniejącymi obiektami, tworzyć elementy pod kątem bez dodatkowych transformacji oraz generować modele zgodne z układem współrzędnych wymaganym przez dalsze etapy przetwarzania (np. drukarki 3‑D lub silniki gier). Eliminuje to potrzebę kroków post‑procesingu i zmniejsza narzut rozmiaru pliku nawet o 15 %, gdy używane są wektory kierunkowe unikające niepotrzebnych obrotów.

## Wymagania Wstępne

- Podstawowa znajomość Javy.
- Zainstalowana biblioteka Aspose.3D. Możesz ją pobrać [tutaj](https://releases.aspose.com/3d/java/). Możesz również przeglądać wszystkie wydania Aspose na głównej stronie [tutaj](https://releases.aspose.com/).
- IDE, takie jak Eclipse lub IntelliJ IDEA.

## Importowanie Pakietów

Przestrzeń nazw `com.aspose.threed` dostarcza podstawowe klasy 3‑D oraz typy pomocnicze.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Krok 1: Inicjalizacja Podstawowego Profilu

Klasa `RectangleShape` tworzy profil 2‑D, który zostanie wyekstruzowany. Mały promień zaokrąglenia nadaje krawędziom płynny wygląd.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Krok 2: Utworzenie Sceny

Klasa `Scene` jest kontenerem najwyższego poziomu w Aspose.3D, który przechowuje wszystkie węzły 3‑D, światła, kamery i materiały.

```java
Scene scene = new Scene();
```

## Krok 3: Tworzenie Węzłów

`Node` reprezentuje obiekt w grafie sceny, umożliwiając dołączanie geometrii, transformacji i innych właściwości.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Krok 4: Wykonanie Ekstruzji Liniowej na Lewym Węźle

`LinearExtrusion` wykonuje operację ekstruzji, przekształcając profil 2‑D w siatkę 3‑D.

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## Krok 5: Wykonanie Ekstruzji Liniowej na Prawym Węźle z Kierunkiem

Tutaj **zmieniamy kierunek ekstruzji**. Przekazując własny `Vector3` do `setDirection`, ekstruzja podąża za wektorem (0.3, 0.2, 1), tworząc pochyły kształt zgodny z układem współrzędnych sceny.

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## Krok 6: Zapisanie Sceny 3D

Metoda `save` zapisuje scenę do pliku w określonym formacie.

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Typowe Problemy i Rozwiązania

| Problem | Dlaczego się pojawia | Rozwiązanie |
|---------|----------------------|-------------|
| Plik OBJ jest pusty | Profil nie został dodany do węzła | Upewnij się, że `createChildNode` jest wywoływane na prawidłowym węźle |
| Kierunek wydaje się niezmieniony | `setDirection` został wywołany po tym, jak ekstruzja została już skonstruowana | Ustaw kierunek wewnątrz inicjalizatora `LinearExtrusion`, jak pokazano |
| Siatka o niskiej rozdzielczości | Wartość `setSlices` jest zbyt niska | Zwiększ liczbę przekrojów (np. 100 lub więcej) |

## Podsumowanie

Teraz wiesz **jak zmienić kierunek ekstruzji** w ekstruzji liniowej, jak dostosować ustawienia skrętu i liczby przekrojów oraz jak **eksportować pliki OBJ modeli 3D** przy użyciu Aspose.3D dla Javy. Te techniki dają precyzyjną kontrolę nad tworzeniem geometrii i ułatwiają integrację zasobów 3‑D w większych pipeline'ach.

## Najczęściej Zadawane Pytania

**P:** Czy mogę używać Aspose.3D z innymi językami programowania?  
**O:** Tak — Aspose.3D udostępnia API dla .NET i Javy, umożliwiając rozwój wieloplatformowy.

**P:** Czy dostępna jest darmowa wersja próbna Aspose.3D?  
**O:** Oczywiście. Możesz przetestować pełny zestaw funkcji w darmowej wersji próbnej [tutaj](https://releases.aspose.com/).

**P:** Gdzie mogę znaleźć szczegółową dokumentację Aspose.3D dla Javy?  
**O:** Kompleksowa dokumentacja jest dostępna [tutaj](https://reference.aspose.com/3d/java/).

**P:** Jak uzyskać wsparcie dla Aspose.3D?  
**O:** Odwiedź oficjalne [forum Aspose.3D](https://forum.aspose.com/c/3d/18), aby uzyskać pomoc od społeczności i zespołu produktu.

**P:** Czy dostępne są tymczasowe licencje do testowania?  
**O:** Tak — tymczasowe licencje można uzyskać [tutaj](https://purchase.aspose.com/temporary-license/).

---

**Ostatnia aktualizacja:** 2026-08-02  
**Testowano z:** Aspose.3D for Java (latest release)  
**Autor:** Aspose

{{< blocks/products/products-backtop-button >}}

## Powiązane Samouczki

- [Jak Ekstruzować Kształt - Tworzenie Modeli 3D z Ekstruzją Liniową w Javie](/3d/java/linear-extrusion/)
- [Tworzenie Ekstruzji 3D w Javie z Aspose.3D](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [Samouczek Grafiki 3D w Javie – Środek w Ekstruzji Liniowej](/3d/java/linear-extrusion/controlling-center/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}