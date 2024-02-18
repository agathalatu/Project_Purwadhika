from tabulate import tabulate
from datetime import datetime
from datetime import date
import re


##### GLOBAL VARIABLE dan DUMMY DATA #####
separator = "====================================="

#Dictionary user berguna untuk menyiimpan user login
users = {
    1:{'username':'2005024410','password':'12345','role':'SDM'},
    2:{'username':'2006029950','password':'12345','role':'Karyawan'},
    3:{'username':'2012027204','password':'12345','role':'Karyawan'},
    4:{'username':'2015024844','password':'12345','role':'Karyawan'},
    5:{'username':'2007021348','password':'12345','role':'Karyawan'},
    6:{'username':'2010031296','password':'12345','role':'SDM'},
    7:{'username':'2006036941','password':'12345','role':'Karyawan'},
    8:{'username':'2001058527','password':'12345','role':'Karyawan'},
    9:{'username':'2002055875','password':'12345','role':'Karyawan'},
    10:{'username':'2002052406','password':'12345','role':'SDM'},
    11:{'username':'2003054740','password':'12345','role':'Karyawan'},
    12:{'username':'2004056480','password':'12345','role':'Karyawan'},
    13:{'username':'2017018204','password':'12345','role':'SDM'},
    14:{'username':'2020033117','password':'12345','role':'Karyawan'},
    15:{'username':'2012035262','password':'12345','role':'Karyawan'},
    16:{'username':'2021034458','password':'12345','role':'Karyawan'},
    17:{'username':'2002048541','password':'12345','role':'Karyawan'},
    18:{'username':'2003047054','password':'12345','role':'Karyawan'},
    19:{'username':'2003045807','password':'12345','role':'SDM'},
    20:{'username':'2004043081','password':'12345','role':'Karyawan'},
    21:{'username':'2002045469','password':'12345','role':'Karyawan'},
    22:{'username':'2018011818','password':'12345','role':'Karyawan'},
    23:{'username':'2018019870','password':'12345','role':'Karyawan'},
    24:{'username':'2024018620','password':'12345','role':'Karyawan'},
    25:{'username':'2023011346','password':'12345','role':'Karyawan'}
} 

