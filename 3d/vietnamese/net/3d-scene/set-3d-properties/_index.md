---
date: 2026-01-17
description: Tìm hiểu cách liệt kê các thuộc tính vật liệu, thay đổi màu khuếch tán
  và chỉnh sửa các thuộc tính vật liệu 3D bằng Aspose.3D cho .NET. Bao gồm các ví
  dụ mã từng bước.
linktitle: List Material Properties in 3D Scenes with Aspose.3D
second_title: Aspose.3D .NET API
title: Liệt kê các thuộc tính vật liệu trong các cảnh 3D với Aspose.3D
url: /vi/net/3d-scene/set-3d-properties/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Liệt kê các thuộc tính vật liệu trong cảnh 3D với Aspose.3D

## Giới thiệu

Nếu bạn cần **liệt kê các thuộc tính vật liệu** của một mô hình 3D và sau đó điều chỉnh các yếu tố như màu diffuse, bạn đang ở đúng nơi. Aspose.3D for .NET cung cấp cho bạn một API sạch sẽ, hướng đối tượng, cho phép bạn kiểm tra, truy xuất và sửa đổi các thuộc tính vật liệu mà không rời khỏi mã C# của mình. Trong hướng dẫn này, chúng ta sẽ đi qua việc tải một cảnh, liệt kê các thuộc tính vật liệu của nó, và thay đổi các giá trị như thành phần diffuse — để bạn có thể tạo ra ngoại hình chính xác cho mô hình của mình.

## Câu trả lời nhanh
- **Mục tiêu chính là gì?** Liệt kê các thuộc tính vật liệu và sửa đổi chúng (ví dụ: màu diffuse).  
- **Thư viện nào cần thiết?** Aspose.3D for .NET.  
- **Có cần giấy phép không?** Cần một giấy phép tạm thời hoặc đầy đủ cho việc sử dụng trong môi trường sản xuất.  
- **Các định dạng tệp được hỗ trợ?** FBX, OBJ, STL, STL‑ASCII, 3MF và nhiều hơn nữa.  
- **Thời gian triển khai điển hình?** Khoảng 10‑15 phút cho một script liệt kê thuộc tính cơ bản.

## **Liệt kê các thuộc tính vật liệu** là gì?
Liệt kê các thuộc tính vật liệu có nghĩa là duyệt qua `PropertyCollection` của một vật liệu để đọc mỗi tên thuộc tính và giá trị hiện tại của nó. Điều này hữu ích cho việc gỡ lỗi, kiểm tra trực quan, hoặc xây dựng các điều khiển UI cho phép người dùng tinh chỉnh cài đặt vật liệu tại thời gian chạy.

## Tại sao nên dùng Aspose.3D để **truy cập các thuộc tính vật liệu**?
- **Không cần bộ chuyển đổi bên ngoài** – làm việc trực tiếp với các đối tượng .NET gốc.  
- **Mô hình thuộc tính phong phú** – hỗ trợ các thuộc tính tùy chỉnh đặc thù của FBX bên cạnh các giá trị PBR tiêu chuẩn.  
- **Đa nền tảng** – hoạt động trên .NET Framework, .NET Core và .NET 5/6+.  

## Yêu cầu trước

