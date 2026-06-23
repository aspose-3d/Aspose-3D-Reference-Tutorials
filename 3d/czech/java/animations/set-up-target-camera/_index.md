---
date: 2026-06-23
description: Zjistěte, jak nastavit cíl kamery a pozici kamery při inicializaci 3D
  scény v Javě pomocí Aspose.3D. Obsahuje tipy na camera look at a základy animation.
keywords:
- set camera target
- create 3d scene
- camera look at
- add camera scene
- orbit camera animation
linktitle: Nastavte cíl kamery a pozici kamery v Javě | Aspose.3D
schemas:
- author: Aspose
  dateModified: '2026-06-23'
  description: Learn how to set camera target and position the camera while initializing
    a 3D scene in Java using Aspose.3D. Includes camera look at tips and animation
    basics.
  headline: Set Camera Target and Position Camera in Java | Aspose.3D
  type: TechArticle
- questions:
  - answer: Create a new `Scene` object with `new Scene()`.
    question: What is the first step?
  - answer: '`com.aspose.threed.Camera`.'
    question: Which class represents the camera?
  - answer: Call `Camera.setTarget(Node)` on the camera node.
    question: How do I point the camera at a target?
  - answer: DISCREET3DS (`.3ds`).
    question: What file format does the example export?
  - answer: Yes—a commercial license is required; a free trial is fine for development.
    question: Do I need a license for production?
  type: FAQPage
second_title: Aspose.3D Java API
title: Nastavte cíl kamery a pozici kamery v Javě | Aspose.3D
url: /cs/java/animations/set-up-target-camera/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Nastavení cíle kamery a pozice kamery v Javě | Aspose.3D

V tomto podrobném průvodci objevíte **jak nastavit cíl kamery** při inicializaci 3D scény s Aspose.3D pro Javu. Správné umístění kamery je základem každé interaktivní vizualizace— ať už vytváříte hru, konfigurátor produktu nebo vědecký model. Provedeme vás vytvořením scény, přidáním uzlu kamery, definováním cílového uzlu a uložením výsledku, vše s jasnými vysvětleními a praktickými tipy.

Scéna je kořenový kontejner, který v projektu obsahuje všechny 3D objekty.  
Kamera představuje pohledový bod, ze kterého je scéna renderována.  
Camera.setTarget(Node) přiřadí cílový uzel, na který bude kamera vždy směřovat.

## Rychlé odpovědi
- **Jaký je první krok?** Vytvořte nový objekt `Scene` pomocí `new Scene()`.  
- **Která třída představuje kameru?** `com.aspose.threed.Camera`.  
- **Jak nasměrovat kameru na cíl?** Zavolejte `Camera.setTarget(Node)` na uzlu kamery.  
- **Do jakého formátu souboru příklad exportuje?** DISCREET3DS (`.3ds`).  
- **Potřebuji licenci pro produkci?** Ano—vyžaduje se komerční licence; pro vývoj stačí bezplatná zkušební verze.

## Co znamená „initialize 3d scene java“?
Inicializace 3D scény vytvoří kořenový kontejner, který obsahuje sítě, světla, kamery a transformace, a poskytne vám sandbox pro tvorbu a animaci objektů před exportem. Je to první logický krok v jakémkoli workflow Aspose.3D.

## Proč nastavit cílovou kameru?
Target kamera automaticky orientuje svůj pohled směrem k určenému uzlu, což zajišťuje, že objekt zůstane ve středu bez ohledu na pohyb kamery. To eliminuje ruční výpočty look‑at, zjednodušuje orbitální animace a poskytuje konzistentní rámování, což je ideální pro prezentace produktů, interaktivní prohlížeče a filmové sekvence.

- Udržení modelu ve středu, zatímco se kamera kolem něj pohybuje.  
- Vytváření orbitálních animací bez ručního výpočtu rotačních matic.  
- Zjednodušení UI ovládacích prvků pro koncové uživatele, kteří potřebují zaměřit konkrétní objekt.

## Jak nastavit cíl kamery v Aspose.3D?
Camera.setTarget(Node) nastaví zaměření kamery na zadaný cílový uzel. Načtěte svou scénu, přidejte uzel kamery, vytvořte podřízený uzel, který bude sloužit jako ohniskový bod, a zavolejte `Camera.setTarget(targetNode)`. Kamera bude nyní vždy směřovat k cíli, bez ohledu na to, jak ji později přesunete. Tento jediný volání metody nahrazuje složité maticové výpočty a zajišťuje spolehlivé zarovnání pohledu.

## Konfigurace cíle kamery

