---
date: 2026-03-26
description: Μάθετε πώς να δημιουργήσετε κύλινδρο και να εξάγετε αρχείο OBJ χρησιμοποιώντας
  το Aspose.3D για .NET. Αυτός ο οδηγός για αρχάριους καλύπτει τη ρύθμιση σκηνής 3D
  και την εξαγωγή OBJ.
linktitle: Customized Shear Bottom Cylinder
second_title: Aspose.3D .NET API
title: Πώς να δημιουργήσετε κύλινδρο με πλαγιαστή βάση – Aspose.3D για .NET
url: /el/net/3d-modeling/working-with-cylinder/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Πώς να δημιουργήσετε Cylinder με Shear Bottom – Aspose.3D for .NET

## Εισαγωγή
Αν αναρωτιέστε **πώς να δημιουργήσετε cylinder** αντικείμενα με προσαρμοσμένη shear bottom σε περιβάλλον .NET, βρίσκεστε στο σωστό μέρος. Σε αυτό το tutorial θα περάσουμε από κάθε βήμα—από τη δημιουργία μιας 3‑D σκηνής μέχρι την εξαγωγή του τελικού μοντέλου ως αρχείο OBJ—ώστε να ενισχύσετε τις *αρχικές σας δεξιότητες 3D μοντελοποίησης* χρησιμοποιώντας **Aspose.3D for .NET**.

## Γρήγορες Απαντήσεις
- **Ποια είναι η κύρια κλάση για την έναρξη ενός 3D μοντέλου;** `Scene` δημιουργεί το ριζικό container για όλα τα γεωμετρικά στοιχεία.  
- **Ποια μέθοδος εξάγει το μοντέλο σε OBJ;** `scene.Save(..., FileFormat.WavefrontOBJ)`.  
- **Χρειάζομαι άδεια για δοκιμή;** Διατίθεται δωρεάν δοκιμή — δείτε τον σύνδεσμο δοκιμής στο FAQ.  
- **Μπορώ να αλλάξω τη γωνία shear;** Ναι, τροποποιήστε το `ShearBottom` με μια τιμή `Vector2`.  
- **Είναι κατάλληλο για αρχάριους;** Απόλυτα· το API αφαιρεί την πολυπλοκότητα του χαμηλού επιπέδου χειρισμού mesh.

## Τι είναι μια 3D Σκηνή;
Μια *3D σκηνή* είναι ένας ιεραρχικός container που περιέχει όλα τα γεωμετρικά αντικείμενα, τα φώτα, τις κάμερες και τις μετασχηματισμούς. Στο Aspose.3D η κλάση `Scene` παρέχει έναν καθαρό τρόπο οργάνωσης και μετέπειτα εξαγωγής των μοντέλων σας.

## Γιατί να εξάγετε σε OBJ;
Το OBJ είναι μια ευρέως υποστηριζόμενη, κειμενική μορφή που πολλές εφαρμογές 3‑D (Blender, Maya, Unity) μπορούν να εισάγουν. Η εξαγωγή σε OBJ σας επιτρέπει να μοιραστείτε ή να επεξεργαστείτε περαιτέρω τα μοντέλα cylinder εκτός του .NET.

