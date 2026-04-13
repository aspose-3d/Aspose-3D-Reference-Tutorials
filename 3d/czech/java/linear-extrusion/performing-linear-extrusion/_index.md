---
date: 2026-02-25
description: Naučte se, jak vytvořit 3D extruzi v Javě pomocí Aspose.3D a exportovat
  soubor OBJ v Javě, a tím dodávat vysoce kvalitní 3D modely v Java aplikacích.
linktitle: Create 3D Extrusion Java with Aspose.3D
second_title: Aspose.3D Java API
title: Vytvořte 3D extruzi v Javě s Aspose.3D
url: /cs/java/linear-extrusion/performing-linear-extrusion/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Vytvoření 3D extruze v Javě s Aspose.3D

## Úvod

Pokud potřebujete **rychle a spolehlivě vytvořit 3d extruzi v Javě**, jste na správném tutoriálu. V následujících několika minutách si projdeme, jak vygenerovat lineární extruzi, přizpůsobit její geometrii a **exportovat OBJ soubor v Javě** pomocí knihovny Aspose.3D. Ať už budujete nástroj podobný CAD, pipeline pro herní assety nebo jakýkoli Java‑based 3‑D workflow, tento průvodce vám poskytne solidní, produkčně připravený základ.

## Rychlé odpovědi
- **Co znamená „lineární extruze“?** Jedná se o tažení 2‑D profilu podél přímky, čímž vznikne 3‑D těleso.  
- **Která knihovna provádí extruzi?** Aspose.3D pro Java poskytuje vysoce‑úrovňové API.  
- **Mohu výsledek exportovat jako OBJ?** Ano – tutoriál končí voláním `scene.save(..., FileFormat.WAVEFRONTOBJ)`.  
- **Potřebuji licenci pro vývoj?** Pro výuku stačí bezplatná zkušební verze; pro produkci je vyžadována komerční licence.  
- **Jaká verze Javy je podporována?** Java 1.6 a novější.

## Co je Vytvoření 3D extruze v Javě?
Vytvoření 3D extruze v Javě znamená převést jednoduchý 2‑D tvar (např. obdélník) do třetí dimenze. Výsledná síť může být uložena do běžných formátů, jako je OBJ, které rozumí mnohé 3‑D editory.

## Proč použít Aspose.3D pro lineární extruzi?
- **Čisté Java API** – žádné nativní závislosti, ideální pro multiplatformní projekty.  
- **Bohaté ovládání geometrie** – zaoblení, torze, řezy a offset jsou dostupné přes jednoduché vlastnosti.  
- **Přímý export** – ukládání do OBJ, STL, FBX a dalších bez extra konvertorů.  
- **Podpora na úrovni podniku** – licence, dokumentace a komunitní fóra jsou snadno dostupné.

## Požadavky

Než začnete, ujistěte se, že máte:

