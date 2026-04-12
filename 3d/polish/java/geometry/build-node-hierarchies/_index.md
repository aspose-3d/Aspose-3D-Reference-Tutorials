---
date: 2026-04-12
description: Dowiedz się, jak tworzyć węzły potomne, dodawać siatkę do węzła i eksportować
  FBX przy użyciu Aspose.3D Java API do solidnych grafów scen 3D.
keywords:
- create child nodes
- how to export fbx
- add mesh to node
- java 3d scene graph
- save scene fbx
linktitle: Tworzenie hierarchii węzłów w scenach 3D przy użyciu Javy i Aspose.3D
second_title: Aspose.3D Java API
title: Tworzenie węzłów potomnych i eksportowanie FBX w Javie z Aspose.3D
url: /pl/java/geometry/build-node-hierarchies/
weight: 16
---

{{< blocks/products/pf/main-wrap-class >}}  
{{< blocks/products/pf/main-container >}}  
{{< blocks/products/pf/tutorial-page-section >}}  

# Jak wyeksportować FBX i zbudować hierarchie węzłów w Javie z Aspose.3D  

## Wprowadzenie  

Jeśli szukasz przejrzystego przewodnika krok po kroku dotyczącego **create child nodes**, **add mesh to node** oraz **how to export FBX** w aplikacji Java, jesteś we właściwym miejscu. W tym samouczku przeprowadzimy Cię przez budowanie **java 3d scene graph**, dołączanie siatek, stosowanie transformacji i w końcu zapisywanie sceny jako pliku FBX przy użyciu Aspose.3D Java API. Niezależnie od tego, czy tworzysz prostą demonstrację, czy projektujesz gotowy do produkcji silnik 3D, opanowanie tych koncepcji daje pełną kontrolę nad hierarchią sceny i procesem eksportu.  

## Szybkie odpowiedzi  
- **Jaki jest główny cel tego samouczka?** Demonstrating how to **create child nodes**, attach meshes, and **export FBX** after building a node hierarchy.  
- **Jakiej biblioteki użyto?** Aspose.3D for Java.  
- **Czy potrzebna jest licencja?** A free trial works for development; a commercial license is required for production.  
- **Jaki format pliku jest generowany?** FBX (ASCII 7500).  
- **Czy mogę dostosować transformacje węzłów?** Yes – translation, rotation, and scaling are all supported.  

## Co oznacza „create child nodes” w kontekście Aspose.3D?  

Tworzenie węzłów potomnych oznacza dodawanie podległych obiektów `Node` do węzła nadrzędnego w grafie sceny. Ta hierarchiczna struktura pozwala zastosować transformację raz na poziomie rodzica i automatycznie wpływać na wszystkie jego dzieci, co jest niezbędne dla realistycznych relacji obiektów, takich jak podwozie samochodu z obracającymi się kołami.  

## Dlaczego budować hierarchie węzłów przed eksportem?  

Dobrze ustrukturyzowana hierarchia redukuje duplikację kodu, upraszcza animację i odzwierciedla rzeczywiste relacje. Gdy później **convert scene fbx** (lub inny format), hierarchia jest zachowana, dzięki czemu narzędzia takie jak Blender, Maya czy Unity rozumieją relacje rodzic‑dziecko dokładnie tak, jak je zaprojektowałeś.  

## Typowe przypadki użycia hierarchii węzłów  

| Przypadek użycia | Dlaczego hierarchia pomaga | Typowy rezultat |
|------------------|----------------------------|-----------------|
| **Złożenia mechaniczne** (np. ramię robota) | Obrót węzła bazowego przesuwa wszystkie podłączone segmenty | Łatwa animacja złożonych mechanizmów |
| **Rigowanie postaci** | Kości szkieletu są węzłami potomnymi korzenia | Spójne transformacje pozy |
| **Organizacja sceny** | Grupowanie statycznych rekwizytów pod węzłem „props” | Czystsze zarządzanie sceną i selektywny eksport |
| **Przełączanie poziomu szczegółowości (LOD)** | Węzeł nadrzędny przełącza widoczność siatek potomnych | Zoptymalizowane renderowanie dla różnych urządzeń |

## Wymagania wstępne  