- Aspose.3D for .NET đã được cài đặt trong dự án của bạn. Tải xuống [tại đây](https://releases.aspose.com/3d/net/).  
- Một thư mục trên đĩa để lưu các tệp nguồn 3‑D của bạn (ví dụ: một tệp FBX có kết hợp texture).

Bây giờ bạn đã có những kiến thức cơ bản, hãy bắt đầu với mã.

## Import Namespaces

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```

## Bước 1: Tải cảnh 3D

```csharp
//ExStart: Load3DScene
string dataDir = "Your Document Directory";
Scene scene = new Scene(dataDir + "EmbeddedTexture.fbx");
//ExEnd: Load3DScene
```

## Bước 2: **Truy cập các thuộc tính vật liệu** của nút đầu tiên

```csharp
//ExStart: AccessMaterialProperties
Material material = scene.RootNode.ChildNodes[0].Material;
PropertyCollection props = material.Properties;
//ExEnd: AccessMaterialProperties
```

## Bước 3: **Liệt kê các thuộc tính vật liệu** – xem mọi cặp tên/giá trị

```csharp
//ExStart: ListAllProperties
foreach (var prop in props)
{
    Console.WriteLine("{0} = {1}", prop.Name, prop.Value);
}

//or using ordinal for loop
for (int i = 0; i < props.Count; i++)
{
    var prop = props[i];
    Console.WriteLine("{0} = {1}", prop.Name, prop.Value);
}
//ExEnd: ListAllProperties
```

## Bước 4: **Cách thay đổi diffuse** – sửa thuộc tính Diffuse

```csharp
//ExStart: GetModifyPropertyByName
var diffuse = props["Diffuse"];
Console.WriteLine(diffuse);

//modify property value by name
props["Diffuse"] = new Vector3(1, 0, 1); // sets a magenta diffuse color
//ExEnd: GetModifyPropertyByName
```

## Bước 5: **Truy xuất thuộc tính theo tên** – nhận một thể hiện kiểu mạnh

```csharp
//ExStart: GetPropertyInstanceByName
Property pdiffuse = props.FindProperty("Diffuse");
Console.WriteLine(pdiffuse);
//ExEnd: GetPropertyInstanceByName
```

## Bước 6: Duyệt các thuộc tính con của một thuộc tính (nâng cao)

```csharp
//ExStart: TraversePropertyProperties
Console.WriteLine("Property flags = {0}", pdiffuse.GetProperty("flags"));

//and some properties that only defined in FBX file:
Console.WriteLine("Label = {0}", pdiffuse.GetProperty("label"));
Console.WriteLine("Type Name = {0}", pdiffuse.GetProperty("typeName"));

//traversal on property's property is possible
foreach (var pp in pdiffuse.Properties)
{
    Console.WriteLine("Diffuse.{0} = {1}", pp.Name, pp.Value);
}
//ExEnd: TraversePropertyProperties
```

## Cách **thay đổi màu vật liệu 3d** ngoài diffuse
Nếu bạn cần ảnh hưởng đến màu specular, ambient, hoặc emissive, chỉ cần thay `"Diffuse"` bằng `"Specular"` hoặc `"Ambient"` trong phép gán `props["..."]` ở trên. Các cấu trúc `Vector3` hoặc `Vector4` vẫn được áp dụng.

## Những lỗi thường gặp & Mẹo
- **Phân biệt chữ hoa‑thường của tên thuộc tính** – các khóa thuộc tính của Aspose.3D phân biệt chữ hoa‑thường; hãy sử dụng đúng tên hiển thị trong kết quả liệt kê.  
- **Thuộc tính thiếu** – Không phải tất cả vật liệu đều cung cấp mọi thuộc tính PBR. Kiểm tra `props.ContainsKey("Specular")` trước khi truy cập.  
- **Lưu thay đổi** – Sau khi sửa đổi các thuộc tính, gọi `scene.Save("output.fbx");` để lưu lại các thay đổi.

## Kết luận

Bạn đã học cách **liệt kê các thuộc tính vật liệu**, **truy xuất một thuộc tính theo tên**, và **thay đổi màu diffuse** (hoặc bất kỳ thuộc tính vật liệu nào khác) bằng Aspose.3D for .NET. Hãy thử nghiệm với các loại thuộc tính khác nhau để tinh chỉnh ngoại hình của tài sản 3‑D của bạn.

## Câu hỏi thường gặp

### Q1: Tôi có thể sử dụng Aspose.3D for .NET với các định dạng tệp 3D khác không?

A1: Có, Aspose.3D hỗ trợ nhiều định dạng tệp 3D, bao gồm FBX, STL và nhiều hơn nữa.

### Q2: Làm sao tôi có thể lấy giấy phép tạm thời cho Aspose.3D for .NET?

A2: Truy cập [tại đây](https://purchase.aspose.com/temporary-license/) để nhận giấy phép tạm thời.

### Q3: Có diễn đàn cộng đồng cho người dùng Aspose.3D không?

A3: Có, bạn có thể tìm hỗ trợ và thảo luận tại [diễn đàn Aspose.3D](https://forum.aspose.com/c/3d/18).

### Q4: Tôi có thể tìm tài liệu chi tiết cho Aspose.3D for .NET ở đâu?

A4: Tham khảo [tài liệu](https://reference.aspose.com/3d/net/) để có hướng dẫn toàn diện.

### Q5: Tôi có thể dùng thử Aspose.3D for .NET miễn phí trước khi mua không?

A5: Chắc chắn! Tải xuống [phiên bản dùng thử miễn phí](https://releases.aspose.com/) để khám phá các tính năng.

## Frequently Asked Questions

**Q: `Vector3(1, 0, 1)` đại diện cho gì?**  
A: Nó đặt màu diffuse thành màu hồng tím (đỏ = 1, xanh lá = 0, xanh dương = 1) trong không gian màu tuyến tính.

**Q: Tôi có cần gọi `scene.Save` sau khi thay đổi thuộc tính không?**  
A: Có, việc lưu cảnh sẽ ghi các sửa đổi của bạn ra đĩa; nếu không, các thay đổi sẽ chỉ tồn tại trong bộ nhớ.

**Q: Tôi có thể liệt kê các thuộc tính FBX tùy chỉnh không?**  
A: Chắc chắn. `PropertyCollection` sẽ bao gồm bất kỳ thuộc tính tùy chỉnh nào, bạn có thể truy cập chúng qua `GetProperty("customName")`.

**Q: Có cách nào để cập nhật hàng loạt nhiều vật liệu không?**  
A: Lặp qua `scene.RootNode.ChildNodes` và lặp lại các bước sửa đổi thuộc tính cho mỗi vật liệu.

**Q: Aspose.3D có hỗ trợ .NET 6 không?**  
A: Có, thư viện hoàn toàn tương thích với .NET 6 và các phiên bản sau.

---

**Last Updated:** 2026-01-17  
**Tested With:** Aspose.3D 24.11 for .NET  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}