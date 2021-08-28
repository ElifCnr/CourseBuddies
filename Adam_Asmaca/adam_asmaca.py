import random
from cizimler import asamalar, logo


print(logo)
isim = input("Bana ismini söyle :)\n")
print("İyi Şanslar "+ isim +"!")

hayvanlar=['KÖPEK', 'TAPİR', 'LAGOS', 'EBABİL', 'BİZON', 'TIRTIL', 'BOĞA', 'SİVRİSİNEK', 'YENGEÇ', 'TAVUK', 'ORNİTORENK', 'MERCAN', 'KANGURU', 'KEÇİ', 'ZÜRAFA', 'AYI', 'KAPLAN', 'LÜFER', 'VAŞAK', 'ÖRDEK', 'KEDİ', 'DENİZ YILDIZI', 'ATMACA', 'AY BALIĞI', 'BALİNA', 'CEYLAN', 'DEVE', 'FLAMİNGO', 'GORİL', 'GELİNCİK', 'HİNDİ', 'HOROZ', 'HAMSİ', 'GÜVERCİN', 'HAMSTER', 'İNEK', 'JAGUAR', 'JAPON KÖPEĞİ', 'KAPLAN', 'KAPLUMBAĞA', 'KANARYA', 'KADİFE BALIĞI', 'KARINCA', 'KATIR', 'KAYA KEKLİĞİ', 'KALAMAR', 'KIRLANGIÇ', 'KOALA', 'KOKARCA', 'KUĞU', 'KUNDUZ', 'KURBAĞA', 'KURT', 'KUKUS', 'KUTUP AYISI', 'KARİDES', 'KUZGUN', 'KARINCAYİYEN', 'KATİL BALİNA', 'KÜELA', 'KUTUP TİLKİSİ', 'KELEBEK', 'KÖPEK BALIĞI', 'KÖSTEBEK', 'PAPAĞAN', 'PELİKAN', 'PENGUEN', 'YUNUS BALIĞI', 'YILAN BALIĞI', 'ÇEKİRGE', 'ÖRÜMCEK', 'ISTAKOZ']
ulkeler=['AFGANİSTAN', 'ALMANYA', 'AMERİKA BİRLEŞİK DEVLETLERİ', 'ANDORRA', 'ANGOLA', 'ANTİGUA', 'BARBUDA', 'ARJANTİN', 'ARNAVUTLUK', 'AVUSTRALYA', 'AVUSTURYA', 'AZERBAYCAN', 'BAHAMALAR', 'BAHREYN', 'BANGLADEŞ', 'BARBADOS', 'BATI SAHRA', 'BELÇİKA', 'BELİZE', 'BENİN', 'BEYAZ RUSYA', 'BHUTAN', 'BİRLEŞİK ARAP EMİRLİKLERİ', 'BOLİVYA', 'BOSNA HERSEK', 'BOTSVANA', 'BREZİLYA', 'BRUNEİ', 'BULGARİSTAN', 'BURKİNA FASO', 'BURUNDİ', 'CEZAYİR', 'CİBUTİ', 'ÇAD', 'ÇEK CUMHURİYETİ', 'ÇİN HALK CUMHURİYETİ', 'DAĞLIK KARABAĞ CUMHURİYETİ', 'DANİMARKA', 'DOĞU TİMOR', 'DOMİNİK CUMHURİYETİ', 'DOMİNİKA', 'EKVADOR', 'GİNESİ', 'EL SALVADOR', 'ENDONEZYA', 'ERİTRE', 'ERMENİSTAN', 'ESTONYA', 'ETİYOPYA', 'FAS', 'FİJİ', 'FİLDİŞİ SAHİLLERİ', 'FİLİPİNLER', 'FİLİSTİN', 'FİNLANDİYA', 'FRANSA', 'GABON', 'GAMBİYA', 'GANA', 'GİNE', 'GİNE', 'BİSSAU', 'GİNE', 'BİSSAU', 'BATI AFRİKA', 'GRENADA', 'GUYANA', 'GUATEMALA', 'GÜNEY AFRİKA CUMHURİYETİ', 'GÜNEY KORE', 'GÜNEY OSETYA', 'GÜNEY SUDAN', 'GÜRCİSTAN', 'HAİTİ', 'HIRVATİSTAN', 'HİNDİSTAN', 'HOLLANDA', 'HONDURAS', 'IRAK', 'İNGİLTERE', 'İRAN', 'İRLANDA', 'İSPANYA', 'İSRAIL', 'İSVEÇ', 'İSVİÇRE', 'İTALYA', 'İZLANDA', 'JAMAİKA', 'JAPONYA', 'KAMBOÇYA', 'KAMERUN', 'KANADA', 'KARADAĞ', 'KATAR', 'KAZAKİSTAN', 'KENYA', 'KIRGIZİSTAN', 'KIBRIS CUMHURİYETİ', 'KİRİBATİ', 'KOLOMBİYA', 'KOMORLAR', 'KONGO', 'KONGO DEMOKRATİK CUMHURİYETİ', 'KOSOVA', 'KOSTA', 'RİKA', 'KUVEYT', 'KUZEY KIBRIS TÜRK CUMHURİYETİ', 'KUZEY KORE', 'KÜBA', 'LAOS', 'LESOTHO', 'LETONYA', 'LİBERYA', 'LİBYA', 'LİECHTENSTEİN', 'LİTVANYA', 'LÜBNAN', 'LÜKSEMBURG', 'MACARİSTAN', 'MADAGASKAR', 'MAKEDONYA CUMHURİYETİ', 'MALAVİ', 'MALDİVLER', 'MALEZYA', 'MALİ', 'MALTA', 'MARSHALL ADALARI', 'MEKSİKA', 'MISIR', 'MİKRONEZYA', 'MOĞOLİSTAN', 'MOLDOVA', 'MONAKO', 'MORİTANYA', 'MORİTİUS', 'MOZAMBİK', 'MYANMAR', 'NAMİBYA', 'NAURU', 'NEPAL', 'NİKARAGUA', 'NİJER', 'NİJERYA', 'NORVEÇ', 'ORTA AFRİKA CUMHURİYETİ', 'ÖZBEKİSTAN', 'PAKİSTAN', 'PALAU', 'PANAMA', 'PAPUA', 'PARAGUAY', 'PERU', 'POLONYA', 'PORTEKİZ', 'PORTO RİKO', 'ROMANYA', 'RUANDA', 'RUSYA FEDERASYONU', 'SAİNT KİTTS', 'SAİNT LUCİA', 'SAİNT VİNCENT VE GRENADİNLER', 'SAMOA', 'SAN MARİNO', 'SAO TOME VE PRINCIPE', 'SEALAND', 'SENEGAL', 'SEYŞELLER', 'SIRBİSTAN', 'SİERRA LEONE', 'SİNGAPUR', 'SLOVAKYA', 'SLOVENYA', 'SOLOMON ADALARI', 'SOMALİ', 'SOMALİLAND', 'SRİ LANKA', 'SUDAN', 'SURİNAM', 'SURİYE', 'SUUDİ ARABİSTAN', 'SVAZİLAND', 'ŞİLİ', 'TACİKİSTAN', 'TANZANYA', 'TAYLAND', 'TAYVAN', 'TOGO', 'TONGA', 'TRANSDİNYESTER', 'TRİNİDAD VE TOBAGO', 'TUNUS', 'TUVALU', 'TÜRKİYE', 'TÜRKMENİSTAN', 'UGANDA', 'UKRAYNA', 'UMMAN', 'URUGUAY', 'ÜRDÜN', 'VANUATU', 'VATİKAN', 'VENEZUELA', 'VİETNAM', 'YEMEN', 'YENİ ZELANDA', 'YEŞİL BURUN', 'YUNANİSTAN', 'ZAMBİYAV', 'ZİMBABVE']
nesneler = ['DUVAR', 'KAPI', 'SİLGİ', 'KALEM', 'MASA', 'SIRA', 'LAMBA', 'BARDAK', 'DOLAP', 'KİTAPLIK', 'KARTON', 'DEFTER', 'KİTAP', 'TELEFON', 'TAKVİM', 'SAAT', 'KAĞIT', 'RESİM', 'ANAHTAR', 'BİLGİSAYAR', 'SÖZLÜK', 'ARABA', 'GAZETE', 'TUĞLA', 'KASK', 'KLAVYE', 'SANDALYE', 'KOLTUK', 'BUZDOLABI', 'ÇAMAŞIR MAKİNESİ', 'BULAŞIK MAKİNESİ', 'DİŞ MACUNU', 'DİŞ FIRÇASI', 'TRAŞ MAKİNESİ', 'ŞAMPUAN', 'PİL', 'OYUNCAK', 'YEMEK', 'İÇECEK', 'KALEMTIRAŞ', 'ŞİŞE', 'SÜRAHİ', 'HALI', 'SOPA', 'AVİZE', 'VAZO', 'KABLO', 'FİŞ', 'BANT', 'TIPA', 'MUSLUK', 'KOLONYA', 'KUTU', 'MONİTÖR', 'MOUSE', 'CAM', 'PENCERE', 'TIRNAK MAKASI', 'MAKAS', 'SEHPA', 'TABURE', 'İĞNE', 'TIĞ', 'KUMAŞ', 'İPLİK', 'ATLAMA İPİ', 'HALTER', 'BARFİKS BARI', 'GÖMLEK', 'PANTOLON', 'TİŞÖRT', 'ŞORT', 'MONT', 'ÇADIR', 'BIÇAK', 'ÇAKI', 'BALTA', 'ODUN', 'FALÇATA', 'YAĞMURLUK', 'ÇORAP', 'TEKERLEK', 'TEYP', 'DİREKSİYON', 'ATKI', 'MASKE', 'BERE', 'ELDİVEN', 'ATLET', 'ANAHTARLIK', 'CÜZDAN', 'KREDİ KARTI', 'TARAK', 'ELEKTRİKLİ SÜPÜRGE', 'TOST MAKİNESİ', 'MİXER', 'SAKLAMA KABI', 'BLENDER', 'TELEFON', 'KULAKLIK', 'POWERBANK', 'KÜL TABLASI', 'CETVEL', 'PENSE', 'ÇEKİÇ', 'TESTERE', 'DİL TEMİZLEYİCİ', 'MODEM', 'KLASÖR', 'POŞET DOSYA', 'DÜĞME']
kelimeler = ['KÖPEK', 'TAPİR','AFGANİSTAN', 'ALMANYA', 'AMERİKA BİRLEŞİK DEVLETLERİ', 'DUVAR','BOĞA', 'SİVRİSİNEK', 'YENGEÇ', 'TAVUK', 'ORNİTORENK', 'MERCAN','ARNAVUTLUK', 'AVUSTRALYA', 'AVUSTURYA', 'AZERBAYCAN','ATMACA', 'AY BALIĞI', 'BALİNA', 'CEYLAN','KENYA', 'KIRGIZİSTAN','SÖZLÜK', 'ARABA', 'GAZETE', 'TUĞLA', 'KASK', 'KLAVYE','SURİYE', 'SUUDİ ARABİSTAN', 'SVAZİLAND', 'ŞİLİ', 'TACİKİSTAN','DİŞ FIRÇASI', 'TRAŞ MAKİNESİ', 'ŞAMPUAN', 'PİL', 'OYUNCAK', 'YEMEK','TAYVAN', 'TOGO', 'TONGA','MONİTÖR', 'MOUSE', 'CAM', 'PENCERE', 'TIRNAK MAKASI','KIRLANGIÇ', 'KOALA', 'KOKARCA', 'KUĞU', 'KUNDUZ', 'KURBAĞA', 'KURT', 'KUKUS', 'KUTUP AYISI','ERMENİSTAN', 'ESTONYA', 'ETİYOPYA', 'FAS', 'FİJİ', 'FİLDİŞİ SAHİLLERİ','KÖPEK BALIĞI', 'KÖSTEBEK', 'PAPAĞAN', 'PELİKAN', 'PENGUEN','TİŞÖRT', 'ŞORT', 'MONT', 'ÇADIR', 'BIÇAK', 'ÇAKI', 'BALTA', 'ODUN','NEPAL', 'NİKARAGUA', 'NİJER', 'NİJERYA', 'NORVEÇ','YILAN BALIĞI', 'ÇEKİRGE', 'ÖRÜMCEK', 'ISTAKOZ', 'TEYP', 'DİREKSİYON', 'ATKI', 'MASKE', 'BERE', 'ELDİVEN', 'ATLET','PERU', 'POLONYA', 'PORTEKİZ','TELEFON', 'KULAKLIK', 'POWERBANK', 'KÜL TABLASI', 'CETVEL', 'PENSE', 'ÇEKİÇ','İRAN', 'İRLANDA', 'İSPANYA', 'İSRAIL', 'İSVEÇ', 'İSVIÇRE', 'İTALYA', 'İZLANDA','MODEM', 'KLASÖR', 'POŞET DOSYA', 'DÜĞME']
kategori = -1
rastgele_kelime =""