1. **Vývojové prostředí Java** – nainstalovaný a nakonfigurovaný JDK 1.6+.  
2. **Knihovnu Aspose.3D** – stáhněte nejnovější JAR z oficiální stránky [zde](https://releases.aspose.com/3d/java/).  

## Import balíčků

Přidejte hlavní jmenný prostor Aspose.3D do vašeho Java souboru:

```java
import com.aspose.threed.*;
```

## Krok 1: Nastavení adresáře dokumentu

Definujte, kam budou generované soubory zapisovány:

```java
String MyDir = "Your Document Directory";
```

> **Tip:** Použijte absolutní cestu nebo konfigurovatelnou vlastnost, aby umístění výstupu fungovalo napříč prostředími.

## Krok 2: Inicializace základního tvaru

Vytvořte obdélník, který bude sloužit jako profil extruze. Poloměr zaoblení změkčuje rohy:

```java
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

Můžete experimentovat s `setRoundingRadius` pro získání kulatějšího nebo ostřejšího profilu.

## Krok 3: Provedení lineární extruze

Nyní proměníme 2‑D obdélník na 3‑D objekt. Konstruktor přijímá profil a hloubku extruze (v tomto případě 10 jednotek). Další vlastnosti jemně ladí síť:

```java
LinearExtrusion extrusion = new LinearExtrusion(profile, 10) {{ setSlices(100); setCenter(true); setTwist(360); setTwistOffset(new Vector3(10, 0, 0));}};
```

- **Slices** – řídí hladkost extruze.  
- **Center** – zarovnává geometrii kolem počátku.  
- **Twist** – otáčí profil podél osy extruze (zde plných 360°).  
- **TwistOffset** – posouvá střed otáčení, což ukazuje, jak vytvořit spirály.

## Krok 4: Vytvoření 3D scény

`Scene` je kontejner pro všechny 3‑D objekty. Přidání extruze jako podřízeného uzlu ji zahrne do grafu scény:

```java
Scene scene = new Scene();
scene.getRootNode().createChildNode(extrusion);
```

## Krok 5: Uložení 3D scény

Nakonec exportujte scénu do souboru Wavefront OBJ – formátu široce podporovaného 3‑D editory, herními enginy i tiskovými pipeline:

```java
scene.save(MyDir +  "LinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

Po spuštění kódu najdete **LinearExtrusion.obj** v adresáři, který jste zadali, připravený k otevření v Blenderu, Maye nebo jakémkoli jiném prohlížeči podporujícím OBJ.

## Časté problémy a řešení

| Příznak | Pravděpodobná příčina | Oprava |
|---------|-----------------------|--------|
| `FileNotFoundException` při ukládání | `MyDir` neexistuje nebo nemá oprávnění k zápisu | Vytvořte složku předem nebo použijte absolutní cestu s odpovídajícími oprávněními. |
| OBJ se v prohlížeči zobrazuje prázdně | Do scény nebyla přidána geometrie | Ověřte, že objekt `LinearExtrusion` je správně vytvořen a připojen k kořenovému uzlu. |
| Torze vypadá špatně | Nesprávné hodnoty `TwistOffset` | Upravte souřadnice `Vector3`; pamatujte, že offset se aplikuje před rotací torze. |

## Často kladené otázky

### Q1: Je Aspose.3D kompatibilní se všemi verzemi Javy?
A1: Aspose.3D je navrženo tak, aby fungovalo s Java 1.6 a novějšími verzemi.

### Q2: Mohu použít Aspose.3D v komerčních projektech?
A2: Ano, Aspose.3D může být použito jak pro osobní, tak pro komerční projekty. Podrobnosti o licencování najdete [zde](https://purchase.aspose.com/buy).

### Q3: Jak získám podporu pro Aspose.3D?
A3: Navštivte [forum Aspose.3D](https://forum.aspose.com/c/3d/18) pro komunitní podporu nebo zvažte zakoupení [dočasné licence](https://purchase.aspose.com/temporary-license/) pro prémiovou podporu.

### Q4: Existují v Aspose.3D i další funkce pro 3D modelování?
A4: Rozhodně! Prozkoumejte rozsáhlou dokumentaci [zde](https://reference.aspose.com/3d/java/) pro kompletní seznam funkcí a příkladů.

### Q5: Je k dispozici bezplatná zkušební verze Aspose.3D?
A5: Ano, bezplatnou zkušební verzi získáte [zde](https://releases.aspose.com/).

## Závěr

Nyní víte, jak **vytvořit 3d extruzi v Javě** pomocí Aspose.3D, přizpůsobit její geometrii a **exportovat OBJ soubor v Javě** pro další použití. Experimentujte s různými profily, torzemi a výstupními formáty, aby vyhovovaly vašim konkrétním potřebám. Až budete připraveni, prozkoumejte další možnosti Aspose.3D, jako je manipulace s meshí, mapování textur a animace, a ještě více obohaťte své Java‑based 3‑D aplikace.

---

**Poslední aktualizace:** 2026-02-25  
**Testováno s:** Aspose.3D 24.12 pro Java  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}