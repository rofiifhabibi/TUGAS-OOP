class KarakterSurfer:
    def __init__(self, nama):
        self.nama = nama
        self.skor = 0
        self.koin = 0
        self.is_running = True
    
    def berlari(self):
        print("karakter sedang berlari...")
        self.is_running = True
        return self.is_running
    
    def ambil_koin(self, jumlah):
        
        