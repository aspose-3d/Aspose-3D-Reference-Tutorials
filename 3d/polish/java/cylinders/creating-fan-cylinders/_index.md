---
date: 2025-12-09
description: Dowiedz się, jak dodać węzeł potomny, pozycjonować obiekty 3D i zapisać
  scenę jako OBJ, tworząc własne cylindry wentylatorowe przy użyciu Aspose.3D dla
  Javy.
language: pl
linktitle: Adding Child Node for Fan Cylinders with Aspose.3D Java
second_title: Aspose.3D Java API
title: Dodaj węzeł podrzędny, aby zbudować cylindry wachlarzowe przy użyciu Aspose.3D
  dla Javy
url: /java/cylinders/creating-fan-cylinders/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Dodaj węzeł potomny, aby zbudować cylindry wentylatora z Aspose.3D dla Javy

## Wprowadzenie

Gotowy, aby **dodać węzeł potomny** do sceny 3‑D i stworzyć przyciągające uwagę cylindry wentylatora? W tym samouczku przeprowadzimy Cię przez każdy krok — od przygotowania sceny, po pozycjonowanie obiektów 3D, aż po **zapisanie sceny jako OBJ** — przy użyciu Aspose.3D dla Javy. Niezależnie od tego, czy dopracowujesz zasób gry, czy tworzysz szybki prototyp, przedstawione koncepcje zapewnią Ci solidną kontrolę nad modelami 3‑D.

## Szybkie odpowiedzi
- **Co robi „add child node”?** Wstawia nowy obiekt do grafu sceny, dziedzicząc transformacje od swojego rodzica.  
- **Jak mogę pozycjonować obiekt 3D?** Poprzez zastosowanie translacji (lub rotacji/skali) do transformacji węzła.  
- **Jaki format pliku jest używany do eksportu?** Przykład zapisuje model jako plik Wavefront OBJ.  
- **Czy potrzebna jest licencja do uruchomienia kodu?** Darmowa wersja próbna wystarcza do oceny; licencja jest wymagana w produkcji.  
- **Jakie IDE jest najlepsze?** Dowolne IDE Java (IntelliJ IDEA, Eclipse, VS Code), które obsługuje JDK 8+.

## Czym jest „add child node” w Aspose.3D?
Dodanie węzła potomnego oznacza utworzenie nowego węzła pod istniejącym rodzicem w hierarchii sceny. Dziecko dziedziczy układ współrzędnych rodzica, co ułatwia **pozycjonowanie obiektów 3d** względem siebie.

## Dlaczego dodawać węzeł potomny przy budowie cylindrów wentylatora?
- **Projekt modularny:** Każdy cylinder (wentylatorowy lub nie‑wentylatorowy) znajduje się w własnym węźle, co upraszcza późniejsze edycje.  
- **Dziedziczenie transformacji:** Przesuwanie, obracanie lub skalowanie rodzica powoduje automatyczne zastosowanie tych zmian do wszystkich dzieci.  
- **Czystszy graf sceny:** Zwiększa czytelność i ułatwia debugowanie złożonych modeli.

## Wymagania wstępne

