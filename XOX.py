#İki kişilik XOX oyunu.

''' Konsolu masa olarak kullanıp, hangi tuşların hangi konumda olacağını (örn: sol üst, sağ orta, vb.)
    1'den 9'a kadar olan sıralama ile yazılacağını belirteceğiz, ardından her hareketten sonra
    değeri oyuncunun tercihine göre değişecek. '''

theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

board_keys = []

for key in theBoard:
    board_keys.append(key)

''' Oyundaki her hareketten sonra güncellenmiş masayı yazdırmamız gerekecek, 
    böylece "printBoard" fonksiyonunu tanımlayacağımız bir fonksiyon yazdım.
    böylece her zaman bu işlevi çağırarak masaya kolayca yazdırabiliyorum. '''

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

# Şimdi bu kısımda tüm oyun işlevselliğine sahip olan ana işlevi yazıcam.
def game():

    turn = 'X'
    count = 0


    for i in range(10):
        printBoard(theBoard)
        print("Senin sıran," + turn + ".Nereye yerleşiceksin?")

        move = input()        

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("Denediğin yer zaten dolu.\nbaşka bir konuma yerleş.")
            continue

        # Şimdi 5 hamleden sonraki her hamle için,X veya O oyuncusunun kazanıp kazanmadığını kontrol edeceğim.
        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # Masada ki üst kısım konumlandırma.
                printBoard(theBoard)
                print("\nOyun Bitti.\n")                
                print(" **** " +turn + " Kazandı. ****")                
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # Masada ki üst kısım konumladırma.
                printBoard(theBoard)
                print("\nOyun Bitti.\n")                
                print(" **** " +turn + " Kazandı. ****")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # Masada ki alt kısım konumlandırma.
                printBoard(theBoard)
                print("\nOyun Bitti.\n")                
                print(" **** " +turn + " Kazandı. ****")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # Masada ki sol aşağıdan yukarı konumlandırma.
                printBoard(theBoard)
                print("\nOyun Bitti.\n")                
                print(" **** " +turn + " Kazandı. ****")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # Masada ki orta aşağıdan yukarı konumlandırma.
                printBoard(theBoard)
                print("\nOyun Bitti.\n")                
                print(" **** " +turn + " Kazandı. ****")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # Masada ki sağ aşağıdan yukarı konumlandırma.
                printBoard(theBoard)
                print("\nOyun Bitti.\n")                
                print(" **** " +turn + " Kazandı. ****")
                break 
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # Masada ki sol en üst'ten sağ en alt olan çapraz konumlandırma. 
                printBoard(theBoard)
                print("\nOyun Bitti.\n")                
                print(" **** " +turn + " Kazandı. ****")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # Masada ki sol en alt'tan sağ en üst olan çapraz konumlandırma.
                printBoard(theBoard)
                print("\nOyun Bitti.\n")                
                print(" **** " +turn + " Kazandı. ****")
                break 

        # X yada O kazanamazsa ise ve masada yazıcak yer kalmadı ise, sonucu 'beraber' olarak ilan ettim.
        if count == 9:
            print("\nOyun Bitti.\n")                
            print("Berabere!!")

        # Şimdi her hamle sonunda, oyuncu değişikliği yapacağım.
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    # Şimdi oyuncunun oyunu yeniden başlatmak isteyip istemediğini soracağım.
    restart = input("Bir oyun daha oynamak ister misin?(E (Evet)/h (Hayır))")
    if restart == "e" or restart == "E":  
        for key in board_keys:
            theBoard[key] = " "

        game()

if __name__ == "__main__":
    game()