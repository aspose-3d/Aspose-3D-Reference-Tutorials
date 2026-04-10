---
date: 2026-02-20
description: Dowiedz się, jak łączyć macierze transformacji w samouczku grafiki 3D
  w Javie przy użyciu Aspose.3D, obejmując kolejność mnożenia macierzy 3D, transformacje
  węzłów i eksport sceny.
linktitle: Concatenate Transformation Matrices in Java 3D Graphics Tutorial with Aspose.3D
second_title: Aspose.3D Java API
title: Samouczek grafiki 3D w Javie – Łączenie macierzy Aspose.3D
url: /pl/java/geometry/transform-3d-nodes-with-matrices/
weight: 21
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Transformuj węzły 3D przy użyciu macierzy transformacji z Aspose.3D

## Introduction

Witamy w tym krok po kroku **java 3d graphics tutorial**. W tym przewodniku nauczysz się **concatenate transformation matrices**, aby łatwo przekształcać węzły 3D przy użyciu Aspose.3D. Niezależnie od tego, czy tworzysz silnik gier, przeglądarkę CAD, czy wizualizator naukowy, opanowanie łączenia macierzy daje precyzyjną kontrolę nad translacją, rotacją i skalowaniem w jednej operacji.

## Quick Answers
- **Jaka jest podstawowa klasa dla sceny 3D?** `Scene` – przechowuje wszystkie węzły, siatki i światła.  
- **Jak zastosować wiele transformacji?** Poprzez concatenating transformation matrices na obiekcie `Transform` węzła.  
- **Jaki format pliku jest używany do zapisu?** Pokazany jest FBX (ASCII 7500), ale Aspose.3D obsługuje wiele innych.  
- **Czy potrzebna jest licencja do rozwoju?** Tymczasowa licencja działa w trybie ewaluacji; pełna licencja jest wymagana w produkcji.  
- **Jakie IDE jest najlepsze?** Dowolne IDE Java (IntelliJ IDEA, Eclipse, NetBeans), które obsługuje Maven/Gradle.

## What is “concatenate transformation matrices”?

Łączenie macierzy transformacji oznacza mnożenie dwóch lub więcej macierzy, tak aby pojedyncza połączona macierz reprezentowała sekwencję transformacji (np. translate → rotate → scale). W Aspose.3D stosujesz otrzymaną macierz do transformacji węzła, co pozwala na skomplikowane pozycjonowanie przy użyciu jednego wywołania.

## Understanding matrix multiplication order 3d

Kolejność **matrix multiplication order 3d** ma znaczenie, ponieważ mnożenie macierzy nie jest przemienne. W praktyce zazwyczaj mnożysz w kolejności **scale → rotate → translate**, aby uzyskać oczekiwany efekt wizualny. `Matrix4.multiply()` w Aspose.3D stosuje tę samą konwencję, więc pamiętaj o kolejności przy budowaniu połączonej macierzy.

## Why this java 3d graphics tutorial matters

- **High‑performance rendering** – Aspose.3D jest zoptymalizowane pod kątem dużych scen.  
- **Cross‑format support** – Eksport do FBX, OBJ, STL, glTF i innych.  
- **Simple yet powerful API** – Biblioteka abstrahuje niskopoziomową matematykę, jednocześnie udostępniając operacje na macierzach dla precyzyjnej kontroli.  

## Prerequisites

Zanim zaczniemy, upewnij się, że masz:

- Podstawową wiedzę programistyczną w Javie.  
- Zainstalowaną bibliotekę Aspose.3D – pobierz ją [tutaj](https://releases.aspose.com/3d/java/).  
- IDE Java (IntelliJ, Eclipse lub NetBeans) z obsługą Maven/Gradle.

## Import Packages

W swoim projekcie Java zaimportuj niezbędne klasy Aspose.3D. Ten blok importu musi pozostać dokładnie taki, jak pokazano:

```java
import com.aspose.threed.*;

```

## Step-by-Step Guide

### Step 1: Initialize the Scene Object

Utwórz `Scene`, które pełni rolę głównego kontenera dla wszystkich elementów 3D.

```java
Scene scene = new Scene();
```

### Step 2: Initialize a Node (Cube)

Zainicjalizuj `Node`, który będzie przechowywać geometrię sześcianu.

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

Tutaj **concatenate transformation matrices** poprzez bezpośrednie podanie własnego `Matrix4`. Można najpierw stworzyć oddzielne macierze translacji, rotacji i skalowania i je pomnożyć, ale dla zwięzłości pokazujemy jedną połączoną macierz.

```java
cubeNode.getTransform().setTransformMatrix(new Matrix4(
    1, -0.3, 0, 0,
    0.4, 1, 0.3, 0,
    0, 0, 1, 0,
    0, 20, 0, 1
));
```

> **Pro tip:** Aby **concatenate** wiele macierzy, utwórz każdą `Matrix4` (np. `translation`, `rotation`, `scale`) i użyj `Matrix4.multiply()` przed przypisaniem wyniku do `setTransformMatrix`.

### Step 6: Add the Cube Node to the Scene

Wstaw węzeł do hierarchii sceny pod węzłem głównym.

```java
scene.getRootNode().addChildNode(cubeNode);
```

### Step 7: Save the 3D Scene

Wybierz katalog i nazwę pliku, a następnie wyeksportuj scenę. Przykład zapisuje jako FBX ASCII, ale możesz przełączyć na OBJ, STL itp., zmieniając `FileFormat`.

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "TransformationToNode.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
System.out.println("\nTransformation added successfully to node.\nFile saved at " + MyDir);
```

## Common Issues and Solutions

| Problem | Przyczyna | Rozwiązanie |
|---------|-----------|-------------|
| **Scene not saving** | Nieprawidłowa ścieżka katalogu lub brak uprawnień do zapisu | Zweryfikuj, że `MyDir` wskazuje istniejący folder i aplikacja ma prawa do systemu plików. |
| **Matrix seems to have no effect** | Użycie macierzy jednostkowej lub zapomnienie o jej przypisaniu | Upewnij się, że wywołujesz `setTransformMatrix` po stworzeniu macierzy i podwójnie sprawdź wartości macierzy. |
| **Incorrect orientation** | Nieprawidłowa kolejność rotacji przy łączeniu macierzy | Mnoż macierze w kolejności *scale → rotate → translate*, aby uzyskać oczekiwane wyniki. |

## Frequently Asked Questions

### Q1: Can I apply multiple transformations to a single 3D node?

Tak. Utwórz oddzielne macierze dla każdej transformacji (translation, rotation, scaling) i **concatenate transformation matrices** przy użyciu mnożenia przed przypisaniem ostatecznej macierzy.

### Q2: How can I rotate a 3D object in Aspose.3D?

Zbuduj macierz rotacji (np. wokół osi Y) przy użyciu `Matrix4.createRotationY(angle)` i **concatenate** ją z istniejącą macierzą.

### Q3: Is there a limit to the size of the 3D scenes I can create?

Praktyczny limit zależy od pamięci i CPU twojego systemu. Aspose.3D jest zaprojektowane do efektywnego obsługiwania dużych scen, ale monitoruj zużycie zasobów przy bardzo złożonych modelach.

### Q4: Where can I find additional examples and documentation?

Odwiedź [Aspose.3D documentation](https://reference.aspose.com/3d/java/) aby uzyskać pełną listę API, przykłady kodu i przewodniki najlepszych praktyk.

### Q5: How do I obtain a temporary license for Aspose.3D?

Możesz uzyskać tymczasową licencję [tutaj](https://purchase.aspose.com/temporary-license/).

## Conclusion

Teraz opanowałeś, jak **concatenate transformation matrices**, aby manipulować węzłami 3D w środowisku Java przy użyciu Aspose.3D. Eksperymentuj z różnymi kombinacjami macierzy — translate, rotate, scale — aby tworzyć zaawansowane animacje i modele. Gdy będziesz gotowy, odkryj inne funkcje Aspose.3D, takie jak oświetlenie, kontrola kamery i eksport do dodatkowych formatów.

---

**Ostatnia aktualizacja:** 2026-02-20  
**Testowano z:** Aspose.3D 24.11 for Java  
**Autor:** Aspose

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}