#Dictionary employees berguna untuk menyimpan data karyawan yg nantinya akan di show, update, delete, dan add
employees = {
    1:{'NIK':'2005024410','NAMA':'Delia Cristabella','TEMPAT_LAHIR':'Jakarta','TGL_LAHIR':'12/12/1985','USIA':'38','JABATAN':'Manager','KODE_JABATAN':'02','JENIS_KELAMIN':'F','DIVISI':'SDM','ALAMAT':'BSD','NO_TELP':'827686','EMAIL':'delia.cristabella@mtpm.co.id','STATUS':'Menikah','JUMLAH_TANGGUNGAN':'2'},
    2:{'NIK':'2006029950','NAMA':'Lala Bella','TEMPAT_LAHIR':'Jakarta','TGL_LAHIR':'03/08/1970','USIA':'53','JABATAN':'Manager','KODE_JABATAN':'02','JENIS_KELAMIN':'F','DIVISI':'OPERATIONAL','ALAMAT':'BINTARO','NO_TELP':'873876','EMAIL':'lala.bella@mtpm.co.id','STATUS':'Lajang','JUMLAH_TANGGUNGAN':'0'},
    3:{'NIK':'2012027204','NAMA':'Agus Purwanto','TEMPAT_LAHIR':'Jakarta','TGL_LAHIR':'10/01/1979','USIA':'45','JABATAN':'Manager','KODE_JABATAN':'02','JENIS_KELAMIN':'M','DIVISI':'LEGAL COMPLIANCE','ALAMAT':'DEPOK','NO_TELP':'246238','EMAIL':'agus.purwanto@mtpm.co.id','STATUS':'Menikah','JUMLAH_TANGGUNGAN':'1'},
    4:{'NIK':'2015024844','NAMA':'Donny Damara','TEMPAT_LAHIR':'Jakarta','TGL_LAHIR':'15/08/1969','USIA':'54','JABATAN':'Manager','KODE_JABATAN':'02','JENIS_KELAMIN':'M','DIVISI':'MARKETING','ALAMAT':'JAGAKARSA','NO_TELP':'157934','EMAIL':'donny.damara@mtpm.co.id','STATUS':'Menikah','JUMLAH_TANGGUNGAN':'1'},
    5:{'NIK':'2007021348','NAMA':'Lea Andreas','TEMPAT_LAHIR':'Jakarta','TGL_LAHIR':'30/05/1989','USIA':'34','JABATAN':'Manager','KODE_JABATAN':'02','JENIS_KELAMIN':'M','DIVISI':'IT','ALAMAT':'BEKASI','NO_TELP':'378246','EMAIL':'lea.andreas@mtpm.co.id','STATUS':'Lajang','JUMLAH_TANGGUNGAN':'0'},
    6:{'NIK':'2010031296','NAMA':'Darmadi','TEMPAT_LAHIR':'Jakarta','TGL_LAHIR':'17/11/1984','USIA':'39','JABATAN':'KaDiv','KODE_JABATAN':'03','JENIS_KELAMIN':'M','DIVISI':'SDM','ALAMAT':'KEMANG','NO_TELP':'231168','EMAIL':'darmadi@mtpm.co.id','STATUS':'Menikah','JUMLAH_TANGGUNGAN':'2'},
    7:{'NIK':'2006036941','NAMA':'Hosean','TEMPAT_LAHIR':'Jakarta','TGL_LAHIR':'27/02/1986','USIA':'37','JABATAN':'KaDiv','KODE_JABATAN':'03','JENIS_KELAMIN':'M','DIVISI':'OPERATIONAL','ALAMAT':'LEBAK BULUS','NO_TELP':'275900','EMAIL':'hosean@mtpm.co.id','STATUS':'Lajang','JUMLAH_TANGGUNGAN':'0'},
    8:{'NIK':'2001058527','NAMA':'Agatha','TEMPAT_LAHIR':'Jakarta','TGL_LAHIR':'17/03/1980','USIA':'43','JABATAN':'Direktur','KODE_JABATAN':'05','JENIS_KELAMIN':'F','DIVISI':'OPERATIONAL','ALAMAT':'PASAR MINGGU','NO_TELP':'426455','EMAIL':'agatha@mtpm.co.id','STATUS':'Menikah','JUMLAH_TANGGUNGAN':'3'},
    9:{'NIK':'2002055875','NAMA':'Hermawan','TEMPAT_LAHIR':'Jakarta','TGL_LAHIR':'26/06/1975','USIA':'48','JABATAN':'Direktur','KODE_JABATAN':'05','JENIS_KELAMIN':'M','DIVISI':'IT','ALAMAT':'SENAYAN','NO_TELP':'213480','EMAIL':'hermawan@mtpm.co.id','STATUS':'Menikah','JUMLAH_TANGGUNGAN':'3'},
    10:{'NIK':'2002052406','NAMA':'Anatama','TEMPAT_LAHIR':'Jakarta','TGL_LAHIR':'21/05/1984','USIA':'39','JABATAN':'Direktur','KODE_JABATAN':'05','JENIS_KELAMIN':'F','DIVISI':'SDM','ALAMAT':'PONDOK INDAH','NO_TELP':'485629','EMAIL':'anatama@mtpm.co.id','STATUS':'Lajang','JUMLAH_TANGGUNGAN':'0'},
    11:{'NIK':'2003054740','NAMA':'Gemah ','TEMPAT_LAHIR':'Jakarta','TGL_LAHIR':'12/12/1985','USIA':'38','JABATAN':'Direktur','KODE_JABATAN':'05','JENIS_KELAMIN':'F','DIVISI':'MARKETING','ALAMAT':'PONDOK INDAH','NO_TELP':'315556','EMAIL':'gemah.@mtpm.co.id','STATUS':'Lajang','JUMLAH_TANGGUNGAN':'0'},
    12:{'NIK':'2004056480','NAMA':'Ripah','TEMPAT_LAHIR':'Jakarta','TGL_LAHIR':'03/08/1973','USIA':'50','JABATAN':'Direktur','KODE_JABATAN':'05','JENIS_KELAMIN':'F','DIVISI':'LEGAL COMPLIANCE','ALAMAT':'PONDOK INDAH','NO_TELP':'970046','EMAIL':'ripah@mtpm.co.id','STATUS':'Lajang','JUMLAH_TANGGUNGAN':'0'},
    13:{'NIK':'2017018204','NAMA':'Josh Pittsburgh','TEMPAT_LAHIR':'London','TGL_LAHIR':'10/01/1979','USIA':'45','JABATAN':'Staf','KODE_JABATAN':'01','JENIS_KELAMIN':'M','DIVISI':'SDM','ALAMAT':'TEROGONG','NO_TELP':'368468','EMAIL':'josh.pittsburgh@mtpm.co.id','STATUS':'Lajang','JUMLAH_TANGGUNGAN':'0'},
    14:{'NIK':'2020033117','NAMA':'Fellastra','TEMPAT_LAHIR':'Jakarta','TGL_LAHIR':'15/08/1969','USIA':'54','JABATAN':'KaDiv','KODE_JABATAN':'03','JENIS_KELAMIN':'M','DIVISI':'IT','ALAMAT':'KEMANG','NO_TELP':'254790','EMAIL':'fellastra@mtpm.co.id','STATUS':'Menikah','JUMLAH_TANGGUNGAN':'1'},
    15:{'NIK':'2012035262','NAMA':'tomi Sunarto','TEMPAT_LAHIR':'Malang','TGL_LAHIR':'30/05/1989','USIA':'34','JABATAN':'KaDiv','KODE_JABATAN':'03','JENIS_KELAMIN':'M','DIVISI':'MARKETING','ALAMAT':'LEBAK BULUS','NO_TELP':'467234','EMAIL':'tomi.sunarto@mtpm.co.id','STATUS':'Menikah','JUMLAH_TANGGUNGAN':'2'},
    16:{'NIK':'2021034458','NAMA':'Suahasil','TEMPAT_LAHIR':'Yogyakarta','TGL_LAHIR':'17/11/1984','USIA':'39','JABATAN':'KaDiv','KODE_JABATAN':'03','JENIS_KELAMIN':'M','DIVISI':'LEGAL COMPLIANCE','ALAMAT':'BSD','NO_TELP':'213537','EMAIL':'suahasil@mtpm.co.id','STATUS':'Lajang','JUMLAH_TANGGUNGAN':'0'},
    17:{'NIK':'2002048541','NAMA':'Sri','TEMPAT_LAHIR':'Denpasar','TGL_LAHIR':'27/02/1986','USIA':'37','JABATAN':'Group Head','KODE_JABATAN':'04','JENIS_KELAMIN':'F','DIVISI':'MARKETING','ALAMAT':'DEPOK','NO_TELP':'246168','EMAIL':'sri@mtpm.co.id','STATUS':'Menikah','JUMLAH_TANGGUNGAN':'3'},
    18:{'NIK':'2003047054','NAMA':'Henny','TEMPAT_LAHIR':'Yogyakarta','TGL_LAHIR':'17/03/1980','USIA':'43','JABATAN':'Group Head','KODE_JABATAN':'04','JENIS_KELAMIN':'F','DIVISI':'LEGAL COMPLIANCE','ALAMAT':'BOGOR','NO_TELP':'246135','EMAIL':'henny@mtpm.co.id','STATUS':'Menikah','JUMLAH_TANGGUNGAN':'2'},
    19:{'NIK':'2003045807','NAMA':'Dwi','TEMPAT_LAHIR':'Yogyakarta','TGL_LAHIR':'26/06/1975','USIA':'48','JABATAN':'Group Head','KODE_JABATAN':'04','JENIS_KELAMIN':'M','DIVISI':'SDM','ALAMAT':'DEPOK','NO_TELP':'348670','EMAIL':'dwi@mtpm.co.id','STATUS':'Menikah','JUMLAH_TANGGUNGAN':'2'},
    20:{'NIK':'2004043081','NAMA':'Putu','TEMPAT_LAHIR':'Buleleng','TGL_LAHIR':'21/05/1984','USIA':'39','JABATAN':'Group Head','KODE_JABATAN':'04','JENIS_KELAMIN':'M','DIVISI':'IT','ALAMAT':'BOGOR','NO_TELP':'458679','EMAIL':'putu@mtpm.co.id','STATUS':'Menikah','JUMLAH_TANGGUNGAN':'1'},
    21:{'NIK':'2002045469','NAMA':'Wiryawan','TEMPAT_LAHIR':'Jakarta','TGL_LAHIR':'28/07/1970','USIA':'53','JABATAN':'Group Head','KODE_JABATAN':'04','JENIS_KELAMIN':'M','DIVISI':'OPERATIONAL','ALAMAT':'PASAR MINGGU','NO_TELP':'478397','EMAIL':'wiryawan@mtpm.co.id','STATUS':'Lajang','JUMLAH_TANGGUNGAN':'0'},
    22:{'NIK':'2018011818','NAMA':'Tedy Mahendra','TEMPAT_LAHIR':'Jakarta','TGL_LAHIR':'23/10/1983','USIA':'40','JABATAN':'Staf','KODE_JABATAN':'01','JENIS_KELAMIN':'M','DIVISI':'OPERATIONAL','ALAMAT':'TANAH ABANG','NO_TELP':'532806','EMAIL':'tedy.mahendra@mtpm.co.id','STATUS':'Lajang','JUMLAH_TANGGUNGAN':'0'},
    23:{'NIK':'2018019870','NAMA':'Wregas','TEMPAT_LAHIR':'Jakarta','TGL_LAHIR':'18/11/1961','USIA':'62','JABATAN':'Staf','KODE_JABATAN':'01','JENIS_KELAMIN':'M','DIVISI':'MARKETING','ALAMAT':'TEROGONG','NO_TELP':'609223','EMAIL':'wregas@mtpm.co.id','STATUS':'Lajang','JUMLAH_TANGGUNGAN':'0'},
    24:{'NIK':'2024018620','NAMA':'Randraru','TEMPAT_LAHIR':'Jakarta','TGL_LAHIR':'01/01/2000','USIA':'24','JABATAN':'Staf','KODE_JABATAN':'01','JENIS_KELAMIN':'M','DIVISI':'LEGAL COMPLIANCE','ALAMAT':'BANGKA','NO_TELP':'704860','EMAIL':'randraru@mtpm.co.id','STATUS':'Menikah','JUMLAH_TANGGUNGAN':'2'},
    25:{'NIK':'2023011346','NAMA':'Banyu','TEMPAT_LAHIR':'Yogyakarta','TGL_LAHIR':'07/03/2001','USIA':'22','JABATAN':'Staf','KODE_JABATAN':'01','JENIS_KELAMIN':'M','DIVISI':'IT','ALAMAT':'KEMANG','NO_TELP':'295789','EMAIL':'banyu@mtpm.co.id','STATUS':'Menikah','JUMLAH_TANGGUNGAN':'2'},
}
opsiJabatan = '''
Masukan Jabatan :
1. Staf 
2. Manager
3. KaDiv
4. Group Head
5. Direktur
'''

