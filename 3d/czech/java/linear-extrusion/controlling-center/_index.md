---
date: 2025-12-18
description: Naučte se, jak přidat podkladovou rovinu a nastavit vlastnost střed při
  lineární extruzi pomocí Aspose.3D pro Javu, s krok‑za‑krokem ukázkami kódu.
linktitle: Controlling Center in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Jak přidat podkladovou rovinu a řídicí centrum při lineárním extruzi pomocí
  Aspose.3D pro Javu
url: /cs/java/linear-extrusion/controlling-center/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Řízení středu lineární extruze pomocí Aspose.3D pro Java

## Úvod

Když v Javě vytváříte 3D scény, schopnost **přidat podkladovou rovinu** a zároveň přesně **nastavit vlastnost center** u lineární extruze může rozhodnout o rozdílu mezi plochým prototypem a vylepšenou vizualizací. V tomto tutoriálu projdeme kompletní proces řízení středu extruze a přidání podkladové roviny pomocí Aspose.3D pro Java. Uvidíte, proč je to důležité, jak to nastavit, a získáte připravený ukázkový kód, který můžete přizpůsobit svým projektům.

## Rychlé odpovědi
- **Co dělá „add ground plane“?** Vytvoří tenkou referenční geometrii, která vám pomůže vidět polohu extruze vzhledem k světovým osám.  
- **Jak nastavit střed lineární extruze?** Použijte metodu `setCenter(boolean)` na objektu `LinearExtrusion`.  
- **Potřebuji licenci pro spuštění ukázky?** Dočasná licence stačí pro testování; pro produkci je vyžadována plná licence.  
- **Jaký formát souboru se používá pro ukládání?** Příklad ukládá do formátu Wavefront OBJ (`.obj`).  
- **Jaká verze Javy je vyžadována?** Java 8 nebo novější je dostačující.

## Co je „add ground plane“ ve 3D scéně?

Přidání podkladové roviny znamená vložení tenké obdélníkové geometrie (často krabice s minimální tloušťkou), která leží v rovině X‑Z. Funguje jako vizuální podlaha, usnadňuje posouzení výšky a zarovnání ostatních objektů, zejména při experimentování se středy extruze.

## Proč nastavit vlastnost center u lineární extruze?

Ve výchozím nastavení lineární extruze začíná v počátku profilu. Nastavením vlastnosti center (`setCenter(true)`) posunete profil tak, aby extruze byla vycentrována kolem počátku, což je užitečné pro symetrické návrhy nebo když potřebujete konzistentní zarovnání napříč více objekty.

## Předpoklady

Než se pustíme do tohoto tutoriálu, ujistěte se, že máte následující předpoklady:

