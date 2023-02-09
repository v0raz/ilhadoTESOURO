print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Bem vindo a Ilha do Tesouro.")
print("Sua missão é encontrar o tesouro.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
leaving_house = input("Você está saindo de sua casa em busca de aventuras, gostaria de ir para a cidade ou para os campos?: ")
if leaving_house.lower() == "cidade":
  priest_interaction = input("Você encontra um padre na frente de uma igreja, Você gostaria de interagir com ele? Y/N? ")
  if priest_interaction.lower() == "y":
    print("O padre fala com você sobre amor e sobre deus, também fala sobre a falta de compaixão no mundo moderno.\nIsso lhe deixa muito triste, então você desiste da sua aventura e vai para casa chorar." )
    print('''

                       `;.`;'.  
                     `;);.(~;(`; 
                   `(;);;;;;);(::` 
                    ;)(; ; ;;~;;;(; 
                 `(`;;~-  -~(;~;)`) 
                  ;(`;)    ' ;);;; ;
               `;);;(;`\ ^_/(;)~;;); 
                 (;);.;)   ':);( ..(;  
                  `'((;);   )(.');`: 
                   ;.' );("'(""/; ;`.)
                    |  | / / \ \;);:
                    |  |/ /WwW\ \;`'
                     \   /) .X.\  \
                     ''')
  else:
    tavern_interaction = input("Passando pela igreja você encontra um velho amigo, que te convida para a taverna local, aceitas? Y/N")
    if tavern_interaction.lower() == "y":
      drunk_interaction = input("Aceita uma bebida? Y/N ")
      if drunk_interaction.lower() == "y":
        print("Você é um alcoolatra e acaba morrendo durante uma briga de bar. Bela aventura!")
        print('''

⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠛⠛⠋⠉⠈⠉⠉⠉⠉⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢿⣿⣿⣿⣿
⣿⣿⣿⣿⡏⣀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿
⣿⣿⣿⢏⣴⣿⣷⠀⠀⠀⠀⠀⢾⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿
⣿⣿⣟⣾⣿⡟⠁⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣷⢢⠀⠀⠀⠀⠀⠀⠀⢸⣿
⣿⣿⣿⣿⣟⠀⡴⠄⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⣿
⣿⣿⣿⠟⠻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠶⢴⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⣿
⣿⣁⡀⠀⠀⢰⢠⣦⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⡄⠀⣴⣶⣿⡄⣿
⣿⡋⠀⠀⠀⠎⢸⣿⡆⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⠗⢘⣿⣟⠛⠿⣼
⣿⣿⠋⢀⡌⢰⣿⡿⢿⡀⠀⠀⠀⠀⠀⠙⠿⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣧⢀⣼
⣿⣿⣷⢻⠄⠘⠛⠋⠛⠃⠀⠀⠀⠀⠀⢿⣧⠈⠉⠙⠛⠋⠀⠀⠀⣿⣿⣿⣿⣿
⣿⣿⣧⠀⠈⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠟⠀⠀⠀⠀⢀⢃⠀⠀⢸⣿⣿⣿⣿
⣿⣿⡿⠀⠴⢗⣠⣤⣴⡶⠶⠖⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡸⠀⣿⣿⣿⣿
⣿⣿⣿⡀⢠⣾⣿⠏⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠉⠀⣿⣿⣿⣿
⣿⣿⣿⣧⠈⢹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿
⣿⣿⣿⣿⡄⠈⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣦⣄⣀⣀⣀⣀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠙⣿⣿⡟⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠁⠀⠀⠹⣿⠃⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢐⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⠿⠛⠉⠉⠁⠀⢻⣿⡇⠀⠀⠀⠀⠀⠀⢀⠈⣿⣿⡿⠉⠛⠛⠛⠉⠉
⣿⡿⠋⠁⠀⠀⢀⣀⣠⡴⣸⣿⣇⡄⠀⠀⠀⠀⢀⡿⠄⠙⠛⠀⣀⣠⣤⣤⠄''')
      else:
        sober_interaction = input("Sou amigo lhe acha nojento por não beber, por isso ele te expulsa do bar. Na saída você encontra um homem que parece com uma velha lenda da cidade. Você sente que deveria falar com ele, você vai? Y/N")
        if sober_interaction.lower() == "y":
          print("Você vai até o homem e lhe pergunta se ele sabe algo sobre a Ilha do Tesouro")
          print("Ele responde que essa ilha não existe, e que o verdadeiro tesouro são os amigos que fazemos no caminho")
          print("Nesse ponto você percebe que: No caminho você não fez nenhum amigo, aliás, você acabou de perder um amigo. Esse homem não pode estar certo")
          filosophy_fight = input("Você quer desafiar o homem para um duelo filosófico? Y/N")
          if filosophy_fight.lower() == "y":
           print("Por que você fez isso? O homem te desafia a definir o que é filosofia e a formar argumentos convincentes sobre a relevância dos juízos sintéticos a priori")
           print("Durate o discurso do seu 'oponente' você fica entediado, com sono, desmaia e bate a cabeça, finalmente se libertando desta conversa. Sua aventura terminou e você não encontrou nenhum tesouro.")
          else:
            tavern_outside = input("Pelos Deuses! Ainda bem que você escolheu não sofrer, você sai do bar em busca de um rumo, uma aventura, um tesouro, ou pelo menos de um amigo. Enquanto você caminha pelas ruas peripatéticamente acaba encontrando uma apresentação musical na praça da cidade. Gostaria de assistir? Y/N")
            if tavern_outside.lower() == "y":
              print("Os bardos começam a tocar a sua música favorita, o que lhe deixa instantaneamente MALUCO.")
              print("As pessoas param para te assistir dançando e cantando junto com a banda")
              print("Quando a música acaba você percebe o nome da banda: Tesouro")
              print("Parabéns você encontrou o TESOURO")
              print(''' __   __  _______  __   __    _     _  ___   __    _ 
                        |  | |  ||       ||  | |  |  | | _ | ||   | |  |  | |
                        |  |_|  ||   _   ||  | |  |  | || || ||   | |   |_| |
                        |       ||  | |  ||  |_|  |  |       ||   | |       |
                        |_     _||  |_|  ||       |  |       ||   | |  _    |
                          |   |  |       ||       |  |   _   ||   | | | |   |
                          |___|  |_______||_______|  |__| |__||___| |_|  |__|''')
            else:
              print("Me pergunto se você realmente quer participar de uma aventura, volte para casa e tente novamente amanhã.")
        else: 
          print("Ao não conversar com o homem, você ignora sua intuição, o que pode ser fatal para um aventureiro.")
          print("Você é um péssimo aventureiro!. Volte para casa e pense nas suas escolhas")
    if tavern_interaction.lower() == "n":
      print("Ao negar a fé (conversando com um padre) e a amizade(encontrando um velho amigo), você percebe que não há mais muito o que se fazer nesse mundo, volte para casa e tente novamente amanhã.")
if leaving_house.lower() == "campos":
  print("Você anda em direção dos campos, vê fazendas, camponeses e decide pular uma cerca de arame para cortar caminho, nesse cercado você encontra uma vaca leitera chamada Tesouro, foi um grande dia e uma grande aventura, parabéns!")
  print('''
           .        .
           \'.____.'/
          __'-.  .-'__                         .--.
          '_i:'oo':i_'---...____...----i"""-.-'.-"\\
            /._  _.\       :       /   '._   ;/    ;'-._
           (  o  o  )       '-.__.'       '. '.     '-."
            '-.__.-' _.--.                 '-.:
             : '-'  /     ;   _..--,  /       ;
             :      '-._.-'  ;     ; :       :
              :  `      .'    '-._.' :      /
               \  :    /    ____....--\    :
                '._\  :"""""    '.     !.   :
                 : |: :           'www'| \ '|
                 | || |              : |  | :
                 | || |             .' !  | |
                .' !| |            /__I   | |
               /__I.' !                  .' !
                  /__I                  /__I  ''')