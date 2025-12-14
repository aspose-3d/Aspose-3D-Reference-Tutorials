---
date: 2025-12-14
description: Dowiedz się, jak łączyć macierze przekształceń w samouczku grafiki 3D
  w Javie przy użyciu Aspose.3D. Przekształcaj węzły, zapisuj sceny i poznawaj praktyczne
  przykłady.
linktitle: Concatenate Transformation Matrices in Java 3D Graphics Tutorial with Aspose.3D
second_title: Aspose.3D Java API
title: Jak łączyć macierze transformacji i przekształcać węzły 3D przy użyciu Aspose.3D
url: /pl/java/geometry/transform-3d-nodes-with-matrices/
weight: 21
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Transformuj węzły 3D przy użyciu macierzy transformacji z Aspose.3D

## Introduction

Witamy w tym krok‑po‑kroku **samouczku grafiki 3D w Javie**. W tym przewodniku nauczysz się, jak **łączyć macierze transformacji**, aby łatwo przekształcać węzły 3D przy użyciu Aspose.3D. Niezależnie od tego, czy tworzysz silnik gry, przeglądarkę CAD, czy wizualizator naukowy, opanowanie łączenia macierzy daje precyzyjną kontrolę nad translacją, rotacją i skalowaniem w jednej operacji.

## Quick Answers
- **Jaka jest główna klasa sceny 3D?** `Scene` – przechowuje wszystkie węzły, siatki i światła.  
- **Jak zastosować wiele transformacji?** Poprzez łączenie macierzy transformacji w obiekcie `Transform` węzła.  
- **Jaki format pliku jest używany do zapisu?** Pokazany jest FBX (ASCII 7500), ale Aspose.3D obsługuje wiele innych.  
- **Czy potrzebna jest licencja do rozwoju?** Tymczasowa licencja działa w trybie ewaluacji; pełna licencja jest wymagana w produkcji.  
- **Jakie IDE jest najlepsze?** Dowolne IDE Javy (IntelliJ IDEA, Eclipse, NetBeans) obsługujące Maven/Gradle.

## What is “concatenate transformation matrices”?

Co oznacza „łączenie macierzy transformacji”?

Łączenie macierzy transformacji oznacza mnożenie dwóch lub więcej macierzy, tak aby pojedyncza połączona macierz reprezentowała sekwencję transformacji (np. translacja → rotacja → skalowanie). W Aspose.3D stosujesz otrzymaną macierz do transformacji węzła, co pozwala na skomplikowane pozycjonowanie za pomocą jednego wywołania.

## Why use a Java 3D graphics tutorial with Aspose.3D?

- **Wysokowydajne renderowanie** – Aspose.3D jest zoptymalizowane pod kątem dużych scen.  
- **Obsługa wielu formatów** – Eksport do FBX, OBJ, STL, glTF i innych.  
- **Proste API** – Biblioteka ukrywa niskopoziomową matematykę, jednocześnie udostępniając operacje na macierzach dla precyzyjnej kontroli.  

## Prerequisites

Wymagania wstępne:

