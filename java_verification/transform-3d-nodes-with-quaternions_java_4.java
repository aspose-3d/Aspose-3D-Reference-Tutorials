import com.aspose.threed.*;
public class TempVerify {
// Create mesh manually with vertices and polygons
Mesh mesh = new Mesh();
mesh.addControlPoint(-1, 1, 1);
mesh.addControlPoint(1, 1, 1);
mesh.addControlPoint(1, -1, 1);
mesh.addControlPoint(-1, -1, 1);
mesh.addControlPoint(-1, 1, -1);
mesh.addControlPoint(1, 1, -1);
mesh.addControlPoint(1, -1, -1);
mesh.addControlPoint(-1, -1, -1);

mesh.createPolygon(0, 1, 2, 3);
mesh.createPolygon(4, 6, 7, 5);
mesh.createPolygon(0, 3, 7, 4);
mesh.createPolygon(1, 5, 6, 2);
mesh.createPolygon(0, 4, 5, 1);
mesh.createPolygon(3, 2, 6, 7);
}
