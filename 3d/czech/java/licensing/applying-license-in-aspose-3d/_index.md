---
date: 2026-05-24
description: Zjistěte, jak nastavit licenci aspose 3d v Javě, použít license file,
  streamovat jej nebo použít metered licensing s public and private keys.
keywords:
- set aspose 3d license
- aspose 3d java licensing
- metered licensing java
linktitle: Jak nastavit licenci Aspose v Aspose.3D pro Java
schemas:
- author: Aspose
  dateModified: '2026-05-24'
  description: Learn how to set aspose 3d license in Java, apply a license file, stream
    it, or use metered licensing with public and private keys.
  headline: How to Set Aspose 3D License in Java (set aspose 3d license)
  type: TechArticle
- description: Learn how to set aspose 3d license in Java, apply a license file, stream
    it, or use metered licensing with public and private keys.
  name: How to Set Aspose 3D License in Java (set aspose 3d license)
  steps:
  - name: Create a `License` object
    text: Instantiate the `License` class; this prepares the runtime to accept a license
      file.
  - name: Apply the license file
    text: Provide the absolute or relative path to your `.lic` file and call `setLicense`.
      The method returns `void`, and the license is cached after the first successful
      call, so subsequent calls are inexpensive.
  - name: Create a `License` object
    text: As before, start by creating an instance of the `License` class.
  - name: Load the license via `FileInputStream`
    text: Open a `FileInputStream` pointing to your `.lic` file (or any `InputStream`)
      and pass it to `setLicense`. The stream is read once and then closed automatically.
  - name: Initialize a `Metered` license object
    text: The `Metered` class represents a cloud‑based license that validates usage
      against Aspose’s metering server.
  - name: Set public and private keys
    text: Call `setMeteredKey(publicKey, privateKey)` with the keys you received when
      you purchased a metered license. The library contacts the server once to verify
      the keys and then caches the result.
  type: HowTo
