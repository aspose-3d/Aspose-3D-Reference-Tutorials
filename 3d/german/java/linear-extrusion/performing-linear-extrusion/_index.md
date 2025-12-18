---
date: 2025-12-18
description: Erfahren Sie, wie Sie Formen in Java mit Aspose.3D extrudieren, eine
  3D‑Szene erstellen und Wavefront‑OBJ-Dateien mühelos exportieren.
linktitle: How to Extrude Shape in Java with Aspose.3D Linear Extrusion
second_title: Aspose.3D Java API
title: Wie man eine Form in Java mit Aspose.3D linear extrudiert
url: /de/java/linear-extrusion/performing-linear-extrusion/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Lineare Extrusion in Aspose.3D für Java durchführen

## Einleitung

Willkommen zu diesem umfassenden Tutorial, das erklärt, **wie man Formen extrudiert** in Aspose.3D für Java! Wenn Sie Ihre 3D‑Modellierungsfähigkeiten mit Java erweitern möchten, sind Sie hier genau richtig. Wir führen Sie durch das Erstellen einer 3D‑Szene, das Durchführen einer linearen Extrusion und das Exportieren des Ergebnisses als Wavefront‑OBJ‑Datei – alles mit klaren, schrittweisen Code‑Beispielen.

## Schnelle Antworten
- **Was ist lineare Extrusion?** Ein 2D‑Profil entlang eines geraden Pfades ausdehnen, um einen 3D‑Körper zu erzeugen.  
- **Welche Bibliothek erledigt das in Java?** Aspose.3D für Java.  
- **Kann ich nach OBJ exportieren?** Ja, mit der Wavefront‑OBJ‑Exportfunktion.  
- **Benötige ich eine Lizenz für die Entwicklung?** Eine kostenlose Testversion reicht für Tests; für die Produktion ist eine Lizenz erforderlich.  
- **Welche Java‑Version wird benötigt?** Java 1.6 oder neuer.

## Was ist „how to extrude shape“?
Lineare Extrusion ist eine grundlegende Technik im **3d modeling java**, die ein flaches Profil – zum Beispiel ein Rechteck – in ein volumetrisches Objekt verwandelt, indem es über eine definierte Strecke gezogen wird. Diese Methode wird häufig zum Erstellen von mechanischen Bauteilen, architektonischen Elementen und dekorativen Modellen verwendet.

## Warum Aspose.3D für lineare Extrusion verwenden?
- **Vollständige Kontrolle** über Geometrie (Slices, Twist, Offset).  
- **Nahtlose Integration** in Java‑Projekte – keine nativen Abhängigkeiten.  
- **Integrierte Exporter** für gängige Formate, einschließlich Wavefront OBJ, wodurch das **generate 3d model**‑Dateien für nachgelagerte Pipelines leicht erstellt werden können.

## Voraussetzungen

Bevor Sie in das Tutorial einsteigen, stellen Sie sicher, dass die folgenden Voraussetzungen erfüllt sind:

1. **Java-Entwicklungsumgebung** – ein JDK (1.6 oder neuer) und Ihre bevorzugte IDE.  
2. **Aspose.3D-Bibliothek** – laden Sie die Bibliothek von der offiziellen Seite **[here](https://releases.aspose.com/3d/java/)** herunter und installieren Sie sie.

## Pakete importieren

Nachdem Sie Ihre Entwicklungsumgebung eingerichtet und die Aspose.3D‑Bibliothek installiert haben, importieren Sie das erforderliche Paket:

```java
import com.aspose.threed.*;
```

### Schritt 1: Dokumentverzeichnis festlegen

Definieren Sie den Ordner, in dem die erzeugten Dateien gespeichert werden:

```java
String MyDir = "Your Document Directory";
```

> Dies stellt sicher, dass die **generate 3d model**‑Operation die OBJ‑Datei an einem bekannten Ort schreibt.

### Schritt 2: Basisform initialisieren

Erstellen Sie ein Rechteck, das als Extrusionsprofil dient:

```java
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

Sie können den Rundungsradius anpassen, um abgerundete Ecken zu erhalten, oder ihn auf `0` setzen, um ein perfektes Rechteck zu erhalten.

### Schritt 3: Lineare Extrusion durchführen

Jetzt extrudieren wir das Rechteck entlang der Z‑Achse, fügen Slices hinzu, aktivieren das Zentrieren und wenden eine Verdrehung mit einem Offset an:

```java
LinearExtrusion extrusion = new LinearExtrusion(profile, 10) {{ setSlices(100); setCenter(true); setTwist(360); setTwistOffset(new Vector3(10, 0, 0));}};
```

- **Extrusionslänge** – `10` Einheiten.  
- **Slices** – `100` für glatte Geometrie.  
- **Twist** – `360°` erzeugt eine vollständige Umdrehung.  
- **Twist‑Offset** – verschiebt den Ursprung der Verdrehung nach `(10, 0, 0)`.

### Schritt 4: 3D‑Szene erstellen

Erstellen Sie einen Szenen‑Container und fügen Sie die Extrusion als Kindknoten hinzu. Dieser Schritt **creates 3d scene**, das mehrere Objekte aufnehmen kann:

```java
Scene scene = new Scene();
scene.getRootNode().createChildNode(extrusion);
```

### Schritt 5: 3D‑Szene speichern

Exportieren Sie die Szene in eine Wavefront‑OBJ‑Datei. Dies demonstriert die Fähigkeiten von **wavefront obj export** und **save 3d obj**:

```java
scene.save(MyDir +  "LinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

Nach dem Ausführen des Codes finden Sie `LinearExtrusion.obj` im von Ihnen angegebenen Verzeichnis, bereit zum Öffnen in jedem 3D‑Betrachter oder zur Weiterverarbeitung.

## Häufige Probleme und Lösungen

| Problem | Ursache | Lösung |
|---------|---------|--------|
| OBJ-Datei ist leer | Ausgabeverzeichnis-Pfad ist falsch oder nicht beschreibbar | Stellen Sie sicher, dass `MyDir` auf einen existierenden Ordner mit Schreibrechten zeigt. |
| Twist nicht angewendet | `setCenter(true)` wurde weggelassen | Stellen Sie sicher, dass das Zentrieren aktiviert ist, oder passen Sie die Werte von `setTwistOffset` an. |
| Kompilierungsfehler bei `LinearExtrusion` | Verwendung einer älteren Aspose.3D‑Version | Aktualisieren Sie auf die neueste Aspose.3D‑Version. |

## Häufig gestellte Fragen

**Q: Ist Aspose.3D mit allen Java‑Versionen kompatibel?**  
A: Aspose.3D funktioniert mit Java 1.6 und später.

**Q: Kann ich Aspose.3D für kommerzielle Projekte nutzen?**  
A: Ja, die kommerzielle Nutzung ist mit einer gültigen Lizenz erlaubt. Sie können eine Lizenz **[here](https://purchase.aspose.com/buy)** erhalten.

**Q: Wo kann ich Unterstützung erhalten, wenn ich auf Probleme stoße?**  
A: Besuchen Sie das **[Aspose.3D forum](https://forum.aspose.com/c/3d/18)** für Community‑Hilfe oder erwerben Sie eine **[temporary license](https://purchase.aspose.com/temporary-license/)** für Premium‑Support.

**Q: Welche weiteren 3D‑Modellierungsfunktionen bietet Aspose.3D?**  
A: Die Bibliothek enthält Mesh‑Manipulation, Boolesche Operationen, Textur‑Mapping und mehr. Die vollständige Liste finden Sie **[here](https://reference.aspose.com/3d/java/)**.

**Q: Gibt es eine kostenlose Testversion?**  
A: Ja, Sie können eine Testversion **[here](https://releases.aspose.com/)** herunterladen.

## Fazit

Sie haben nun gelernt, **how to extrude shape** mit Aspose.3D für Java zu verwenden, eine 3D‑Szene erstellt und das Ergebnis als Wavefront‑OBJ‑Datei exportiert. Diese Technik eröffnet eine Vielzahl von **3d modeling java**‑Projekten – von einfachen Bauteilen bis zu komplexen Baugruppen. Erkunden Sie zusätzliche Funktionen wie Boolesche Operationen oder Textur‑Mapping, um Ihre Modelle weiter zu bereichern.

---

**Zuletzt aktualisiert:** 2025-12-18  
**Getestet mit:** Aspose.3D 24.11 for Java  
**Autor:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

## ZIEL-KEYWORDS:

**Primary Keyword (HIGHEST PRIORITY):**
how to extrude shape

**Secondary Keywords (SUPPORTING):**
create 3d scene, 3d modeling java, generate 3d model, wavefront obj export, save 3d obj