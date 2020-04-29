import random

# Klasik taş-kağıt-makas oyununu BOT'a karşı oynayalım.
# Kaybetme,Kazanma ve Beraberlik seçenekleri olsun.
# 'random.choice' ile bot bir hamleyi rasgele seçsin
# 3 puandan başlayalım ve puanımız azalsın veya artsın.


bot_hamle_liste = ["taş","kağıt","makas"]

puan = 3

tas = bot_hamle_liste[0]
kagıt = bot_hamle_liste[1]
makas = bot_hamle_liste[2]

print("=============================================\n- Taş / Kağıt / Makas oyununa giriş yaptın!\n- Unutma taş makası kırar , makas kağıdı keser, kağıt da taşı sarar.\n- Başlangıç puanın : 3\n- Lütfen komutlar dışında bir şey yazma kabul edemem.\n- Ayrıca çıkış yapmak istersen 'q' yazman yeterli.\n=============================================")


while True : 
	bot_hamle = random.choice(bot_hamle_liste)
	hamle = input("Taş? Kağıt? Makas? : ")
	hamle = hamle.lower()
	

	if hamle == tas :
		if bot_hamle == tas:
			print("BOT'un Hamlesi : Taş - Berabere! - Puanın :" , puan )
		elif bot_hamle == kagıt:
			puan -= 1
			print("BOT'un Hamlesi : Kağıt - Kaybettin! \nPuanın : " , puan)
		else:
			puan += 1
			print("BOT'un Hamlesi : Makas - Kazandın! \nPuanın : " , puan)
	elif hamle == kagıt :
		if bot_hamle == kagıt:
			print("BOT'un Hamlesi : Kağıt - Berabere! - Puanın :" , puan )
		elif bot_hamle == makas:
			puan -= 1
			print("BOT'un Hamlesi : Makas - Kaybettin! \nPuanın : " , puan)
		else:
			puan += 1
			print("BOT'un Hamlesi : Taş - Kazandın! \nPuanın : " , puan)
	if hamle == makas :
		if bot_hamle == makas:
			print("BOT'un Hamlesi : Makas - Berabere! - Puanın :" , puan )
		elif bot_hamle == tas:
			puan -= 1
			print("BOT'un Hamlesi : Taş - Kaybettin! \nPuanın : " , puan)
		else:
			puan += 1
			print("BOT'un Hamlesi : Kağıt - Kazandın! \nPuanın : " , puan)
	elif hamle == "q" :
		print("Çıkış yapılıyor...") 
		break

	elif puan < 1 :
		print("Kaybettin!")
		break







 



	
            




