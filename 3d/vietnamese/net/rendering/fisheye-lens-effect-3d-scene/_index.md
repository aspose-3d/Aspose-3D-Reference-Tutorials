---
title: Áp dụng hiệu ứng ống kính mắt cá với Aspose.3D cho .NET
linktitle: Áp dụng hiệu ứng ống kính mắt cá cho cảnh 3D
second_title: API Aspose.3D .NET
description: Nâng cao cảnh 3D của bạn với Aspose.3D cho .NET! Tìm hiểu cách áp dụng hiệu ứng thấu kính mắt cá quyến rũ từng bước. Tải ngay!
type: docs
weight: 12
url: /vi/net/rendering/fisheye-lens-effect-3d-scene/
---
## Giới thiệu
Bạn đang tìm cách nâng cao sức hấp dẫn trực quan của cảnh 3D của mình? Đắm mình vào thế giới hấp dẫn của các hiệu ứng thấu kính mắt cá với Aspose.3D cho .NET. Hướng dẫn này sẽ hướng dẫn bạn từng bước cách áp dụng hiệu ứng thấu kính mắt cá cho cảnh 3D của bạn, mang lại cho chúng một phối cảnh độc đáo và quyến rũ.
## Điều kiện tiên quyết
Trước khi chúng ta bắt đầu, hãy đảm bảo bạn có sẵn các điều kiện tiên quyết sau:
-  Aspose.3D for .NET: Đảm bảo rằng bạn đã cài đặt thư viện Aspose.3D cho .NET. Nếu không, bạn có thể tải xuống[đây](https://releases.aspose.com/3d/net/).
-  Cảnh 3D mẫu: Chúng tôi sẽ làm việc với tệp cảnh 3D mẫu (VirtualCity.glb). Bạn có thể sử dụng cảnh của riêng mình hoặc tải xuống mẫu từ[Tài liệu Aspose.3D](https://reference.aspose.com/3d/net/).
## Nhập không gian tên
Trong dự án .NET của bạn, hãy bao gồm các vùng tên cần thiết để truy cập các chức năng Aspose.3D. Thêm các không gian tên sau vào đầu mã của bạn:
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
## Bước 1: Tải cảnh 3D
Tải tệp cảnh 3D vào dự án của bạn bằng mã sau:
```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("VirtualCity.glb"));
```
## Bước 2: Thiết lập camera và đèn
Tạo máy ảnh và đèn để nâng cao khía cạnh trực quan của cảnh của bạn. Điều chỉnh các tham số như NearPlane, FarPlane và RotationMode nếu cần:
```csharp
Camera cam = new Camera(ProjectionType.Perspective)
{
    NearPlane = 0.1,
    FarPlane = 200,
    RotationMode = RotationMode.FixedDirection
};
scene.RootNode.CreateChildNode(cam).Transform.Translation = new Vector3(5, 6, 0);
scene.RootNode.CreateChildNode(new Light() { LightType = LightType.Point }).Transform.Translation = new Vector3(-10, 7, -10);
scene.RootNode.CreateChildNode(new Light() { Color = new Vector3(Color.CadetBlue) }).Transform.Translation = new Vector3(49, 0, 49);
```
## Bước 3: Tạo mục tiêu kết xuất và kết xuất
Thiết lập trình kết xuất và tạo mục tiêu kết xuất cho bản đồ khối và kết cấu 2D:
```csharp
using (var renderer = Renderer.CreateRenderer())
{
    IRenderTexture rt = renderer.RenderFactory.CreateCubeRenderTexture(new RenderParameters(false), 512, 512);
    IRenderTexture final = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(false, 32, 0, 0), 1024, 1024);
    rt.CreateViewport(cam, RelativeRectangle.FromScale(0, 0, 1, 1));
    renderer.Render(rt);
```
## Bước 4: Áp dụng hiệu ứng ống kính mắt cá
Thực hiện xử lý hậu kỳ hiệu ứng ống kính mắt cá trên bản đồ khối được hiển thị:
```csharp
PostProcessing fisheye = renderer.GetPostProcessing("fisheye");
fisheye.FindProperty("fov").Value = 360.0;
fisheye.Input = rt.Targets[0];
renderer.Execute(fisheye, final);
((ITexture2D)final.Targets[0]).Save("Your Output Directory" + "fisheye.png", ImageFormat.Png);
```
## Phần kết luận
Chúc mừng! Bạn đã áp dụng thành công hiệu ứng thấu kính mắt cá cho cảnh 3D của mình bằng Aspose.3D for .NET. Thử nghiệm với các cảnh và thông số khác nhau để phát huy khả năng sáng tạo của bạn.
## Các câu hỏi thường gặp
### Tôi có thể áp dụng hiệu ứng mắt cá cho bất kỳ cảnh 3D nào không?
Có, bạn có thể áp dụng hiệu ứng mắt cá cho bất kỳ cảnh 3D nào. Đảm bảo rằng cảnh được tải và chiếu sáng đúng cách để có kết quả tối ưu.
### Tầm quan trọng của việc điều chỉnh trường nhìn (fov) thành 360 độ là gì?
Trường nhìn 360 độ đảm bảo chiếu hình cầu hoàn chỉnh, tạo hiệu ứng mắt cá tuyệt đẹp.
### Làm cách nào tôi có thể tùy chỉnh ánh sáng trong cảnh 3D của mình?
Bạn có thể điều chỉnh các thuộc tính của đèn, chẳng hạn như vị trí, loại và màu sắc, để đạt được hiệu ứng ánh sáng mong muốn.
### Có giới hạn nào về kích thước của cảnh 3D có thể được xử lý không?
Kích thước của cảnh 3D chủ yếu bị giới hạn bởi tài nguyên hệ thống. Đảm bảo rằng phần cứng của bạn có thể xử lý kích thước cảnh của bạn.
### Tôi có thể sử dụng định dạng đầu ra khác thay vì PNG cho kết quả hiệu ứng mắt cá không?
Có, bạn có thể sửa đổi mã để lưu đầu ra ở các định dạng hình ảnh khác nhau dựa trên yêu cầu của bạn.