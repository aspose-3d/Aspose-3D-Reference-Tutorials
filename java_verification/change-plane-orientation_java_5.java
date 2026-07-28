import com.aspose.threed.*;
public class TempVerify {
// ExStart:ChangePlaneOrientation
String MyDir = "Your Document Directory";

Scene scene = new Scene();

Plane plane = new Plane();

plane.setUp(new Vector3(1, 1, 3));

scene.getRootNode().createChildNode(plane);

scene.save(MyDir + "ChangePlaneOrientation.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:ChangePlaneOrientation
}