while kategori < 0:
    print("""Kategoriler
    1. Hayvanlar
    2. Ülkeler
    3. Nesneler
    4. Rastgele
    """)

    try:
        kategori = int(input("Bir kategori numarası giriniz: "))
    except:
        print("Geçersiz giriş yaptınız..")
        continue

    if kategori == 1:
        rastgele_kelime = random.choice(hayvanlar)
    elif kategori == 2:
        rastgele_kelime = random.choice(ulkeler)
    elif kategori == 3:
        rastgele_kelime = random.choice(nesneler)
    elif kategori == 4:
        rastgele_kelime = random.choice(kelimeler)
    else:
        print("Yalnış kategori seçtiniz. 1- 4 arasında değer giriniz!")
        kategori = -1

print("Kelimeyi tahmin edin..")
tahminler = ''
can = len(asamalar) - 1
tahmin_listesi=[]

while can > 0:
    hata= 0

    for harf in rastgele_kelime:
        if harf in tahminler:
            print(harf,end=' ')

        elif harf==' ':
            print(" ",end=' ')
        else:
            print("_",end=' ')
            hata += 1

    print(asamalar[can])

    if hata == 0:
        print("\nKazandın !!")
        print("Kelime: ", rastgele_kelime)
        break

    tahmin = input("\nHarf tahmin edin: ").upper()

    if tahmin in tahminler:
        print("Zaten "+tahmin+" harfini tahmin etmiştiniz.")
        pass
    else:
        tahminler += tahmin

        if tahmin not in rastgele_kelime:
            can -= 1
            print("Yanlış")
            print(can,'tahmin hakkınız kaldı.')

            if can == 0:
                print(asamalar[can])
                print("Kaybettin :(")
                print("Kelime: ", rastgele_kelime)
                break
