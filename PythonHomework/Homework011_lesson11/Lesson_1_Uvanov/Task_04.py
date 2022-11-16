
def enc_str_dec(text):
    for i in text:
        i_byt = i.encode('utf-8')
        print("Преобразование из строкового представления в байтовое:")
        print(f"{i} == {i_byt}")
        print("Преобразование из байтового представления в строковое")
        print(f"{i_byt} == {i_byt.decode('utf-8')}")
        print()

enc_str_dec (["разработка", "администрирование", "protocol", "standard"])



