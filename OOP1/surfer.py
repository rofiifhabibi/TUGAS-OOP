class KarakterSurfer:
    def __init__(self, nama):
        self.nama = nama
        self.skor = 0
        self.koin = 0
        self.is_running = True
    
    def berlari(self):
        print("karakter sedang berlari...")
        self.is_running = True
    
    def ambil_koin(self, jumlah):
        self.koin += jumlah
        print(f"karakter {self.nama} mengambil {jumlah} koin. Total koin: {self.koin}")
        
    def tabrak_rintangan(self):
        if self.is_running:
            print("karakter menabrak rintangan! game over!")
            self.is_running = False     
    
    def info(self):
        print(f"Nama: {self.nama}, Skor: {self.skor}, Koin: {self.koin}, Status: {'Berjalan' if self.is_running else 'Berhenti'}")
    
pemain1 = KarakterSurfer("Jake")
pemain1.info()
pemain1.berlari()
pemain1.ambil_koin(15)
pemain1.ambil_koin(10)
pemain1.info()
pemain1.tabrak_rintangan()
pemain1.info()