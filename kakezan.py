tate = int(input("縦軸の桁数を入力してください＞＞"))
yoko = int(input("横軸の桁数を入力してください＞＞"))

for i in range(1,tate+1):
    for j in range(1,yoko+1):
        for k in range( len( str( tate * yoko ) ) - len( str( i * j ) ) ):
            print(" ", end="")
        print(i * j," ", end="")
    print()