# ახსენით რომელი გირჩევნით და რატომ:


num = 2


# მე მირჩევნია F'' რადგან აქ ვქმნით ეს მონაცემთა 
# ტიპს და უფრო მოსახერხებელია ჩემთვის
print(f'Hello {num} world')

# მაგ ეს უფრო მეტად საწავალებელია დასაწერად ვიდრე f'' სტრინგი 
# აქ string ვაერთიანებთ ინტეჯერთან რომელიც ფუნქციით გადავაქციეთ string-ად და ვუმატებთ string-ს
# მე თუ მკითხავ f'' უფრო ადვილია გამოსაყენებლად და კომფორტული
print("Hello " + str(num) + " world")

# და აქ გვაქ ცალცალკე დაწერილი ინფორმაცია - str, int, str და ერთიანი ინფორმაციისთვის f''-ს ვამჯობინებ <3
print("Hello", num, "world")