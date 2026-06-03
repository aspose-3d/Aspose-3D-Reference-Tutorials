---
date: 2026-06-03
description: Μάθετε πώς να εξάγετε τη σκηνή ως FBX και να δημιουργήσετε 3D κυλίνδρου,
  κουτί και άλλα primitive μοντέλα χρησιμοποιώντας το Aspose.3D για Java.
keywords:
- export scene as fbx
- convert 3d model fbx
- Aspose 3D primitives
- Java 3D modeling
linktitle: Κατασκευή primitive 3D μοντέλων με Aspose.3D για Java
schemas:
- author: Aspose
  dateModified: '2026-06-03'
  description: Learn how to export scene as FBX and create 3D cylinder, box, and other
    primitive models using Aspose.3D for Java.
  headline: Export scene as FBX and build cylinder with Aspose.3D Java
  type: TechArticle
- description: Learn how to export scene as FBX and create 3D cylinder, box, and other
    primitive models using Aspose.3D for Java.
  name: Export scene as FBX and build cylinder with Aspose.3D Java
  steps:
  - name: Initialize a Scene Object
    text: The `Scene` class is Aspose.3D's top‑level container that holds all nodes,
      lights, cameras, and materials in memory.
  - name: Build a 3D box model
    text: The `Box` class represents a rectangular prism and is useful for testing
      the coordinate system. Adding it as a child of the scene’s root node positions
      it at the origin.
  - name: Create a 3D cylinder model
    text: The `Cylinder` class is Aspose.3D's built‑in cylinder primitive. It comes
      with default dimensions (radius = 1, height = 2) but you can customise them
      via its constructor.
  - name: Save the drawing in the FBX format
    text: After assembling the scene, export it so other tools (e.g., Unity, Blender)
      can read it. We use the `FBX7500ASCII` format, which is widely supported and
      human‑readable.
  type: HowTo