- questions:
  - answer: Yes, Aspose.3D supports Java 6 through Java 21, covering more than 15
      major releases.
    question: Is Aspose.3D compatible with all Java versions?
  - answer: You can refer to the documentation [here](https://reference.aspose.com/3d/java/).
    question: Where can I find additional documentation?
  - answer: Yes, you can explore a free trial [here](https://releases.aspose.com/).
    question: Can I try Aspose.3D before purchasing?
  - answer: Visit the [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) for support.
    question: How can I get support for Aspose.3D?
  - answer: Yes, obtain a temporary license [here](https://purchase.aspose.com/temporary-license/).
    question: Do I need a temporary license for testing?
  type: FAQPage
second_title: Aspose.3D Java API
title: Jak nastavit licenci Aspose 3D v Javě (nastavit aspose 3d licenci)
url: /cs/java/licensing/applying-license-in-aspose-3d/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Jak nastavit licenci Aspose 3D v Javě (nastavit licenci aspose 3d)

## Úvod

V tomto komplexním tutoriálu objevíte **how to set aspose 3d license** pro Aspose.3D v prostředí Java. Ať už dáváte přednost načtení licenčního souboru, streamování nebo použití měřeného licencování s veřejnými a soukromými klíči, projdeme každý přístup krok za krokem, abyste mohli rychle a sebejistě odemknout plnou sadu funkcí Aspose.3D. Správné nastavení licence odstraňuje vodoznaky hodnocení, umožňuje prémiové 3D formáty a zajišťuje úplnou shodu s licenčním modelem Aspose.

## Rychlé odpovědi
- **Jaký je hlavní způsob nastavení licence Aspose.3D?** Použijte třídu `License` a zavolejte `setLicense` s cestou k souboru nebo streamem.  
- **Mohu načíst licenci ze streamu?** Ano – zabalte soubor `.lic` do `FileInputStream` a předáte jej `setLicense`.  
- **Co když potřebuji měřenou licenci?** Inicializujte objekt `Metered` a zavolejte `setMeteredKey` s vašimi veřejnými a soukromými klíči.  
- **Potřebuji licenci pro vývojové sestavení?** Pro jakýkoli ne‑evaluační scénář je vyžadována zkušební nebo dočasná licence.  
- **Které verze Javy jsou podporovány?** Aspose.3D funguje s Java 6 až Java 21, pokrývá více než 15 hlavních vydání.

## Co je třída `License`?
Třída `License` je hlavní licenční objekt Aspose.3D, který načte soubor `.lic` do paměti, ověří licenční informace a po vytvoření aplikuje licenci globálně pro proces JVM, čímž zajišťuje, že všechny následné operace Aspose.3D běží v licencovaném režimu bez evaluačních omezení.

## Proč nastavit licenci Aspose 3D?
Aplikace platné licence umožňuje **více než 50 prémiových 3D formátů souborů** (včetně FBX, OBJ, STL a GLTF) a odstraňuje vodoznak „Evaluation“ z renderovaných obrázků. Také zruší omezení velikosti scény, což umožňuje zpracování modelů s **až 1 milionem vrcholů** bez zhoršení výkonu.

## Předpoklady

Než začneme, ujistěte se, že máte následující předpoklady:

- Základní znalost programování v Javě.  
- Knihovna Aspose.3D nainstalována. Můžete si ji stáhnout ze [stránky vydání](https://releases.aspose.com/3d/java/).

## Import balíčků

Pro zahájení importujte potřebné balíčky do vašeho Java projektu. Ujistěte se, že Aspose.3D je přidáno do classpath. Zde je příklad:

```java
import com.aspose.threed.License;
import com.aspose.threed.Metered;

import java.io.FileInputStream;
import java.io.IOException;
```

Třída `License` je zodpovědná za načtení souboru `.lic` a jeho globální aplikaci, zatímco třída `Metered` umožňuje cloud‑založené měřené licencování ověřováním veřejných a soukromých klíčů proti licenčnímu serveru Aspose.

## Jak aplikovat licenci ze souboru?

Načtěte licenci přímo ze souboru `.lic` na disku. Tato metoda je nejjednodušší přístup pro desktopové nebo on‑premise aplikace a zajišťuje, že licence je načtena jednou při spuštění a uložena do mezipaměti po celou dobu běhu JVM, čímž eliminuje jakékoli runtime zatížení po úvodním načtení.

### Krok 1: Vytvořte objekt `License`
Instancujte třídu `License`; tím připravíte runtime k přijetí licenčního souboru.

### Krok 2: Aplikujte licenční soubor
Zadejte absolutní nebo relativní cestu k vašemu souboru `.lic` a zavolejte `setLicense`. Metoda vrací `void` a licence je uložena do mezipaměti po prvním úspěšném volání, takže následná volání jsou levná.

```java
import com.aspose.threed.License;
import com.aspose.threed.Metered;

import java.io.FileInputStream;
import java.io.IOException;
```

## Jak aplikovat licenci ze streamu?

Streamování licence je užitečné, když je soubor vložen jako zdroj, uložen na zabezpečeném místě nebo načten ze vzdálené služby za běhu. Použitím `InputStream` se vyhnete odhalení fyzické cesty k souboru a můžete udržet licenční data šifrovaná nebo zabalená uvnitř vašeho JAR, čímž zvyšujete bezpečnost a zároveň umožňujete knihovně číst bajty licence.

### Krok 1: Vytvořte objekt `License`
Stejně jako předtím, začněte vytvořením instance třídy `License`.

### Krok 2: Načtěte licenci pomocí `FileInputStream`
Otevřete `FileInputStream` ukazující na váš soubor `.lic` (nebo jakýkoli `InputStream`) a předáte jej `setLicense`. Stream je načten jednou a poté automaticky uzavřen.

```java
License license = new License();
```

## Jak použít veřejné a soukromé klíče pro měřené licencování?

Měřené licencování vám umožní aktivovat Aspose.3D bez fyzického souboru `.lic` pomocí klíčů vydaných cloudovou službou Aspose. Tento přístup je ideální pro SaaS nebo cloud‑založené nasazení, kde je správa licenčních souborů na každé instanci nepraktická; knihovna se jednou spojí s metrickým serverem Aspose, aby ověřila klíče, a výsledek uloží do mezipaměti pro relaci.

### Krok 1: Inicializujte licenční objekt `Metered`
Třída `Metered` představuje cloud‑založenou licenci, která ověřuje využití proti metrickému serveru Aspose.

### Krok 2: Nastavte veřejný a soukromý klíč
Zavolejte `setMeteredKey(publicKey, privateKey)` s klíči, které jste obdrželi při zakoupení měřené licence. Knihovna se jednou spojí se serverem pro ověření klíčů a poté výsledek uloží do mezipaměti.

```java
license.setLicense("Aspose._3D.lic");
```

## Časté problémy a tipy

- **Soubor nenalezen** – Ověřte, že cesta k souboru `.lic` je správná vzhledem k pracovnímu adresáři nebo použijte absolutní cestu.  
- **Stream uzavřen předčasně** – Při použití streamu udržujte objekt `License` živý po celou dobu běhu aplikace; licence je uložena do mezipaměti po prvním úspěšném volání.  
- **Neshoda měřených klíčů** – Dvakrát zkontrolujte, že veřejný a soukromý klíč odpovídají stejné měřené licenci; překlep způsobí výjimku za běhu.  
- **Pro tip:** Uložte licenční soubor na zabezpečené místo mimo zdrojový strom a načtěte jej pomocí proměnné prostředí, abyste se vyhnuli jeho zařazení do verzovacího systému.

## Závěr

Gratulujeme! Úspěšně jste se naučili **how to set aspose 3d license** v Javě pomocí tří spolehlivých metod: aplikace licence ze souboru, streamování a konfigurace měřeného licencování s veřejnými a soukromými klíči. S licencí na místě můžete nyní bez problémů integrovat Aspose.3D do vašich Java aplikací, odemknout všechny prémiové funkce 3D zpracování a splnit licenční požadavky Aspose.

## Často kladené otázky

**Q: Je Aspose.3D kompatibilní se všemi verzemi Javy?**  
A: Ano, Aspose.3D podporuje Java 6 až Java 21, pokrývá více než 15 hlavních vydání.

**Q: Kde mohu najít další dokumentaci?**  
A: Dokumentaci můžete najít [zde](https://reference.aspose.com/3d/java/).

**Q: Mohu vyzkoušet Aspose.3D před zakoupením?**  
A: Ano, můžete si vyzkoušet bezplatnou verzi [zde](https://releases.aspose.com/).

**Q: Jak mohu získat podporu pro Aspose.3D?**  
A: Navštivte [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) pro podporu.

**Q: Potřebuji dočasnou licenci pro testování?**  
A: Ano, získáte dočasnou licenci [zde](https://purchase.aspose.com/temporary-license/).

**Q: Jaký je rozdíl mezi souborovou licencí a měřenou licencí?**  
A: Souborová licence je statický soubor `.lic` svázaný s konkrétní verzí produktu, zatímco měřená licence ověřuje využití proti cloud‑založené metrické službě Aspose pomocí veřejných/soukromých klíčů.

**Q: Mohu vložit kód načítání licence do statického inicializátoru?**  
A: Rozhodně – umístění inicializace `License` do statického bloku zajistí, že licence bude aplikována jednou při prvním načtení třídy.

```java
License license = new License();
```
```java
try (FileInputStream myStream = new FileInputStream("Aspose._3D.lic")) {
    license.setLicense(myStream);
}
```
```java
Metered metered = new Metered();
```
```java
metered.setMeteredKey("your-public-key", "your-private-key");
```

{{< blocks/products/products-backtop-button >}}

## Související tutoriály

- [Postupný průvodce licencí pro Aspose.3D Java](/3d/java/licensing/)
- [Vytvořte 3D scénu v Javě s Aspose 3D Java](/3d/java/3d-scenes-and-models/)
- [Vytvořte 3D krychli, aplikujte PBR materiály v Javě s Aspose.3D](/3d/java/geometry/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}