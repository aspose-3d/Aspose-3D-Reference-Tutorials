import com.aspose.threed.*;
public class TempVerify {
import java.io.IOException;
import com.aspose.threed.Material;
import com.aspose.threed.Property;
import com.aspose.threed.PropertyCollection;
import com.aspose.threed.Scene;
import com.aspose.threed.Vector3;

String dataDir = "Your Document Directory";
Scene scene = Scene.fromFile(dataDir + "EmbeddedTexture.fbx");

Material material = scene.getRootNode().getChildNodes().get(0).getMaterial();
PropertyCollection props = material.getProperties();

// List All Properties (Inspect Before Changing)
for (Property prop : props) {
    System.out.println("Name" + prop.getName() + " Value = " + prop.getValue());
}

// Set Vector3 Value to Change Diffuse Color
props.set("Diffuse", new Vector3(1, 0, 1));

// Retrieve Material Property by Name
Object diffuse = (Vector3) props.get("Diffuse");
System.out.println(diffuse);

// Access Property Instance Directly
Property pdiffuse = props.findProperty("Diffuse");
System.out.println(pdiffuse);

// Access property value directly
System.out.println("Property value: " + pdiffuse.getValue());
}