Krok **configure camera target** říká kameře, na který uzel se má dívat. Konfigurací cíle kamery se vyhnete ručním výpočtům look‑at a zajistíte, že kamera bude vždy zaměřena na objekt zájmu.

## Předpoklady

Než se ponoříme do tutoriálu, ujistěte se, že máte připravené následující předpoklady:

- Základní znalost programování v Javě.  
- Nainstalovaný Java Development Kit (JDK) na vašem počítači.  
- Knihovna Aspose.3D stažena a přidána do vašeho projektu. Můžete ji stáhnout [zde](https://releases.aspose.com/3d/java/).

## Import balíčků

Začněte importováním potřebných balíčků, aby kód běžel hladce. Ve svém Java projektu zahrňte následující:

```java
import com.aspose.threed.*;
```

## Inicializace 3D scény v Javě

Základ každého 3D workflow je objekt scény. Zde jej vytvoříme a nastavíme adresář pro výstupní soubor.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
// Initialize scene object
Scene scene = new Scene();
```

## Krok 1: Vytvořit uzel kamery

Dále vytvořte uzel kamery ve scéně, který zachytí 3D prostředí.

```java
// Get a child node object
Node cameraNode = scene.getRootNode().createChildNode("camera", new Camera());
```

## Krok 2: Nastavit translaci uzlu kamery

Upravte translaci uzlu kamery, aby byla vhodně umístěna ve 3D prostoru.

```java
// Set camera node translation
cameraNode.getTransform().setTranslation(new Vector3(100, 20, 0));
```

## Krok 3: Nastavit cíl kamery

Určete cíl pro kameru vytvořením podřízeného uzlu pro kořenový uzel. Kamera bude automaticky směřovat na tento uzel.

```java
((Camera)cameraNode.getEntity()).setTarget(scene.getRootNode().createChildNode("target"));
```

## Krok 4: Uložit scénu

Uložte nakonfigurovanou scénu do souboru ve požadovaném formátu (v tomto příkladu DISCREET3DS).

```java
MyDir = MyDir + "camera-test.3ds";
scene.save(MyDir, FileFormat.DISCREET3DS);
```

## Jak animovat kameru

I když se tento tutoriál zaměřuje na umístění, stejný uzel kamery lze později animovat pomocí animačních API Aspose.3D. Například můžete vytvořit rotační animaci, která obíhá cílový uzel, nebo přesunout kameru podél spline cesty. Klíčové je, že jakmile je **target camera** nastavena, animace potřebuje měnit pouze transformaci uzlu kamery – pohled bude vždy zamčen na cíl.

## Časté chyby a tipy

- **Zapomněli jste přidat cílový uzel?** Kamera bude ve výchozím nastavení směřovat podél záporné osy Z, což nemusí dát očekávaný pohled. Vždy vytvořte cílový uzel nebo ručně nastavte směr look‑at.  
- **Nesprávná cesta k souboru?** Ujistěte se, že `MyDir` končí oddělovačem cesty (`/` nebo `\\`) před připojením názvu souboru.  
- **Licence není nastavena?** Spuštění kódu bez platné licence vloží vodoznak do exportovaného souboru.

## Často kladené otázky

**Q1: Jak si mohu stáhnout Aspose.3D pro Javu?**  
A: Můžete si stáhnout knihovnu ze [stránky ke stažení Aspose.3D Java](https://releases.aspose.com/3d/java/).

**Q2: Kde najdu dokumentaci k Aspose.3D?**  
A: Viz [dokumentace Aspose.3D Java](https://reference.aspose.com/3d/java/) pro komplexní návod.

**Q3: Je k dispozici bezplatná zkušební verze?**  
A: Ano, můžete vyzkoušet bezplatnou zkušební verzi Aspose.3D [zde](https://releases.aspose.com/).

**Q4: Potřebujete podporu nebo máte otázky?**  
A: Navštivte [forum Aspose.3D](https://forum.aspose.com/c/3d/18) a získejte pomoc od komunity a odborníků.

**Q5: Jak mohu získat dočasnou licenci?**  
A: Dočasnou licenci můžete získat [zde](https://purchase.aspose.com/temporary-license/).

---

**Poslední aktualizace:** 2026-06-23  
**Testováno s:** Aspose.3D for Java 24.11  
**Autor:** Aspose

## Související tutoriály

- [Vytvořit 3D scénu v Javě s Aspose 3D Java](/3d/java/3d-scenes-and-models/)
- [Vytvořit animovanou 3D scénu v Javě – tutoriál Aspose.3D](/3d/java/animations/)
- [Lineární interpolace 3D – Jak animovat 3D scény v Javě – Přidat animační vlastnosti s Aspose.3D](/3d/java/animations/add-animation-properties-to-scenes/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}