- **Java Development Kit (JDK)** – pobierz ze [strony oficjalnej](https://www.oracle.com/java/technologies/javase-downloads.html).  
- **Aspose.3D for Java** – pobierz najnowszą bibliotekę z [linku do pobrania](https://releases.aspose.com/3d/java/).

## Importowanie pakietów

Rozpocznij od zaimportowania niezbędnych pakietów do swojego projektu Java. Ten krok jest kluczowy, aby uzyskać dostęp do funkcjonalności udostępnianych przez Aspose.3D.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Krok 1: Utwórz scenę

Najpierw tworzymy pustą scenę 3‑D, która będzie hostować wszystkie nasze obiekty.

```java
// ExStart:2
// Create a Scene
Scene scene = new Scene();
// ExEnd:2
```

## Krok 2: Utwórz cylinder wentylatora

Następnie budujemy cylinder, który zostanie wyrenderowany jako wentylator (częściowy zakres).

```java
// ExStart:3
// Create a cylinder with fan
Cylinder fan = new Cylinder(2, 2, 10, 20, 1, false);
fan.setGenerateFanCylinder(true);
fan.setThetaLength(MathUtils.toRadian(270.0));
// ExEnd:3
```

## Krok 3: Dodaj węzeł potomny i pozycjonuj obiekt 3D

Teraz **dodajemy węzeł potomny** do sceny i **pozycjonujemy obiekt 3d**, ustawiając jego translację. To właśnie w tym miejscu cylinder wentylatora staje się częścią grafu sceny.

```java
// ExStart:4
// Create ChildNode and set translation
scene.getRootNode().createChildNode(fan).getTransform().setTranslation(10, 0, 0);
// ExEnd:4
```

## Krok 4: Utwórz cylinder nie‑wentylatorowy

Aby pokazać elastyczność Aspose.3D, tworzymy również zwykły cylinder bez wentylatora i dodajemy go jako kolejny węzeł potomny.

```java
// ExStart:5
// Create a cylinder without a fan
Cylinder nonfan = new Cylinder(2, 2, 10, 20, 1, false);
// Create ChildNode
scene.getRootNode().createChildNode(nonfan);
// ExEnd:5
```

## Krok 5: Zapisz scenę jako OBJ

Na koniec **zapisujemy scenę jako OBJ**, abyś mógł obejrzeć wynik w dowolnym standardowym przeglądarce 3‑D.

```java
// ExStart:6
// Save scene
scene.save("Your Document Directory" + "CreateFanCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

Gratulacje! Pomyślnie **dodałeś węzeł potomny**, pozycjonowałeś swoje obiekty i wyeksportowałeś model.

## Typowe problemy i wskazówki

| Problem | Rozwiązanie |
|-------|----------|
| **Plik nie znaleziony** podczas zapisywania | Upewnij się, że docelowy katalog istnieje i masz uprawnienia do zapisu. |
| **Cylinder wygląda na spłaszczony** | Sprawdź wartości promienia i wysokości; Aspose.3D oczekuje jednostek w tej samej skali. |
| **Fragment wentylatora wygląda niekompletnie** | Dostosuj `ThetaLength` (w radianach), aby objąć żądany kąt. |
| **Scena nie jest widoczna w przeglądarce** | Upewnij się, że plik OBJ został zapisany wraz z towarzyszącym plikiem `.mtl` (materiał), jeśli jest potrzebny. |

## Najczęściej zadawane pytania

**Q:** *Czy Aspose.3D jest kompatybilny z innymi bibliotekami Java do modelowania 3D?*  
**A:** Tak, Aspose.3D działa obok innych bibliotek Java 3‑D, umożliwiając łączenie funkcji w razie potrzeby.

**Q:** *Czy mogę dalej dostosować wygląd wygenerowanych cylindrów wentylatora?*  
**A:** Oczywiście. Możesz zastosować materiały, tekstury i oświetlenie przy użyciu klas `Material` i `Light`.

**Q:** *Gdzie mogę znaleźć dodatkowe wsparcie lub pomoc dla Aspose.3D?*  
**A:** Odwiedź [forum Aspose.3D](https://forum.aspose.com/c/3d/18) po pomoc społeczności i oficjalne odpowiedzi.

**Q:** *Czy dostępna jest darmowa wersja próbna Aspose.3D?*  
**A:** Tak, możesz wypróbować Aspose.3D za pomocą [darmowej wersji próbnej](https://releases.aspose.com/) przed zakupem.

**Q:** *Jak mogę uzyskać tymczasową licencję dla Aspose.3D?*  
**A:** Uzyskaj tymczasową licencję [tutaj](https://purchase.aspose.com/temporary-license/) do testów i rozwoju.

## Podsumowanie

W tym przewodniku pokazaliśmy, jak **dodać węzeł potomny**, **pozycjonować obiekt 3d** oraz **zapisać scenę jako OBJ**, tworząc jednocześnie spersonalizowane cylindry wentylatora przy użyciu Aspose.3D dla Javy. Te elementy budulcowe dają Ci elastyczność w konstruowaniu złożonych hierarchii 3‑D i ich eksportowaniu do dowolnego dalszego przepływu pracy.

---

**Ostatnia aktualizacja:** 2025-12-09  
**Testowano z:** Aspose.3D 24.12 dla Javy  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}