---
title: Tùy chọn tải tùy chỉnh
linktitle: Tùy chọn tải tùy chỉnh
second_title: API Aspose.3D .NET
description: Khám phá Aspose.3D cho .NET giải pháp tối ưu để tải và lưu mô hình 3D liền mạch.
weight: 15
url: /vi/net/loading-and-saving/custom-load-options/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Tùy chọn tải tùy chỉnh

## Giới thiệu

Chào mừng bạn đến với thế giới của Aspose.3D cho .NET - một thư viện mạnh mẽ cho phép các nhà phát triển làm việc liền mạch với các tệp 3D. Trong hướng dẫn này, chúng ta sẽ đi sâu vào sự phức tạp của việc tải và lưu mô hình 3D, tập trung vào các tùy chọn tải tùy chỉnh. Cho dù bạn là nhà phát triển dày dạn kinh nghiệm hay người mới, hướng dẫn này sẽ hướng dẫn bạn từng bước quy trình, đảm bảo bạn khai thác toàn bộ tiềm năng của Aspose.3D cho .NET.

## Điều kiện tiên quyết

Trước khi chúng ta bắt đầu cuộc hành trình này, hãy đảm bảo bạn có sẵn các điều kiện tiên quyết sau:

-  Aspose.3D for .NET: Đảm bảo bạn đã cài đặt thư viện. Bạn có thể tải nó xuống[đây](https://releases.aspose.com/3d/net/).

- Thư mục Tài liệu: Tạo thư mục để lưu trữ các tệp mô hình 3D của bạn.

Bây giờ bạn đã có những thứ cần thiết, hãy cùng đi sâu vào thế giới thú vị của thao tác mô hình 3D!

## Nhập không gian tên

Trước tiên, hãy nhập các không gian tên cần thiết. Điều này sẽ tạo tiền đề cho cuộc hành trình của chúng ta vào vương quốc Aspose.3D.

```csharp
using System;
using System.IO;
using System.Collections.Generic;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Formats;
```

## Tải và lưu - Tùy chọn tải tùy chỉnh

### Bước 1: Tải tập tin Discreet3DS

```csharp
private static void Discreet3DSLoadOption()
{
    Discreet3dsLoadOptions loadOpts = new Discreet3dsLoadOptions();

    //Đặt tùy chọn tùy chỉnh
    loadOpts.ApplyAnimationTransform = true;
    loadOpts.FlipCoordinateSystem = true;
    loadOpts.GammaCorrectedColor = true;
    loadOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //Tải tập tin với các tùy chọn tải
    var scene = Scene.FromFile("test.3ds", loadOpts);
}
```

### Bước 2: Tải tệp OBJ

```csharp
private static void ObjLoadOption()
{
    ObjLoadOptions loadObjOpts = new ObjLoadOptions();

    //Đặt tùy chọn tùy chỉnh
    loadObjOpts.EnableMaterials = true;
    loadObjOpts.FlipCoordinateSystem = true;
    loadObjOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //Tải tập tin với các tùy chọn tải
    var scene = Scene.FromFile("test.obj", loadObjOpts);

}
```

### Bước 3: Tải tệp STL

```csharp
private static void STLLoadOption()
{
    // Đường dẫn đến thư mục tài liệu.
    StlLoadOptions loadSTLOpts = new StlLoadOptions();

    //Đặt tùy chọn tùy chỉnh
    loadSTLOpts.FlipCoordinateSystem = true;
    loadSTLOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //Tải tập tin với các tùy chọn tải
    var scene = Scene.FromFile("test.stl", loadSTLOpts);
}
```

### Bước 4: Tải tệp U3D

```csharp
private static void U3DLoadOption()
{
    // Đường dẫn đến thư mục tài liệu.
    string dataDir = "Your Document Directory";
    U3dLoadOptions loadU3DOpts = new U3dLoadOptions();

    //Đặt tùy chọn tùy chỉnh
    loadU3DOpts.FlipCoordinateSystem = true;
    loadU3DOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //Tải tập tin với các tùy chọn tải
    var scene = Scene.FromFile("test.u3d", loadU3DOpts);
}
```

### Bước 5: Tải tập tin glTF

```csharp
private static void glTFLoadOptions()
{
    // Đường dẫn đến thư mục tài liệu.
    Scene scene = new Scene();
    GltfLoadOptions loadOpt = new GltfLoadOptions();

    //Đặt tùy chọn tùy chỉnh
    loadOpt.FlipTexCoordV = true;
    scene.Open("Duck.gltf", loadOpt);
}
```

### Bước 6: Tải tệp PLY

```csharp
private static void PlyLoadOptions()
{
    // Đường dẫn đến thư mục tài liệu.
    string dataDir = "Your Document Directory";
    Scene scene = new Scene();
    PlyLoadOptions loadPLYOpts = new PlyLoadOptions();

    //Đặt tùy chọn tùy chỉnh
    loadPLYOpts.FlipCoordinateSystem = true;
    scene.Open("vase-v2.ply", loadPLYOpts);
}
```

### Bước 7: Tải tệp FBX

```csharp
private static void FBXLoadOptions()
{
    // Đường dẫn đến thư mục tài liệu.
    Scene scene = new Scene();
    FbxLoadOptions opt = new FbxLoadOptions() { KeepBuiltinGlobalSettings = true };

    //Đặt tùy chọn tùy chỉnh
    scene.Open("test.FBX", opt);

    // Thuộc tính đầu ra được xác định trong GlobalSettings trong tệp FBX
    foreach (Property property in scene.RootNode.AssetInfo.Properties)
    {
        Console.WriteLine(property);
    }
}
```

## Phần kết luận

Chúc mừng! Bạn đã điều hướng thành công trong thế giới tải và lưu mô hình 3D phức tạp bằng Aspose.3D cho .NET. Hướng dẫn này bao gồm các định dạng tệp khác nhau và các tùy chọn tải tùy chỉnh của chúng, cho phép bạn thao tác nội dung 3D một cách dễ dàng.

## Câu hỏi thường gặp

### Câu hỏi 1: Aspose.3D cho .NET có phù hợp cho người mới bắt đầu không?

A1: Chắc chắn rồi! Aspose.3D for .NET cung cấp giao diện thân thiện với người dùng, giúp các nhà phát triển ở mọi cấp độ có thể truy cập được.

### Câu hỏi 2: Tôi có thể sử dụng Aspose.3D cho các dự án thương mại không?

Câu trả lời 2: Có, Aspose.3D cho .NET đi kèm với giấy phép thương mại, cho phép bạn sử dụng nó trong các dự án của mình.

### Câu hỏi 3: Có bất kỳ hạn chế nào đối với các định dạng tệp được hỗ trợ không?

 Câu trả lời 3: Aspose.3D cho .NET hỗ trợ nhiều định dạng tệp 3D phổ biến, bao gồm OBJ, STL, FBX, v.v. Tham khảo đến[tài liệu](https://reference.aspose.com/3d/net/) để có danh sách đầy đủ.

### Q4: Có phiên bản dùng thử không?

Câu trả lời 4: Có, bạn có thể khám phá các khả năng của Aspose.3D dành cho .NET bằng cách tải xuống[dùng thử miễn phí](https://releases.aspose.com/).

### Câu hỏi 5: Tôi có thể tìm kiếm sự hỗ trợ cho Aspose.3D cho .NET ở đâu?

 A5: Tham quan[Diễn đàn Aspose.3D](https://forum.aspose.com/c/3d/18) để được cộng đồng hỗ trợ và giúp đỡ.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
