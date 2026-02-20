---
date: 2026-01-27
description: Naučte se 3D modelování v Javě vytvářením válců se skoseným dnem pomocí
  Aspose.3D pro Java. Tento úvodní 3D tutoriál ukazuje, jak nainstalovat Aspose 3D,
  aplikovat skosovou transformaci a exportovat soubor OBJ v Javě.
linktitle: Java 3D Modeling – Sheared Bottom Cylinders with Aspose.3D
second_title: Aspose.3D Java API
title: Java 3D modelování – Válce se zkoseným dnem s Aspose.3D
url: /cs/java/cylinders/creating-cylinders-with-sheared-bottom/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Java 3D modelování – Válce se šikmým dnem s Aspose.3D

## Úvod

Vítejte v tomto **java 3d modeling** tutoriálu! V tomto krok‑za‑krokem průvodci si ukážeme, jak vytvořit válec, jehož dno je šikmé, pomocí knihovny Aspose.3D pro Javu. Ať už sledujete **beginner 3d tutorial** nebo chcete přidat vlastní transformaci šikmosti k existujícímu modelu, uvidíte přesně, jak nastavit scénu, aplikovat šikmost a nakonec **export OBJ file java** pro použití v jiných nástrojích.

## Rychlé odpovědi
- **What library is used?** Aspose.3D for Java  
- **Can I install Aspose 3D via Maven?** Yes – add the Aspose.3D dependency to your `pom.xml`  
- **Is a license required for development?** A temporary license is sufficient for testing; a full license is needed for production  
- **Which file format is demonstrated?** Wavefront OBJ (`.obj`)  
- **How long does the example take to run?** Under a second on a typical workstation  

## Předpoklady

Než začneme, ujistěte se, že máte následující:

- Java Development Kit (JDK) nainstalovaný ve vašem systému.  
- **Install Aspose 3D** – stáhněte knihovnu z oficiální stránky [here](https://releases.aspose.com/3d/java/).  
- IDE nebo nástroj pro sestavení (Maven/Gradle) pro správu závislosti Aspose.3D.  

## Import balíčků

Nejprve importujte třídy, které budeme potřebovat pro scénu, geometrii a práci se soubory.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Krok 1: Vytvoření scény

Scéna je kontejner pro všechny 3‑D objekty. Začneme vytvořením prázdné scény.

```java
// ExStart:3
// Create a scene
Scene scene = new Scene();
// ExEnd:3
```

## Krok 2: Vytvoření válce 1 – Jak šikmout válec

Nyní vytvoříme první válec a **aplikujeme transformaci šikmosti** na jeho dno. Toto ukazuje **jak šikmout válec** přímo pomocí API.

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

## Krok 3: Vytvoření válce 2 – Standardní válec (bez šikmosti)

Pro srovnání přidáme druhý válec, který **nemá** šikmé dno.

```java
// ExStart:5
// Create cylinder 2
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// Add cylinder 2 without a ShearBottom to the scene
scene.getRootNode().createChildNode(cylinder2);
// ExEnd:5
```

## Krok 4: Uložení scény – Export OBJ souboru Java

Nakonec exportujeme scénu do souboru Wavefront OBJ, což ilustruje použití **export obj file java**.

```java
// ExStart:6
// Save scene
scene.save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

## Proč je to důležité pro Java 3D modelování

Přidání šikmosti k primitivnímu objektu vám umožní vytvořit organičtější tvary bez nutnosti externích modelovacích nástrojů. Tato technika je užitečná pro:

- Architektonické vizualizace, kde jsou požadovány šikmé základy.  
- Herní assety, které potřebují vlastní otisky, přičemž geometrie zůstává lehká.  
- Rychlé prototypování, kde chcete programově upravovat rozměry.

## Časté problémy a řešení

| Problém | Řešení |
|-------|----------|
| **Shear appears too extreme** | Adjust the `Vector2` values; they represent the shear factor (0‑1 range). |
| **OBJ file not opening in viewer** | Verify that the target directory exists and that you have write permissions. |
| **License exception at runtime** | Apply a temporary or permanent license before creating the scene (`License license = new License(); license.setLicense("Aspose.3D.lic");`). |

## Často kladené otázky

**Q: Can I use Aspose.3D for Java with other Java 3D libraries?**  
A: Aspose.3D is designed to work independently. While you can integrate it with other libraries, it already provides a full‑featured API for most 3‑D tasks.

**Q: Is Aspose.3D suitable for beginners in 3D modeling?**  
A: Absolutely. The API is straightforward, and this **beginner 3d tutorial** demonstrates core concepts with minimal code.

**Q: Where can I find additional support for Aspose.3D for Java?**  
A: Visit the [Aspose.3D forum](https://forum.aspose.com/c/3d/18) for community help and official answers.

**Q: How can I obtain a temporary license for Aspose.3D?**  
A: You can get a temporary license [here](https://purchase.aspose.com/temporary-license/).

**Q: Where do I purchase a full Aspose.3D for Java license?**  
A: Purchase options are available [here](https://purchase.aspose.com/buy).

---

**Poslední aktualizace:** 2026-01-27  
**Testováno s:** Aspose.3D 24.11 for Java  
**Autor:** Aspose

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Poslední aktualizace:** 2026-01-27  
**Testováno s:** Aspose.3D 24.11 for Java  
**Autor:** Aspose