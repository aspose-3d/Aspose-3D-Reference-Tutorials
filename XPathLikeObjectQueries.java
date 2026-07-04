import com.aspose.threed.*;

public class XPathLikeObjectQueries {
    public static void main(String[] args) {
        Scene s = new Scene();
        Node a = s.getRootNode().createChildNode("a");
        a.createChildNode("a1");
        a.createChildNode("a2");
        s.getRootNode().createChildNode("b");
        Node c = s.getRootNode().createChildNode("c");
        c.createChildNode("c1").addEntity(new Camera("cam"));
        c.createChildNode("c2").addEntity(new Light("light"));
        java.util.List<Object> objects = s.getRootNode().selectObjects("//*[(@Type = 'Camera') or (@Name = 'light')]");
        A3DObject c1 = (A3DObject) s.getRootNode().selectSingleObject("/c/*/ <Camera>");
        A3DObject obj = (A3DObject) s.getRootNode().selectSingleObject("a1");
        obj = (A3DObject) s.getRootNode().selectSingleObject("/");
    }
}
