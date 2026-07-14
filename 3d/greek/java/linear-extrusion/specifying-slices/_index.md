---
date: 2026-05-24
description: Μάθετε πώς να δημιουργήσετε 3D εξώθηση με φέτες χρησιμοποιώντας το Aspose.3D
  for Java. Αυτός ο οδηγός βήμα‑βήμα καλύπτει τη γραμμική εξώθηση, τον καθορισμό της
  ακτίνας στρογγυλοποίησης και την εξαγωγή OBJ.
keywords:
- create 3d extrusion java
- Aspose 3D slices
- linear extrusion Java
linktitle: Δημιουργία 3D Εξώθησης με Φέτες – Aspose.3D for Java
schemas:
- author: Aspose
  dateModified: '2026-05-24'
  description: Learn how to create 3d extrusion with slices using Aspose.3D for Java.
    This step‑by‑step guide covers linear extrusion, set rounding radius, and exporting
    OBJ.
  headline: Create 3D Extrusion with Slices – Aspose.3D for Java
  type: TechArticle
- description: Learn how to create 3d extrusion with slices using Aspose.3D for Java.
    This step‑by‑step guide covers linear extrusion, set rounding radius, and exporting
    OBJ.
  name: Create 3D Extrusion with Slices – Aspose.3D for Java
  steps:
  - name: Set up the scene and define the profile
    text: '`RectangleShape` is a class that defines a 2‑D rectangle profile. First
      we create a `RectangleShape` and give it a **rounding radius** so the corners
      are smooth. `Scene` is the root container for all nodes and geometry. Then we
      initialise a new `Scene` that will hold all geometry.'
  - name: Create child node objects for each extrusion
    text: '`Node` represents an element in the scene graph that can hold geometry
      and transformations. Every piece of geometry lives under a `Node`. Here we generate
      two sibling nodes – one for a low‑slice extrusion and another for a high‑slice
      extrusion – and move the left node a little to the side so the res'
  - name: Perform linear extrusion and set slices
    text: '`LinearExtrusion` is the class that creates a solid by sweeping a profile
      linearly. `LinearExtrusion` is Aspose.3D''s class that generates a solid by
      extruding a 2‑D profile along a straight line. Using an **anonymous inner class**
      we call `setSlices` to control the smoothness. The left node gets onl'
  - name: Export OBJ – save the scene
    text: Finally we write the scene to a Wavefront OBJ file, a format widely supported
      by 3‑D editors and game engines. This demonstrates the **export OBJ Java** capability
      of Aspose.3D.
  type: HowTo
