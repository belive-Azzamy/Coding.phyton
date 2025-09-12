class Motor:

    def __init__(self, merk_motor, warna_motor, kecepatan_motor):
        self.merk = merk_motor
        self.warna = warna_motor
        self.kecepatan = kecepatan_motor
    
    def laporan(self):
        print(f'Motor dengan merk {self.merk} berwarna {self.warna} sedang melaju dengan kecepatan {self.kecepatan} km/jam')

honda = Motor('Vario 150 gen 2', 'BlackGlossy', '80')
honda.laporan()