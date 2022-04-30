from time import sleep 
from os import system


class contagem:
    def __init__(self): 
        days = input("Dias: ")
        days = self.validation(days)

        nh=0 
        while nh == 0: 
            hours = input("Horas: ")
            hours = self.validation(hours)

            if hours > 23:
                print("O número máximo de horas é '23")
            else:
                nh =+ 1 

        nh=0
        while nh == 0:
            minutes = input("Minutos: ")
            minutes = self.validation(minutes)

            if minutes > 59:
                print("O número máximo de minutos é '59")
            else:
                nh =+ 1
        
        nh=0
        while nh == 0:
            seconds = input("Segundos: ")
            seconds = self.validation(seconds)

            if seconds > 59:
                print("O número máximo de segundos é '59")
            else:
                nh =+1

        time = days * 86400 + hours * 3600 + minutes * 60 + seconds

        while time != 0:
            sleep(1)

            time -= 1

            if seconds == 0 and minutes == 0 and hours == 0:
                days -= 1
                hours = 23
                minutes = 59
                seconds = 59
            elif seconds == 0 and minutes == 0:
                hours -= 1
                minutes = 59
                seconds = 59
            elif seconds == 0:
                minutes -= 1
                seconds = 59
            else:
                seconds -= 1

            system('clear')
            print(f'Dias: {days}, Horas: {hours}, Minutos: {minutes}, Segundos: {seconds}')

        system('clear')
        print('Fim do timer')

    def validation(self, i):
        if i == '' or i.isdecimal() == False:
            return 0
        else:
            return int(i)


def main():
    n = 0
    while n == 0:
        system('clear')

        contagem()

        again = input('Iniciar outro timer?(s/n): ')

        if again != 's':
            n += 1

if __name__ == '__main__':
    main()