1. **Środowisko programistyczne Java** – JDK 8+ oraz wybrane IDE lub narzędzie budujące.  
2. **Biblioteka Aspose.3D for Java** – Pobierz i zainstaluj bibliotekę ze [strony pobierania](https://releases.aspose.com/3d/java/).  
3. **Katalog dokumentów** – Folder na twoim komputerze, w którym zostanie zapisany wygenerowany plik FBX.  

## Importowanie pakietów  

Rozpocznij od zaimportowania niezbędnych klas Aspose.3D:  

```java
import com.aspose.threed.*;
```  

## Krok 1: Inicjalizacja obiektu sceny  

```java
// Initialize scene object
Scene scene = new Scene();
```  

## Krok 2: Tworzenie węzłów potomnych i dodawanie siatki do węzła  

W tym kroku demonstrujemy **how to create child nodes** i **add mesh to node**.  

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

## Krok 3: Zastosowanie rotacji do górnego węzła  

Obracanie węzła nadrzędnego automatycznie obraca wszystkie jego dzieci, co jest kluczową zaletą scen hierarchicznych.  

```java
// Rotate the top node, affecting all child nodes
top.getTransform().setRotation(Quaternion.fromEulerAngle(Math.PI, 4, 0));
```  

## Krok 4: Zapis sceny 3D – Jak wyeksportować FBX  

Teraz **save scene as FBX**, kończąc przepływ pracy „how to export fbx”.  

```java
// Save 3D scene in the supported file format (FBX in this case)
String MyDir = "Your Document Directory";
MyDir = MyDir + "NodeHierarchy.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
System.out.println("\nNode hierarchy added successfully to document.\nFile saved at " + MyDir);
```  

### Oczekiwany wynik  

Uruchomienie kodu tworzy plik o nazwie **NodeHierarchy.fbx** w określonym katalogu. Otwórz go w dowolnym przeglądarce obsługującej FBX, aby zobaczyć dwa sześciany umieszczone po lewej i prawej stronie centralnego punktu obrotu, wszystkie obracające się razem.  

## Typowe problemy i rozwiązania  

| Problem | Dlaczego się pojawia | Rozwiązanie |
|---------|----------------------|-------------|
| **Błąd pliku nie znaleziony** podczas zapisywania | Ścieżka `MyDir` jest niepoprawna lub brakuje końcowego separatora | Ensure the directory exists and ends with a file separator (`/` or `\\`). |
| **Siatka niewidoczna** po eksporcie | Jednostka siatki nie została przypisana lub translacja przenosi ją poza widok | Verify `cube1.setEntity(mesh)` and check translation values. |
| **Rotacja wygląda niepoprawnie** | Nieprawidłowe użycie radianów zamiast stopni | `Quaternion.fromEulerAngle` expects radians; adjust values accordingly. |

## Wskazówki dotyczące rozwiązywania problemów  

- **Sprawdź katalog**: użyj `new File(MyDir).mkdirs();` przed `scene.save`, jeśli folder może nie istnieć.  
- **Sprawdź graf sceny**: wywołaj `scene.getRootNode().getChildren().size()`, aby potwierdzić, że węzły potomne zostały dodane.  
- **Sprawdź kompatybilność wersji FBX**: niektóre starsze narzędzia obsługują tylko FBX 2013; możesz zmienić format na `FileFormat.FBX2013`, jeśli to konieczne.  

## Najczęściej zadawane pytania  

**P: Czy Aspose.3D for Java jest odpowiedni dla początkujących?**  
O: Zdecydowanie! API jest zaprojektowane z czystym, obiektowo‑zorientowanym podejściem, co ułatwia naukę, nawet jeśli jesteś nowicjuszem w programowaniu 3D.  

**P: Czy mogę używać Aspose.3D for Java w projektach komercyjnych?**  
O: Tak, możesz. Odwiedź [stronę zakupu](https://purchase.aspose.com/buy) po szczegóły licencjonowania.  

**P: Jak mogę uzyskać wsparcie dla Aspose.3D for Java?**  
O: Dołącz do [forum Aspose.3D](https://forum.aspose.com/c/3d/18), aby uzyskać pomoc od społeczności i zespołu wsparcia Aspose.  

**P: Czy dostępna jest darmowa wersja próbna?**  
O: Oczywiście! Przetestuj funkcje za pomocą [darmowej wersji próbnej](https://releases.aspose.com/) przed podjęciem decyzji.  

**P: Gdzie mogę znaleźć dokumentację?**  
O: Odwołaj się do [dokumentacji](https://reference.aspose.com/3d/java/) po szczegółowe informacje o Aspose.3D for Java.  

## Zakończenie  

Opanowanie **create child nodes**, **add mesh to node** oraz **how to export FBX** to kluczowe kroki w budowaniu zaawansowanych aplikacji 3D w Javie. Dzięki Aspose.3D otrzymujesz potężne, przyjazne licencyjnie rozwiązanie, które ukrywa szczegóły niskiego poziomu, jednocześnie dając pełną kontrolę nad grafem sceny. Eksperymentuj z różnymi siatkami, transformacjami i formatami eksportu, aby odkrywać jeszcze więcej możliwości.  

---  

**Ostatnia aktualizacja:** 2026-04-12  
**Testowane z:** Aspose.3D for Java 24.11  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}  

{{< /blocks/products/pf/main-container >}}  
{{< /blocks/products/pf/main-wrap-class >}}  

{{< blocks/products/products-backtop-button >}}