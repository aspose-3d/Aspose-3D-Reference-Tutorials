import com.aspose.threed.*;

public class CreateHierarchy {
    public static void main(String[] args) {
        Scene s = new Scene();
        Node a = s.getRootNode().createChildNode("a");
        a.createChildNode("a1");
        a.createChildNode("a2");
        s.getRootNode().createChildNode("b");
        Node c = s.getRootNode().createChildNode("c");
        c.createChildNode("c1").addEntity(new Camera("cam"));
        c.createChildNode("c2").addEntity(new Light("light"));
    }
}
