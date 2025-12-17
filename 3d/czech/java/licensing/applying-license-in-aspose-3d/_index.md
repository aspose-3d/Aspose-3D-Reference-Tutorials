---
date: 2025-12-17
description: Naučte se, jak nastavit licenci v Aspose.3D pro Javu a jak používat veřejné
  a soukromé klíče pro měřenou licenci.
linktitle: Applying a License in Aspose.3D for Java
second_title: Aspose.3D Java API
title: Jak nastavit licenci v Aspose.3D pro Javu – kompletní průvodce
url: /cs/java/licensing/applying-license-in-aspose-3d/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Jak nastavit licenci v Aspose.3D pro Java

## Úvod

Vítejte! V tomto krok‑za‑krokem tutoriálu objevíte **jak nastavit licenci** pro Aspose.3D v Java aplikaci a také se naučíte **jak používat veřejné a soukromé klíče** pro měřenou licenci. Aspose.3D je výkonná Java knihovna, která usnadňuje práci s 3D formáty souborů, a platná licence odemkne celý její funkční soubor. Na konci tohoto průvodce budete schopni bez problémů integrovat licencování do jakéhokoli Java projektu.

## Rychlé odpovědi
- **Jaký je hlavní způsob nastavení licence?** Použijte třídu `License` a zavolejte `setLicense` s cestou k souboru nebo streamem.  
- **Mohu načíst licenci ze streamu?** Ano – `FileInputStream` funguje perfektně.  
- **K čemu slouží veřejné/soukromé klíče?** Umožňují měřenou licenci pomocí třídy `Metered`.  
- **Potřebuji licenci pro vývoj?** Dočasná nebo zkušební licence stačí pro testování; pro produkci je vyžadována plná licence.  
- **Které verze Javy jsou podporovány?** Aspose.3D funguje s Javou 6 a novějšími.

## Požadavky

Než začneme, ujistěte se, že máte:

- Základní znalosti programování v Javě.  
- Knihovnu Aspose.3D přidanou do vašeho projektu. Stáhněte ji ze [stránky vydání](https://releases.aspose.com/3d/java/).  
- Platný soubor `.lic` nebo vaše veřejné a soukromé měřené klíče.

## Import balíčků

Přidejte požadované importy do vašeho Java zdrojového souboru. Ujistěte se, že JAR Aspose.3D je v classpath.

```java
import com.aspose.threed.License;
import com.aspose.threed.Metered;

import java.io.FileInputStream;
import java.io.IOException;
```

## Jak nastavit licenci pomocí souboru

### Krok 1: Vytvořte objekt License

Vytvořte instanci třídy `License` – tento objekt bude obsahovat informace o licenci.

```java
License license = new License();
```

### Krok 2: Nastavte licenci ze souboru

Zadejte relativní nebo absolutní cestu k vašemu souboru `.lic` a použijte ji.

```java
license.setLicense("Aspose._3D.lic");
```

> **Tip:** Uchovávejte soubor licence mimo adresář se zdrojovým kódem, aby nedošlo k neúmyslnému odhalení.

## Jak nastavit licenci pomocí streamu

### Krok 1: Vytvořte objekt License

Stejně jako předtím, začněte s novou instancí `License`.

```java
License license = new License();
```

### Krok 2: Nastavte licenci ze streamu

Načtěte soubor licence do `FileInputStream` a předávejte stream metodě `setLicense`. Blok try‑with‑resources zaručuje automatické uzavření streamu.

```java
try (FileInputStream myStream = new FileInputStream("Aspose._3D.lic")) {
    license.setLicense(myStream);
}
```

## Jak používat veřejné a soukromé klíče pro měřenou licenci

### Krok 1: Inicializujte objekt Metered License

Vytvořte instanci třídy `Metered`, která spravuje měřenou (pay‑as‑you‑go) licenci.

```java
Metered metered = new Metered();
```

### Krok 2: Nastavte veřejný a soukromý klíč

Poskytněte klíče, které jste obdrželi od Aspose. Tyto klíče umožňují knihovně hlásit využití zpět na licenční server.

```java
metered.setMeteredKey("your-public-key", "your-private-key");
```

> **Varování:** Nikdy neukládejte soukromý klíč přímo v JAR distribuovaném veřejně. Zvažte načtení z bezpečného umístění nebo proměnné prostředí.

## Běžné případy použití

- **Enterprise 3D rendering pipelines** – odemkněte vysoce výkonné API po nastavení licence.  
- **Automatizovaná testovací prostředí** – použijte dočasnou licenci (viz FAQ) k ověření funkčnosti bez zakoupení plné licence.  
- **Měřená SaaS řešení** – integrujte veřejné/soukromé klíče pro fakturaci zákazníků na základě skutečného využití.

## Závěr

Gratulujeme! Nyní víte **jak nastavit licenci** pro Aspose.3D v Javě pomocí souboru, streamu a také **jak používat veřejné a soukromé klíče** pro měřenou licenci. S těmito kroky můžete sebejistě integrovat Aspose.3D do jakékoli Java aplikace a plně využít jeho 3D zpracovatelské schopnosti.

## Často kladené otázky

**Q1: Je Aspose.3D kompatibilní se všemi verzemi Javy?**  
A1: Ano, Aspose.3D funguje s Javou 6 a novějšími verzemi.

**Q2: Kde mohu najít další dokumentaci?**  
A2: Dokumentaci můžete najít [zde](https://reference.aspose.com/3d/java/).

**Q3: Můžu si Aspose.3D vyzkoušet před zakoupením?**  
A3: Ano, můžete si vyzkoušet bezplatnou verzi [zde](https://releases.aspose.com/).

**Q4: Jak mohu získat podporu pro Aspose.3D?**  
A4: Navštivte [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) pro komunitní a oficiální podporu.

**Q5: Potřebuji dočasnou licenci pro testování?**  
A5: Ano, získat dočasnou licenci můžete [zde](https://purchase.aspose.com/temporary-license/).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}
{{< blocks/products/products-backtop-button >}}

---

**Poslední aktualizace:** 2025-12-17  
**Testováno s:** Aspose.3D 24.11 for Java  
**Autor:** Aspose  

---