opsiDivisi = '''
Masukan Divisi :
1. OPERATIONAL 
2. IT
3. MARKETING
4. SDM
5. LEGAL COMPLIANCE
'''


##### METHOD YANG DIGUNAKAN #####

#Method untuk pengecekan username & password 
def login() :
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    result = ["",""]
    for i in users :
        if(('username',usernameInput) in users[i].items()):
            if(('password',passwordInput) in users[i].items()):
                result[0] = "Login Berhasil"
                result[1] = users[i]['role']
                break
            else:
                result[0] = "Login gagal"
                result[1] = "Password yang Anda masukan salah"
                break
        else:
            result[0] = "Login gagal"
            result[1] = "Username yang Anda masukan salah"

    return result

#Method yang digunakan untuk pengecekan format email berdasarkan regex/p attern yang sudah ditentukan
def validateEmail(emailInput):
    email_format = r"(^[a-zA-Z0-9'_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    if re.match(email_format, emailInput, re.IGNORECASE) :
        return True
    else :
        return False

#Method yang digunakan untuk menghitung umur
def calculateAge(bornDate):
    born = datetime.strptime(bornDate, '%Y-%m-%d')
    today = date.today()
    if today.month < born.month :
        return today.year - born.year -1
    else :
        return today.year - born.year

