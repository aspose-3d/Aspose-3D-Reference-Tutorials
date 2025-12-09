---
date: 2025-12-09
description: Μάθετε πώς να προσθέτετε πλέγμα σε κόμβο και να δημιουργείτε δυναμικές
  3D σκηνές σε Java με το Aspose.3D. Αποθηκεύστε τη σκηνή ως FBX και δημιουργήστε
  εύκολα θυγατρικούς κόμβους.
language: el
linktitle: Add Mesh to Node and Build 3D Hierarchies with Java
second_title: Aspose.3D Java API
title: Προσθήκη πλέγματος σε κόμβο και δημιουργία 3Δ ιεραρχιών με Java
url: /java/geometry/build-node-hierarchies/
weight: 16
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Προσθήκη Πλέγματος σε Κόμβο και Δημιουργία Ιεραρχιών 3D με Java

## Εισαγωγή

Η προσθήκη ενός πλέγματος σε έναν κόμβο αποτελεί τη βάση για την κατασκευή πλούσιων 3D σκηνών σε Java. Με το **Aspose.3D for Java**, μπορείτε να **add mesh to node**, να δημιουργήσετε σύνθετες ιεραρχίες και στη συνέχεια να **save scene as FBX** για χρήση σε οποιοδήποτε 3D pipeline. Αυτό το tutorial σας καθοδηγεί βήμα‑βήμα—from τη ρύθμιση του περιβάλλοντος μέχρι την εξαγωγή του τελικού αρχείου—ώστε να αρχίσετε να δημιουργείτε διαδραστικά 3D γραφικά αμέσως.

## Γρήγορες Απαντήσεις
- **Τι σημαίνει «add mesh to node»;** Συνδέει ένα γεωμετρικό πλέγμα (π.χ. έναν κύβο) με έναν κόμβο του γραφήματος σκηνής, επιτρέποντάς σας να το μετασχηματίζετε ως μέρος μιας ιεραρχίας.  
- **Σε ποια μορφή μπορώ να εξάγω;** Το παράδειγμα αποθηκεύει τη σκηνή ως **FBX** (FBX7500ASCII).  
- **Χρειάζομαι άδεια για το Aspose.3D;** Μια δωρεάν δοκιμή λειτουργεί για αξιολόγηση· απαιτείται άδεια για παραγωγική χρήση.  
- **Ποια έκδοση της Java απαιτείται;** Java 8 ή νεότερη.  
- **Μπορώ να δημιουργήσω πολλαπλούς κόμβους-παιδιά;** Ναι—χρησιμοποιήστε το `createChildNode` επανειλημμένα για να χτίσετε το βάθος που χρειάζεστε.

## Τι είναι το «add mesh to node» στο Aspose.3D;

Στο Aspose.3D, ένας **Node** αντιπροσωπεύει ένα μετασχηματιζόμενο στοιχείο στο γράφημα σκηνής. Καλώντας `setEntity(mesh)` **add mesh to node**, συνδέετε τη γεωμετρία με τον πίνακα μετασχηματισμού του. Αυτό σας επιτρέπει να μετακινείτε, περιστρέφετε ή κλιμακώνετε το πλέγμα χειρίζοντας τον μετασχηματισμό του κόμβου.

## Γιατί να χρησιμοποιήσετε το Aspose.3D for Java για τη δημιουργία κόμβων-παιδιών;

- **Απλό API** – Δεν απαιτείται προγραμματισμός χαμηλού επιπέδου γραφικών.  
- **Υποστήριξη πολλαπλών μορφών** – Εξαγωγή σε FBX, OBJ, 3MF και άλλα.  
- **Βελτιστοποιημένη απόδοση** – Διαχειρίζεται μεγάλες ιεραρχίες αποδοτικά.  
- **Πλήρης ισοδυναμία .NET/Java** – Συνεπείς λειτουργίες σε όλες τις πλατφόρμες.

## Προαπαιτούμενα

