---
date: 2026-05-24
description: Naučte se, jak extrudovat tvar pomocí Aspose.3D for Java. Tento tutoriál
  o 3D modelování v Javě pokrývá linear extrusion, center control, direction, slices,
  twist a další!
keywords:
- how to extrude shape
- java 3d geometry
- create 3d model java
- create solid from 2d
linktitle: Vytváření 3D modelů s Linear Extrusion v Javě
schemas:
- author: Aspose
  dateModified: '2026-05-24'
  description: Learn how to extrude shape using Aspose.3D for Java. This java 3d modeling
    tutorial covers linear extrusion, center control, direction, slices, twist and
    more!
  headline: How to Extrude Shape - Creating 3D Models with Linear Extrusion in Java
  type: TechArticle
- description: Learn how to extrude shape using Aspose.3D for Java. This java 3d modeling
    tutorial covers linear extrusion, center control, direction, slices, twist and
    more!
  name: How to Extrude Shape - Creating 3D Models with Linear Extrusion in Java
  steps:
  - name: Define the 2‑D profile
    text: Create a `Polygon` or `Polyline` that represents the shape you want to extrude.
      *A `Polygon` represents a closed shape defined by vertices, while a `Polyline`
      is an open series of line segments.* Ready to get started? [Perform Linear Extrusion
      Now](./performing-linear-extrusion/) For a detailed tuto
  - name: Configure extrusion options
    text: 'Set the center, direction, slices, twist, and twist offset on an `Extrusion`
      object. *The `Extrusion` class encapsulates all parameters needed to generate
      a 3‑D mesh from a 2‑D profile.* Get hands‑on with center control: [Control Center
      in Linear Extrusion](./controlling-center/) Read more about cen'
  - name: Add the extrusion to the scene
    text: 'Instantiate a `Scene`, attach the extrusion mesh, and export to your desired
      format. *`Scene` is the container that holds all 3‑D objects and handles exporting
      to various file formats.* Ready to set the direction? [Explore Now](./setting-direction/)
      Learn more about direction: [Setting Direction in '
  - name: Export or render
    text: 'Use `Scene.save()` to write the model to OBJ, STL, or any supported format.
      *`Scene.save()` writes the entire scene to the specified file format, applying
      any necessary post‑processing.* Start specifying slices: [Learn More](./specifying-slices/)
      Detailed guide: [Specifying Slices in Linear Extrusio'
  type: HowTo
- questions:
  - answer: Yes, a valid Aspose license is required for production use, but a free
      trial is available for evaluation.
    question: Can I use Aspose.3D for Java in a commercial project?
  - answer: The library works with Java 8 and newer runtimes, including Java 11, 17,
      and 21.
    question: Which Java versions are supported?
  - answer: Aspose.3D handles mesh generation efficiently, but you can call `scene.dispose()`
      when you’re done with large scenes to free native resources.
    question: Do I need to manage memory for large extrusions?
  - answer: Absolutely – you can create several extrusion objects, position them independently,
      and add them to the same scene.
    question: Can I combine multiple extrusion operations in one model?
  - answer: Yes, the “Applying Twist” and “Using Twist Offset” tutorials demonstrate
      how to set both properties on the same extrusion object.
    question: Is there sample code for applying twist and twist offset together?
  type: FAQPage
second_title: Aspose.3D Java API
title: Jak extrudovat tvar - Vytváření 3D modelů s Linear Extrusion v Javě
url: /cs/java/linear-extrusion/
weight: 23
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Jak extrudovat tvar – Vytváření 3D modelů lineární extruzí v Javě

Pokud jste se někdy zamýšleli nad **jak extrudovat tvar** v Java aplikaci, jste na správném místě. V tomto tutoriálu projdeme funkce lineární extruze v Aspose.3D for Java a ukážeme vám, jak převést jednoduché 2‑D profily na plnohodnotné 3‑D modely. Ať už budujete CAD‑stylový prohlížeč, pipeline pro herní assety, nebo jen experimentujete s geometrií, zvládnutí lineární extruze vám dodá jistotu vytvářet složité tvary pomocí několika řádků kódu.

## Rychlé odpovědi
- **Co je lineární extruze?** Přeměna 2‑D náčrtu na 3‑D těleso prodloužením podél směru.  
- **Která knihovna vám pomůže?** Aspose.3D for Java poskytuje plynulé API pro úlohy extruze.  
- **Potřebuji licenci?** Bezplatná zkušební verze stačí pro učení; pro produkci je vyžadována komerční licence.  
- **Jaká verze Javy je vyžadována?** Java 8 nebo novější.  
- **Mohu použít zkroucení nebo posuny?** Ano – API podporuje úhel zkroucení a posun zkroucení přímo.  

## Co je „jak extrudovat tvar“ v Javě?
Operace `Extrusion` je jádrová funkce Aspose.3D, která převádí plochý obrys na objemovou síť. Jednoduše řečeno, dodáte 2‑D profil (například obdélník nebo vlastní polygon), určíte, jak daleko jej vytáhnout, a knihovna pro vás vytvoří 3‑D geometrii.

## Proč používat Aspose.3D pro Javu?
Aspose.3D podporuje **více než 50 vstupních a výstupních formátů** – včetně OBJ, STL, FBX a GLTF – a může generovat sítě až s **10 000 vrcholy na extruzi** bez načítání celé scény do paměti. Jeho multiplatformní engine běží na Windows, Linuxu i macOS a poskytuje konzistentní výsledky, ať už pracujete na desktopovém workstationu nebo na bezhlavém CI serveru.

## Požadavky
- Java 8 nebo novější nainstalovaná na vašem vývojovém počítači.  
- Maven nebo Gradle pro správu závislostí.  
- Licenční soubor Aspose.3D for Java (volitelně pro zkušební verzi).  

## Jak funguje lineární extruze?
Lineární extruze vytváří 3‑D těleso tím, že provléká 2‑D profil podél přímky. Engine nejprve trianguluje profil, poté jej replikují v každém řezu podél osy extruze a nakonec spojí řezy dohromady, čímž vznikne vodotěsná síť. Tento proces automaticky vypočítá normály a UV souřadnice, takže můžete výsledek renderovat bez dalšího zpracování geometrie.

## Jaké jsou klíčové parametry lineární extruze?
Lineární extruze lze přizpůsobit pomocí několika parametrů. **Center** určuje pivotní bod profilu před extruzí. Vektor **direction** nastavuje osu extruze, výchozí je kladná osa Z. **Slices** řídí počet mezikřížových řezu, což ovlivňuje hladkost u zkroucených nebo zúžených tvarů. **Twist angle** otáčí profil postupně od začátku do konce, zatímco **twist offset** přidává lineární posun podél osy, což umožňuje spirálové tvary.

- **Center** – Pivotní bod, kolem kterého je profil umístěn před extruzí.  
- **Direction** – Vektor definující osu extruze; výchozí je kladná osa Z.  
- **Slices** – Počet mezikřížových řezu; více řezů poskytuje hladší přechody u zkroucených nebo zúžených extruzí.  
- **Twist Angle** – Celková rotace aplikovaná na profil od začátku do konce, vyjádřeno ve stupních.  
- **Twist Offset** – Lineární posun, který posouvá profil podél osy extruze při otáčení, umožňující spirálové tvary.

## Provádění lineární extruze v Aspose.3D pro Javu

Načtěte svůj profil, nastavte parametry a nechte API vygenerovat síť. Následující kroky popisují typický pracovní postup.

### Krok 1: Definovat 2‑D profil
Vytvořte `Polygon` nebo `Polyline`, který představuje tvar, který chcete extrudovat.  
*`Polygon` představuje uzavřený tvar definovaný vrcholy, zatímco `Polyline` je otevřená řada úseček.*  
Ready to get started? [Provést lineární extruzi nyní](./performing-linear-extrusion/)  
For a detailed tutorial, see [Performing Linear Extrusion in Aspose.3D for Java](./performing-linear-extrusion/).

### Krok 2: Konfigurovat možnosti extruze
Nastavte center, direction, slices, twist a twist offset na objektu `Extrusion`.  
*Třída `Extrusion` zapouzdřuje všechny parametry potřebné k vytvoření 3‑D sítě z 2‑D profilu.*  
Get hands‑on with center control: [Control Center in Linear Extrusion](./controlling-center/)  
Read more about center control: [Controlling Center in Linear Extrusion with Aspose.3D for Java](./controlling-center/)

### Krok 3: Přidat extruzi do scény
Instancujte `Scene`, připojte síť extruze a exportujte do požadovaného formátu.  
*`Scene` je kontejner, který drží všechny 3‑D objekty a zajišťuje export do různých souborových formátů.*  
Ready to set the direction? [Explore Now](./setting-direction/)  
Learn more about direction: [Setting Direction in Linear Extrusion with Aspose.3D for Java](./setting-direction/)

### Krok 4: Exportovat nebo renderovat
Použijte `Scene.save()` k zápisu modelu do OBJ, STL nebo libovolného podporovaného formátu.  
*`Scene.save()` zapíše celou scénu do zvoleného formátu souboru a aplikuje potřebné post‑processing.*  
Start specifying slices: [Learn More](./specifying-slices/)  
Detailed guide: [Specifying Slices in Linear Extrusion with Aspose.3D for Java](./specifying-slices/)

## Jak aplikovat zkroucení na extruzi?
Aplikujte zkroucení nastavením vlastnosti `twistAngle` v možnostech extruze. Engine otáčí každý řez úměrně, čímž vzniká šroubovitý efekt. Úpravou úhlu můžete vytvořit vše od jemného torze po plné 360° spirály, užitečné pro dekorativní prvky nebo funkční pružiny.  
Ready to twist it up? [Apply Twist Now](./applying-twist/)  
Full example: [Applying Twist in Linear Extrusion with Aspose.3D for Java](./applying-twist/)

## Jak použít posun zkroucení pro spirálové tvary?
Posun zkroucení posouvá každý řez podél osy extruze při otáčení, čímž vzniká spirálová schodiště nebo šroubová geometrie. Kombinace úhlu zkroucení s kladným posunem dává hladký šroubový ramp, zatímco záporný posun může vytvořit klesající spirály. Tato technika je ideální pro modelování závitů, pružin nebo uměleckých stuh.  
Enhance your skills: [Learn Twist Offset](./using-twist-offset/)  
Comprehensive guide: [Using Twist Offset in Linear Extrusion with Aspose.3D for Java](./using-twist-offset/)

## Běžné případy použití lineární extruze
- **Mechanical parts** – Rychle generujte šrouby, hřídele a držáky z jednoduchých náčrtů.  
- **Architectural elements** – Extrudujte půdorysy na stěny nebo sloupy pro BIM prototypy.  
- **Game assets** – Vytvořte low‑poly rekvizity jako ploty, potrubí nebo dekorativní zábradlí přímo z 2‑D umění.  
- **Educational tools** – Vizualizujte matematické povrchy extruzí parametrických křivek.

## Řešení běžných problémů
- **Missing faces** – Ujistěte se, že profil je uzavřená smyčka; otevřené obrysy způsobují mezery.  
- **Excessive memory usage** – Snižte počet `slices` nebo povolte `scene.setMemoryOptimization(true)`.  
- **Incorrect twist direction** – Kladné úhly otáčejí ve směru hodinových ručiček při pohledu podél směru extruze; použijte záporné hodnoty pro opačný směr.  

## Často kladené otázky

**Q: Mohu použít Aspose.3D for Java v komerčním projektu?**  
A: Ano, pro produkční použití je vyžadována platná licence Aspose, ale k vyzkoušení je k dispozici bezplatná zkušební verze.

**Q: Jaké verze Javy jsou podporovány?**  
A: Knihovna funguje s Java 8 a novějšími runtime, včetně Java 11, 17 a 21.

**Q: Musím spravovat paměť pro velké extruze?**  
A: Aspose.3D efektivně generuje sítě, ale můžete zavolat `scene.dispose()` po dokončení práce s velkými scénami, aby se uvolnily nativní zdroje.

**Q: Můžu kombinovat více operací extruze v jednom modelu?**  
A: Rozhodně – můžete vytvořit několik objektů extruze, umístit je nezávisle a přidat je do stejné scény.

**Q: Existuje ukázkový kód pro kombinaci zkroucení a posunu zkroucení?**  
A: Ano, tutoriály „Applying Twist“ a „Using Twist Offset“ ukazují, jak nastavit obě vlastnosti na stejném objektu extruze.

**Poslední aktualizace:** 2026-05-24  
**Testováno s:** Aspose.3D for Java 24.11  
**Autor:** Aspose  

{{< blocks/products/products-backtop-button >}}

## Související tutoriály

- [Java 3D Graphics Tutorial – Center in Linear Extrusion](/3d/java/linear-extrusion/controlling-center/)
- [How to Set Direction in Linear Extrusion with Aspose.3D for Java](/3d/java/linear-extrusion/setting-direction/)
- [Create 3D Extrusion with Slices – Aspose.3D for Java](/3d/java/linear-extrusion/specifying-slices/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}