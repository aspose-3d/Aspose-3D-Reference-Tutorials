import com.aspose.threed.FileFormat;
import com.aspose.threed.Plane;
import com.aspose.threed.Scene;
import com.aspose.threed.Vector3;

public class ChangePlaneOrientation {
    public static void main(String[] args) {
        String MyDir = "Your Document Directory";
        Scene scene = new Scene();
        Plane plane = new Plane();
        plane.setUp(new Vector3(1, 1, 3));
        scene.getRootNode().createChildNode(plane);
        scene.save(MyDir + "ChangePlaneOrientation.obj", FileFormat.WAVEFRONTOBJ);
    }
}