1. **Περιβάλλον Ανάπτυξης Java** – JDK 8+ και το αγαπημένο σας IDE.  
2. **Aspose.3D for Java Library** – Κατεβάστε από τη [Aspose 3D Java download page](https://releases.aspose.com/3d/java/).  
3. **Φάκελος Εγγράφων** – Ένας φάκελος όπου θα αποθηκευτεί το παραγόμενο αρχείο FBX.

## Εισαγωγή Πακέτων

```java
import com.aspose.threed.*;
```

## Βήμα 1: Αρχικοποίηση του Αντικειμένου Scene

```java
// Initialize scene object
Scene scene = new Scene();
```

## Βήμα 2: Δημιουργία Κόμβων-Παιδιών Java – Add Mesh to Node

Εδώ **δημιουργούμε κόμβους-παιδιά** κάτω από τον ριζικό κόμβο, συνδέουμε το ίδιο πλέγμα σε καθέναν και το τοποθετούμε ανεξάρτητα.

```java
// Get a child node object
Node top = scene.getRootNode().createChildNode();

// Create the first cube node
Node cube1 = top.createChildNode("cube1");
Mesh mesh = Common.createMeshUsingPolygonBuilder(); // Use your mesh creation method
cube1.setEntity(mesh);                     // <-- add mesh to node
cube1.getTransform().setTranslation(new Vector3(-10, 0, 0));

// Create the second cube node
Node cube2 = top.createChildNode("cube2");
cube2.setEntity(mesh);                     // <-- add mesh to node
cube2.getTransform().setTranslation(new Vector3(10, 0, 0));
```

## Βήμα 3: Εφαρμογή Περιστροφής στον Κορυφαίο Κόμβο (Επηρεάζει Όλα τα Παιδιά)

```java
// Rotate the top node, affecting all child nodes
top.getTransform().setRotation(Quaternion.fromEulerAngle(Math.PI, 4, 0));
```

## Βήμα 4: Αποθήκευση της 3D Σκηνής – Save Scene as FBX

```java
// Save 3D scene in the supported file format (FBX in this case)
String MyDir = "Your Document Directory";
MyDir = MyDir + "NodeHierarchy.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
System.out.println("\nNode hierarchy added successfully to document.\nFile saved at " + MyDir);
```

### Τι συνέβη μόλις τώρα;

- Οι **Κόμβοι** `cube1` και `cube2` κληρονομούν την περιστροφή που εφαρμόστηκε στο `top`.  
- Και οι δύο κόμβοι μοιράζονται το **ίδιο πλέγμα**, δείχνοντας πώς να **add mesh to node** αποδοτικά.  
- Η τελική κλήση `scene.save` **αποθηκεύει τη σκηνή ως FBX**, την οποία μπορείτε να ανοίξετε στο Unity, Blender ή οποιονδήποτε προβολέα συμβατό με FBX.

## Συχνά Προβλήματα και Λύσεις

| Πρόβλημα | Γιατί συμβαίνει | Διόρθωση |
|----------|----------------|----------|
| **Mesh not visible** | Το πλέγμα μπορεί να είναι συνδεδεμένο σε κόμβο χωρίς σωστό μετασχηματισμό ή η κάμερα να βρίσκεται πολύ μακριά. | Βεβαιωθείτε ότι η μετάφραση του κόμβου βρίσκεται μέσα στο πεδίο θέασης της κάμερας και ότι το πλέγμα έχει γεωμετρία. |
| **Exported FBX is empty** | Η `scene.save` κλήθηκε πριν προστεθούν οι κόμβοι ή χρησιμοποιείται λανθασμένη διαδρομή αρχείου. | Επαληθεύστε ότι οι κόμβοι προστέθηκαν πριν την κλήση `save` και ότι το `MyDir` δείχνει σε θέση με δικαιώματα εγγραφής. |
| **Rotation looks wrong** | Οι γωνίες Euler δόθηκαν σε ακτίνια· η χρήση μοιρών θα παράγει απρόσμενα αποτελέσματα. | Χρησιμοποιήστε `Math.toRadians(degrees)` ή δώστε άμεσα ακτίνια όπως φαίνεται στο παράδειγμα. |

## Συχνές Ερωτήσεις

**Ε: Είναι το Aspose.3D for Java κατάλληλο για αρχάριους;**  
Α: Απόλυτα! Το API αφαιρεί τις λεπτομέρειες χαμηλού επιπέδου, επιτρέποντάς σας να εστιάσετε στην κατασκευή σκηνών αντί στην υλοποίηση γραφικών.

**Ε: Μπορώ να χρησιμοποιήσω το Aspose.3D for Java για εμπορικά έργα;**  
Α: Ναι. Αγοράστε άδεια στη [Aspose purchase page](https://purchase.aspose.com/buy) για παραγωγική χρήση.

**Ε: Πώς μπορώ να λάβω υποστήριξη αν αντιμετωπίσω προβλήματα;**  
Α: Εγγραφείτε στο [Aspose.3D forum](https://forum.aspose.com/c/3d/18) για βοήθεια από την κοινότητα και επίσημη υποστήριξη από μηχανικούς της Aspose.

**Ε: Υπάρχει διαθέσιμη δωρεάν δοκιμή;**  
Α: Φυσικά. Κατεβάστε μια δοκιμαστική έκδοση από τη [Aspose releases page](https://releases.aspose.com/) και αξιολογήστε όλες τις δυνατότητες πριν αγοράσετε.

**Ε: Πού μπορώ να βρω την πλήρη τεκμηρίωση του API;**  
Α: Η πλήρης αναφορά φιλοξενείται στον ιστότοπο [Aspose 3D Java documentation site](https://reference.aspose.com/3d/java/).

## Συμπέρασμα

Τώρα ξέρετε πώς να **add mesh to node**, να δημιουργήσετε ισχυρές **ιεραρχίες κόμβων-παιδιών** και να **save the scene as FBX** χρησιμοποιώντας το Aspose.3D for Java. Πειραματιστείτε με διαφορετικά πλέγματα, πιο βαθιές ιεραρχίες και πρόσθετους μετασχηματισμούς για να δημιουργήσετε καθηλωτικές 3D εμπειρίες. Καλό κώδικα!

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Τελευταία Ενημέρωση:** 2025-12-09  
**Δοκιμή με:** Aspose.3D for Java 24.12 (latest)  
**Συγγραφέας:** Aspose  

---