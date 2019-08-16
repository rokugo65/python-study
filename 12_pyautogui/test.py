import pyautogui as pgui

#pgui.PAUSE = 2.5
pgui.FAILSAFE = True # Falseで無効

# 画面サイズを取得
width, height = pgui.size()
print(width)
print(height)

# 絶対座標で移動
pgui.moveTo(100, 100, duration=0.25)
pgui.moveTo(100, 100, duration=0.0)
pgui.moveTo(100, 100, duration=1.0)

for i in range(3):
    pgui.moveTo(100, 100, duration=0.25)
    pgui.moveTo(200, 100, duration=0.25)
    pgui.moveTo(200, 200, duration=0.25)
    pgui.moveTo(100, 200, duration=0.25)

# 相対座標で移動
pgui.moveRel(100, 0, duration=0.25)
pgui.moveRel(100, 0, duration=0.25)
pgui.moveRel(100, 0, duration=0.25)

# マウスの現在位置を取得
x, y = pgui.position()
print(x)
print(y)

# クリック
x = 100
y = 100
for ii in range(10):
    pgui.click(x, y)
    x += 1
    y += 1

# ドラッグ
pgui.moveTo(100, 100)
distance = 200
pgui.dragRel(distance, 0, duration=0.5)     # →
pgui.dragRel(0, distance, duration=0.5)     # ↓
pgui.dragRel(-distance, 0, duration=0.5)    # ←
pgui.dragRel(0, -distance, duration=0.5)    # ↑