- Podstawowa znajomość programowania w Javie.  
- Biblioteka Aspose.3D zainstalowana – pobierz ją [tutaj](https://releases.aspose.com/3d/java/).  
- IDE Javy (IntelliJ, Eclipse lub NetBeans) z obsługą Maven/Gradle.

## Import Packages

W swoim projekcie Java zaimportuj niezbędne klasy Aspose.3D. Ten blok importu musi pozostać dokładnie taki, jak przedstawiono:

```java
import com.aspose.threed.*;

```

## Transforming 3D Nodes

Poniżej znajduje się kompletny przepływ pracy. Każdy krok jest wyjaśniony prostym językiem, a następnie podany jest oryginalny blok kodu (bez zmian).

### Step 1: Initialize the Scene Object

Utwórz obiekt `Scene`, który pełni rolę głównego kontenera dla wszystkich elementów 3D.

```java
Scene scene = new Scene();
```

### Step 2: Initialize a Node (Cube)

Zainicjalizuj `Node`, który będzie przechowywał geometrię sześcianu.

```java
Node cubeNode = new Node("cube");
```

### Step 3: Create Mesh Using Polygon Builder

Wygeneruj siatkę dla sześcianu przy użyciu metody pomocniczej w `Common`.

```java
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

### Step 4: Attach Mesh to the Node

Połącz geometrię z węzłem, aby scena wiedziała, co renderować.

```java
cubeNode.setEntity(mesh);
```

### Step 5: Set a Custom Translation Matrix (Concatenation Example)

Tutaj **łączymy macierze transformacji** podając bezpośrednio własną macierz `Matrix4`. Można najpierw utworzyć osobne macierze translacji, rotacji i skalowania i je pomnożyć, ale dla zwięzłości pokazujemy jedną połączoną macierz.

```java
cubeNode.getTransform().setTransformMatrix(new Matrix4(
    1, -0.3, 0, 0,
    0.4, 1, 0.3, 0,
    0, 0, 1, 0,
    0, 20, 0, 1
));
```

> **Wskazówka:** Aby połączyć wiele macierzy, utwórz każdą `Matrix4` (np. `translation`, `rotation`, `scale`) i użyj `Matrix4.multiply()` przed przypisaniem wyniku do `setTransformMatrix`.

### Step 6: Add the Cube Node to the Scene

Wstaw węzeł do hierarchii sceny pod węzłem głównym.

```java
scene.getRootNode().addChildNode(cubeNode);
```

### Step 7: Save the 3D Scene

Wybierz katalog i nazwę pliku, a następnie wyeksportuj scenę. Przykład zapisuje jako FBX ASCII, ale możesz przełączyć się na OBJ, STL itp., zmieniając `FileFormat`.

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "TransformationToNode.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
System.out.println("\nTransformation added successfully to node.\nFile saved at " + MyDir);
```

## Common Issues and Solutions

| Problem | Przyczyna | Rozwiązanie |
|---------|-----------|-------------|
| **Scena nie zapisuje się** | Nieprawidłowa ścieżka katalogu lub brak uprawnień do zapisu | Sprawdź, czy `MyDir` wskazuje istniejący folder i aplikacja ma prawa do systemu plików. |
| **Macierz nie wywiera widocznego efektu** | Użycie macierzy jednostkowej lub zapomnienie o jej przypisaniu | Upewnij się, że wywołujesz `setTransformMatrix` po utworzeniu macierzy i podwójnie sprawdź jej wartości. |
| **Nieprawidłowa orientacja** | Nieprawidłowa kolejność rotacji przy łączeniu macierzy | Mnoż macierze w kolejności *skalowanie → rotacja → translacja*, aby uzyskać oczekiwane rezultaty. |

## Frequently Asked Questions

### Q1: Czy mogę zastosować wiele transformacji do jednego węzła 3D?

A1: Tak. Utwórz osobne macierze dla każdej transformacji (translacja, rotacja, skalowanie) i **połącz macierze transformacji** przy pomocy mnożenia przed przypisaniem ostatecznej macierzy.

### Q2: Jak mogę obrócić obiekt 3D w Aspose.3D?

A2: Utwórz macierz rotacji (np. wokół osi Y) za pomocą `Matrix4.createRotationY(angle)` i połącz ją z dowolną istniejącą macierzą.

### Q3: Czy istnieje limit rozmiaru scen 3D, które mogę tworzyć?

A3: Praktyczny limit zależy od pamięci i procesora twojego systemu. Aspose.3D jest zaprojektowane do efektywnego obsługiwania dużych scen, ale warto monitorować zużycie zasobów przy bardzo złożonych modelach.

### Q4: Gdzie mogę znaleźć dodatkowe przykłady i dokumentację?

A4: Odwiedź [dokumentację Aspose.3D](https://reference.aspose.com/3d/java/), aby uzyskać pełną listę API, przykłady kodu i przewodniki najlepszych praktyk.

### Q5: Jak uzyskać tymczasową licencję dla Aspose.3D?

A5: Tymczasową licencję możesz uzyskać [tutaj](https://purchase.aspose.com/temporary-license/).

## Conclusion

Teraz opanowałeś, jak **łączyć macierze transformacji**, aby manipulować węzłami 3D w środowisku Java przy użyciu Aspose.3D. Eksperymentuj z różnymi kombinacjami macierzy — translacją, rotacją, skalowaniem — aby tworzyć zaawansowane animacje i modele. Gdy będziesz gotowy, poznaj inne funkcje Aspose.3D, takie jak oświetlenie, kontrola kamery oraz eksport do dodatkowych formatów.

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Ostatnia aktualizacja:** 2025-12-14  
**Testowano z:** Aspose.3D 24.11 dla Java  
**Autor:** Aspose