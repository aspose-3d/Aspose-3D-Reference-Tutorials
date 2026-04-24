---
date: 2026-03-13
description: Dowiedz się, jak tworzyć modele prymitywne 3D, takie jak cylinder, sześcian
  i inne, przy użyciu Aspose.3D dla Javy oraz zapisać scenę w formacie FBX.
linktitle: Building Primitive 3D Models with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Jak utworzyć cylinder 3D i inne prymitywne modele 3D przy użyciu Aspose.3D
  dla Javy
url: /pl/java/primitive-3d-models/building-primitive-3d-models/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Budowanie prymitywnych modeli 3D przy użyciu Aspose.3D dla Javy

## Wprowadzenie

Jeśli kiedykolwiek potrzebowałeś **tworzyć 3D cylinder** (lub dowolny inny podstawowy kształt) bezpośrednio w kodzie Javy, Aspose.3D sprawia, że zadanie jest bezbolesne. W tym samouczku przeprowadzimy Cię przez cały proces — od konfiguracji środowiska po zapisanie finalnej sceny jako pliku FBX — abyś mógł od razu zacząć generować geometrię 3D programowo.

## Szybkie odpowiedzi
- **Jakiej biblioteki użyć, aby stworzyć 3D cylinder w Javie?** Aspose.3D for Java.
- **Do jakiego formatu mogę wyeksportować scenę?** FBX (ASCII 7500) using `FileFormat.FBX7500ASCII`.
- **Czy potrzebna jest licencja do rozwoju?** Darmowa wersja próbna działa do testów; stała licencja jest wymagana w produkcji.
- **Jakie są główne obsługiwane prymitywy?** Box, Cylinder, Sphere, Cone i inne.
- **Czy kod jest kompatybilny z Java 8 i nowszymi?** Tak, Aspose.3D celuje w JDK 8+.

## Co to jest prymitywny cylinder 3D?

Cylinder prymityw to podstawowy kształt geometryczny określony promieniem i wysokością. W wielu pipeline'ach 3D służy jako element budulcowy bardziej złożonych modeli, takich jak rury, koła czy kolumny architektoniczne. Aspose.3D udostępnia gotową klasę `Cylinder`, więc nie musisz ręcznie obliczać wierzchołków.

## Dlaczego używać Aspose.3D dla Javy?

- **Pełnoprawny silnik 3D** – obsługuje import/eksport popularnych formatów (FBX, OBJ, STL, itp.).
- **Czyste API Java** – brak zależności natywnych, idealne dla projektów wieloplatformowych.
- **Solidny graf sceny** – pozwala organizować obiekty hierarchicznie.
- **Łatwa licencjonowanie** – rozpocznij od wersji próbnej, a następnie przejdź na stałą licencję.

## Wymagania wstępne

1. **Java Development Kit (JDK)** – JDK 8 lub nowszy zainstalowany na Twoim komputerze.  
2. **Biblioteka Aspose.3D for Java** – pobierz i zainstaluj ją ze [strony pobierania](https://releases.aspose.com/3d/java/).  

## Importowanie pakietów

Zacznij od zaimportowania podstawowego przestrzeni nazw Aspose.3D. Dzięki temu uzyskasz dostęp do `Scene`, `Box`, `Cylinder` oraz stałych formatów plików.

```java
import com.aspose.threed.*;
```

Teraz, gdy biblioteka jest zaimportowana, utwórzmy scenę i dodajmy trochę prymitywnej geometrii.

## Jak tworzyć cylinder 3D i inne prymitywy w scenie

### Krok 1: Inicjalizacja obiektu Scene

Najpierw potrzebujemy kontenera `Scene`, który będzie przechowywał wszystkie nasze węzły 3D.

```java
// The path to the documents directory.
String myDir = "Your Document Directory";

// Initialize a Scene object
Scene scene = new Scene();
```

### Krok 2: Zbuduj model pudełka 3D

Prymitwa pudełka jest przydatna do testowania układu współrzędnych. Tutaj dodajemy ją jako dziecko węzła głównego sceny.

```java
// Create a Box model
scene.getRootNode().createChildNode("box", new Box());
```

### Krok 3: Utwórz model cylindra 3D

Teraz faktycznie **tworzymy geometrię 3D cylinder**. Klasa `Cylinder` posiada rozsądne domyślne wymiary, ale w razie potrzeby możesz dostosować promień i wysokość poprzez jej konstruktor.

```java
// Create a Cylinder model
scene.getRootNode().createChildNode("cylinder", new Cylinder());
```

### Krok 4: Zapisz rysunek w formacie FBX

Po złożeniu sceny wyeksportuj ją, aby inne narzędzia (np. Unity, Blender) mogły ją odczytać. Używamy formatu `FBX7500ASCII`, który jest szeroko wspierany.

```java
// Save drawing in the FBX format
myDir = myDir + "test.fbx";
scene.save(myDir, FileFormat.FBX7500ASCII);
```

## Częste problemy i rozwiązania

| Problem | Dlaczego się pojawia | Rozwiązanie |
|---------|----------------------|-------------|
| **Plik nie znaleziony** podczas zapisu | `myDir` wskazuje na nieistniejący folder | Upewnij się, że katalog istnieje lub utwórz go za pomocą `new File(myDir).mkdirs();` |
| **Pusta scena** po eksporcie | Nie dodano żadnych węzłów przed wywołaniem `save` | Sprawdź, czy wywołania `createChildNode` są wykonywane (debuguj przy pomocy `scene.getRootNode().getChildCount()` ) |
| **Wyjątek licencyjny** | Uruchamianie bez ważnej licencji w środowisku produkcyjnym | Zastosuj tymczasową lub stałą licencję używając `License license = new License(); license.setLicense("Aspose.3D.Java.lic");` |

## Najczęściej zadawane pytania

**Q: Czy mogę używać Aspose.3D dla Javy z innymi językami programowania?**  
A: Aspose.3D głównie wspiera Javę, ale dostępne są wersje dla innych języków, takich jak .NET.

**Q: Czy Aspose.3D nadaje się do złożonych zadań modelowania 3D?**  
A: Zdecydowanie! Aspose.3D oferuje wszechstronny zestaw funkcji, co czyni go odpowiednim zarówno do prostych, jak i złożonych zadań modelowania 3D.

**Q: Gdzie mogę znaleźć dodatkową pomoc i wsparcie?**  
A: Odwiedź [Forum Aspose.3D](https://forum.aspose.com/c/3d/18) aby uzyskać wsparcie społeczności i dyskusje.

**Q: Czy mogę wypróbować Aspose.3D przed zakupem?**  
A: Tak, możesz wypróbować [bezpłatną wersję próbną](https://releases.aspose.com/) przed podjęciem decyzji o zakupie.

**Q: Jak uzyskać tymczasową licencję dla Aspose.3D?**  
A: Możesz uzyskać [tymczasową licencję](https://purchase.aspose.com/temporary-license/) dla Aspose.3D poprzez stronę internetową.

## Podsumowanie

Teraz wiesz, jak **tworzyć 3D cylinder**, pudełko i inne modele prymitywne przy użyciu Aspose.3D dla Javy oraz jak **zapisać scenę jako FBX** do dalszego wykorzystania. Śmiało eksperymentuj z innymi prymitywami (Sphere, Cone, itp.) i odkrywaj przypisywanie materiałów, aby nadać swoim modelom realistyczny wygląd.

---

**Last Updated:** 2026-03-13  
**Testowano z:** Aspose.3D for Java 24.11 (latest at time of writing)  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}