---
date: 2025-12-17
description: Scopri come impostare la licenza in Aspose.3D per Java e come utilizzare
  chiavi pubbliche e private per la licenza a consumo.
linktitle: Applying a License in Aspose.3D for Java
second_title: Aspose.3D Java API
title: Come impostare la licenza in Aspose.3D per Java – Guida completa
url: /it/java/licensing/applying-license-in-aspose-3d/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Come impostare la licenza in Aspose.3D per Java

## Introduzione

Benvenuti! In questo tutorial passo‑per‑passo scoprirete **come impostare la licenza** per Aspose.3D in un'applicazione Java e imparerete anche **come utilizzare chiavi pubbliche e private** per la licenza a consumo. Aspose.3D è una potente libreria Java che semplifica il lavoro con i formati di file 3D, e una licenza valida sblocca l'intero set di funzionalità. Alla fine di questa guida sarete in grado di integrare la licenza senza problemi in qualsiasi progetto Java.

## Risposte rapide
- **Qual è il modo principale per impostare una licenza?** Utilizzare la classe `License` e chiamare `setLicense` con un percorso file o uno stream.  
- **Posso caricare la licenza da uno stream?** Sì – un `FileInputStream` funziona perfettamente.  
- **A cosa servono le chiavi pubbliche/private?** Consentono la licenza a consumo tramite la classe `Metered`.  
- **Ho bisogno di una licenza per lo sviluppo?** Una licenza temporanea o di prova è sufficiente per i test; è necessaria una licenza completa per la produzione.  
- **Quali versioni di Java sono supportate?** Aspose.3D funziona con Java 6 e versioni successive.

## Prerequisiti

Prima di iniziare, assicuratevi di avere:

- Una conoscenza di base della programmazione Java.  
- La libreria Aspose.3D aggiunta al vostro progetto. Scaricatela dalla [pagina di rilascio](https://releases.aspose.com/3d/java/).  
- Un file `.lic` valido o le vostre chiavi pubbliche e private per la licenza a consumo.

## Importare i pacchetti

Aggiungete gli import necessari al vostro file sorgente Java. Assicuratevi che il JAR di Aspose.3D sia nel classpath.

```java
import com.aspose.threed.License;
import com.aspose.threed.Metered;

import java.io.FileInputStream;
import java.io.IOException;
```

## Come impostare la licenza usando un file

### Passo 1: Creare un oggetto License

Istanziare la classe `License` – questo oggetto conterrà le informazioni di licenza.

```java
License license = new License();
```

### Passo 2: Impostare la licenza da file

Fornite il percorso relativo o assoluto al vostro file `.lic` e applicatelo.

```java
license.setLicense("Aspose._3D.lic");
```

> **Suggerimento professionale:** Tenete il file di licenza al di fuori della directory di controllo versione per evitare esposizioni accidentali.

## Come impostare la licenza usando uno stream

### Passo 1: Creare un oggetto License

Come prima, iniziate con una nuova istanza di `License`.

```java
License license = new License();
```

### Passo 2: Impostare la licenza da uno stream

Leggete il file di licenza in un `FileInputStream` e passate lo stream a `setLicense`. Il blocco try‑with‑resources garantisce che lo stream venga chiuso automaticamente.

```java
try (FileInputStream myStream = new FileInputStream("Aspose._3D.lic")) {
    license.setLicense(myStream);
}
```

## Come utilizzare chiavi pubbliche e private per la licenza a consumo

### Passo 1: Inizializzare un oggetto di licenza Metered

Create un'istanza della classe `Metered`, che gestisce la licenza a consumo (pay‑as‑you‑go).

```java
Metered metered = new Metered();
```

### Passo 2: Impostare le chiavi pubbliche e private

Fornite le chiavi ricevute da Aspose. Queste chiavi consentono alla libreria di segnalare l'utilizzo al server di licenza.

```java
metered.setMeteredKey("your-public-key", "your-private-key");
```

> **Attenzione:** Non codificate mai in modo fisso la vostra chiave privata in un JAR distribuito pubblicamente. Considerate di caricarla da una posizione sicura o da una variabile d'ambiente.

## Casi d'uso comuni

- **Pipeline di rendering 3D aziendali** – sbloccate le API ad alte prestazioni dopo aver impostato la licenza.  
- **Ambienti di test automatizzati** – usate una licenza temporanea (vedi le FAQ) per convalidare le funzionalità senza acquistare una licenza completa.  
- **Soluzioni SaaS a consumo** – integrate chiavi pubbliche/private per fatturare i clienti in base all'uso reale.

## Conclusione

Congratulazioni! Ora sapete **come impostare la licenza** per Aspose.3D in Java usando un file, uno stream, e come **utilizzare chiavi pubbliche e private** per la licenza a consumo. Con questi passaggi potete integrare con sicurezza Aspose.3D in qualsiasi applicazione Java e sfruttare appieno le sue capacità di elaborazione 3D.

## Domande frequenti

**Q1: Aspose.3D è compatibile con tutte le versioni di Java?**  
A1: Sì, Aspose.3D funziona con Java 6 e versioni successive.

**Q2: Dove posso trovare documentazione aggiuntiva?**  
A2: Potete consultare la documentazione [qui](https://reference.aspose.com/3d/java/).

**Q3: Posso provare Aspose.3D prima di acquistarlo?**  
A3: Sì, potete esplorare una prova gratuita [qui](https://releases.aspose.com/).

**Q4: Come posso ottenere supporto per Aspose.3D?**  
A4: Visitate il [Forum Aspose.3D](https://forum.aspose.com/c/3d/18) per il supporto della community e ufficiale.

**Q5: È necessaria una licenza temporanea per i test?**  
A5: Sì, ottenete una licenza temporanea [qui](https://purchase.aspose.com/temporary-license/).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}
{{< blocks/products/products-backtop-button >}}

---

**Ultimo aggiornamento:** 2025-12-17  
**Testato con:** Aspose.3D 24.11 per Java  
**Autore:** Aspose