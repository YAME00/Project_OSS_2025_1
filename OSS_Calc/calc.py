import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x400")

        self.expression = ""
        self.history = []

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 버튼 생성
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['=']
        ]

        for row in buttons:
            frame = tk.Frame(root)
            frame.pack(expand=True, fill="both")
            for char in row:
                btn = tk.Button(
                    frame,
                    text=char,
                    font=("Arial", 18),
                    command=lambda ch=char: self.on_click(ch)
                )
                btn.pack(side="left", expand=True, fill="both")

        self.history_label = tk.Label(root, text = "", justify="left", anchor="w", font=("Arial", 12))
        self.history_label.pack(fill="both", padx = 10, pady = 5)

    def on_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '=':
            try:
                result = str(eval(self.expression))
                self.add_to_history(self.expression, result)
                self.expression = result
            except Exception:
                self.expression = "에러"
        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

    def add_to_history(self, expression, result):
        entry = f"{expression} = {result}"
        self.history.insert(0, entry)

        if len(self.history) > 5:
            self.history = self.history[:5]

        self.history_label.config(text = "\n".join(self.history))



