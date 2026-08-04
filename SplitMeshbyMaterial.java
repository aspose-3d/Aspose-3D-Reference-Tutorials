import com.aspose.threed.*;

public class SplitMeshbyMaterial {
    public static void main(String[] args) {
        Mesh box = (new Box()).toMesh();
        VertexElementMaterial mat = (VertexElementMaterial) box.createElement(VertexElementType.MATERIAL, MappingMode.POLYGON, ReferenceMode.INDEX);
        mat.setIndices(new int[]{0, 1, 2, 3, 4, 5});
        Mesh[] planes = PolygonModifier.splitMesh(box, SplitMeshPolicy.CLONE_DATA);
        mat.getIndices().clear();
        mat.setIndices(new int[]{0, 0, 0, 1, 1, 1});
        planes = PolygonModifier.splitMesh(box, SplitMeshPolicy.COMPACT_DATA);
        System.out.println("\nSplitting a mesh by specifying the material successfully.");
    }
}
