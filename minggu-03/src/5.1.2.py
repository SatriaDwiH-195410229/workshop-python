from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry") # Terry masuk
queue.append("Graham") # Graham masuk
print(queue.popleft()) # Pertama masuk sekarang keluar
print(queue.popleft()) # Kedua masuk sekarang keluar
print(queue) # Sisa antrian yang diurutkan berdasarkan kedatangan