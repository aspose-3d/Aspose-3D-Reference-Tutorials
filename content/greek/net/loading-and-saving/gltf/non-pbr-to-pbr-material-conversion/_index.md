---
title: Μετατροπή υλικού χωρίς PBR σε PBR
linktitle: Μετατροπή υλικού χωρίς PBR σε PBR
second_title: Aspose.3D .NET API
description: Εξερευνήστε το Aspose.3D για .NET - Μετατρέψτε υλικά που δεν είναι PBR σε PBR χωρίς κόπο. Ολοκληρωμένο σεμινάριο και ισχυρό API.
type: docs
weight: 16
url: /el/net/loading-and-saving/gltf/non-pbr-to-pbr-material-conversion/
---
## Εισαγωγή

Καλώς ήρθατε σε αυτόν τον αναλυτικό οδηγό σχετικά με τη χρήση του Aspose.3D για .NET για τη μετατροπή Non-PBR (Physically Based Rendering) σε υλικά PBR. Το Aspose.3D είναι ένα ισχυρό API που επιτρέπει στους προγραμματιστές να εργάζονται απρόσκοπτα με τρισδιάστατες μορφές αρχείων στις εφαρμογές τους .NET.

## Προαπαιτούμενα

Πριν ξεκινήσουμε το σεμινάριο, βεβαιωθείτε ότι έχετε τις ακόλουθες προϋποθέσεις:

-  Aspose.3D για .NET: Βεβαιωθείτε ότι έχετε εγκαταστήσει τη βιβλιοθήκη Aspose.3D για .NET. Μπορείτε να βρείτε τον σύνδεσμο λήψης[εδώ](https://releases.aspose.com/3d/net/).

- Βασική κατανόηση της C#: Αυτό το σεμινάριο προϋποθέτει ότι έχετε μια θεμελιώδη κατανόηση του προγραμματισμού C#.

- IDE (Integrated Development Environment): Επιλέξτε το IDE που προτιμάτε για την ανάπτυξη .NET, όπως το Visual Studio.

## Εισαγωγή χώρων ονομάτων

Στον κώδικα C#, ξεκινήστε εισάγοντας τους απαραίτητους χώρους ονομάτων:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
```

## Βήμα 1: Αρχικοποιήστε μια νέα τρισδιάστατη σκηνή

Ξεκινήστε δημιουργώντας μια νέα τρισδιάστατη σκηνή χρησιμοποιώντας τον ακόλουθο κώδικα:

```csharp
// ExStart:Non_PBRtoPBRMaterial
// αρχικοποιήστε μια νέα τρισδιάστατη σκηνή
var scene = new Scene();
```

## Βήμα 2: Δημιουργήστε ένα αντικείμενο 3D

Στη συνέχεια, δημιουργήστε ένα τρισδιάστατο αντικείμενο, για παράδειγμα, ένα πλαίσιο:

```csharp
var box = new Box();
scene.RootNode.CreateChildNode("box1", box).Material = new PhongMaterial() { DiffuseColor = new Vector3(1, 0, 1) };
```

## Βήμα 3: Διαμόρφωση μετατροπής υλικού

Ρυθμίστε επιλογές μετατροπής υλικού για μετατροπή μη PBR σε PBR:

```csharp
GltfSaveOptions options = new GltfSaveOptions(FileFormat.GLTF2);
options.MaterialConverter = delegate (Material material)
{
    PhongMaterial phongMaterial = (PhongMaterial)material;
    return new PbrMaterial() { Albedo = new Vector3(phongMaterial.DiffuseColor.x, phongMaterial.DiffuseColor.y, phongMaterial.DiffuseColor.z) };
};
```

## Βήμα 4: Αποθήκευση σε μορφή GLTF 2.0

Αποθηκεύστε τη σκηνή που έχει μετατραπεί σε μορφή GLTF 2.0:

```csharp
scene.Save("Your Output Directory" + "Non_PBRtoPBRMaterial_Out.gltf", options);
// ExEnd:Non_PBRtoPBRMaterial
```

Επαναλάβετε αυτά τα βήματα όπως απαιτείται για τη συγκεκριμένη περίπτωση χρήσης, διασφαλίζοντας ότι κάθε λεπτομέρεια έχει διαμορφωθεί σωστά.

## συμπέρασμα

Συγχαρητήρια! Μάθατε με επιτυχία πώς να μετατρέπετε υλικά Non-PBR σε PBR χρησιμοποιώντας το Aspose.3D για .NET. Αυτό το ισχυρό εργαλείο ανοίγει ατελείωτες δυνατότητες για χειρισμό τρισδιάστατων γραφικών στις εφαρμογές σας .NET.

## Συχνές ερωτήσεις

### Ε1: Είναι το Aspose.3D συμβατό με όλες τις μορφές αρχείων 3D;

A1: Ναι, το Aspose.3D υποστηρίζει ένα ευρύ φάσμα μορφών αρχείων 3D, παρέχοντας ευελιξία στα έργα σας.

### Ε2: Μπορώ να χρησιμοποιήσω το Aspose.3D για εμπορικές εφαρμογές;

 Α2: Απολύτως! Το Aspose.3D είναι ένα εμπορικό προϊόν και μπορείτε να το αγοράσετε[εδώ](https://purchase.aspose.com/buy).

### Ε3: Χρειάζομαι μια προσωρινή άδεια για δοκιμή;

 A3: Ναι, μπορείτε να αποκτήσετε μια προσωρινή άδεια για σκοπούς δοκιμής[εδώ](https://purchase.aspose.com/temporary-license/).

### Ε4: Πού μπορώ να βρω υποστήριξη για το Aspose.3D;

 A4: Επισκεφθείτε το[Aspose.3D φόρουμ](https://forum.aspose.com/c/3d/18) για κοινοτική υποστήριξη και συζητήσεις.

### Ε5: Υπάρχει δωρεάν δοκιμή διαθέσιμη;

 A5: Ναι, μπορείτε να εξερευνήσετε μια δωρεάν δοκιμαστική έκδοση[εδώ](https://releases.aspose.com/).