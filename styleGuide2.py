'''
Lint adalah proses pengecekan kode atas kemungkinan terjadi kesalahan (error), 
termasuk dalam proses ini adalah mengecek kesesuaian terhadap arahan gaya penulisan kode (style guide) PEP8. Aplikasi yang digunakan untuk proses ini disebut linter. 
Integrasi linter dengan editor kode Anda akan membuat efisien dalam menulis kode Python. 
Berikut akan dibahas 3 jenis aplikasi linter
'''

class Kalkulator:
    """kalkulator tambah kurang"""
    def __init__(self, _i=0):
        self.i = _i
    def tambah(self, _i): return self.i + _i
    def kurang(self, _i):
        return self.i - _i

        # ndatau kok nda otomatis brubah wkwk, intinya itulah kegunaan linter biar gampng formatting penulisan kodenya
