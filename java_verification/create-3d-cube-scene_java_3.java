import com.aspose.threed.*;
public class TempVerify {
// Initialize Node class object
Node cubeNode = new Node("box");

// Call Common class create mesh using polygon builder method to set mesh instance
Mesh mesh = new Mesh();

// Point node to the Mesh geometry
cubeNode.setEntity(mesh);
}
