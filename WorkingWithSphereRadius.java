import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Sphere;

public class WorkingWithSphereRadius {
    public static void main(String[] args) {
        Scene scene = new Scene();
        Sphere sphere = new Sphere();
        sphere.setRadius(10);
        scene.getRootNode().createChildNode(sphere);
        scene.save("sphere.obj", FileFormat.WAVEFRONTOBJ);
    }
}
