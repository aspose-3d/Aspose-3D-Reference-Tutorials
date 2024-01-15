---
title: Customize 3D File Loading in Java with Aspose.3D LoadOptions
linktitle: Customize 3D File Loading in Java with Aspose.3D LoadOptions
second_title: Aspose.3D Java API
description: 
type: docs
weight: 12
url: /java/load-and-save/customize-3d-file-loading/
---

## Complete Source Code
```java
package examples.loadsave;

import com.aspose.threed.*;


import java.io.IOException;

public class LoadOptions {

        public static void run() throws IOException {

            discreet3DSLoadOption();
            objLoadOption();
            stlLoadOption();
            u3dLoadOption();
            gltfLoadOptions();
            plyLoadOptions();
            xLoadOptions();
        }
        public static void discreet3DSLoadOption()
        {
            // ExStart:Discreet3DSOption
            // The path to the documents directory.
            String MyDir = "Your Document Directory";
            Discreet3dsLoadOptions loadOpts = new Discreet3dsLoadOptions();
            // Sets wheather to use the transformation defined in the first frame of animation track.
            loadOpts.setApplyAnimationTransform(true);
            // Flip the coordinate system
            loadOpts.setFlipCoordinateSystem(true);
            // Prefer to use gamma-corrected color if a 3ds file provides both original color and gamma-corrected color.
            loadOpts.setGammaCorrectedColor(true);
            // Configure the look up paths to allow importer to find external dependencies.
            loadOpts.getLookupPaths().add(MyDir);
            // ExEnd:Discreet3DSOption
        }
        public static void objLoadOption()
        {
            // ExStart:ObjLoadOption
            // The path to the documents directory.
            String MyDir = "Your Document Directory";
            // Initialize an object
            ObjLoadOptions loadObjOpts = new ObjLoadOptions();
            // Import materials from external material library file
            loadObjOpts.setEnableMaterials(true);
            // Flip the coordinate system.
            loadObjOpts.setFlipCoordinateSystem(true);
            // Configure the look up paths to allow importer to find external dependencies.
            loadObjOpts.getLookupPaths().add(MyDir);
            // ExEnd:ObjLoadOption
        }
        public static void stlLoadOption()
        {
            // ExStart:STLLoadOption
            // The path to the documents directory.
            String MyDir = "Your Document Directory";
            // Initialize an object
            StlLoadOptions loadSTLOpts = new StlLoadOptions();
            // Flip the coordinate system.
            loadSTLOpts.setFlipCoordinateSystem(true);
            // Configure the look up paths to allow importer to find external dependencies.
            loadSTLOpts.getLookupPaths().add(MyDir);
            // ExEnd:STLLoadOption
        }
        public static void u3dLoadOption()
        {
            // ExStart:U3DLoadOption
            // The path to the documents directory.
            String MyDir = "Your Document Directory";
            // Initialize an object
            U3dLoadOptions loadU3DOpts = new U3dLoadOptions();
            // Flip the coordinate system.
            loadU3DOpts.setFlipCoordinateSystem(true);
            // Configure the look up paths to allow importer to find external dependencies.
            loadU3DOpts.getLookupPaths().add(MyDir);
            // ExEnd:U3DLoadOption
        }
        public static void gltfLoadOptions() throws IOException {
            // ExStart:glTFLoadOptions
            // The path to the documents directory.
            String MyDir = "Your Document Directory";
            // Initialize Scene class object
            Scene scene = new Scene();
            // Set load options
            GltfLoadOptions loadOpt = new GltfLoadOptions();
            // The default value is true, usually we don't need to change it. Aspose.3D will automatically flip the V/T texture coordinate during load and save.
            loadOpt.setFlipTexCoordV(true);
            scene.open( MyDir + "Duck.gltf", loadOpt);
            // ExEnd:glTFLoadOptions
        }
        public static void plyLoadOptions() throws IOException {
            // ExStart:PlyLoadOptions
            // the path to the documents directory.
            String MyDir = "Your Document Directory";
            // initialize Scene class object
            Scene scene = new Scene();
            // initialize an object
            PlyLoadOptions loadPLYOpts = new PlyLoadOptions();
            // Flip the coordinate system.
            loadPLYOpts.setFlipCoordinateSystem(true);
            // load 3D Ply model
            scene.open(MyDir + "vase-v2.ply", loadPLYOpts);
            // ExEnd:PlyLoadOptions
        }
        public static void xLoadOptions() throws IOException {
            // ExStart:XLoadOptions
            // the path to the documents directory.
            String MyDir = "Your Document Directory";
            // initialize Scene class object
            Scene scene = new Scene();
            // initialize an object
            XLoadOptions loadXOpts = new XLoadOptions(FileContentType.ASCII);
            // flip the coordinate system.
            loadXOpts.setFlipCoordinateSystem(true);
            // load 3D X file
            scene.open(MyDir + "warrior.x", loadXOpts);
            // ExEnd:XLoadOptions
        }
        private static void FBXLoadOptions() throws IOException
        {
            //ExStart: FBXLoadOptions
            String dataDir = "Your Document Directory";
            //This will output all properties defined in GlobalSettings in FBX file.
            Scene scene = new Scene();
            FbxLoadOptions opt = new FbxLoadOptions();
            opt.setKeepBuiltinGlobalSettings(true);
            scene.open(dataDir + "test.FBX", opt);
            for(Property property:scene.getRootNode().getAssetInfo().getProperties())
            {
                System.out.println(property);
            }
            //ExEnd: FBXLoadOptions
        }
}

```