#Method yang digunakan untuk mendapatkan index terakhir untuk menambahkan data baru ke dictionary
def getNewIndex(dictionary):
    lastIdx = int(sorted(dictionary.keys())[-1])
    return lastIdx+1

#Method yang digunakan untuk mencari suatu kata dari key yang ada pada dictionary
def searchEmployee(kolom,searchText,dictionary):
    result = {}
    for key,value in dictionary.items():
        if (value[kolom].upper() == searchText.upper()) :
            result[key] = value
    return result

#Method yang digunakan untuk menampilkan data karyawan
#Method ini juga memiliki fungsi sorting secara ascending dan juga filter berdasarkan kolom dan kata yang ingin dicari
def showEmployee(dictionary) :
    headers = ["No","NIK", "NAMA", "TEMPAT LAHIR", "TGL LAHIR","USIA","JABATAN","KODE JABATAN","JENIS KELAMIN","DIVISI","ALAMAT","NO TELP","EMAIL","STATUS","JUMLAH TANGGUNGAN"]
    values = [[name,*inner.values()] for name, inner in dictionary.items()]
    #print dictionary yang sudah diset kedalam bentuk table
    print(tabulate(values, headers=headers,tablefmt="grid"))

    opsiSortFilter = input("Pilih Menu (Sort/Filter) : ")
    while(opsiSortFilter.upper() != "SORT" and opsiSortFilter.upper() != "FILTER"):
        print("Opsi yang Anda masukan salah")
        opsiSortFilter = input("Pilih Menu (Sort/Filter) : ")
    
    if(opsiSortFilter.upper() == "SORT") :
        field = input("Silahkan pilih kolom yang ingin disorting (NIK/Nama/Usia) : ")
        while(field.upper() != "NIK" and field.upper() != "NAMA" and field.upper() != "USIA"):
            print("Kolom yang Anda pilih salah")
            field = input("Silahkan pilih kolom yang ingin disorting (NIK/Nama/Usia) : ")
        
        if(field.upper() == "NIK"):
            sortedDict = dict(sorted(dictionary.items(), key=lambda x: x[1]["NIK"]))
        elif(field.upper() == "NAMA") :
            sortedDict = dict(sorted(dictionary.items(), key=lambda x: x[1]["NAMA"]))
        else :
            sortedDict = dict(sorted(dictionary.items(), key=lambda x: x[1]["USIA"]))
        
        values = [[name,*inner.values()] for name, inner in sortedDict.items()]
        print(tabulate(values, headers=headers,tablefmt="grid"))
    else :
        field = input("Silahkan pilih kolom yang ingin difilter (Jabatan/Divisi/Status) : ")
        while(field.upper() != "JABATAN" and field.upper() != "DIVISI" and field.upper() != "STATUS"):
            print("Kolom yang Anda pilih salah")
            field = input("Silahkan pilih kolom yang ingin difilter (Jabatan/Divisi/Status) : ")
        searchText = input("Masukan kata yang ingin dicari : ")
        
        if(field.upper() == "JABATAN"):
            filteredDict = searchEmployee("JABATAN",searchText,employees)
        elif(field.upper() == "DIVISI") :
            filteredDict = searchEmployee("DIVISI",searchText,employees)
        else :
            filteredDict = searchEmployee("STATUS",searchText,employees)
        
        values = [[name,*inner.values()] for name, inner in filteredDict.items()]
        print(tabulate(values, headers=headers,tablefmt="grid"))


