import com.aspose.threed.*;

import java.io.IOException;

public class TestGenerateMeshData {
    public static void main(String[] args) {
        // The path to the documents directory.
        String MyDir = "Your Document Directory";

        // Load a 3ds file, 3ds file doesn't have normal data, but it has smoothing group
        Scene s = new Scene(MyDir + "camera.3ds");

        s.getRootNode().accept(new NodeVisitor() {
            @Override
            public boolean call(Node node) {
                Mesh mesh = (Mesh) node.getEntity();
                if (mesh != null) {
                    VertexElementNormal normals = PolygonModifier.generateNormal(mesh);
                    mesh.addElement(normals);
                }
                return true;
            }
        });

        System.out.println("\nNormal data generated successfully for all meshes.");
    }
}
