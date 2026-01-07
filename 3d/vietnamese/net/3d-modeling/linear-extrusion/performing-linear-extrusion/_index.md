---
date: 2026-01-07
description: Tìm hiểu cách extrude tuyến tính một hồ sơ 2D và xuất mô hình 3D định
  dạng OBJ bằng Aspose.3D cho .NET. Hướng dẫn extrude tuyến tính này sẽ chỉ dẫn bạn
  từng bước.
linktitle: Performing Linear Extrusion
second_title: Aspose.3D .NET API
title: Cách thực hiện Extrude tuyến tính với Aspose.3D cho .NET
url: /vi/net/3d-modeling/linear-extrusion/performing-linear-extrusion/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Cách linear extrude với Aspose.3D cho .NET

## Giới thiệu

Chào mừng bạn đến với **linear extrusion tutorial**! Trong hướng dẫn này, bạn sẽ khám phá **how to linear extrude** một profile 2‑D và biến nó thành một đối tượng 3‑D hoàn chỉnh bằng cách sử dụng Aspose.3D cho .NET. Dù bạn đang xây dựng một ứng dụng kiểu CAD hay chỉ cần **export 3d model obj** cho quá trình xử lý tiếp theo, hướng dẫn chi tiết này sẽ giúp bạn tự tin thêm khả năng tạo hình học mạnh mẽ vào dự án của mình.

## Câu trả lời nhanh
- **What is linear extrusion?** Mở rộng một hình dạng 2‑D dọc theo một đường thẳng để tạo ra một khối rắn 3‑D.  
- **Which library do we use?** Thư viện chúng ta sử dụng là Aspose.3D cho .NET.  
- **Do I need a license?** Một giấy phép tạm thời hoạt động cho việc thử nghiệm; giấy phép đầy đủ cần thiết cho môi trường sản xuất.  
- **Can I export to OBJ?** Có – cảnh cuối cùng được lưu dưới dạng tệp Wavefront OBJ.  
- **How many lines of code?** Dưới 30 dòng C# cộng với các chú thích giải thích.

## Linear Extrusion là gì?

Linear extrusion lấy một profile phẳng (như hình chữ nhật hoặc vòng tròn) và quét nó dọc theo một đường thẳng, tùy chọn có thể thêm các vòng xoắn, thu phóng hoặc độ dịch. Kết quả là một khối rắn có thể được render, chỉnh sửa hoặc export để sử dụng trong các công cụ 3‑D khác.

## Tại sao nên sử dụng Aspose.3D cho Linear Extrusion?

* **Zero‑dependency:** Không cần các kernel CAD bên ngoài.  
* **Full .NET support:** Hoạt động với .NET Framework, .NET Core và .NET 5/6+.  
* **Export flexibility:** Lưu trực tiếp sang OBJ, STL, FBX và nhiều định dạng khác.  
* **Rich API:** Kiểm soát slices, twist và offsets chỉ bằng một vài thuộc tính.

## Tiền đề

Trước khi bắt đầu, hãy chắc chắn rằng bạn đã có:

1. **Aspose.3D installed** – tải xuống từ [here](https://releases.aspose.com/3d/net/).  
2. **Documentation access** – làm theo hướng dẫn cài đặt [here](https://reference.aspose.com/3d/net/).  
3. Môi trường phát triển .NET (Visual Studio, VS Code, hoặc Rider) với các namespace cần thiết đã được tham chiếu.

## Nhập các Namespace

Bao gồm các namespace thiết yếu để mở khóa chức năng của Aspose.3D:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

Các namespace này cho phép bạn truy cập vào `Scene`, `LinearExtrusion`, `RectangleShape` và các lớp tiện ích như `Vector3`.

## Thực hiện Linear Extrusion

Dưới đây là quy trình hoàn chỉnh. Mỗi bước được giải thích bằng ngôn ngữ đơn giản trước khối mã tương ứng, để bạn có thể theo dõi mà không phải đoán mã làm gì.

### Bước 1: Khởi tạo Profile Cơ bản

Đầu tiên, tạo hình dạng 2‑D sẽ được extrude. Trong ví dụ này chúng ta sử dụng một hình chữ nhật với bán kính bo tròn nhỏ.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

*Why this matters:* Profile xác định phần mặt cắt ngang của đối tượng 3‑D cuối cùng. Điều chỉnh `RoundingRadius`, chiều rộng hoặc chiều cao để có các hình dạng khác nhau.

### Bước 2: Áp dụng Linear Extrusion

Bây giờ chúng ta quét profile 10 đơn vị dọc theo trục Z, thêm 100 slices để mịn hơn, căn giữa geometry và áp dụng một vòng xoắn 360° đầy đủ cùng offset.

```csharp
var extrusion = new LinearExtrusion(profile, 10) { Slices = 100, Center = true, Twist = 360, TwistOffset = new Vector3(10, 0, 0) };
```

*Pro tip:* Thử thay đổi `Slices` để cân bằng giữa hiệu năng và chất lượng hình ảnh, và thử nghiệm `Twist` để tạo hiệu ứng xoắn ốc.

### Bước 3: Tạo Scene

`Scene` hoạt động như một container cho tất cả các thực thể 3‑D — hãy nghĩ nó như một canvas.

```csharp
Scene scene = new Scene();
```

### Bước 4: Thêm Extrusion vào Scene

Gắn geometry đã extrude vào node gốc của scene để nó trở thành một phần của hierarchy có thể render.

```csharp
scene.RootNode.CreateChildNode(extrusion);
```

### Bước 5: Lưu mô hình 3‑D

Cuối cùng, export scene thành tệp OBJ được hỗ trợ rộng rãi. Điều này thể hiện khả năng **export 3d model obj** của Aspose.3D.

```csharp
scene.Save(RunExamples.GetOutputFilePath("LinearExtrusion.obj"), FileFormat.WavefrontOBJ);
```

Khi bạn mở tệp `LinearExtrusion.obj` kết quả trong bất kỳ trình xem 3‑D nào, bạn sẽ thấy một khối chữ nhật xoắn — chính xác như mô tả trong mã.

## Những lỗi thường gặp & Mẹo

| Issue | Why it Happens | How to Fix |
|-------|----------------|------------|
| **Profile không hiển thị** | Quên thêm extrusion vào scene. | Đảm bảo gọi `CreateChildNode`. |
| **Twist trông phẳng** | `Slices` quá thấp, gây ra hình học thô. | Tăng `Slices` (ví dụ, 200) để có twist mượt hơn. |
| **Export thất bại** | Thư mục đầu ra không tồn tại hoặc thiếu quyền ghi. | Sử dụng `RunExamples.GetOutputFilePath` hoặc tạo thư mục thủ công. |
| **Scaling không mong muốn** | `Center` được đặt thành `false` làm dịch chuyển geometry. | Đặt `Center = true` trừ khi bạn cần offset. |

## Câu hỏi thường gặp

### Q1: Aspose.3D có phù hợp cho người mới bắt đầu không?

A1: Chắc chắn! Aspose.3D cung cấp một API thân thiện với người dùng, và hướng dẫn này dẫn bạn qua các kiến thức cơ bản của linear extrusion.

### Q2: Tôi có thể sử dụng Aspose.3D cho các dự án thương mại không?

A2: Có, Aspose.3D có các tùy chọn giấy phép cho cả sử dụng cá nhân và thương mại. Kiểm tra [here](https://purchase.aspose.com/buy) để biết chi tiết.

### Q3: Làm sao tôi có thể nhận giấy phép tạm thời để thử nghiệm?

A3: Truy cập [this link](https://purchase.aspose.com/temporary-license/) để lấy giấy phép tạm thời cho mục đích thử nghiệm.

### Q4: Tôi có thể tìm hỗ trợ cộng đồng ở đâu?

A4: Tham gia [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) để kết nối với cộng đồng năng động và nhận trợ giúp.

### Q5: Có bản dùng thử miễn phí không?

A5: Chắc chắn! Tải phiên bản dùng thử miễn phí [here](https://releases.aspose.com/) để trải nghiệm khả năng của Aspose.3D ngay lập tức.

**Cập nhật lần cuối:** 2026-01-07  
**Kiểm tra với:** Aspose.3D 24.11 for .NET  
**Tác giả:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}