#Method yang digunakan untuk menambahkan data employee dan data user untuk login
#Pada method ini terdapat validasi untuk beberapa input
def createEmployeeAndUser():
    nik = input("Masukan NIK : ")
    while (len(nik) != 10 or not nik.isnumeric()) :
        print("NIK yang dimasukan kurang/lebih dari 10 digit atau mengandung karakter selain angka")
        nik = input("Masukan NIK : ")
        
    nama = input("Masukan NAMA : ")
    while (len(nama) > 100 or not nik.isalnum()) :
        print("nama yang dimasukan melebihi 100 karakter atau mengandung karakter selain alphanumeric")
        nama = input("Masukan NAMA : ")

    tempatLahir = input("Masukan Tempat Lahir : ")
    
    tanggalLahir = input("Masukan Tanggal Lahir (yyyy-mm-dd): ")
    while True :
        try:
            #pengecekan format tanggal berdasarkan pattern yang sudah ditentukan
            datetime.strptime(tanggalLahir, "%Y-%m-%d")
            break
        except ValueError:
            print("Tanggal lahir yang dimasukan harus dalam format yyyy-mm-dd")
            tanggalLahir = input("Masukan Tanggal Lahir (yyyy-mm-dd): ")

    usia = calculateAge(tanggalLahir)

    inputJabatan = input(opsiJabatan)
    while (inputJabatan != "1" and inputJabatan != "2" and inputJabatan != "3" and inputJabatan != "4" and inputJabatan != "5") :
        print("Masukan opsi jabatan yang sesuai")
        inputJabatan = input(opsiJabatan)
        
    if inputJabatan == "1" :
        jabatan = "Staf"
    elif inputJabatan == "2" :
        jabatan = "Manager"
    elif inputJabatan == "3" :
        jabatan = "KaDiv"
    elif inputJabatan == "4" :
        jabatan = "Group Head"
    else :
        jabatan = "Direktur"
    
    kodeJabatan = "0"+inputJabatan

    jenisKelamin = input("Masukan Jenis Kelamin (F/M): ")
    while (jenisKelamin.upper() != "F" and jenisKelamin.upper() != "M"):
        print("Masukan jenis kelamin yang sesuai")
        jenisKelamin = input("Masukan Jenis Kelamin (F/M): ")

    inpuitDivisi = input(opsiDivisi)
    while (inpuitDivisi != "1" and inpuitDivisi != "2" and inpuitDivisi != "3" and inpuitDivisi != "4" and inpuitDivisi != "5") :
        print("Masukan opsi divisi yang sesuai")
        inpuitDivisi = input(opsiDivisi)

    if inpuitDivisi == "1" :
        divisi = "OPERATIONAL"
    elif inpuitDivisi == "2" :
        divisi = "IT"
    elif inpuitDivisi == "3" :
        divisi = "MARKETING"
    elif inpuitDivisi == "4" :
        divisi = "SDM"
    else :
        divisi = "LEGAL COMPLIANCE"

    alamat = input("Masukan Alamat : ")

    noTelepon = input("Masukan Nomor Telepon : ")
    while(not noTelepon.isnumeric()):
        print("Nomor Telepon hanya boleh diisi angka")
        noTelepon = input("Masukan Nomor Telepon : ")
    
    email = input("Masukan Email (xxx@xxx.xxx) : ")
    while(not validateEmail(email)):
        print("Email format tidak sesuai")
        email = input("Masukan Email (xxx@xxx.xxx) : ")
    
    status = input("Masukan Status (Menikah/Lajang) : ")
    while(status.upper() != "MENIKAH" and status.upper() != "LAJANG"):
        print("Masukan status yang sesuai")
        status = input("Masukan Status (Menikah/Lajang) : ")

    jmlTanggungan = input("Masukan Jumlah Tanggungan : ")
    while(not jmlTanggungan.isnumeric()):
        print("Jumlah tanggungan hanya boleh diisi angka")
        jmlTanggungan = input("Masukan Jumlah Tanggungan : ")

    #Membuat data dictionary baru dari hasil inputan sebelumnya dimana ada beberapa data yang dibuat uppercase
    newEmployee = dict(NIK=nik,NAMA=nama.upper(),TEMPAT_LAHIR=tempatLahir.upper(),TGL_LAHIR=tanggalLahir,USIA=usia,JABATAN=jabatan.upper(),KODE_JABATAN=kodeJabatan,JENIS_KELAMIN=jenisKelamin.upper(),DIVISI=divisi,ALAMAT=alamat.upper(),NO_TELP=noTelepon,EMAIL=email.upper(),STATUS=status.upper(),JUMLAH_TANGGUNGAN=jmlTanggungan)
    newIndexEmployee = getNewIndex(employees) #Mendapatkan index terakhir dari dictionary employees
    #Menambahakan data dictionary baru tersebut ke dictionary yang sudah ada sebelumnya
    employees[newIndexEmployee] = newEmployee

    #Membuat data user baru supaya bisa login
    newRole = ""
    if(divisi=="SDM"):
        newRole = "SDM"
    else:
        newRole = "Karyawan"
    newUser = dict(username=nik,password="12345",role=newRole)
    newIndexUser = getNewIndex(users) #Mendapatkan index terakhir dari dictionary users
    users[newIndexUser] = newUser


