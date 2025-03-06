---
title: Chụp các khung nhìn trong cảnh 3D
linktitle: Chụp các khung nhìn trong cảnh 3D
second_title: API Aspose.3D .NET
description: Tìm hiểu cách chụp các khung nhìn 3D tuyệt đẹp bằng Aspose.3D cho .NET. Hướng dẫn từng bước để hiển thị cảnh một cách linh hoạt.
weight: 11
url: /vi/net/rendering/capture-viewport/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Chụp các khung nhìn trong cảnh 3D

## Giới thiệu

Trong lĩnh vực đồ họa và trực quan hóa 3D, việc chụp khung nhìn là một kỹ năng thiết yếu giúp nâng cao độ sâu và chi tiết cho cảnh của bạn. Aspose.3D for .NET cung cấp một giải pháp mạnh mẽ để hiển thị và thao tác các cảnh 3D. Hướng dẫn này sẽ hướng dẫn bạn quy trình chụp các khung nhìn trong cảnh 3D bằng Aspose.3D, cho phép bạn tạo các hình ảnh trực quan tuyệt đẹp một cách dễ dàng.

## Điều kiện tiên quyết

Trước khi đi sâu vào hướng dẫn, hãy đảm bảo bạn có sẵn các điều kiện tiên quyết sau:

-  Aspose.3D for .NET Library: Đảm bảo bạn đã cài đặt thư viện Aspose.3D. Bạn có thể tải nó xuống từ[đây](https://releases.aspose.com/3d/net/).

## Nhập không gian tên

Để bắt đầu, hãy nhập các vùng tên cần thiết vào dự án .NET của bạn:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using System.Drawing;
using System.Drawing.Imaging;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Render;
using Aspose.ThreeD.Utilities;
```

## Bước 1: Tải cảnh 3D hiện có

Bắt đầu bằng cách tải cảnh 3D hiện có vào dự án của bạn. Đoạn mã sau đây minh họa điều này:

```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("scene.obj"));
```

## Bước 2: Tạo máy ảnh

Tiếp theo, tạo một phiên bản của máy ảnh và đặt vị trí cũng như mục tiêu của nó:

```csharp
Camera camera = new Camera();
scene.RootNode.CreateChildNode("camera", camera).Transform.Translation = new Vector3(2, 44, 66);
camera.LookAt = new Vector3(50, 12, 0);
```

## Bước 3: Thêm ánh sáng vào cảnh

Cải thiện cảnh của bạn bằng cách thêm nguồn sáng. Đoạn mã bên dưới minh họa cách tạo điểm sáng:

```csharp
scene.RootNode.CreateChildNode("light", new Light() { Color = new Vector3(Color.White), LightType = LightType.Point }).Transform.Translation = new Vector3(26, 57, 43);
```

## Bước 4: Định cấu hình Trình kết xuất và Mục tiêu kết xuất

Thiết lập trình kết xuất và tạo mục tiêu kết xuất để chụp cảnh:

```csharp
using (var renderer = Renderer.CreateRenderer())
{
    renderer.EnableShadows = false;

    using (IRenderTexture rt = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(), 1, 1024, 1024))
    {
        // ... (tiếp tục ở các bước tiếp theo)
    }
}
```

## Bước 5: Xác định khung nhìn và kết xuất

Xác định khung nhìn và hiển thị cảnh để tạo hình ảnh đầu ra:

```csharp
Viewport vp = rt.CreateViewport(camera, new RelativeRectangle() { ScaleWidth = 1, ScaleHeight = 1 });
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "file-1viewports_out.png", ImageFormat.Png);
```

## Bước 6: Sửa đổi khung nhìn và kết xuất lại

Sửa đổi khung nhìn và hiển thị cảnh một lần nữa, thể hiện tính linh hoạt của Aspose.3D:

```csharp
vp.Area = new RelativeRectangle() { ScaleWidth = 0.5f, ScaleHeight = 1 };
rt.CreateViewport(camera, new RelativeRectangle() { ScaleX = 0.5f, ScaleWidth = 0.5f, ScaleHeight = 1 });
camera.FieldOfView = 90;
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "file-2viewports_out.png", ImageFormat.Png);
```

Tiếp tục thử nghiệm các cấu hình khác nhau để đạt được hiệu ứng hình ảnh mong muốn.

## Phần kết luận

Trong hướng dẫn này, chúng tôi đã khám phá quá trình chụp các khung nhìn trong cảnh 3D bằng Aspose.3D cho .NET. Tận dụng các tính năng mạnh mẽ của nó, bạn có thể nâng các dự án đồ họa 3D của mình lên tầm cao mới, mang lại trải nghiệm hình ảnh quyến rũ.

## Câu hỏi thường gặp

### Câu hỏi 1: Aspose.3D có tương thích với các định dạng tệp 3D khác không?

Câu trả lời 1: Có, Aspose.3D hỗ trợ nhiều định dạng tệp 3D khác nhau, đảm bảo khả năng tương thích với nhiều công cụ thiết kế.

### Câu hỏi 2: Tôi có thể sử dụng Aspose.3D để phát triển trò chơi không?

Câu trả lời 2: Mặc dù Aspose.3D được thiết kế chủ yếu cho đồ họa và trực quan nhưng các chức năng của nó có thể bổ sung cho một số khía cạnh nhất định của quá trình phát triển trò chơi.

### Câu hỏi 3: Tôi có thể tìm thêm ví dụ và tài liệu ở đâu?

 A3: Khám phá toàn diện[Tài liệu Aspose.3D](https://reference.aspose.com/3d/net/) để biết thêm ví dụ và thông tin chi tiết.

### Q4: Có bản dùng thử miễn phí không?

 Câu trả lời 4: Có, bạn có thể truy cập bản dùng thử miễn phí[đây](https://releases.aspose.com/).

### Câu hỏi 5: Làm cách nào tôi có thể tìm kiếm sự giúp đỡ hoặc tham gia vào cộng đồng?

 Câu trả lời 5: Tham gia cộng đồng Aspose.3D trên[diễn đàn hỗ trợ](https://forum.aspose.com/c/3d/18) để được hỗ trợ và hợp tác.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
