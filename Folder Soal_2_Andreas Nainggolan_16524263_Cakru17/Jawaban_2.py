import random

class Robot:
    def __init__(self, nama):
        self.nama = nama
        self.nyawa = 150  # darah robot

    def __str__(self):
        return f"{self.nama} (Kesehatan: {self.nyawa})"

class Battle:
    def start_fight(self, robot1, robot2):
        print("Pertandingan antar robot dimulai!")
        while robot1.nyawa > 0 and robot2.nyawa > 0:
            # Robot 1 menyerang Robot ke 2
            rusakan1 = random.randint(1, 20)
            robot2.nyawa -= rusakan1
            print(f"{robot1.nama} menyerang {robot2.nama}!")

            if robot2.nyawa <= 0:
                print(f"{robot2.nama} sekarat dan pergi meninggalkan pertandingan!")
                print(f"{robot1.nama} memenangkan pertandingan!")
                return
            
            # Robot 2 menyerang Robot ke 1
            rusakan2 = random.randint(1, 20)
            robot1.nyawa -= rusakan2
            print(f"{robot2.nama} menyerang {robot1.nama}!")

            if robot1.nyawa <= 0:
                print(f"{robot1.nama} sekarat dan pergi meninggalkan pertandingan!")
                print(f"{robot2.nama} memenangkan pertandingan!")
                return

class Game:
    def __init__(self):
        self.robots = []

    def add_robot(self, robot):
        self.robots.append(robot)

    def start_game(self):
        print("\nPilihlah robot untuk dipertandingkan!:")
        for i, robot in enumerate(self.robots, start=1):
            print(f"{i}. {robot}")

        try:
            pilihan1 = int(input("Masukkan robot pertama yang ingin ditandingkan (nomor): ")) - 1
            pilihan2 = int(input("Masukkan robot kedua yang ingin ditandingkan (nomor): ")) - 1

            if (0 <= pilihan1 < len(self.robots) and 
                0 <= pilihan2 < len(self.robots) and 
                pilihan1 != pilihan2):
                
                battle = Battle()
                battle.start_fight(self.robots[pilihan1], self.robots[pilihan2])
            else:
                print("Kamu salah memasukkan nomor, robot tidak bisa dimasukkan!")
        except ValueError:
            print("Masukkan nomor sesuai pilihan diatas!.")

def main():
    game = Game()

    # Menambahkan pilihan robot ke dalam permainan
    game.add_robot(Robot("Alfa"))
    game.add_robot(Robot("Delta"))
    game.add_robot(Robot("Gamma"))
    game.add_robot(Robot("beta"))

    # Permainan dimulai
    game.start_game()

if __name__ == "__main__":
    main()