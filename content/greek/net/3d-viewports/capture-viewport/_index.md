---
title: Λήψη θυρών προβολής σε σκηνές 3D
linktitle: Λήψη θυρών προβολής σε σκηνές 3D
second_title: Aspose.3D .NET API
description: Μάθετε να καταγράφετε εντυπωσιακές θύρες προβολής 3D χρησιμοποιώντας το Aspose.3D για .NET. Οδηγός βήμα προς βήμα για απόδοση σκηνών με ευελιξία.
type: docs
weight: 11
url: /el/net/3d-viewports/capture-viewport/
---
## Εισαγωγή

Στον τομέα των τρισδιάστατων γραφικών και της οπτικοποίησης, η λήψη θυρών προβολής είναι μια βασική δεξιότητα που βελτιώνει το βάθος και τη λεπτομέρεια των σκηνών σας. Το Aspose.3D for .NET παρέχει μια ισχυρή λύση για απόδοση και χειρισμό τρισδιάστατων σκηνών. Αυτό το σεμινάριο θα σας καθοδηγήσει στη διαδικασία λήψης θυρών προβολής σε σκηνές 3D χρησιμοποιώντας το Aspose.3D, επιτρέποντάς σας να δημιουργήσετε εκπληκτικές απεικονίσεις με ευκολία.

## Προαπαιτούμενα

Πριν ξεκινήσετε το σεμινάριο, βεβαιωθείτε ότι έχετε τις ακόλουθες προϋποθέσεις:

-  Aspose.3D for .NET Library: Βεβαιωθείτε ότι έχετε εγκαταστήσει τη βιβλιοθήκη Aspose.3D. Μπορείτε να το κατεβάσετε από[εδώ](https://releases.aspose.com/3d/net/).

## Εισαγωγή χώρων ονομάτων

Για να ξεκινήσετε, εισαγάγετε τους απαραίτητους χώρους ονομάτων στο έργο σας .NET:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using System.Drawing;
using System.Drawing.Imaging;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Render;
using Aspose.ThreeD.Utilities;
```

## Βήμα 1: Φορτώστε μια υπάρχουσα τρισδιάστατη σκηνή

Ξεκινήστε φορτώνοντας μια υπάρχουσα τρισδιάστατη σκηνή στο έργο σας. Το παρακάτω απόσπασμα κώδικα το δείχνει αυτό:

```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("scene.obj"));
```

## Βήμα 2: Δημιουργήστε μια κάμερα

Στη συνέχεια, δημιουργήστε ένα στιγμιότυπο της κάμερας και ορίστε τη θέση και τον στόχο της:

```csharp
Camera camera = new Camera();
scene.RootNode.CreateChildNode("camera", camera).Transform.Translation = new Vector3(2, 44, 66);
camera.LookAt = new Vector3(50, 12, 0);
```

## Βήμα 3: Προσθέστε φωτισμό στη σκηνή

Βελτιώστε τη σκηνή σας προσθέτοντας μια πηγή φωτός. Το παρακάτω απόσπασμα κώδικα δείχνει πώς να δημιουργήσετε μια φωτεινή ένδειξη σημείου:

```csharp
scene.RootNode.CreateChildNode("light", new Light() { Color = new Vector3(Color.White), LightType = LightType.Point }).Transform.Translation = new Vector3(26, 57, 43);
```

## Βήμα 4: Διαμόρφωση Renderer και Render Target

Ρυθμίστε το renderer και δημιουργήστε έναν στόχο απόδοσης για τη λήψη της σκηνής:

```csharp
using (var renderer = Renderer.CreateRenderer())
{
    renderer.EnableShadows = false;

    using (IRenderTexture rt = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(), 1, 1024, 1024))
    {
        // ... (συνέχεια στα επόμενα βήματα)
    }
}
```

## Βήμα 5: Ορισμός θυρών προβολής και απόδοσης

Ορίστε τις θύρες προβολής και αποδώστε τη σκηνή για τη δημιουργία εικόνων εξόδου:

```csharp
Viewport vp = rt.CreateViewport(camera, new RelativeRectangle() { ScaleWidth = 1, ScaleHeight = 1 });
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "file-1viewports_out.png", ImageFormat.Png);
```

## Βήμα 6: Τροποποίηση θυρών προβολής και απόδοση ξανά

Τροποποιήστε τις θύρες προβολής και αποδώστε τη σκηνή για άλλη μια φορά, αποδεικνύοντας την ευελιξία του Aspose.3D:

```csharp
vp.Area = new RelativeRectangle() { ScaleWidth = 0.5f, ScaleHeight = 1 };
rt.CreateViewport(camera, new RelativeRectangle() { ScaleX = 0.5f, ScaleWidth = 0.5f, ScaleHeight = 1 });
camera.FieldOfView = 90;
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "file-2viewports_out.png", ImageFormat.Png);
```

Συνεχίστε να πειραματίζεστε με διαφορετικές διαμορφώσεις για να επιτύχετε τα επιθυμητά οπτικά εφέ.

## συμπέρασμα

Σε αυτό το σεμινάριο, εξερευνήσαμε τη διαδικασία λήψης θυρών προβολής σε σκηνές 3D χρησιμοποιώντας το Aspose.3D για .NET. Αξιοποιώντας τα ισχυρά χαρακτηριστικά του, μπορείτε να ανεβάσετε τα έργα τρισδιάστατων γραφικών σας σε νέα ύψη, παρέχοντας συναρπαστικές οπτικές εμπειρίες.

## Συχνές ερωτήσεις

### Ε1: Είναι το Aspose.3D συμβατό με άλλες μορφές αρχείων 3D;

A1: Ναι, το Aspose.3D υποστηρίζει διάφορες μορφές αρχείων 3D, διασφαλίζοντας τη συμβατότητα με ένα ευρύ φάσμα εργαλείων σχεδίασης.

### Ε2: Μπορώ να χρησιμοποιήσω το Aspose.3D για την ανάπτυξη παιχνιδιών;

A2: Ενώ το Aspose.3D έχει σχεδιαστεί κυρίως για γραφικά και οπτικοποίηση, οι λειτουργίες του μπορούν να συμπληρώσουν ορισμένες πτυχές της ανάπτυξης παιχνιδιών.

### Ε3: Πού μπορώ να βρω πρόσθετα παραδείγματα και τεκμηρίωση;

 A3: Εξερευνήστε την περιεκτική[Aspose.3D τεκμηρίωση](https://reference.aspose.com/3d/net/) για περισσότερα παραδείγματα και λεπτομερείς πληροφορίες.

### Ε4: Υπάρχει διαθέσιμη δωρεάν δοκιμή;

 A4: Ναι, μπορείτε να έχετε πρόσβαση σε μια δωρεάν δοκιμή[εδώ](https://releases.aspose.com/).

### Ε5: Πώς μπορώ να αναζητήσω βοήθεια ή να συμμετάσχω στην κοινότητα;

 A5: Εγγραφείτε στην κοινότητα Aspose.3D στο[φόρουμ υποστήριξης](https://forum.aspose.com/c/3d/18) για βοήθεια και συνεργασία.