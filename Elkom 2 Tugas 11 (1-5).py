# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 15:55:49 2021

@author: Quina
"""

print(" @@@    @   @  @@@  @    @      @@")
print("@   @   @   @   @   @@   @     @  @")
print("@ @ @   @   @   @   @ @  @    @@@@@@")
print("@   @   @   @   @   @  @ @   @      @")
print(" @@@ @  @ @ @  @@@  @    @  @        @")

import sys 

file_name = str(input("Masukkan nama file: "))

try:
    file = open(f"{file_name}.txt","r")
    print(f"File dengan nama {file_name}.txt ditemukan")
    noun = file.readlines()
    file.close() 
except:
    print(f"File dengan nama {file_name}.txt tidak ditemukan")
    file_name = str(input("Masukkan nama file: "))
    try:
        file = open(f"{file_name}.txt",'r')
        print(f"File dengan nama {file_name}.txt ditemukan")
        noun = file.readlines()
        file.close() 
    except: 
        print(f"File dengan nama {file_name}.txt tidak ditemukan")
        sys.exit()
        noun = file.readlines()
        file.close()   
        
update =  []
    
while True:
    option = input(""" MENU
 1. Lihat  Data
 2. Mencari Nilai Rata-Rata Praktikum Mahasiswa
 3. Update Nilai Praktikum Mahasiswa
 4. Simpan Perubahan Nilai
 5. Exit
 
 Pilih menu yang tersedia: """)
 
    if option == "1":
        print("\n [1. LIHAT DATA] ")
        for i in noun:
            print("\n\t",i.strip())
            
    elif option == "2":
        print("\n [2. MENCARI NILAI RATA-RATA PRAK MAHASISWA] ")
        name = input("\tMasukkan nama mahasiswa: ")
        for i in noun:
            noun_list = i.strip().split(' ')
            value1, value2, value3 = noun_list[-3], noun_list[-2], noun_list[-1]  
            title = ' '.join(noun_list[0:noun_list.index(value1)])
            if name == title:
                average = (int(value1) + int(value2) + int(value3)) / 3
                print(f"\tNilai = [{value1}, {value2}, {value3}]")
                print(f"\tRata-rata nilai praktikum {name} = {average}")

    elif option == "3":
        print ("\n [3. UPDATE NILAI PRAK MAHASISWA]")
        name = input("\tMasukkan nama mahasiswa: ")
        value_to = int(input("\tIngin update nilai praktikum ke-: "))
        new_value = int(input("\tNilai baru: "))
        for i in noun:
            noun_list = i.strip().split(' ')
            value1, value2, value3 = noun_list[-3], noun_list[-2], noun_list[-1]
            title = ' '.join(noun_list[0:noun_list.index(value1)])
            if name == title:
                tempdata = [title, int(value1), int(value2), int(value3)]
                old_value = tempdata[value_to]
                tempdata[value_to] = new_value
                noun[noun.index(i)] = f"{title} {tempdata[1]} {tempdata[2]} {tempdata[3]}\n"
                print(f"\n\tData berhasil di update dari nilai {old_value} menjadi nilai {new_value}")
                update.append(f"\tUpdate nilai prak {value_to} {title} >> {old_value} menjadi {new_value}")

    elif option == "4":
        print("\n [4. SIMPAN UPDATE NILAI]")
        file = open(f'{file_name}.txt','w')
        file.write(''.join(noun))
        file.close()
        for x in update:
            print(x)
        print(f'\tFILE {file_name}.txt BERHASIL DISIMPAN')
        update = []
    
    elif option == "5":
        print("\n [5. EXIT]")
        print("\tTERIMAKASIH ATAS KUNJUNGANNYA")
        sys.exit()
    
    else:
        print("\n [ERROR!!!]""\n\tINVALID INPUT, SILAHKAN MASUKKAN KEMBALI (menu hanya terdapat 1-5)")
