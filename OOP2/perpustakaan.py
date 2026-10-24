class Buku:
    def __init__(self, judul, penulis, tahun_terbit):
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit
        self.tersedia = True
             
    def pinjam_buku(self):
        if self.tersedia:
            self.tersedia = False
            print("Buku berhasil dipinjam.")
        else:
            print("Buku yang anda pilih sedang tidak tersedia untuk dipinjam.")
    
    def kembalikan_buku(self):
        if not self.tersedia:
            self.tersedia = True
            print("Buku berhasil dikembalikan.")
        else:
            print("Buku yang anda pilih tidak sedang dipinjam.")
    
    def info_buku(self):
        print(f"Judul: {self.judul}, Penulis: {self.penulis}, Tahun Terbit: {self.tahun_terbit}, Status: {'Tersedia' if self.tersedia else 'Tidak Tersedia'}")
        
        
buku1 = perpustakaan("Bumi Manusia", "Pramoedya Ananta Toer", 1980)
buku1.info_buku()
buku1.pinjam_buku()
buku1.info_buku()
buku1.kembalikan_buku()
buku1.info_buku()            