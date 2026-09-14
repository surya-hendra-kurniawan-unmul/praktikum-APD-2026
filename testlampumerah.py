import time

def Lampu_Merah():
    while True:
        # Lampu Merah
        print("🔴 Lampu Merah: Berhenti! (3 detik)")
        time.sleep(3)
        
        # Lampu Kuning
        print("🟡 Lampu Kuning: Hati-hati! (1 detik)")
        time.sleep(1)
        
        # Lampu Hijau
        print("🟢 Lampu Hijau: Silakan Jalan! (3 detik)")
        time.sleep(3)

Lampu_Merah()
