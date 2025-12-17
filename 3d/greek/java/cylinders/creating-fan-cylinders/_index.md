---
date: 2025-12-09
description: Μάθετε πώς να προσθέτετε υποκόμβο, να τοποθετείτε αντικείμενα 3D και
  να αποθηκεύετε τη σκηνή ως OBJ, δημιουργώντας προσαρμοσμένους κυλίνδρους ανεμιστήρα
  με το Aspose.3D για Java.
language: el
linktitle: Adding Child Node for Fan Cylinders with Aspose.3D Java
second_title: Aspose.3D Java API
title: Προσθήκη παιδικού κόμβου για τη δημιουργία κυλίνδρων ανεμιστήρα με το Aspose.3D
  για Java
url: /java/cylinders/creating-fan-cylinders/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Προσθήκη child node για δημιουργία fan cylinders με Aspose.3D για Java

## Introduction

Έτοιμοι να **προσθέσετε child node** σε μια 3‑D σκηνή και να δημιουργήσετε εντυπωσιακούς fan cylinders; Σε αυτό το tutorial θα περάσουμε από κάθε βήμα — από τη ρύθμιση της σκηνής, την τοποθέτηση 3D αντικειμένων, μέχρι τελικά **αποθήκευση σκηνής ως OBJ** — χρησιμοποιώντας το Aspose.3D για Java. Είτε βελτιώνετε ένα στοιχείο παιχνιδιού είτε δημιουργείτε ένα γρήγορο πρωτότυπο, οι έννοιες εδώ θα σας δώσουν πλήρη έλεγχο πάνω στα 3‑D μοντέλα σας.

## Quick Answers
- **Τι κάνει το “add child node”;** Εισάγει ένα νέο αντικείμενο στο γράφημα σκηνής, κληρονομώντας τις μετασχηματισμούς από τον γονέα του.  
- **Πώς μπορώ να τοποθετήσω ένα 3D αντικείμενο;** Εφαρμόζοντας μια μετάφραση (ή περιστροφή/κλιμάκωση) στον μετασχηματισμό του node.  
- **Ποια μορφή αρχείου χρησιμοποιείται για εξαγωγή;** Το παράδειγμα αποθηκεύει το μοντέλο ως αρχείο Wavefront OBJ.  
- **Χρειάζομαι άδεια για την εκτέλεση του κώδικα;** Μια δωρεάν δοκιμή λειτουργεί για αξιολόγηση· απαιτείται άδεια για παραγωγή.  
- **Ποιο IDE είναι το καλύτερο;** Οποιοδήποτε Java IDE (IntelliJ IDEA, Eclipse, VS Code) που υποστηρίζει JDK 8+.

## What is “add child node” in Aspose.3D?
Η προσθήκη ενός child node σημαίνει δημιουργία ενός νέου node κάτω από έναν υπάρχοντα γονέα στη ιεραρχία σκηνής. Το παιδί κληρονομεί το σύστημα συντεταγμένων του γονέα, καθιστώντας εύκολη τη **θέση 3d object** των στιγμιοτύπων σχετικά μεταξύ τους.

## Why add a child node when building fan cylinders?
- **Μοντέλο σχεδίασης:** Κάθε κύλινδρος (fan ή non‑fan) ζει στο δικό του node, απλοποιώντας τις μετέπειτα επεξεργασίες.  
- **Κληρονομία μετασχηματισμού:** Μετακινήστε, περιστρέψτε ή κλιμακώστε τον γονέα και όλα τα παιδιά ακολουθούν αυτόματα.  
- **Καθαρότερο γράφημα σκηνής:** Βελτιώνει την αναγνωσιμότητα και τον εντοπισμό σφαλμάτων σε σύνθετα μοντέλα.

## Prerequisites

