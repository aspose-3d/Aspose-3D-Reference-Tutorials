---
date: 2026-02-09
description: Dowiedz się, jak eksportować FBX i dodać siatkę do węzła, tworząc jednocześnie
  węzły potomne w Javie przy użyciu Aspose.3D.
linktitle: Build Node Hierarchies in 3D Scenes with Java and Aspose.3D
second_title: Aspose.3D Java API
title: Jak eksportować FBX i tworzyć hierarchie węzłów w Javie
url: /pl/java/geometry/build-node-hierarchies/
weight: 16
---

.

Now produce final answer.{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Jak wyeksportować FBX i zbudować hierarchie węzłów w Javie z Aspose.3D

## Wstęp

Jeśli szukasz przejrzystego, krok po kroku przewodnika **jak wyeksportować FBX** z aplikacji Java, jesteś we właściwym miejscu. W tym tutorialu pokażemy, jak zbudować hierarchie węzłów, **dodać siatkę do węzła**, i w końcu zapisać scenę jako plik FBX przy użyciu Aspose.3D Java API. Niezależnie od tego, czy tworzysz prosty prototyp, czy gotowy do produkcji silnik 3D, te techniki dają pełną kontrolę nad grafem sceny.

## Szybkie odpowiedzi
- **Jaki jest główny cel tego tutorialu?** Demonstracja, jak wyeksportować FBX po zbudowaniu hierarchii węzłów.  
- **Jakiej biblioteki użyto?** Aspose.3D for Java.  
- **Czy potrzebna jest licencja?** Darmowa wersja próbna wystarczy do rozwoju; licencja komercyjna jest wymagana w produkcji.  
- **Jaki format pliku jest generowany?** FBX (ASCII 7500).  
- **Czy mogę dostosować przekształcenia węzłów?** Tak – translacja, rotacja i skalowanie są w pełni obsługiwane.

## Co oznacza „jak wyeksportować FBX” w kontekście Aspose.3D?
Eksportowanie FBX oznacza konwersję grafu sceny w pamięci, który budujesz przy pomocy Aspose.3D, do pliku FBX, który można otworzyć w popularnych narzędziach 3D, takich jak Blender, Maya czy Unity. API zajmuje się ciężką pracą, pozwalając Ci skupić się na tworzeniu sceny.

## Dlaczego budować hierarchie węzłów przed eksportem?
Dobrze ustrukturyzowana hierarchia węzłów pozwala zastosować przekształcenia raz na węźle rodzicu, automatycznie wpływając na wszystkie jego dzieci. Redukuje to duplikację kodu i odzwierciedla rzeczywiste relacje obiektów (np. podwozie samochodu z kołami jako węzłami potomnymi).

## Wymagania wstępne

Zanim przejdziesz dalej, upewnij się, że masz:

1. **Środowisko programistyczne Java** – JDK 8+ oraz IDE lub narzędzie do budowania według własnego wyboru.  
2. **Aspose.3D for Java Library** – Pobierz i zainstaluj bibliotekę ze [strony pobierania](https://releases.aspose.com/3d/java/).  
3. **Katalog dokumentów** – Folder na Twoim komputerze, w którym zostanie zapisany wygenerowany plik FBX.

## Importowanie pakietów

Rozpocznij od zaimportowania niezbędnych klas Aspose.3D:

```java
import com.aspose.threed.*;

```

## Krok 1: Inicjalizacja obiektu Scene

```java
// Initialize scene object
Scene scene = new Scene();
```

## Krok 2: Tworzenie węzłów potomnych i dodawanie siatki do węzła

W tym kroku demonstrujemy **jak tworzyć węzły potomne** oraz **dodawać siatkę do obiektów węzła**.

```java
// Get a child node object
Node top = scene.getRootNode().createChildNode();

// Create the first cube node
Node cube1 = top.createChildNode("cube1");
Mesh mesh = Common.createMeshUsingPolygonBuilder(); // Use your mesh creation method
cube1.setEntity(mesh);
cube1.getTransform().setTranslation(new Vector3(-10, 0, 0));

// Create the second cube node
Node cube2 = top.createChildNode("cube2");
cube2.setEntity(mesh);
cube2.getTransform().setTranslation(new Vector3(10, 0, 0));
```

## Krok 3: Zastosowanie rotacji do węzła nadrzędnego

Obracanie węzła rodzica automatycznie obraca wszystkie jego dzieci, co jest kluczową zaletą scen hierarchicznych.

```java
// Rotate the top node, affecting all child nodes
top.getTransform().setRotation(Quaternion.fromEulerAngle(Math.PI, 4, 0));
```

## Krok 4: Zapis sceny 3D – Jak wyeksportować FBX

Teraz **zapisujemy scenę jako FBX**, kończąc przepływ pracy „jak wyeksportować FBX”.

```java
// Save 3D scene in the supported file format (FBX in this case)
String MyDir = "Your Document Directory";
MyDir = MyDir + "NodeHierarchy.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
System.out.println("\nNode hierarchy added successfully to document.\nFile saved at " + MyDir);
```

### Oczekiwany rezultat
Uruchomienie kodu tworzy plik o nazwie **NodeHierarchy.fbx** w określonym katalogu. Otwórz go w dowolnym przeglądarce obsługującej FBX, aby zobaczyć dwa sześciany umieszczone po lewej i prawej stronie centralnego punktu obrotu, wszystkie obracające się razem.

## Typowe problemy i rozwiązania

| Problem | Dlaczego się pojawia | Rozwiązanie |
|-------|----------------|-----|
| **Błąd „File not found”** przy zapisie | Ścieżka `MyDir` jest niepoprawna lub brakuje końcowego separatora | Upewnij się, że katalog istnieje i kończy się separatorem pliku (`/` lub `\\`). |
| **Siatka niewidoczna** po eksporcie | Nie przypisano encji siatki lub translacja przeniosła ją poza widok | Sprawdź `cube1.setEntity(mesh)` i zweryfikuj wartości translacji. |
| **Rotacja wygląda niepoprawnie** | Nieprawidłowe użycie radianów zamiast stopni | `Quaternion.fromEulerAngle` oczekuje radianów; dostosuj wartości odpowiednio. |

## Najczęściej zadawane pytania

**P: Czy Aspose.3D for Java jest odpowiedni dla początkujących?**  
O: Zdecydowanie! API zostało zaprojektowane z czystym, obiektowo‑zorientowanym podejściem, które ułatwia naukę, nawet jeśli dopiero zaczynasz przygodę z programowaniem 3D.

**P: Czy mogę używać Aspose.3D for Java w projektach komercyjnych?**  
O: Tak. Odwiedź [stronę zakupu](https://purchase.aspose.com/buy), aby uzyskać szczegóły licencjonowania.

**P: Jak mogę uzyskać wsparcie dla Aspose.3D for Java?**  
O: Dołącz do [forum Aspose.3D](https://forum.aspose.com/c/3d/18), aby uzyskać pomoc od społeczności i zespołu wsparcia Aspose.

**P: Czy dostępna jest darmowa wersja próbna?**  
O: Oczywiście! Wypróbuj funkcje za pomocą [darmowej wersji próbnej](https://releases.aspose.com/) przed podjęciem decyzji.

**P: Gdzie mogę znaleźć dokumentację?**  
O: Zapoznaj się z [dokumentacją](https://reference.aspose.com/3d/java/) poświęconą Aspose.3D for Java.

## Podsumowanie

Opanowanie **jak wyeksportować FBX**, budowanie hierarchii węzłów oraz **dodawanie siatki do węzła** to kluczowe kroki w kierunku tworzenia zaawansowanych aplikacji 3D w Javie. Dzięki Aspose.3D otrzymujesz potężne, przyjazne licencjonowaniu rozwiązanie, które abstrahuje szczegóły niskiego poziomu, jednocześnie dając pełną kontrolę nad grafem sceny. Eksperymentuj z różnymi siatkami, przekształceniami i formatami eksportu, aby odblokować jeszcze więcej możliwości.

---

**Ostatnia aktualizacja:** 2026-02-09  
**Testowano z:** Aspose.3D for Java 24.11  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}