#Method yang digunakan untuk menghapus employee dan user berdasarkan NIK
#Asumsi setiap kali pembuatan employee baru maka akan membuat user login baru juga dengan NIK dan index yang sama
def deleteEmployeeAndUser(deletedNik,employeeDictionary,userDictionary):
    result = "NIK tidak ditemukan"
    for key in employeeDictionary:
        if employeeDictionary[key]["NIK"] == deletedNik :
            del employeeDictionary[key]
            del userDictionary[key]
            result = "Penghapusan data karyawan berhasil"
            return result
    return result    


#Method yang digunakan untuk mengupdate data employee berdasarkan NIK
#Pada method ini hanya dibuat beberapa data yang bisa diupdate sebagai contoh dan dilakukan validasi juga terhadap method tersebut
def updateEmployee(updatedNik,dictionary):
    result = "NIK tidak ditemukan"
    #Melakukan looping terhadap data employee berdasarkan NIK yang ingin diupdate
    for key in dictionary:
        #Jika data NIK tersebut terdapat pada dictionary, maka lakukan update
        if dictionary[key]["NIK"] == updatedNik :
            inputDivisi = input(opsiDivisi)
            while (inputDivisi != "1" and inputDivisi != "2" and inputDivisi != "3" and inputDivisi != "4" and inputDivisi != "5") :
                print("Masukan opsi divisi yang sesuai")
                inputDivisi = input(opsiDivisi)

            if inputDivisi == "1" :
                divisi = "OPERATIONAL"
            elif inputDivisi == "2" :
                divisi = "IT"
            elif inputDivisi == "3" :
                divisi = "MARKETING"
            elif inputDivisi == "4" :
                divisi = "SDM"
            else :
                divisi = "LEGAL COMPLIANCE"

            alamat = input("Masukan Alamat : ")

            noTelepon = input("Masukan Nomor Telepon : ")
            while(not noTelepon.isnumeric()):
                print("Nomor Telepon hanya boleh diisi angka")
                noTelepon = input("Masukan Nomor Telepon : ")

            status = input("Masukan Status (Menikah/Lajang) : ")
            while(status.upper() != "MENIKAH" and status.upper() != "LAJANG"):
                print("Masukan status yang sesuai")
                status = input("Masukan Status (Menikah/Lajang) : ")

            jmlTanggungan = input("Masukan Jumlah Tanggungan : ")
            while(not jmlTanggungan.isnumeric()):
                print("Jumlah tanggungan hanya boleh diisi angka")
                jmlTanggungan = input("Masukan Jumlah Tanggungan : ")

            #Melakukan update pada beberapa key dari NIK yang dicari
            dictionary[key]["DIVISI"] = divisi.upper()
            dictionary[key]["ALAMAT"] = alamat.upper()
            dictionary[key]["NO_TELP"] = noTelepon
            dictionary[key]["STATUS"] = status.upper()
            dictionary[key]["JUMLAH_TANGGUNGAN"] = jmlTanggungan
            result = "Perubahan data karyawan berhasil"

            #Jika sudah NIK sudah ditemukan dan data sudah berhasil diupdate maka akan mengembalikan pesan berhasil dan menghentikan loop (looping tidak akan dilanjut ke item berikutnya untuk dilakukan pencarian lagi)
            return result
    return result 