## Προαπαιτούμενα
- Βασικές γνώσεις C# και ανάπτυξης .NET.  
- **Aspose.3D for .NET** εγκατεστημένο – μπορείτε να το κατεβάσετε **[εδώ](https://releases.aspose.com/3d/net/)**.  
- Ένα IDE .NET (Visual Studio, Rider ή VS Code) έτοιμο για προγραμματισμό.

## Εισαγωγή Namespaces
Πρώτα, φέρετε τα απαιτούμενα namespaces στο scope ώστε οι τύποι του API να αναγνωρίζονται.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```

## Βήμα 1: Δημιουργία 3D Σκηνής
Το αντικείμενο `Scene` λειτουργεί ως η ρίζα της ιεραρχίας του μοντέλου σας.

```csharp
Scene scene = new Scene();
```

## Βήμα 2: Δημιουργία Cylinder 1
Δημιουργούμε τον πρώτο cylinder με ακτίνα 2, ύψος 10 και 20 ακτινικές τμηματικές.

```csharp
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```

## Βήμα 3: Προσαρμογή Shear Bottom για Cylinder 1
Εφαρμόστε μια shear μετασχηματισμό, ενεργοποιήστε τη δημιουργία fan‑cylinder και προσαρμόστε άλλες ιδιότητες για να πετύχετε το επιθυμητό σχήμα.

```csharp
// Shear 47.5deg in the xy plane (z-axis)
cylinder1.ShearBottom = new Vector2(0, 0.83); 

// Set GenerateFanCylinder to true
cylinder1.GenerateFanCylinder = true;
// Set ThetaLength
cylinder1.ThetaLength = MathUtils.ToRadian(270);

// Set OffsetTop
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```

## Βήμα 4: Προσθήκη Cylinder 1 στη Σκηνή
Τοποθετήστε τον πρώτο cylinder σε μια βολική θέση χρησιμοποιώντας έναν translation μετασχηματισμό.

```csharp
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```

## Βήμα 5: Δημιουργία Cylinder 2
Δημιουργείται ένας δεύτερος cylinder με τις ίδιες βασικές διαστάσεις αλλά χωρίς προσαρμοσμένο shear—ιδανικό για σύγκριση πλάι‑πλάι.

```csharp
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```

## Βήμα 6: Προσθήκη Cylinder 2 στη Σκηνή
Απλώς συνδέουμε τον δεύτερο cylinder στο γράφο της σκηνής.

```csharp
scene.RootNode.CreateChildNode(cylinder2);
```

## Βήμα 7: Εξαγωγή της Σκηνής ως αρχείο OBJ
Τέλος, αποθηκεύουμε ολόκληρη τη σκηνή σε αρχείο OBJ ώστε να μπορεί να ανοιχθεί σε οποιονδήποτε τυπικό 3‑D viewer.

```csharp
scene.Save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WavefrontOBJ);
```

## Κοινά Προβλήματα και Λύσεις
| Πρόβλημα | Γιατί Συμβαίνει | Διόρθωση |
|----------|----------------|----------|
| **Το αρχείο OBJ είναι κενό** | Η σκηνή δεν έχει συνδεδεμένη γεωμετρία. | Βεβαιωθείτε ότι και τα δύο cylinders έχουν προστεθεί στο `scene.RootNode`. |
| **Το shear φαίνεται λανθασμένο** | `ShearBottom` αναμένει την εφαπτομένη της γωνίας. | Χρησιμοποιήστε `Math.Tan(angleInRadians)` ή το δοσμένο `0.83` για ~47.5°. |
| **Σφάλματα διαδρομής αρχείου** | Μη έγκυρος ή ελλιπής φάκελος. | Χρησιμοποιήστε `Path.Combine(Environment.CurrentDirectory, "CustomizedShearBottomCylinder.obj")`. |

## Συχνές Ερωτήσεις
### Είναι το Aspose.3D for .NET κατάλληλο για αρχάριους;
Απόλυτα! Το Aspose.3D for .NET προσφέρει ένα υψηλού επιπέδου API που αφαιρεί τα μαθηματικά βαριά τμήματα της 3‑D μοντελοποίησης, καθιστώντας το προσιτό για προγραμματιστές οποιουδήποτε επιπέδου δεξιοτήτων.

### Μπορώ να εφαρμόσω διαφορετικές γωνίες shear σε cylinders;
Ναι, κάθε αντικείμενο `Cylinder` έχει τη δική του ιδιότητα `ShearBottom`, ώστε να μπορείτε να αναθέσετε μια μοναδική γωνία σε κάθε αντικείμενο.

### Υπάρχει διαθέσιμη έκδοση δοκιμής;
Ναι, μπορείτε να εξερευνήσετε τη δωρεάν έκδοση δοκιμής **[εδώ](https://releases.aspose.com/)**.

### Πού μπορώ να βρω επιπλέον υποστήριξη;
Επισκεφθείτε το **[Aspose.3D forum](https://forum.aspose.com/c/3d/18)** για βοήθεια από την κοινότητα, δείγματα κώδικα και συζητήσεις.

### Πώς μπορώ να αποκτήσω προσωρινή άδεια;
Αποκτήστε την προσωρινή άδεια **[εδώ](https://purchase.aspose.com/temporary-license/)**.

**Πρόσθετες Ε&Ρ;**

**Ε: Πώς εξάγω το μοντέλο σε διαφορετική μορφή, όπως STL;**  
Α: Αντικαταστήστε το `FileFormat.WavefrontOBJ` με `FileFormat.STL` στην κλήση `scene.Save`.

**Ε: Μπορώ να δημιουργήσω animation για τα cylinders μετά τη δημιουργία;**  
Α: Ναι, μπορείτε να προσθέσετε key‑frame animations σε node transforms χρησιμοποιώντας τις κλάσεις `Animation` που παρέχονται από το Aspose.3D.

**Ε: Υποστηρίζει το API το .NET Core;**  
Α: Η βιβλιοθήκη είναι πλήρως συμβατή με .NET Core, .NET 5+ και .NET 6+.

---

**Τελευταία ενημέρωση:** 2026-03-26  
**Δοκιμάστηκε με:** Aspose.3D for .NET (τελευταία έκδοση)  
**Συγγραφέας:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}