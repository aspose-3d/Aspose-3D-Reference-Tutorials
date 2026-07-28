import com.aspose.threed.*;
public class TempVerify {
Mesh mesh = new Mesh();
mesh.addControlPoint(-1, -1, 1);
mesh.addControlPoint(1, -1, 1);
mesh.addControlPoint(-1, 1, 1);
mesh.addControlPoint(1, 1, 1);
mesh.addControlPoint(-1, -1, -1);
mesh.addControlPoint(1, -1, -1);
mesh.addControlPoint(-1, 1, -1);
mesh.addControlPoint(1, 1, -1);

mesh.createPolygon(0, 2, 3, 1);
mesh.createPolygon(4, 5, 7, 6);
mesh.createPolygon(0, 1, 5, 4);
mesh.createPolygon(2, 6, 7, 3);
mesh.createPolygon(0, 4, 6, 2);
mesh.createPolygon(1, 3, 7, 5);

VertexElementNormal elementNormal = (VertexElementNormal)mesh.createElement(VertexElementType.NORMAL, MappingMode.CONTROL_POINT, ReferenceMode.DIRECT);
elementNormal.setData(normals);
}
