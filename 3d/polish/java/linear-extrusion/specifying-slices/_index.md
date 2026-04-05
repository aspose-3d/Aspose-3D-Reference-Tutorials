---
date: 2026-02-22
description: Dowiedz się, jak tworzyć wyciągnięcia 3D z przekrojami przy użyciu Aspose.3D
  dla Javy. Ten przewodnik krok po kroku obejmuje wyciąganie liniowe, ustawianie promienia
  zaokrąglenia oraz eksportowanie do formatu OBJ.
linktitle: Create 3D Extrusion with Slices – Aspose.3D for Java
second_title: Aspose.3D Java API
title: Tworzenie ekstruzji 3D z przekrojami – Aspose.3D dla Javy
url: /pl/java/linear-extrusion/specifying-slices/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Tworzenie ekstruzji 3D z warstwami – Aspose.3D dla Javy

## Introduction

Jeśli potrzebujesz **tworzyć ekstruzję 3D** obiekty, które wyglądają gładko i precyzyjnie, kluczowe jest kontrolowanie liczby warstw. W tym samouczku przeprowadzimy Cię przez określanie warstw podczas wykonywania liniowej ekstruzji przy użyciu Aspose.3D dla Javy. Zobaczysz, dlaczego liczba warstw ma znaczenie, jak ustawić promień zaokrąglenia oraz jak wyeksportować wynik jako plik OBJ, który można używać w dowolnym potoku 3D.

## Quick Answers
- **Co kontrolują „warstwy”?** Liczbę pośrednich przekrojów używanych do przybliżania powierzchni ekstruzji.  
- **Która metoda ustawia liczbę warstw?** `LinearExtrusion.setSlices(int)`  
- **Czy mogę zmienić promień zaokrąglenia profilu?** Tak, poprzez `RectangleShape.setRoundingRadius(double)`  
- **Jaki format pliku jest używany w tym przykładzie?** Wavefront OBJ (`FileFormat.WAVEFRONTOBJ`)  
- **Czy potrzebna jest licencja do uruchomienia kodu?** Darmowa wersja próbna wystarczy do oceny; licencja komercyjna jest wymagana w produkcji.

## What is a linear extrusion with slices?

Liniowa ekstruzja przyjmuje profil 2‑D (np. prostokąt) i rozciąga go wzdłuż prostej linii, tworząc bryłę 3‑D. Określając **warstwy**, informujesz Aspose.3D, ile pośrednich kroków ma wygenerować, co bezpośrednio wpływa na gładkość zakrzywionych krawędzi, takich jak zaokrąglony prostokąt.

## Why use Aspose.3D for Java to create 3d extrusion?

* **Pełna kontrola** – możesz programowo dostosować liczbę warstw, promień zaokrąglenia i format eksportu.  
* **Wieloplatformowość** – działa w każdym środowisku obsługującym Javę bez zależności natywnych.  
* **Elastyczność eksportu** – bezpośrednio zapisuje do OBJ, FBX, STL i wielu innych formatów.

## Prerequisites

1. **Java Development Kit** – zainstalowany JDK 8 lub nowszy.  
2. **Aspose.3D for Java** – pobierz bibliotekę z oficjalnej strony [tutaj](https://releases.aspose.com/3d/java/).  
3. IDE lub edytor tekstu według własnego wyboru.

## Import Packages

Add the Aspose.3D namespace to your project so you can access the 3‑D modeling classes.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## Step‑by‑Step Guide

### Step 1: Set up the scene and define the profile

Najpierw tworzymy `RectangleShape` i nadajemy mu **promień zaokrąglenia**, aby narożniki były gładkie. Następnie inicjalizujemy nową `Scene`, która będzie przechowywać całą geometrię.

```java
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
Scene scene = new Scene();
```

### Step 2: **Create child node** objects for each extrusion

Każdy element geometrii znajduje się pod `Node`. Tutaj generujemy dwa węzły‑bracia – jeden dla ekstruzji o niskiej liczbie warstw i drugi dla ekstruzji o wysokiej liczbie warstw – i przesuwamy lewy węzeł nieco na bok, aby wyniki były łatwe do porównania.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### Step 3: Perform linear extrusion and **set slices**

Teraz faktycznie **tworzymy obiekty ekstruzji 3D**. Konstruktor `LinearExtrusion` przyjmuje profil oraz głębokość ekstruzji. Korzystając z **anonimowej klasy wewnętrznej**, wywołujemy `setSlices`, aby kontrolować gładkość. Lewy węzeł otrzymuje tylko 2 warstwy (grubo), podczas gdy prawy węzeł otrzymuje 10 warstw (gładko).

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(2);}});
right.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(10);}});
```

### Step 4: **Export OBJ** – save the scene

Na koniec zapisujemy scenę do pliku Wavefront OBJ, formatu szeroko wspieranego przez edytory 3‑D i silniki gier. To demonstruje możliwość **export obj java** w Aspose.3D.

```java
scene.save(MyDir + "SlicesInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Common Issues and Solutions

| Problem | Dlaczego się pojawia | Rozwiązanie |
|---------|----------------------|-------------|
| **Ekstruzja wygląda płasko** | Liczba warstw ustawiona na 1 lub 0 | Upewnij się, że `setSlices` jest wywoływane z wartością ≥ 2. |
| **Zaokrąglone narożniki wyglądają ząbkowanie** | Promień zaokrąglenia zbyt mały w stosunku do liczby warstw | Zwiększ zarówno promień, jak i liczbę warstw, aby uzyskać gładsze krzywe. |
| **Plik nie został znaleziony przy zapisie** | `MyDir` wskazuje na nieistniejący folder | Utwórz katalog wcześniej lub użyj ścieżki bezwzględnej. |

## Frequently Asked Questions

**P: Jak mogę pobrać Aspose.3D dla Javy?**  
O: Bibliotekę możesz pobrać [tutaj](https://releases.aspose.com/3d/java/).

**P: Gdzie mogę znaleźć dokumentację Aspose.3D?**  
O: Dokumentację znajdziesz [tutaj](https://reference.aspose.com/3d/java/).

**P: Czy dostępna jest wersja próbna?**  
O: Tak, wersję próbną możesz wypróbować [tutaj](https://releases.aspose.com/).

**P: Jak mogę uzyskać wsparcie dla Aspose.3D?**  
O: Odwiedź forum wsparcia [tutaj](https://forum.aspose.com/c/3d/18).

**P: Czy mogę kupić tymczasową licencję?**  
O: Tak, tymczasową licencję można nabyć [tutaj](https://purchase.aspose.com/temporary-license/).

---

**Ostatnia aktualizacja:** 2026-02-22  
**Testowano z:** Aspose.3D for Java 24.11 (najnowsza w momencie pisania)  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}