- questions:
  - answer: You can download the library [here](https://releases.aspose.com/3d/java/).
    question: How can I download Aspose.3D for Java?
  - answer: Refer to the documentation [here](https://reference.aspose.com/3d/java/).
    question: Where can I find the documentation for Aspose.3D?
  - answer: Yes, you can explore a free trial [here](https://releases.aspose.com/).
    question: Is there a free trial available?
  - answer: Visit the support forum [here](https://forum.aspose.com/c/3d/18).
    question: How can I get support for Aspose.3D?
  - answer: Yes, a temporary license can be obtained [here](https://purchase.aspose.com/temporary-license/).
    question: Can I purchase a temporary license?
  type: FAQPage
second_title: Aspose.3D Java API
title: Δημιουργία 3D Εξώθησης με Φέτες – Aspose.3D for Java
url: /el/java/linear-extrusion/specifying-slices/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Δημιουργία 3D Εξώθησης με Φέτες – Aspose.3D for Java

## Εισαγωγή

Αν χρειάζεστε **create 3d extrusion** αντικείμενα που φαίνονται ομαλά και ακριβή, ο έλεγχος του αριθμού των φετών είναι το κλειδί. Σε αυτό το tutorial θα δούμε πώς να καθορίζετε τις φέτες κατά την εκτέλεση μιας γραμμικής εξώθησης με Aspose.3D for Java. Θα δείτε γιατί ο αριθμός των φετών είναι σημαντικός, πώς να ορίσετε μια ακτίνα στρογγυλοποίησης, και πώς να εξάγετε το αποτέλεσμα ως αρχείο OBJ που μπορεί να χρησιμοποιηθεί σε οποιοδήποτε pipeline 3‑D.

## Γρήγορες Απαντήσεις
- **Τι ελέγχει το “slices”;** The number of intermediate cross‑sections used to approximate the extrusion surface.  
- **Ποια μέθοδος ορίζει τον αριθμό των φετών;** `LinearExtrusion.setSlices(int)`  
- **Μπορώ να αλλάξω την ακτίνα στρογγυλοποίησης του προφίλ;** Yes, via `RectangleShape.setRoundingRadius(double)`  
- **Τι μορφή αρχείου χρησιμοποιείται σε αυτό το παράδειγμα;** Wavefront OBJ (`FileFormat.WAVEFRONTOBJ`)  
- **Χρειάζομαι άδεια για την εκτέλεση του κώδικα;** Μια δωρεάν δοκιμή λειτουργεί για αξιολόγηση· απαιτείται εμπορική άδεια για παραγωγή.

`LinearExtrusion.setSlices(int)` ορίζει πόσες ενδιάμεσες φέτες θα δημιουργήσει η εξώθηση.  
`RectangleShape.setRoundingRadius(double)` ορίζει την ακτίνα γωνίας ενός ορθογώνιου προφίλ.

## Πώς να δημιουργήσετε 3d extrusion java με φέτες;

Φορτώστε το 2‑D προφίλ σας, επιλέξτε αριθμό φετών, ορίστε την ακτίνα στρογγυλοποίησης και καλέστε `save` – η πλήρης ροή εργασίας χωράει σε λίγες γραμμές. Το Aspose.3D for Java διαχειρίζεται αυτόματα τη δημιουργία γεωμετρίας, την παρεμβολή φετών και την εξαγωγή OBJ, ώστε να μπορείτε να εστιάσετε στην οπτική ποιότητα αντί στις χαμηλού επιπέδου υπολογισμούς πλέγματος.

## Τι είναι μια γραμμική εξώθηση με φέτες;

Μια γραμμική εξώθηση με φέτες μετατρέπει ένα επίπεδο 2‑D σχήμα σε στερεό 3‑D, σκάροντάς το κατά μήκος μιας ευθείας γραμμής ενώ δημιουργεί έναν ρυθμιζόμενο αριθμό ενδιάμεσων διατομών. Ο αριθμός των φετών επηρεάζει άμεσα το πόσο ομαλά αποδίδονται οι καμπυλωτές άκρες, όπως οι στρογγυλεμένες γωνίες.

## Γιατί να χρησιμοποιήσετε Aspose.3D for Java για τη δημιουργία 3d extrusion;

Το Aspose.3D παρέχει **full programmatic control** σε κάθε παράμετρο εξώθησης, υποστηρίζει **50+ input and output formats** (συμπεριλαμβανομένων των OBJ, FBX, STL, και GLTF) και μπορεί να επεξεργαστεί **multi‑hundred‑page models** χωρίς να φορτώνει ολόκληρο το αρχείο στη μνήμη. Εκτελείται σε οποιαδήποτε πλατφόρμα με υποστήριξη Java, δεν απαιτεί εγγενή DLLs και εγγυάται ντετερμινιστικά αποτελέσματα σε Windows, Linux και macOS.

## Προαπαιτούμενα

1. **Java Development Kit** – JDK 8 ή νεότερο εγκατεστημένο.  
2. **Aspose.3D for Java** – Κατεβάστε τη βιβλιοθήκη από την επίσημη ιστοσελίδα [here](https://releases.aspose.com/3d/java/).  
3. Ένα IDE ή κειμενογράφο της επιλογής σας.

## Εισαγωγή Πακέτων

Προσθέστε το namespace του Aspose.3D στο έργο σας ώστε να έχετε πρόσβαση στις κλάσεις μοντελοποίησης 3‑D.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## Οδηγός Βήμα‑βήμα

### Βήμα 1: Ρύθμιση της σκηνής και ορισμός του προφίλ

`RectangleShape` είναι μια κλάση που ορίζει ένα 2‑D προφίλ ορθογωνίου.  
Πρώτα δημιουργούμε ένα `RectangleShape` και του δίνουμε μια **rounding radius** ώστε οι γωνίες να είναι ομαλές.  
`Scene` είναι το ριζικό κοντέινερ για όλους τους κόμβους και τη γεωμετρία.  
Στη συνέχεια αρχικοποιούμε ένα νέο `Scene` που θα περιέχει όλη τη γεωμετρία.

```java
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
Scene scene = new Scene();
```

### Βήμα 2: Δημιουργία αντικειμένων παιδικών κόμβων για κάθε εξώθηση

`Node` αντιπροσωπεύει ένα στοιχείο στο γράφημα σκηνής που μπορεί να περιέχει γεωμετρία και μετασχηματισμούς.  
Κάθε τμήμα γεωμετρίας βρίσκεται κάτω από ένα `Node`. Εδώ δημιουργούμε δύο αδερφικούς κόμβους – έναν για εξώθηση με λίγες φέτες και έναν για εξώθηση με πολλές φέτες – και μετακινούμε τον αριστερό κόμβο λίγο προς τα πλάγια ώστε τα αποτελέσματα να είναι εύκολα συγκρίσιμα.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### Βήμα 3: Εκτέλεση γραμμικής εξώθησης και ορισμός φετών

`LinearExtrusion` είναι η κλάση που δημιουργεί ένα στερεό σκάροντας ένα προφίλ γραμμικά.  
`LinearExtrusion` είναι η κλάση του Aspose.3D που δημιουργεί ένα στερεό εξωθώντας ένα 2‑D προφίλ κατά μήκος μιας ευθείας γραμμής. Χρησιμοποιώντας μια **anonymous inner class** καλούμε το `setSlices` για να ελέγξουμε την ομαλότητα. Ο αριστερός κόμβος λαμβάνει μόνο 2 φέτες (αδυνατό), ενώ ο δεξιός κόμβος λαμβάνει 10 φέτες (ομαλό).

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(2);}});
right.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(10);}});
```

### Βήμα 4: Εξαγωγή OBJ – αποθήκευση της σκηνής

Τέλος γράφουμε τη σκηνή σε αρχείο Wavefront OBJ, μια μορφή που υποστηρίζεται ευρέως από επεξεργαστές 3‑D και μηχανές παιχνιδιών. Αυτό δείχνει τη δυνατότητα **export OBJ Java** του Aspose.3D.

```java
scene.save(MyDir + "SlicesInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Συχνά Προβλήματα και Λύσεις

| Issue | Why it Happens | Fix |
|-------|----------------|-----|
| **Η εξώθηση εμφανίζεται επίπεδη** | Ο αριθμός φετών ορίστηκε σε 1 ή 0 | Βεβαιωθείτε ότι το `setSlices` καλείται με τιμή ≥ 2. |
| **Οι στρογγυλεμένες γωνίες φαίνονται τριγωνικές** | Η ακτίνα στρογγυλοποίησης είναι πολύ μικρή σε σχέση με τον αριθμό φετών | Αυξήστε είτε την ακτίνα είτε τον αριθμό φετών για πιο ομαλές καμπύλες. |
| **Το αρχείο δεν βρέθηκε κατά την αποθήκευση** | `MyDir` δείχνει σε μη υπάρχον φάκελο | Δημιουργήστε τον φάκελο εκ των προτέρων ή χρησιμοποιήστε απόλυτη διαδρομή. |

## Συχνές Ερωτήσεις

**Q: Πώς μπορώ να κατεβάσω το Aspose.3D for Java;**  
A: Μπορείτε να κατεβάσετε τη βιβλιοθήκη [here](https://releases.aspose.com/3d/java/).

**Q: Πού μπορώ να βρω την τεκμηρίωση για το Aspose.3D;**  
A: Ανατρέξτε στην τεκμηρίωση [here](https://reference.aspose.com/3d/java/).

**Q: Υπάρχει διαθέσιμη δωρεάν δοκιμή;**  
A: Ναι, μπορείτε να εξερευνήσετε μια δωρεάν δοκιμή [here](https://releases.aspose.com/).

**Q: Πώς μπορώ να λάβω υποστήριξη για το Aspose.3D;**  
A: Επισκεφθείτε το φόρουμ υποστήριξης [here](https://forum.aspose.com/c/3d/18).

**Q: Μπορώ να αγοράσω προσωρινή άδεια;**  
A: Ναι, μια προσωρινή άδεια μπορεί να ληφθεί [here](https://purchase.aspose.com/temporary-license/).

---

**Τελευταία ενημέρωση:** 2026-05-24  
**Δοκιμή με:** Aspose.3D for Java 24.11 (latest at time of writing)  
**Συγγραφέας:** Aspose

## Σχετικά Μαθήματα

- [Δημιουργία 3D Extrusion Java με Aspose.3D](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [Πώς να ορίσετε κατεύθυνση σε γραμμική εξώθηση με Aspose.3D for Java](/3d/java/linear-extrusion/setting-direction/)
- [Δημιουργία 3D Σκηνής με Twist σε γραμμική εξώθηση – Aspose.3D for Java](/3d/java/linear-extrusion/applying-twist/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}