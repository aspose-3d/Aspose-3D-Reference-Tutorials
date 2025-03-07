---
title: Hiển thị cảnh thành Cubemap với sáu mặt
linktitle: Hiển thị cảnh thành Cubemap với sáu mặt
second_title: API Aspose.3D .NET
description: Tạo các sơ đồ khối tuyệt đẹp với Aspose.3D cho .NET. Làm theo hướng dẫn từng bước của chúng tôi để hiển thị cảnh 3D thành sơ đồ khối sáu mặt quyến rũ.
weight: 14
url: /vi/net/rendering/render-scene-cubemap/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Hiển thị cảnh thành Cubemap với sáu mặt

## Giới thiệu
Chào mừng bạn đến với hướng dẫn từng bước này về cách hiển thị một cảnh thành sơ đồ khối có sáu mặt bằng Aspose.3D cho .NET. Trong hướng dẫn này, chúng tôi sẽ hướng dẫn bạn quy trình tạo sơ đồ khối tuyệt đẹp bằng cách hiển thị cảnh 3D. Aspose.3D là một API .NET mạnh mẽ giúp đơn giản hóa thao tác đồ họa 3D và với hướng dẫn này, bạn sẽ khai thác các khả năng của nó để tạo ra các sơ đồ khối quyến rũ.
## Điều kiện tiên quyết
Trước khi chúng ta đi sâu vào hướng dẫn, hãy đảm bảo bạn có sẵn các điều kiện tiên quyết sau:
- Kiến thức làm việc về phát triển C# và .NET.
-  Aspose.3D cho .NET được cài đặt. Bạn có thể tải nó xuống[đây](https://releases.aspose.com/3d/net/).
- Tệp cảnh 3D ở định dạng GLB (ví dụ: "VirtualCity.glb") để hiển thị.
## Nhập không gian tên
Bắt đầu bằng cách nhập các không gian tên cần thiết cho Aspose.3D trong mã C# của bạn:
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Render;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Drawing.Imaging;
using System.Linq;
using System.Text;
```
## Bước 1: Tải cảnh
Tải tệp cảnh 3D bằng mã sau:
```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("VirtualCity.glb"));
```
## Bước 2: Tạo Camera và Đèn
Tạo một camera và hai đèn để chiếu sáng khung cảnh:
```csharp
Camera cam = new Camera(ProjectionType.Perspective)
{
    NearPlane = 0.1,
    FarPlane = 200,
    RotationMode = RotationMode.FixedDirection
};
scene.RootNode.CreateChildNode(cam).Transform.Translation = new Vector3(5, 6, 0);
scene.RootNode.CreateChildNode(new Light() { LightType = LightType.Point }).Transform.Translation = new Vector3(-10, 7, -10);
scene.RootNode.CreateChildNode(new Light()
{
    Color = new Vector3(Color.CadetBlue)
}).Transform.Translation = new Vector3(49, 0, 49);
```
## Bước 3: Tạo Trình kết xuất và Mục tiêu kết xuất
Tạo trình kết xuất và mục tiêu kết xuất bản đồ khối với kết cấu có chiều sâu:
```csharp
using (var renderer = Renderer.CreateRenderer())
{
    IRenderTexture rt = renderer.RenderFactory.CreateCubeRenderTexture(new RenderParameters(false), 512, 512);
    rt.CreateViewport(cam, RelativeRectangle.FromScale(0, 0, 1, 1));
    renderer.Render(rt);
    ITextureCubemap cubemap = rt.Targets[0] as ITextureCubemap;
```
## Bước 4: Lưu khuôn mặt Cubemap
Lưu từng mặt của sơ đồ khối vào đĩa với tên tệp được chỉ định:
```csharp
CubeFaceData<string> fileNames = new CubeFaceData<string>()
{
    Right = "Your Output Directory" + "right.png",
    Left = "Your Output Directory" + "left.png",
    Back = "Your Output Directory" + "back.png",
    Front = "Your Output Directory" + "front.png",
    Bottom = "Your Output Directory" + "bottom.png",
    Top = "Your Output Directory" + "top.png"
};
cubemap.Save(fileNames, ImageFormat.Png);
```
## Phần kết luận
Chúc mừng! Bạn đã hiển thị thành công cảnh 3D thành sơ đồ khối bằng Aspose.3D cho .NET. Khám phá các tùy chọn tùy chỉnh khác và nâng cao các dự án đồ họa 3D của bạn với API mạnh mẽ này.
## Các câu hỏi thường gặp
### Câu hỏi: Tôi có thể sử dụng Aspose.3D cho .NET với các định dạng tệp 3D khác không?
Có, Aspose.3D hỗ trợ nhiều định dạng tệp 3D khác nhau, mang lại sự linh hoạt cho các dự án của bạn.
### Câu hỏi: Làm cách nào tôi có thể nhận được hỗ trợ cho Aspose.3D?
 Tham quan[Diễn đàn Aspose.3D](https://forum.aspose.com/c/3d/18) để được cộng đồng hỗ trợ và thảo luận.
### Hỏi: Có bản dùng thử miễn phí không?
 Có, bạn có thể truy cập bản dùng thử miễn phí[đây](https://releases.aspose.com/).
### Câu hỏi: Tôi có thể kết xuất cảnh có hoạt ảnh bằng Aspose.3D không?
Tuyệt đối! Aspose.3D hỗ trợ hiển thị cảnh 3D hoạt hình.
### Hỏi: Tôi có thể tìm tài liệu chi tiết ở đâu?
 Tham khảo đến[Tài liệu Aspose.3D](https://reference.aspose.com/3d/net/) để biết thông tin chuyên sâu.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