#Method untuk menampilkan menu user karyawan
#User karyawan hanya bisa melihat data saja
def karyawanMenu() :
    menu = '''
Silahkan Pilih Menu berikut :
1. Menampilkan Data Karyawan
2. Logout
    '''
    print(menu)
    chooseMenu = ""
    exitFlag = False
    while not exitFlag :
        chooseMenu = input("Menu yang dipilih (1/2) : ")
        if(chooseMenu == "1") :
            print("Berikut semua data karyawan")
            showEmployee(employees)
            print(separator)
            print(menu)
        elif(chooseMenu == "2") :
            print("Logout berhasil")
            exitFlag = True
        else :
            print("Menu yang Anda input salah")
            print(separator)
            print(menu)


#Method yang digunakan untuk menampilakn menu user SDM
#User SDM bisa melakuan CRUD
def sdmMenu() :
    menu = '''
Silahkan Pilih Menu berikut :
1. Menambahkan Karyawan
2. Menampilkan Data Karyawan
3. Merubah Data Karyawan
4. Menghapus Data Karyawan
5. Logout
    '''
    chooseMenu = ""
    exitFlag = False

    print(menu)
    while not exitFlag :
        chooseMenu = input("Menu yang dipilih (1/2/3/4/5) : ")
        if(chooseMenu == "1") :
            createEmployeeAndUser() #memanggil method untuk create employee
            print("Penambahan data karyawan berhasil")
            print(separator)
            print(menu)
        elif(chooseMenu == "2") :
            print("Berikut semua data karyawan")
            showEmployee(employees) #memanggil method untuk menampilkan data employee
            print(separator)
            print(menu)
        elif(chooseMenu == "3") :
            updatedNik = input("Masukan NIK yang ingin diubah : ")
            res = updateEmployee(updatedNik,employees) #memanggil method untuk update data employee
            print(res)
            print(separator)
            print(menu)
        elif(chooseMenu == "4") :
            deletedNik = input("Masukan NIK yang ingin dihapus : ")
            res = deleteEmployeeAndUser(deletedNik,employees,users) #memanggil method untuk menghapus data employee
            print(res)
            print(separator)
            print(menu)
        elif(chooseMenu == "5") :
            print("Logout berhasil")
            exitFlag = True #ketika opsi logout dipilih, maka akan merubah data exitFlag menjadi True untuk keluar dari loop
        else :
            print("Menu yang Anda input salah")
            print(separator)
            print(menu)

