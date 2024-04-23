# LD50_calculator
利用寇氏法计算LD50，使用python书写（由chatgpt协助）
## LD50 计算器

这个 LD50 计算器是一个基于 Tkinter 的简单应用程序，用于计算药物的半数致死剂量 (LD50) 和相关统计数据。

### 如何使用

1. **输入数据**：
   - 在药物剂量、小白鼠总数量和死亡老鼠数量的相应列中输入数据。
   - 可以通过点击"增加"按钮来添加新的数据行，或者点击每行数据后的"删除"按钮来删除行。

2. **计算 LD50**：
   - 在输入完所有数据后，点击"计算"按钮进行 LD50 的计算。
   - 程序会根据输入的数据计算出 LD50 的估计值以及相关的统计信息。

### 注意事项

- 确保输入的数据格式正确，包括药物剂量应为数字，小白鼠总数量和死亡老鼠数量应为整数。
- 如果计算过程中出现任何错误，程序会显示错误信息。

### 运行程序

1. **安装依赖**：
   - 确保安装了 Python 和 Tkinter 库。

2. **运行程序**：
   - 在命令行中执行以下命令以运行 LD50 计算器：
     ```
     python your_script_name.py
     ```
   其中 `your_script_name.py` 是包含上述代码的 Python 脚本文件名。

### 其他说明

- 本程序使用了数学库 `math` 和 GUI 库 `tkinter`。
- LD50 是一种毒性学术语，表示药物或毒素导致一半测试生物体死亡所需的剂量。

---

请根据需要修改和补充这份 README，确保包含足够的信息以便用户正确使用和理解 LD50 计算器。
