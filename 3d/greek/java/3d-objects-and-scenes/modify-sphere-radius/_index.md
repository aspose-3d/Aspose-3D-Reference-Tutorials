---
date: 2026-03-31
description: Μάθετε πώς να μετατρέπετε 3D σε OBJ προσθέτοντας μια σφαίρα σε μια σκηνή,
  τροποποιώντας την ακτίνα της και εξάγοντας το αρχείο OBJ σε Java χρησιμοποιώντας
  το Aspose.3D.
linktitle: 'Convert 3D to OBJ: Add Sphere & Modify Radius in Java'
second_title: Aspose.3D Java API
title: 'Μετατροπή 3D σε OBJ: Προσθήκη Σφαίρας & Τροποποίηση Ακτίνας σε Java'
url: /el/java/3d-objects-and-scenes/modify-sphere-radius/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Μετατροπή 3D σε OBJ: Προσθήκη Σφαίρας & Τροποποίηση Ακτίνας σε Java

## Εισαγωγή

Αν χρειάζεστε να **convert 3D to OBJ** γρήγορα και προγραμματιστικά, αυτός ο οδηγός σας δείχνει ακριβώς πώς να προσθέσετε μια σφαίρα σε μια σκηνή, να αλλάξετε την ακτίνα της και να γράψετε το προκύπτον αρχείο OBJ χρησιμοποιώντας τη **Aspose.3D Java library**. Θα περάσουμε από κάθε γραμμή κώδικα, θα εξηγήσουμε γιατί κάθε βήμα είναι σημαντικό και θα σας δώσουμε συμβουλές για να αποφύγετε κοινά προβλήματα—ώστε να μπορείτε να ενσωματώσετε τη ροή εργασίας σε παιχνίδια, εργαλεία CAD ή επιστημονικές απεικονίσεις με σιγουριά.

## Γρήγορες Απαντήσεις
- **What is the main goal of this tutorial?** Για να δείξει πώς να convert 3D to OBJ δημιουργώντας μια σφαίρα, ρυθμίζοντας την ακτίνα της και εξάγοντας το μοντέλο σε Java.  
- **Which library provides the 3D functionality?** Aspose.3D, ένα πλήρες **java 3d library tutorial**.  
- **How do I change the sphere size?** Κλήστε `sphere.setRadius(double)` στο αντικείμενο `Sphere`.  
- **Can I write the OBJ file directly from Java?** Ναι—χρησιμοποιήστε `scene.save("file.obj", FileFormat.WAVEFRONTOBJ)`.  
- **Do I need a license for production?** Μια δωρεάν δοκιμή είναι επαρκής για ανάπτυξη· απαιτείται μόνιμη άδεια για εμπορική χρήση.

## Πώς να Μετατρέψετε 3D σε OBJ Χρησιμοποιώντας το Aspose.3D

### Τι είναι το Aspose.3D για Java;

Το Aspose.3D είναι μια **java 3d library** που επιτρέπει στους προγραμματιστές να δημιουργούν, να επεξεργάζονται και να μετατρέπουν αρχεία 3D χωρίς εξωτερικές εξαρτήσεις. Υποστηρίζει δημοφιλείς μορφές όπως OBJ, FBX, STL και άλλες, καθιστώντας το ιδανικό για παιχνίδια, εργαλεία CAD και επιστημονικές απεικονίσεις.

### Γιατί να Μετατρέψετε 3D σε OBJ;

- **Universal Compatibility** – Το OBJ υποστηρίζεται από σχεδόν κάθε προβολέα 3D, κινητήρα παιχνιδιών και λογισμικό μοντελοποίησης.  
- **Lightweight Export** – Το OBJ αποθηκεύει τη γεωμετρία σε μορφή απλού κειμένου, που είναι εύκολο να επιθεωρηθεί και να εντοπιστούν σφάλματα.  
- **Workflow Flexibility** – Μπορείτε να δημιουργήσετε αρχεία OBJ άμεσα από κώδικα Java στο διακομιστή, επιτρέποντας αυτοματοποιημένες διαδικασίες για τη δημιουργία περιουσιακών στοιχείων.

## Προαπαιτούμενα

