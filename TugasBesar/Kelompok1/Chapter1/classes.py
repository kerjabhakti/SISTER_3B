class Tugas:
    total_tugas = 0

    def __init__(self, nama, deadline):
        self.nama = nama
        self.deadline = deadline
        Tugas.total_tugas += 1

    def info_tugas(self):
        print("Nama Tugas:", self.nama)
        print("Deadline:", self.deadline)

    @classmethod
    def total(cls):
        print("Total Tugas:", cls.total_tugas)


tugas1 = Tugas("Tugas Matematika", "10 Juni 2023")
tugas2 = Tugas("Tugas Bahasa Inggris", "12 Juni 2023")

tugas1.info_tugas()
tugas2.info_tugas()

Tugas.total()