- **Java Development Kit (JDK)** – κατεβάστε από την [official site](https://www.oracle.com/java/technologies/javase-downloads.html).  
- **Aspose.3D for Java** – αποκτήστε τη νεότερη βιβλιοθήκη από το [download link](https://releases.aspose.com/3d/java/).

## Import Packages

Ξεκινήστε εισάγοντας τα απαραίτητα πακέτα στο Java project σας. Αυτό το βήμα είναι κρίσιμο για την πρόσβαση στις λειτουργίες που παρέχει το Aspose.3D.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Step 1: Create a Scene

Πρώτα, δημιουργούμε μια κενή 3‑D σκηνή που θα φιλοξενήσει όλα τα αντικείμενα μας.

```java
// ExStart:2
// Create a Scene
Scene scene = new Scene();
// ExEnd:2
```

## Step 2: Create a Fan Cylinder

Στη συνέχεια, δημιουργούμε έναν κύλινδρο που θα αποδοθεί ως fan (μερική περιστροφή).

```java
// ExStart:3
// Create a cylinder with fan
Cylinder fan = new Cylinder(2, 2, 10, 20, 1, false);
fan.setGenerateFanCylinder(true);
fan.setThetaLength(MathUtils.toRadian(270.0));
// ExEnd:3
```

## Step 3: Add Child Node & Position 3D Object

Τώρα **προσθέτουμε child node** στη σκηνή και **τοποθετούμε το 3d object** ορίζοντας τη μετάφρασή του. Εδώ ο fan cylinder γίνεται μέρος του γραφήματος σκηνής.

```java
// ExStart:4
// Create ChildNode and set translation
scene.getRootNode().createChildNode(fan).getTransform().setTranslation(10, 0, 0);
// ExEnd:4
```

## Step 4: Create a Non‑Fan Cylinder

Για να δείξουμε την ευελιξία του Aspose.3D, δημιουργούμε επίσης έναν κανονικό κύλινδρο χωρίς fan και τον προσθέτουμε ως άλλο child node.

```java
// ExStart:5
// Create a cylinder without a fan
Cylinder nonfan = new Cylinder(2, 2, 10, 20, 1, false);
// Create ChildNode
scene.getRootNode().createChildNode(nonfan);
// ExEnd:5
```

## Step 5: Save the Scene as OBJ

Τέλος, **αποθηκεύουμε τη σκηνή ως OBJ** ώστε να μπορείτε να δείτε το αποτέλεσμα σε οποιονδήποτε τυπικό 3‑D viewer.

```java
// ExStart:6
// Save scene
scene.save("Your Document Directory" + "CreateFanCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

Συγχαρητήρια! Έχετε προσθέσει επιτυχώς **child node**, τοποθετήσει τα αντικείμενά σας και εξάγει το μοντέλο.

## Common Issues & Tips

| Πρόβλημα | Λύση |
|----------|------|
| **File not found** κατά την αποθήκευση | Βεβαιωθείτε ότι ο φάκελος προορισμού υπάρχει και έχετε δικαιώματα εγγραφής. |
| **Cylinder appears flat** | Επαληθεύστε τις τιμές της ακτίνας και του ύψους· το Aspose.3D αναμένει μονάδες στην ίδια κλίμακα. |
| **Fan slice looks incomplete** | Ρυθμίστε το `ThetaLength` (σε ακτίνια) ώστε να καλύπτει την επιθυμητή γωνία. |
| **Scene not visible in viewer** | Επιβεβαιώστε ότι το αρχείο OBJ αποθηκεύτηκε μαζί με το αντίστοιχο αρχείο `.mtl` (υλικού) εάν απαιτείται. |

## Frequently Asked Questions

**Q:** *Είναι το Aspose.3D συμβατό με άλλες βιβλιοθήκες Java για 3D μοντελοποίηση;*  
**A:** Ναι, το Aspose.3D λειτουργεί παράλληλα με άλλες βιβλιοθήκες Java 3‑D, επιτρέποντάς σας να συνδυάσετε λειτουργίες όπως χρειάζεται.

**Q:** *Μπορώ να προσαρμόσω περαιτέρω την εμφάνιση των παραγόμενων fan cylinders;*  
**A:** Απόλυτα. Μπορείτε να εφαρμόσετε υλικά, υφές και φωτισμό χρησιμοποιώντας τις κλάσεις `Material` και `Light`.

**Q:** *Πού μπορώ να βρω επιπλέον υποστήριξη ή βοήθεια για το Aspose.3D;*  
**A:** Επισκεφθείτε το [Aspose.3D forum](https://forum.aspose.com/c/3d/18) για βοήθεια από την κοινότητα και επίσημες απαντήσεις.

**Q:** *Υπάρχει δωρεάν δοκιμή διαθέσιμη για το Aspose.3D;*  
**A:** Ναι, μπορείτε να εξερευνήσετε το Aspose.3D με μια [free trial](https://releases.aspose.com/) πριν την αγορά.

**Q:** *Πώς μπορώ να αποκτήσω προσωρινή άδεια για το Aspose.3D;*  
**A:** Αποκτήστε μια προσωρινή άδεια [εδώ](https://purchase.aspose.com/temporary-license/) για δοκιμές και ανάπτυξη.

## Conclusion

Σε αυτόν τον οδηγό δείξαμε πώς να **προσθέσετε child node**, **τοποθετήσετε 3d object**, και **αποθηκεύσετε τη σκηνή ως OBJ** ενώ δημιουργούμε προσαρμοσμένους fan cylinders με το Aspose.3D για Java. Αυτά τα δομικά στοιχεία σας δίνουν την ευελιξία να κατασκευάσετε σύνθετες 3‑D ιεραρχίες και να τις εξάγετε για οποιαδήποτε επόμενη ροή εργασίας.

---

**Τελευταία ενημέρωση:** 2025-12-09  
**Δοκιμή με:** Aspose.3D 24.12 for Java  
**Συγγραφέας:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}