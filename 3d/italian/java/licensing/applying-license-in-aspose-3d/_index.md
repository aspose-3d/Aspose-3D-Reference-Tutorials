---
date: 2026-02-14
description: Scopri come impostare la licenza Aspose in Aspose.3D per Java, incluso
  come applicare la licenza da file e impostare le chiavi pubbliche e private.
linktitle: How to Set Aspose License in Aspose.3D for Java
second_title: Aspose.3D Java API
title: Come impostare la licenza Aspose in Aspose.3D per Java
url: /it/java/licensing/applying-license-in-aspose-3d/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Come impostare la licenza Aspose in Aspose.3D per Java

## Introduzione

In questo tutorial completo scoprirai **come impostare la licenza Aspose** per Aspose.3D in un ambiente Java. Che tu preferisca caricare un file di licenza, trasmetterlo in streaming o utilizzare la licenza a consumo con chiavi pubbliche e private, ti guideremo passo‑passo in ciascun approccio così potrai sbloccare rapidamente e con sicurezza l’intero set di funzionalità di Aspose.3D.

## Risposte rapide
- **Qual è il modo principale per impostare una licenza Aspose.3D?** Usa la classe `License` e chiama `setLicense` con un percorso file o uno stream.  
- **Posso caricare la licenza da uno stream?** Sì – avvolgi il file `.lic` in un `FileInputStream` e passalo a `setLicense`.  
- **Cosa fare se ho bisogno di una licenza a consumo?** Inizializza un oggetto `Metered` e chiama `setMeteredKey` con le tue chiavi pubblica e privata.  
- **È necessaria una licenza per le build di sviluppo?** È richiesta una licenza di prova o temporanea per qualsiasi scenario non di valutazione.  
- **Quali versioni di Java sono supportate?** Aspose.3D funziona con Java 6 e successive.

## Prerequisiti

Prima di iniziare, assicurati di avere i seguenti prerequisiti:

- Conoscenza di base della programmazione Java.  
- Libreria Aspose.3D installata. Puoi scaricarla dalla [pagina di rilascio](https://releases.aspose.com/3d/java/).  

## Importare i pacchetti

Per iniziare, importa i pacchetti necessari nel tuo progetto Java. Assicurati che Aspose.3D sia aggiunto al classpath. Ecco un esempio:

```java
import com.aspose.threed.License;
import com.aspose.threed.Metered;

import java.io.FileInputStream;
import java.io.IOException;
```

## Applicare una licenza usando un file

### Passo 1: Creare un oggetto License

Innanzitutto, crea un oggetto `License` nel tuo codice Java.

```java
License license = new License();
```

### Passo 2: Applicare la licenza dal file

Specifica il percorso al tuo file di licenza e imposta la licenza usando il codice seguente. Questo dimostra la tecnica **applicare licenza da file**.

```java
license.setLicense("Aspose._3D.lic");
```

## Applicare una licenza usando un oggetto Stream

### Passo 1: Creare un oggetto License

Analogamente, crea un oggetto `License` nel tuo codice Java.

```java
License license = new License();
```

### Passo 2: Impostare la licenza dallo Stream

Utilizza un `FileInputStream` per creare uno stream e impostare la licenza:

```java
try (FileInputStream myStream = new FileInputStream("Aspose._3D.lic")) {
    license.setLicense(myStream);
}
```

## Utilizzare chiavi pubbliche e private per la licenza a consumo

### Passo 1: Inizializzare l'oggetto licenza Metered

Inizializza un oggetto licenza `Metered`:

```java
Metered metered = new Metered();
```

### Passo 2: Impostare le chiavi pubbliche e private

Imposta le tue chiavi pubblica e privata per abilitare la licenza a consumo. Questo copre lo scenario **impostare chiavi pubbliche private**.

```java
metered.setMeteredKey("your-public-key", "your-private-key");
```

## Perché impostare la licenza è importante

Applicare la licenza corretta rimuove le filigrane di valutazione, sblocca i formati di file premium e garantisce la conformità al modello di licenza di Aspose. Utilizzare il metodo appropriato (file, stream o a consumo) ti permette di integrare la licenza senza problemi nei pipeline CI/CD, nelle distribuzioni cloud o nelle applicazioni desktop.

## Problemi comuni e consigli

- **File non trovato** – Verifica che il percorso del file `.lic` sia corretto rispetto alla directory di lavoro o utilizza un percorso assoluto.  
- **Stream chiuso prematuramente** – Quando usi uno stream, mantieni vivo l'oggetto `License` per tutta la durata dell'applicazione; la licenza viene memorizzata nella cache dopo la prima chiamata riuscita.  
- **Mancata corrispondenza della chiave Metered** – Controlla che le chiavi pubblica e privata corrispondano alla stessa licenza a consumo; un errore di battitura causerà un'eccezione a runtime.  
- **Suggerimento professionale:** Conserva il file di licenza in una posizione sicura al di fuori dell’albero sorgente e caricalo tramite una variabile d’ambiente per evitare di commetterlo nel controllo versione.

## Conclusione

Congratulazioni! Hai appreso con successo **come impostare la licenza Aspose** in Aspose.3D per Java utilizzando vari metodi, inclusi l’applicazione della licenza da file, lo streaming e la configurazione della licenza a consumo con chiavi pubbliche e private. Ora puoi integrare Aspose.3D senza problemi nelle tue applicazioni Java e sfruttare appieno le sue capacità di elaborazione 3D.

## Domande frequenti

**D: Aspose.3D è compatibile con tutte le versioni di Java?**  
R: Sì, Aspose.3D è compatibile con Java 6 e versioni successive.

**D: Dove posso trovare documentazione aggiuntiva?**  
R: Puoi consultare la documentazione [qui](https://reference.aspose.com/3d/java/).

**D: Posso provare Aspose.3D prima di acquistarlo?**  
R: Sì, puoi esplorare una prova gratuita [qui](https://releases.aspose.com/).

**D: Come posso ottenere supporto per Aspose.3D?**  
R: Visita il [Forum Aspose.3D](https://forum.aspose.com/c/3d/18) per il supporto.

**D: È necessaria una licenza temporanea per i test?**  
R: Sì, ottieni una licenza temporanea [qui](https://purchase.aspose.com/temporary-license/).

**D: Qual è la differenza tra una licenza file e una licenza a consumo?**  
R: Una licenza file è un file `.lic` statico legato a una versione specifica del prodotto, mentre una licenza a consumo valida l'uso tramite il servizio di metering basato su cloud di Aspose usando chiavi pubbliche/ private.

**D: Posso incorporare il codice di caricamento della licenza in un inizializzatore statico?**  
R: Assolutamente – posizionare l’inizializzazione di `License` in un blocco statico garantisce che la licenza venga applicata una sola volta quando la classe viene caricata per la prima volta.

---

**Ultimo aggiornamento:** 2026-02-14  
**Testato con:** Aspose.3D 24.11 per Java  
**Autore:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}