- questions:
  - answer: Aspose.3D primarily supports Java, but there are versions available for
      .NET and C++ as well.
    question: Can I use Aspose.3D for Java with other programming languages?
  - answer: Absolutely. It provides a comprehensive set of features—including mesh
      manipulation, material assignment, and animation—making it suitable for both
      simple primitives and intricate models.
    question: Is Aspose.3D suitable for complex 3D modeling tasks?
  - answer: Visit the [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) for community
      support and discussions.
    question: Where can I find additional help and support?
  - answer: Yes, you can explore a [free trial](https://releases.aspose.com/) before
      making a purchase decision.
    question: Can I try Aspose.3D before purchasing?
  - answer: You can obtain a [temporary license](https://purchase.aspose.com/temporary-license/)
      for Aspose.3D through the website.
    question: How do I obtain a temporary license for Aspose.3D?
  type: FAQPage
second_title: Aspose.3D Java API
title: Εξαγωγή σκηνής ως FBX και δημιουργία κυλίνδρου με Aspose.3D Java
url: /el/java/primitive-3d-models/building-primitive-3d-models/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Εξαγωγή σκηνής ως FBX και δημιουργία κυλίνδρου με Aspose.3D Java

## Εισαγωγή

Αν ποτέ χρειάστηκε να **δημιουργήσετε έναν 3D κύλινδρο** (ή οποιοδήποτε άλλο βασικό σχήμα) απευθείας από κώδικα Java, το Aspose.3D κάνει την εργασία χωρίς κόπο. Σε αυτό το tutorial θα περάσουμε από όλη τη ροή εργασίας — από τη ρύθμιση του περιβάλλοντος μέχρι την **εξαγωγή σκηνής ως FBX** — ώστε να μπορείτε να αρχίσετε να δημιουργείτε 3D γεωμετρία προγραμματιστικά αμέσως. Θα δείτε πώς η βιβλιοθήκη διαχειρίζεται τα primitives, πώς να τα οργανώσετε σε ένα scene graph, και πώς να αποθηκεύσετε το αποτέλεσμα σε μορφή που μπορεί να διαβάσει το Unity, το Blender ή οποιοδήποτε άλλο 3D εργαλείο.

## Γρήγορες Απαντήσεις
- **Ποια βιβλιοθήκη μου επιτρέπει να δημιουργήσω έναν 3D κύλινδρο σε Java;** Aspose.3D for Java.  
- **Σε ποια μορφή μπορώ να εξάγω τη σκηνή;** FBX (ASCII 7500) using `FileFormat.FBX7500ASCII`.  
- **Χρειάζομαι άδεια για ανάπτυξη;** Μια δωρεάν δοκιμή λειτουργεί για δοκιμές· απαιτείται μόνιμη άδεια για παραγωγή.  
- **Ποια είναι τα κύρια primitives που υποστηρίζονται;** Box, Cylinder, Sphere, Cone, και περισσότερα από 10 επιπλέον σχήματα.  
- **Είναι ο κώδικας συμβατός με Java 8 και νεότερες εκδόσεις;** Ναι, το Aspose.3D στοχεύει στο JDK 8+.

## Τι είναι ένα primitive 3D κύλινδρος;

Ένα primitive κυλίνδρου είναι ένα βασικό γεωμετρικό σχήμα που ορίζεται από ακτίνα και ύψος. Σε πολλές 3D αλυσίδες επεξεργασίας λειτουργεί ως δομικό στοιχείο για πιο σύνθετα μοντέλα όπως σωλήνες, τροχοί ή αρχιτεκτονικές κολώνες. Το Aspose.3D παρέχει μια έτοιμη κλάση `Cylinder`, ώστε να μην χρειάζεται να υπολογίζετε τις κορυφές χειροκίνητα.

## Γιατί να χρησιμοποιήσετε το Aspose.3D για Java;

Το Aspose.3D for Java προσφέρει μια ολοκληρωμένη, καθαρά‑Java 3D μηχανή που εξαλείφει την ανάγκη για εγγενείς βιβλιοθήκες, καθιστώντας το ιδανικό για ανάπτυξη πολλαπλών πλατφορμών. Υποστηρίζει ένα ευρύ φάσμα μορφών εισαγωγής και εξαγωγής, παρέχει ένα ισχυρό scene graph για ιεραρχική οργάνωση και περιλαμβάνει ενσωματωμένα primitives που σας επιτρέπουν να δημιουργήσετε γεωμετρία με ελάχιστο κώδικα. Αυτά τα χαρακτηριστικά μαζί επιταχύνουν την ανάπτυξη και μειώνουν το κόστος συντήρησης.

- **Full‑featured 3D engine** – υποστηρίζει εισαγωγή/εξαγωγή **πάνω από 30** δημοφιλών μορφών (FBX, OBJ, STL, GLTF, 3DS, κλπ).  
- **Pure Java API** – χωρίς εγγενείς εξαρτήσεις, ιδανικό για έργα πολλαπλών πλατφορμών.  
- **Robust scene graph** – σας επιτρέπει να οργανώνετε αντικείμενα ιεραρχικά, καθιστώντας τις μεγάλες σκηνές εύκολες στη διαχείριση.  
- **Easy licensing** – ξεκινήστε με μια δωρεάν δοκιμή, στη συνέχεια αναβαθμίστε σε μόνιμη άδεια όταν μπείτε σε παραγωγή.

## Προαπαιτούμενα

Πριν βυθιστείτε στον κώδικα, βεβαιωθείτε ότι έχετε:

1. **Java Development Kit (JDK)** – JDK 8 ή νεότερο εγκατεστημένο στο μηχάνημά σας.  
2. **Aspose.3D for Java library** – κατεβάστε το και εγκαταστήστε το από τη [download page](https://releases.aspose.com/3d/java/).

## Εισαγωγή Πακέτων

Ξεκινήστε εισάγοντας το βασικό namespace του Aspose.3D. Αυτό σας δίνει πρόσβαση στα `Scene`, `Box`, `Cylinder` και τις σταθερές μορφής αρχείου.

```java
import com.aspose.threed.*;
```

Τώρα που η βιβλιοθήκη έχει αναφερθεί, ας δημιουργήσουμε μια σκηνή και να προσθέσουμε κάποια primitive γεωμετρία.

## Πώς να εξάγετε σκηνή ως FBX και να δημιουργήσετε 3D primitives;

Φορτώστε ένα νέο αντικείμενο `Scene`, προσθέστε primitive κόμβους (Box, Cylinder, κλπ.), και στη συνέχεια καλέστε `save` με τη μορφή FBX7500ASCII. Σε λίγες μόνο γραμμές λαμβάνετε ένα πλήρως‑εξοπλισμένο αρχείο FBX που μπορεί να ανοιχθεί σε οποιονδήποτε σημαντικό 3D επεξεργαστή, επιτρέποντας αδιάλειπτη ενσωμάτωση με μηχανές παιχνιδιών, pipelines απόδοσης ή εφαρμογές AR/VR.

### Βήμα 1: Αρχικοποίηση αντικειμένου Scene

Η κλάση `Scene` είναι το κορυφαίο κοντέινερ του Aspose.3D που κρατά όλους τους κόμβους, τα φώτα, τις κάμερες και τα υλικά στη μνήμη.

```java
// The path to the documents directory.
String myDir = "Your Document Directory";

// Initialize a Scene object
Scene scene = new Scene();
```

### Βήμα 2: Δημιουργία μοντέλου 3D κουτιού

Η κλάση `Box` αντιπροσωπεύει ένα ορθογώνιο πρίσμα και είναι χρήσιμη για δοκιμή του συστήματος συντεταγμένων. Προσθέτοντάς την ως παιδί του ριζικού κόμβου της σκηνής την τοποθετεί στο αρχικό σημείο.

```java
// Create a Box model
scene.getRootNode().createChildNode("box", new Box());
```

### Βήμα 3: Δημιουργία μοντέλου 3D κυλίνδρου

Η κλάση `Cylinder` είναι το ενσωματωμένο primitive κυλίνδρου του Aspose.3D. Διαθέτει προεπιλεγμένες διαστάσεις (ακτίνα = 1, ύψος = 2) αλλά μπορείτε να τις προσαρμόσετε μέσω του κατασκευαστή της.

```java
// Create a Cylinder model
scene.getRootNode().createChildNode("cylinder", new Cylinder());
```

### Βήμα 4: Αποθήκευση του σχεδίου σε μορφή FBX

Μετά τη συναρμολόγηση της σκηνής, εξάγετε την ώστε άλλα εργαλεία (π.χ., Unity, Blender) να μπορούν να την διαβάσουν. Χρησιμοποιούμε τη μορφή `FBX7500ASCII`, η οποία υποστηρίζεται ευρέως και είναι αναγνώσιμη από άνθρωπο.

```java
// Save drawing in the FBX format
myDir = myDir + "test.fbx";
scene.save(myDir, FileFormat.FBX7500ASCII);
```

## Κοινά Προβλήματα και Λύσεις

| Πρόβλημα | Γιατί συμβαίνει | Διόρθωση |
|-------|----------------|-----|
| **File not found** when saving | `myDir` points to a non‑existent folder | Ensure the directory exists or create it with `new File(myDir).mkdirs();` |
| **Empty scene** after export | No nodes were added before calling `save` | Verify that `createChildNode` calls are executed (debug with `scene.getRootNode().getChildCount()` ) |
| **License exception** | Running without a valid license in production | Apply a temporary or permanent license using `License license = new License(); license.setLicense("Aspose.3D.Java.lic");` |

## Συχνές Ερωτήσεις

**Q: Μπορώ να χρησιμοποιήσω το Aspose.3D for Java με άλλες γλώσσες προγραμματισμού;**  
A: Το Aspose.3D υποστηρίζει κυρίως τη Java, αλλά υπάρχουν εκδόσεις διαθέσιμες για .NET και C++ επίσης.

**Q: Είναι το Aspose.3D κατάλληλο για σύνθετες εργασίες 3D μοντελοποίησης;**  
A: Απόλυτα. Παρέχει ένα ολοκληρωμένο σύνολο λειτουργιών — συμπεριλαμβανομένης της επεξεργασίας πλέγματος, της ανάθεσης υλικών και της κίνησης — καθιστώντας το κατάλληλο τόσο για απλά primitives όσο και για πολύπλοκα μοντέλα.

**Q: Πού μπορώ να βρω πρόσθετη βοήθεια και υποστήριξη;**  
A: Επισκεφθείτε το [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) για υποστήριξη κοινότητας και συζητήσεις.

**Q: Μπορώ να δοκιμάσω το Aspose.3D πριν την αγορά;**  
A: Ναι, μπορείτε να εξερευνήσετε μια [free trial](https://releases.aspose.com/) πριν πάρετε απόφαση αγοράς.

**Q: Πώς μπορώ να αποκτήσω προσωρινή άδεια για το Aspose.3D;**  
A: Μπορείτε να αποκτήσετε μια [temporary license](https://purchase.aspose.com/temporary-license/) για το Aspose.3D μέσω της ιστοσελίδας.

## Συμπέρασμα

Τώρα έχετε μάθει πώς να **εξάγετε σκηνή ως FBX**, και πώς να **δημιουργήσετε 3D κύλινδρο**, κουτί και άλλα primitive μοντέλα χρησιμοποιώντας το Aspose.3D for Java. Μη διστάσετε να πειραματιστείτε με επιπλέον primitives όπως Sphere, Cone ή Torus, και να εξερευνήσετε την ανάθεση υλικών για να δώσετε στα μοντέλα σας ρεαλιστική εμφάνιση. Μόλις νιώσετε άνετα, μπορείτε να ενσωματώσετε τα παραγόμενα αρχεία FBX σε μηχανές παιχνιδιών, pipelines AR/VR ή οποιαδήποτε επόμενη 3D ροή εργασίας.

---

**Τελευταία ενημέρωση:** 2026-06-03  
**Δοκιμάστηκε με:** Aspose.3D for Java 24.11 (latest at time of writing)  
**Συγγραφέας:** Aspose

## Σχετικές Οδηγίες

- [Πώς να εξάγετε σκηνή σε FBX και να ανακτήσετε πληροφορίες 3D σκηνής σε Java](/3d/java/3d-scenes-and-models/get-scene-information/)
- [Πώς να εξάγετε FBX και να δημιουργήσετε ιεραρχίες κόμβων σε Java](/3d/java/geometry/build-node-hierarchies/)
- [Πώς να δημιουργήσετε μοντέλα κυλίνδρων με Aspose.3D for Java](/3d/java/cylinders/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< blocks/products/products-backtop-button >}}
{{< /blocks/products/pf/main-wrap-class >}}