#Method untuk menampilkan main menu dan halaman login
def mainMenu() :
    #Definisi variable yang digunakan
    loginMessage = ""
    userRole = ""
    welcomeMessage = '''
****** Selamat datang di PT. Maju Terus Pantang Mundur ******
    '''
    print(welcomeMessage)
    print(separator)
    print("Silahkan login menggunakan NIK dan password Anda")
    loginResult = login()
    #Pengecekan hasil login, jika berhasil maka rolenya akan diambil untuk menentukan opsi pilihan menu selanjutnya
    if(loginResult[0] == "Login Berhasil") :
        loginMessage = loginResult[0] 
        userRole = loginResult[1]
        print(loginMessage)
        print(separator)

        if (userRole == "SDM") :
            sdmMenu()
        else :
            karyawanMenu()
    else :
        loginMessage = loginResult[0] +". "+loginResult[1]
        print(loginMessage)
        print(separator)
    

#Method utama untuk menjalankan program
def run() :
    mainMenu()
    #Dilakukan perulangan apabila setelah user logout ingin melakukan relogin kembali
    while True :
        relogin = input("Ingin Relogin ulang? (Y/N) : ")
        if(relogin.upper() == "Y"):
            mainMenu()
        else :
            print("Program berhenti")
            break
   

#Run Program
run()