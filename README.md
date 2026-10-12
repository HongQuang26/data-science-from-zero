# Data Science từ số 0

Lộ trình thực hành bằng tiếng Việt dành cho người chưa biết lập trình, hướng đến năng lực làm Data Scientist ở môi trường thực tế. Fork repo này, học theo thứ tự và làm lại các bài tập trong notebook bằng dữ liệu của chính bạn.

> Nội dung là bản gốc. Cách tổ chức bài học lấy cảm hứng từ nhịp học ngắn + thực hành của DataCamp và cấu trúc bài học/assignment rõ ràng trong các curriculum mã nguồn mở của Microsoft.

## Bắt đầu trong 10 phút

```bash
git clone https://github.com/HongQuang26/data-science-from-zero.git
cd data-science-from-zero
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
jupyter lab
```

Mở `00-start-here/01_jupyter_and_python.ipynb`, chạy từng ô bằng `Shift + Enter`, rồi chỉ sang bài tiếp theo khi đã hoàn thành phần **Tự luyện**.

## Lộ trình

| Chặng | Mô-đun | Năng lực đầu ra |
| --- | --- | --- |
| 0 | [Khởi động](00-start-here/README.md) | Môi trường, Jupyter, tư duy DS |
| 1 | [Python nền tảng](01-python-foundations/README.md) | Viết chương trình nhỏ, hàm, cấu trúc dữ liệu |
| 2 | [Python nâng cao](02-python-advanced/README.md) | File, lỗi, OOP, iterator, kiểm thử |
| 3 | [Data stack](03-data-stack/README.md) | NumPy, Pandas, thao tác bảng dữ liệu |
| 4 | [Làm sạch dữ liệu](04-data-cleaning/README.md) | Missing values, kiểu dữ liệu, scale, feature engineering |
| 5 | [EDA & trực quan](05-eda-visualization/README.md) | Đặt câu hỏi, biểu đồ, kể chuyện bằng dữ liệu |
| 6 | [Thống kê & A/B test](06-statistics-experimentation/README.md) | Uncertainty, hypothesis testing, thí nghiệm |
| 7 | [SQL](07-sql/README.md) | Query, join, aggregation, window function |
| 8 | [Machine Learning](08-machine-learning/README.md) | Train/test, pipeline, đánh giá, mô hình baseline |
| 9 | [Chủ đề chuyên sâu](09-specialized-topics/README.md) | Clustering, giảm chiều, chuỗi thời gian, NLP nhập môn |
| 10 | [Dự án đầu-cuối](10-end-to-end-project/README.md) | Từ câu hỏi kinh doanh đến báo cáo có thể bàn giao |
| 11 | [Production & sự nghiệp](11-production-career/README.md) | Reproducibility, đạo đức, portfolio, phỏng vấn |

Chi tiết thời lượng, điều kiện hoàn thành và checklist nằm trong [CURRICULUM.md](CURRICULUM.md).

## Cách học để có kết quả

1. Đọc mục tiêu, dự đoán kết quả trước khi chạy code.
2. Gõ lại code; đừng chỉ bấm Run All.
3. Làm phần **Tự luyện**, lưu lời giải vào fork của bạn.
4. Mỗi hai mô-đun, áp dụng vào một dataset mới từ Kaggle, dữ liệu mở hoặc công việc.
5. Hoàn thành ít nhất một dự án đầu-cuối trước khi học deep learning.

Mỗi notebook đi theo cùng một nhịp: mục tiêu → giải thích ngắn → code chạy được → tự luyện → checklist. Cấu trúc này hỗ trợ tự học, lớp học và study group.

## Dùng repo này khi dạy học

- Người học: fork repo, tạo branch cho từng mô-đun và commit bài làm.
- Người dạy: yêu cầu nộp link notebook đã hoàn thành hoặc Pull Request từ fork.
- Study group: mỗi tuần chọn một notebook và thảo luận phần **Tự luyện**.

## Kiểm tra nhanh

```bash
python scripts/validate_notebooks.py
```

Lệnh này chỉ kiểm tra cấu trúc notebook và sự hiện diện của các phần cần thiết; nó không thay thế việc chạy, đọc kết quả và phản biện phân tích.

## Đóng góp

Xem [CONTRIBUTING.md](CONTRIBUTING.md). Hãy ưu tiên sửa lỗi, thêm bài tập có dữ liệu công khai nhỏ, hoặc bổ sung ví dụ sát thực tế ở Việt Nam.

## Tài liệu tham khảo

- [DataCamp – Data Scientist with Python](https://www.datacamp.com/tracks/data-scientist-with-python): cảm hứng về thứ tự kỹ năng Python → xử lý dữ liệu → ML.
- [Microsoft Data Science for Beginners](https://github.com/microsoft/Data-Science-For-Beginners): cảm hứng về lesson structure, assignment và hướng dẫn cho người tự học/giảng viên.
- [Python documentation](https://docs.python.org/3/), [Pandas user guide](https://pandas.pydata.org/docs/user_guide/index.html), [scikit-learn user guide](https://scikit-learn.org/stable/user_guide.html): nguồn kỹ thuật chuẩn để đào sâu.

## Giấy phép

MIT. Xem [LICENSE](LICENSE).
