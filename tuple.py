#tuple pake kurung ()
a = ("apel", "jeruk", "ceri", "durian", "apel")
x = list(a)
x[3] = "melon"
a = tuple(x)

print("Hasil tuple: ")
print(a)

print("Jumlah elemen buah:", len(a))

buah = ("apel", "belimbing", "ceri", "durian")
(b, c, d, e) = buah
print (b)
print (c)
print (d)
print (e)