1. **Java vývojové prostředí** – Zajistěte, aby bylo na vašem počítači nastaveno Java vývojové prostředí.  
2. **Aspose.3D pro Java** – Stáhněte a nainstalujte knihovnu Aspose.3D. Knihovnu a její dokumentaci najdete [zde](https://reference.aspose.com/3d/java/).  
3. **Adresář dokumentů** – Vytvořte adresář pro ukládání vašich Java dokumentů. Nazveme jej „Your Document Directory“.

## Import balíčků

Ve vašem Java vývojovém prostředí importujte potřebné balíčky pro Aspose.3D. Tím zajistíte, že váš kód bude mít přístup k funkcionalitám poskytovaným knihovnou.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Krok 1: Nastavení základního profilu

Inicializujte základní profil, který bude extrudován. V tomto příkladu použijeme tvar obdélníku s poloměrem zaoblení 0.3.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Krok 2: Vytvoření 3D scény

Postavte základ vašeho 3D světa vytvořením scény.

```java
Scene scene = new Scene();
```

## Krok 3: Vytvoření levých a pravých uzlů

Založte levé a pravé uzly ve vaší scéně. Tyto uzly slouží jako plátno pro vaše 3D objekty.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Krok 4: Lineární extruze s vlastností center (levý uzel)

Proveďte lineární extruzi na levém uzlu **bez vycentrování** a nastavte počet řezů na 3. Všimněte si volání `setCenter(false)` – zde **nastavujeme vlastnost center** na *false*.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

## Krok 5: Přidání podkladové roviny pro referenci (levý uzel)

Vylepšete vizuální reprezentaci **přidáním podkladové roviny** k levému uzlu. Tenka krabice funguje jako podlaha, takže můžete jasně vidět výšku extruze.

```java
left.createChildNode(new Box(0.01, 3, 3));
```

## Krok 6: Lineární extruze s vlastností center (pravý uzel)

Nyní proveďte lineární extruzi na pravém uzlu, tentokrát **vycentrovanou**. Volání `setCenter(true)` ukazuje, jak **nastavit vlastnost center** na *true*.

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

## Krok 7: Přidání podkladové roviny pro referenci (pravý uzel)

Stejně jako na levé straně, přidejte podkladovou rovinu k pravému uzlu pro konzistentní vizuální základnu.

```java
right.createChildNode(new Box(0.01, 3, 3));
```

## Krok 8: Uložení 3D scény

Uložte svou 3D scénu ve formátu Wavefront OBJ, abyste ji mohli zobrazit v libovolném standardním 3D prohlížeči.

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Časté problémy a řešení

| Problém | Proč k tomu dochází | Řešení |
|---------|---------------------|--------|
| Podkladová rovina není viditelná | Tloušťka krabice je příliš malá pro měřítko prohlížeče. | Zvyšte tloušťku (první parametr `Box`) nebo oddalte zobrazení v prohlížeči. |
| Extruze je posunutá | Hodnota `setCenter` není nastavena podle očekávání. | Zkontrolujte, jaký boolean je předán metodě `setCenter`. |
| Soubor se neukládá | Nesprávná cesta k adresáři nebo chybějící oprávnění k zápisu. | Ověřte, že `MyDir` ukazuje na existující složku s právy pro zápis. |

## Často kladené otázky

**Q1: Mohu používat Aspose.3D pro Java v komerčních projektech?**  
A1: Ano, Aspose.3D pro Java je k dispozici pro komerční použití. Podrobnosti o licencování najdete [zde](https://purchase.aspose.com/buy).

**Q2: Je k dispozici bezplatná zkušební verze?**  
A2: Ano, můžete vyzkoušet bezplatnou verzi Aspose.3D pro Java [zde](https://releases.aspose.com/).

**Q3: Kde mohu získat podporu pro Aspose.3D pro Java?**  
A3: Fórum komunity Aspose.3D je skvělým místem pro získání podpory a sdílení zkušeností. Navštivte fórum [zde](https://forum.aspose.com/c/3d/18).

**Q4: Potřebuji dočasnou licenci pro testování?**  
A4: Ano, pokud potřebujete dočasnou licenci pro testovací účely, můžete ji získat [zde](https://purchase.aspose.com/temporary-license/).

**Q5: Kde najdu dokumentaci?**  
A5: Dokumentaci pro Aspose.3D pro Java najdete [zde](https://reference.aspose.com/3d/java/).

## Závěr

Řízení středu lineární extruze **a** naučení se, jak **přidat podkladovou rovinu** s Aspose.3D pro Java, otevírá vzrušující možnosti ve vývoji 3D grafiky. Po absolvování výše uvedených kroků máte nyní opakovatelný vzor pro vytváření vycentrovaných extruzí, vizuálních referenčních rovin a export výsledku do OBJ. Nebojte se experimentovat s různými profily, počty řezů a transformacemi, aby vyhovovaly vašim projektovým potřebám.

---

**Poslední aktualizace:** 2025-12-18  
**Testováno s:** Aspose.3D 24.11 pro Java (nejnovější v době psaní)  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}