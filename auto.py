import time
import tkinter as tk
import winsound

# タイマーの設定をする
work_time = 25 # 作業時間（分）
break_time = 5 # 休憩時間（分）
cycles = 4 # 繰り返す回数

# タイマーのウィンドウを作成する
window = tk.Tk()
window.title("集中時計")
window.geometry("300x200")

# タイマーの表示を作成する
label = tk.Label(window, text="", font=("Arial", 32))
label.pack()

# タイマーの動作を定義する
def timer():
    global cycles
    # 作業時間と休憩時間を交互に繰り返す
    for i in range(cycles):
        # 作業時間のカウントダウンを開始する
        label.config(text="作業中", fg="red")
        window.update()
        count_down(work_time * 60)
        # 休憩時間のカウントダウンを開始する
        label.config(text="休憩中", fg="green")
        window.update()
        count_down(break_time * 60)
    # タイマーが終了したら、メッセージを表示する
    label.config(text="お疲れ様でした！", fg="blue")
    window.update()

# カウントダウンの動作を定義する
def count_down(seconds):
    # 指定された秒数だけカウントダウンする
    while seconds > 0:
        # 残り時間を分と秒に変換する
        mins, secs = divmod(seconds, 60)
        # 残り時間を表示する
        time_str = "{:02d}:{:02d}".format(mins, secs)
        label.config(text=time_str)
        window.update()
        # 1秒待つ
        time.sleep(1)
        # 秒数を減らす
        seconds -= 1
    # カウントダウンが終了したら、音を鳴らす
    winsound.Beep(440, 1000)

# タイマーを実行する
timer()

# ウィンドウを閉じる
window.mainloop()
