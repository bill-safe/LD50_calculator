import math
import tkinter as tk
from tkinter import messagebox

class LD50Calculator:
    def calculate_ld50_value(self, data):
        sorted_probabilities = []
        doses, Mouse_population, death_Mouse = zip(*data)
        # 排序
        sorted_lists = sorted(zip(doses, Mouse_population, death_Mouse), key=lambda x: x[0])
        sorted_doses, sorted_Mouse_population, sorted_death_Mouse = zip(*sorted_lists)
        # 计算死亡概率
        for a in range(len(sorted_death_Mouse)):
            sorted_probabilities.append(sorted_death_Mouse[a] / sorted_Mouse_population[a])
        return sorted_doses, sorted_probabilities

    def LD50_roughly(self, sorted_doses, sorted_probabilities):
        ld50_sum = 0.0
        # 计算 LD50
        for i in range(len(sorted_doses) - 1):
            xi = math.log10(sorted_doses[i])
            xi1 = math.log10(sorted_doses[i + 1])
            pi = sorted_probabilities[i]
            pi1 = sorted_probabilities[i + 1]
            ld50_sum += 0.5 * (xi + xi1) * (pi1 - pi)
        ld50_roughly = math.pow(10, ld50_sum)
        return ld50_roughly

    def sm(self, sorted_doses, sorted_probabilities, Mouse_population):
        # 计算标准差
        d = math.log10(sorted_doses[0]) - math.log10(sorted_doses[1])
        pi_sum = sum(sorted_probabilities)
        pi2_sum = sum(x ** 2 for x in sorted_probabilities)
        n = sum(Mouse_population) / len(Mouse_population)
        sm = d * math.sqrt((pi_sum - pi2_sum) / n)
        return sm

    def calculate_ld50_range(self, ld50_roughly, sm):
        LD50_max = ld50_roughly * 10 ** (1.96 * sm)
        LD50_min = ld50_roughly / 10 ** (1.96 * sm)
        return LD50_max, LD50_min

class LD50UI:
    def __init__(self, master):
        self.master = master
        self.data_entries = []
        master.title("LD50 计算器")

        # 分类
        label_doses = tk.Label(master, text="药物剂量")
        label_doses.grid(row=0, column=0, padx=10)

        label_mouse_population = tk.Label(master, text="小白鼠总数量")
        label_mouse_population.grid(row=0, column=1, padx=10)

        label_death_mouse = tk.Label(master, text="死亡老鼠数量")
        label_death_mouse.grid(row=0, column=2, padx=10)

        self.add_data_entry()
        self.add_data_entry()

        self.add_row_button = tk.Button(master, text="增加", command=self.add_data_entry)
        self.add_row_button.grid(row=len(self.data_entries) + 1, column=3, padx=5, pady=5, sticky=tk.E)

        self.calculate_button = tk.Button(master, text="计算", command=self.calculate_ld50)
        self.calculate_button.grid(row=len(self.data_entries) + 2, column=3, padx=10, pady=5, sticky=tk.E)

        master.columnconfigure(0, weight=1)
        master.columnconfigure(1, weight=1)
        master.columnconfigure(2, weight=1)
        master.columnconfigure(3, weight=1)
    # 增加组模块
    def add_data_entry(self):
        row = len(self.data_entries) + 1

        entry_doses = tk.Entry(self.master)
        entry_doses.grid(row=row, column=0, padx=10)

        entry_mouse_population = tk.Entry(self.master)
        entry_mouse_population.grid(row=row, column=1, padx=10)

        entry_death_mouse = tk.Entry(self.master)
        entry_death_mouse.grid(row=row, column=2, padx=10)

        delete_button = tk.Button(self.master, text="删除", command=lambda r=row: self.delete_data_entry(r))
        delete_button.grid(row=row, column=3, padx=5, pady=5, sticky=tk.W)

        self.data_entries.append((entry_doses, entry_mouse_population, entry_death_mouse, delete_button))

        self.master.geometry(f"800x{50 + 40 * len(self.data_entries)}")
    #删除功能模块
    def delete_data_entry(self, row):
        if row > 1 and row <= len(self.data_entries):
            entry_doses, entry_mouse_population, entry_death_mouse, delete_button = self.data_entries[row - 1]
            entry_doses.destroy()
            entry_mouse_population.destroy()
            entry_death_mouse.destroy()
            delete_button.destroy()
            self.data_entries.pop(row - 1)
            self.master.geometry(f"800x{50 + 40 * len(self.data_entries)}")

    def calculate_ld50(self):
        data = []
        for entry_doses, entry_mouse_population, entry_death_mouse, _ in self.data_entries:
            doses = float(entry_doses.get())
            Mouse_population = int(entry_mouse_population.get())
            death_Mouse = int(entry_death_mouse.get())
            data.append((doses, Mouse_population, death_Mouse))

        ld50_calc = LD50Calculator()
        try:
            sorted_doses, sorted_probabilities = ld50_calc.calculate_ld50_value(data)
            ld50_roughly = ld50_calc.LD50_roughly(sorted_doses, sorted_probabilities)
            sm_value = ld50_calc.sm(sorted_doses, sorted_probabilities, [d[1] for d in data])
            LD50_max, LD50_min = ld50_calc.calculate_ld50_range(ld50_roughly, sm_value)

            messagebox.showinfo("LD50 计算结果",
                                f"LD50 : {ld50_roughly}\n"
                                f"标准误差SM: {sm_value}\n"
                                f"LD50 上限: {LD50_max}\n"
                                f"LD50 下限: {LD50_min}")

        except Exception as e:
            messagebox.showerror("Error", f"Error occurred during calculation: {e}")

# 创建主窗口并设置初始大小
root = tk.Tk()
root.geometry("800x800")  # 设置初始窗口大小为宽800像素，高800像素
ld50_ui = LD50UI(root)
root.mainloop()