- Βασικές γνώσεις προγραμματισμού Java.  
- Η βιβλιοθήκη Aspose.3D εγκατεστημένη – κατεβάστε την από την [Aspose.3D for Java documentation](https://reference.aspose.com/3d/java/).  
- JDK 8 ή νεότερο εγκατεστημένο στο μηχάνημά σας.

## Εισαγωγή Πακέτων

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Sphere;

import java.io.IOException;
```

## Οδηγός Βήμα‑βήμα

### Βήμα 1: Αρχικοποίηση Σκηνής

```java
// ExStart:WorkingWithSphereRadius

// initialize a scene
Scene scene = new Scene();
```

Δημιουργώντας ένα `Scene` σας παρέχει ένα κοντέινερ για όλα τα γεωμετρικά στοιχεία, τα φώτα και τις κάμερες. Εδώ θα **add sphere to scene** αργότερα.

### Βήμα 2: Αρχικοποίηση Σφαίρας

```java
// initialize a Sphere
Sphere sphere = new Sphere();
```

Ένα αντικείμενο `Sphere` ξεκινά με προεπιλεγμένη ακτίνα 1.0. Σκεφτείτε το ως ένα κενό καμβά για το σχήμα που θέλετε να εξάγετε.

### Βήμα 3: Ορισμός της Επιθυμητής Ακτίνας

```java
// set radius
sphere.setRadius(10);
```

Εδώ γράφουμε κώδικα σε στυλ **write obj file java** που ορίζει την ακριβή ακτίνα. Αντικαταστήστε το `10` με οποιαδήποτε τιμή `double` που ταιριάζει στις απαιτήσεις του σχεδίου σας.

### Βήμα 4: Προσθήκη Σφαίρας στη Σκηνή

```java
// add sphere to the scene
scene.getRootNode().createChildNode(sphere);
```

Αυτή η γραμμή **adds sphere to scene** δημιουργώντας έναν υποκόμβο κάτω από τον ριζικό κόμβο. Είναι η στιγμή που η γεωμετρία γίνεται μέρος του γραφήματος σκηνής.

### Βήμα 5: Εξαγωγή του Μοντέλου ως OBJ

```java
// save scene
scene.save("sphere.obj", FileFormat.WAVEFRONTOBJ);
```

Καλώντας το `scene.save` **exports obj file java**‑style, ουσιαστικά **save scene as obj**. Το παραγόμενο `sphere.obj` μπορεί να ανοιχτεί σε οποιονδήποτε τυπικό προβολέα 3D.

## Κοινά Προβλήματα και Λύσεις

| Πρόβλημα | Λύση |
|-------|----------|
| **Sphere appears too small in the viewer** | Επαληθεύστε ότι η τιμή της ακτίνας έχει οριστεί σωστά· θυμηθείτε ότι οι μονάδες είναι αυθαίρετες εκτός εάν εφαρμόσετε μια κλιμακωτική μετασχηματισμό. |
| **Exported OBJ has no material** | Το Aspose.3D γράφει μόνο τη γεωμετρία· προσθέστε υλικό στη σφαίρα αν χρειάζεστε υφές (`sphere.setMaterial(...)`). |
| **License exception at runtime** | Βεβαιωθείτε ότι έχετε φορτώσει είτε προσωρινό είτε μόνιμο αρχείο άδειας πριν δημιουργήσετε το `Scene`. |

## Συχνές Ερωτήσεις

### Q: Πού μπορώ να βρω την τεκμηρίωση για το Aspose.3D για Java;

A: Μπορείτε να ανατρέξετε στην [Aspose.3D for Java documentation](https://reference.aspose.com/3d/java/) για ολοκληρωμένη καθοδήγηση.

### Q: Πώς μπορώ να κατεβάσω το Aspose.3D για Java;

A: Κατεβάστε τη βιβλιοθήκη από τη σελίδα εκδόσεων: [Download Aspose.3D for Java](https://releases.aspose.com/3d/java/).

### Q: Υπάρχει δωρεάν δοκιμή διαθέσιμη για το Aspose.3D για Java;

A: Ναι, εξερευνήστε τις δυνατότητες με μια δωρεάν δοκιμή επισκεπτόμενοι το [Aspose.3D Free Trial](https://releases.aspose.com/).

### Q: Πού μπορώ να λάβω υποστήριξη για το Aspose.3D για Java;

A: Ενταχθείτε στην κοινότητα Aspose στο [Aspose.3D Support Forum](https://forum.aspose.com/c/3d/18) για βοήθεια και συζητήσεις.

### Q: Πώς μπορώ να αποκτήσω προσωρινή άδεια για το Aspose.3D;

A: Αποκτήστε μια προσωρινή άδεια επισκεπτόμενοι το [Temporary License](https://purchase.aspose.com/temporary-license/).

### Q: Μπορώ να χρησιμοποιήσω αυτόν τον κώδικα με άλλες μορφές 3D όπως STL;

A: Απόλυτα – απλώς αλλάξτε το enum `FileFormat` κατά την κλήση του `scene.save`, π.χ., `FileFormat.STL`.

## Συμπέρασμα

Τώρα ξέρετε πώς να **convert 3D to OBJ** προσθέτοντας μια σφαίρα, ρυθμίζοντας την ακτίνα της και εξάγοντας το αποτέλεσμα με το Aspose.3D σε Java. Πειραματιστείτε με άλλα primitives, εφαρμόστε υλικά ή συνδυάστε πολλαπλούς μετασχηματισμούς για να δημιουργήσετε πιο πλούσια μοντέλα. Όποτε χρειαστεί να **save scene as obj** ή **write obj file java**, ισχύει το ίδιο πρότυπο.

---

**Τελευταία Ενημέρωση:** 2026-03-31  
**Δοκιμή Με:** Aspose.3D for Java 24.11  
**Συγγραφέας:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}