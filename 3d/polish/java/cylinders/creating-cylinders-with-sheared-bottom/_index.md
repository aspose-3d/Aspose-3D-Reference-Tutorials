---
date: 2025-12-09
description: Dowiedz się, jak używać Aspose do tworzenia spersonalizowanych cylindrów
  z ściętymi podstawami w Javie, idealnych do modelowania 3D w Javie i zapisywania
  scen jako OBJ.
language: pl
linktitle: 'How to Use Aspose: Create Cylinders with Sheared Bottom in Java'
second_title: Aspose.3D Java API
title: 'Jak używać Aspose: Tworzenie cylindrów z pochyłym dnem w Javie'
url: /java/cylinders/creating-cylinders-with-sheared-bottom/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Jak używać Aspose: Tworzenie cylindrów z nachylonym dnem w Javie

## Introduction

W tym praktycznym tutorialu odkryjesz **how to use Aspose**, aby zbudować cylinder, którego dno jest nachylone — technika często potrzebna w projektach *java 3d modeling*. Przejdziemy krok po kroku, od konfiguracji sceny po zapisanie gotowego modelu jako pliku OBJ. Na koniec będziesz mieć gotowy fragment kodu, który możesz wstawić do dowolnej aplikacji 3D opartej na Javie.

## Quick Answers
- **What does “shear bottom” mean?** To nachylenie podstawy cylindra pod określonym kątem w płaszczyźnie XY.  
- **Which library handles the 3D math?** Aspose.3D for Java udostępnia klasy `Cylinder` i `Vector2`.  
- **Do I need a license to run the example?** Tymczasowa licencja działa w trybie ewaluacyjnym; pełna licencja jest wymagana w produkcji.  
- **Can I export the model to other formats?** Tak — użyj `scene.save(..., FileFormat.WAVEFRONTOBJ)`, aby uzyskać plik OBJ.  
- **What Java version is required?** Wystarczy JDK 8 lub nowszy.

## What is “how to use aspose” in the context of 3D modeling?

Aspose.3D for Java to wysokopoziomowe API, które ukrywa złożoność geometrii 3D, formatów plików i przekształceń. Zamiast pracować z niskopoziomowymi buforami wierzchołków, wywołujesz intuicyjne metody takie jak `new Cylinder(...)`, a Aspose zajmuje się ciężką pracą.

## Why use Aspose for Java 3D Modeling?

- **Rapid development:** Twórz złożone kształty w kilku linijkach kodu.  
- **Broad format support:** Eksportuj do OBJ, STL, FBX i wielu innych.  
- **Cross‑platform:** Działa na każdym systemie operacyjnym obsługującym Javę.  
- **Consistent API:** Ten sam kod działa na komputerach stacjonarnych, serwerach i w środowiskach Android.

## Prerequisites

Zanim rozpoczniesz, upewnij się, że masz:

