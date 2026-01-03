print("Seja bem vindo ao Quiz Game!");
answer_user = input("Quer começar? (s/n): ");
print(answer_user);

# Verificação se o usuário quer seguir ou não no game
if answer_user != ("s" or "S"): 
	quit();

score = 0;

print("Começando...");	

# Pergunta 1
print("1. Quem desenvolveu o jogo Grand Theft Auto (GTA)? \n A. Rockstar Games \n B. Ubisoft \n C. Activision \n D. EA \n");
answer_1 = input("Resposta: ");
if answer_1 == "A": 
	print("Correto! \n");
	score = score+1;
else: 
	print("Incorreto!");

# Pergunta 2
print("2. Qual é o nome do protagonista no GTA? \n A. Carlos John \n B. Carl Johnson \n C. Carl Jaquel \n D. Carlos Johnson");
answer_2 = input("Resposta: ");
if answer_2 == "B":
	print("Correto! \n");
	score = score+1;
else:
	print("Incorreto!");

# Pergunta 3
print("3. Qual jogo de simulação de vida permite aos jogadores criarem personagens e construírem casas desde o ano 2000? \n A. SimCity \n B. The Sims \n C. Stardew Valley \n D. Habbo Hotel");
answer_3 = input("Resposta: ");
if answer_3 == "B":
	print("Correto! \n");
	score = score+1;
else:
	print("Incorreto!");

# Pergunta 4
print("4. Qual destes termos refere-se à taxa de quadros por segundo em um jogo? \n A. Ray Tracing \n B. FPS \n C. Ping \n D. DPI");
answer_4 = input("Resposta: ");
if answer_4 == "B":
	print("Correto! \n");
	score = score+1;
else:
	print("Incorreto!");

# Pergunta 5
print("5. Qual é o objetivo principal no jogo 'Minecraft' no modo Sobrevivência? \n A. Derrotar outros 99 jogadores em uma ilha \n B. Capturar monstros em esferas metálicas \n C. Coletar recursos, construir e evitar perigos \n D. Completar uma corrida de carros");
answer_5 = input("Resposta: ");
if answer_5 == "C":
	print("Correto! \n");
	score = score+1;
else:
	print("Incorreto!");

print(f"O Quiz acabou! Pontuação: {score}/5");