- **Java Development Kit (JDK) 8+** zainstalowany i skonfigurowany w IDE.  
- **Aspose.3D for Java** dodany do ścieżki klas projektu. Możesz go pobrać z oficjalnej strony [tutaj](https://releases.aspose.com/3d/java/).  
- **Tymczasowa lub pełna licencja** (opcjonalnie do wersji próbnej).

## Import Packages

Aby rozpocząć, zaimportuj niezbędne klasy Aspose.3D oraz narzędzia Javy:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Step 1: Create a Scene

*Scena* to kontener, który przechowuje wszystkie obiekty 3D, światła i kamery. Pomyśl o niej jak o scenie, na której umieścisz swoje cylindry.

```java
// ExStart:3
// Create a scene
Scene scene = new Scene();
// ExEnd:3
```

## Step 2: Create Cylinder 1 (Sheared Bottom)

Teraz utworzymy pierwszy cylinder i zastosujemy przekształcenie nachylenia do jego dna. Metoda `setShearBottom` przyjmuje obiekt `Vector2`, gdzie komponent X reprezentuje współczynnik nachylenia wzdłuż osi X, a komponent Y wzdłuż osi Y.

```java
// ExStart:4
// Create cylinder 1
Cylinder cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
// Customized shear bottom for cylinder 1
cylinder1.setShearBottom(new Vector2(0, 0.83)); // Shear 47.5deg in the xy plane (z-axis)
// Add cylinder 1 to the scene
scene.getRootNode().createChildNode(cylinder1).getTransform().setTranslation(10, 0, 0);
// ExEnd:4
```

> **Pro tip:** Współczynnik nachylenia `0.83` odpowiada mniej więcej 47,5°; dostosuj tę wartość, aby uzyskać dokładny kąt, którego potrzebujesz.

## Step 3: Create Cylinder 2 (Standard)

Dla porównania dodamy drugi cylinder bez żadnego nachylenia. Dzięki temu łatwo zobaczysz różnicę wizualną bezpośrednio w wyeksportowanym pliku OBJ.

```java
// ExStart:5
// Create cylinder 2
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// Add cylinder 2 without a ShearBottom to the scene
scene.getRootNode().createChildNode(cylinder2);
// ExEnd:5
```

## Step 4: Save the Scene (How to Save Scene as OBJ)

Na koniec zapisujemy scenę na dysku. Stała `FileFormat.WAVEFRONTOBJ` instruuje Aspose, aby zapisał plik w formacie OBJ, który jest szeroko obsługiwany przez edytory 3D takie jak Blender i Maya.

```java
// ExStart:6
// Save scene
scene.save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

> **Note:** Zamień `"Your Document Directory"` na ścieżkę absolutną lub względną odpowiednią dla Twojego środowiska.

## Common Issues and Solutions

| Issue | Cause | Solution |
|-------|-------|----------|
| **Cylinder appears flat** | Incorrect shear factor (outside 0‑1 range) | Use a value between 0 and 1; adjust gradually while previewing. |
| **OBJ file not loading in viewer** | Missing material definitions | Add a simple material to each node or export as STL for geometry‑only testing. |
| **LicenseException at runtime** | No valid license file | Place `Aspose.3D.lic` in the project root or use `License` class to load it programmatically. |

## Frequently Asked Questions

### Q1: Can I use Aspose.3D for Java with other Java 3D libraries?
**A:** Aspose.3D for Java jest zaprojektowane do pracy niezależnej. Choć możesz je integrować z innymi bibliotekami, zapewnia pełny zestaw funkcji potrzebnych do większości zadań modelowania 3D samodzielnie.

### Q2: Is Aspose.3D suitable for beginners in 3D modeling?
**A:** Tak, Aspose.3D oferuje przyjazne API, które ukrywa szczegóły niskiego poziomu, co czyni je dostępnym zarówno dla początkujących, jak i doświadczonych programistów.

### Q3: Where can I find additional support for Aspose.3D for Java?
**A:** Odwiedź [Aspose.3D forum](https://forum.aspose.com/c/3d/18) w celu uzyskania wsparcia społeczności, tutoriali i dyskusji.

### Q4: How can I obtain a temporary license for Aspose.3D?
**A:** Tymczasową licencję możesz uzyskać [tutaj](https://purchase.aspose.com/temporary-license/).

### Q5: Can I buy Aspose.3D for Java?
**A:** Tak, możesz zakupić Aspose.3D for Java [tutaj](https://purchase.aspose.com/buy).

## Conclusion

Przeszliśmy przez **how to use Aspose**, aby stworzyć dwa cylindry — jeden z nachylonym dnem i jeden standardowy — a następnie zapisaliśmy wynik jako plik OBJ. Ta technika jest podstawą do bardziej zaawansowanych modeli 3D, takich jak niestandardowe części, elementy architektoniczne czy zasoby gier. Śmiało eksperymentuj z różnymi wartościami nachylenia, promieniami i wysokościami, aby dopasować je do potrzeb swojego projektu.

---

**Last Updated:** 2025-12-09  
**Tested With:** Aspose.3D for Java 24.11 (latest at time of writing)  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}