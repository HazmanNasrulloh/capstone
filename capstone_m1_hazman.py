
from tabulate import tabulate
import random
import string
import os
os.system('cls')
def display_menu():
    print('='*50)
    print(f"{'SELAMAT DATANG':^50}")
    print(f"{'DI YELLOW PAGES':^50}")
    print(f"{'BANDUNG':^50}")
    print('='*50)
    print('1. Tampilkan Kontak')
    print('2. Cari kontak')
    print('3. Edit Kontak')
    print('4. Exit')
    print('5. Kontak Random')
    print('='*50)

def display_contacts(contacts):
    if contacts=={}:
        print('No contacts to display.')
        return
    headers = ['No.', 'Phone Number', 'Name', 'Profesi/Usaha', 'Tipe No', 'Alamat']
    contact_list = [[index+1, phone, data['Nama'], data['Profesi/Usaha'], data['Tipe No'], data['Alamat']] 
                    for index, (phone, data) in enumerate(contacts.items())]
    print(tabulate(contact_list, headers=headers, tablefmt='fancy_grid'))

def add_contact(contacts):
    phone = input('Enter the phone number: ')
    if phone in contacts:
        print('Contact with this phone number already exists.')
        return
    name = input('Masukkan Nama: ')
    profesi = input('Masukkan Profesi/Usaha: ')
    tipe_no = input('MasukkanTipe No: ')
    alamat = input('Masukkan Alamat: ')
    contacts[phone] = {'Nama': name, 'Profesi/Usaha': profesi, 'Tipe No': tipe_no, 'Alamat': alamat}
    
    print('Kontak Di Tambah')

def delete_contact(contacts):
    display_contacts(contacts)
    if not contacts:
        return
    else :
        while True:
            print('1. Hapus nomor')
            print('2. Hapus semua')
            print('3. Keluar')
            perintah_hapus =  input ('masukan menu yang anda pilih :')
            if perintah_hapus == '1':
                phone = input('Masukkan Kontak Yang anda Akan Hapus: ')
                if phone in contacts:
                    confirm = input('Apakah anda mau menghapus kontak? (y/n) ')
                    if confirm == 'y' or confirm == 'Y':
                        del contacts[phone]
                        print('Kontak Di Hapus')
                    elif confirm == 'n' or confirm == 'N':
                        return
                else:
                    print('Kontak Tidak Ada.')
            if perintah_hapus == '2':
                    confirm = input('Apakah anda mau menghapus kontak? (y/n) ')
                    if confirm == 'y' or confirm == 'Y':
                        contacts.clear()
                        print("Semua kontak telah dihapus.")
                    elif confirm == 'n' or confirm == 'N':
                        return
            if perintah_hapus == '3':
                return

def clear_contacts(contacts):
    contacts.clear()
    print("Semua kontak telah dihapus.")



def edit_contact(contacts):
    display_contacts(contacts)
    if not contacts:
        return
    
    phone = input('Masukkan nomor yang akan diedit: ')
    if phone in contacts:
        print('Edit Kontak:')
        print('='*50)
        print(f'Nomor Telepon: {phone}')
        print(f"Nama: {contacts[phone]['Nama']}")
        print(f"Profesi/Usaha: {contacts[phone]['Profesi/Usaha']}")
        print(f"Tipe No: {contacts[phone]['Tipe No']}")
        print(f"Alamat: {contacts[phone]['Alamat']}")
        print('='*50)

        confirm = input('Apakah Anda yakin ingin mengedit kontak ini? (y/n): ').lower()
        if confirm == 'y' or confirm == 'Y':
            print('Pilih yang ingin diedit (Nama/Profesi/Usaha/Tipe No/Alamat): ')
            choice = input().lower()
            if choice == 'nama':
                contacts[phone]['Nama'] = input('Masukkan nama baru: ')
            elif choice == 'profesi/usaha':
                contacts[phone]['Profesi/Usaha'] = input('Masukkan profesi/usaha baru: ')
            elif choice == 'tipe no':
                contacts[phone]['Tipe No'] = input('Masukkan tipe no baru: ')
            elif choice == 'alamat':
                contacts[phone]['Alamat'] = input('Masukkan alamat baru: ')
            else:
                print('Pilihan tidak valid')
        elif confirm == 'n' or confirm == 'N':
            print('Pengeditan kontak dibatalkan.')
        else:
            print('Pilihan tidak valid')
    else:
        print('Kontak tidak ditemukan.')

def search_contact(contacts):
    search_term = input('Enter the name or phone number to search: ')
    search_results = []
    for phone, data in contacts.items():
        if search_term.lower() in phone.lower() or search_term.lower() in data['Nama'].lower():
            search_results.append([phone, data['Nama'], data['Profesi/Usaha'], data['Tipe No'], data['Alamat']])
    if search_results:
        print('Search Results:')
        headers = ['Phone Number', 'Name', 'Profesi/Usaha', 'Tipe No', 'Alamat']
        print(tabulate(search_results, headers=headers, tablefmt='fancy_grid'))
    else:
        print('Kontak Tidak Ditemukan.')

def random_phone_number():
    return ''.join(random.choices(string.digits, k=12))

def random_profession():
    professions = ['Dokter', 'Pengamen', 'Pelukis', 'Nelayan', 'Chef', 'Scammer', 'Magician', 'Pengangguran', 'Bully']
    return random.choice(professions)

def random_address():
    address = ['Cimahi', 'Sarijadi', 'Dago']
    return random.choice(address)

def random_contact():
    name = ''.join(random.choices(string.ascii_letters, k=random.randint(5, 10)))
    profession = random_profession()
    phone_number = random_phone_number()
    address = random_address()
    return phone_number, {'Nama': name, 'Profesi/Usaha': profession, 'Tipe No': 'Mobile', 'Alamat': address}

def add_random_contacts(contacts, num_contacts):
    for _ in range(num_contacts):
        phone, contact_info = random_contact()
        contacts[phone] = contact_info

contacts = {
        '082214013188': {'Nama': 'Hazman', 'Profesi/Usaha': 'Mahasiswa', 'Tipe No': 'Mobile', 'Alamat': 'Sarijadi'},
        '082141143535': {'Nama': 'Wormo', 'Profesi/Usaha': 'Penulis', 'Tipe No': 'Pribadi', 'Alamat': 'Setiabudi'},
        '085145363937': {'Nama': 'Sundari', 'Profesi/Usaha': 'Pensiun', 'Tipe No': 'Pribadi', 'Alamat': 'Dago'},
        '085174333541': {'Nama': 'Faisal', 'Profesi/Usaha': 'Freelance', 'Tipe No': 'Pribadi', 'Alamat': 'Sarikaso'},
        '08001835566': {'Nama': 'Telkom', 'Profesi/Usaha': 'IT', 'Tipe No': 'Call Center', 'Alamat': 'Gegarkalong'},
        '08118414000': {'Nama': 'Mandiri', 'Profesi/Usaha': 'Bank', 'Tipe No': 'Call Center', 'Alamat': 'Asia Afrika'},
        '14040': {'Nama': 'BSI', 'Profesi/Usaha': 'Bank', 'Tipe No': 'Call Center', 'Alamat': 'Asia Afrika'}
    }

while True:
    display_menu()
    choice = input('Silahkan Pilih: ')
    if choice == '1':
        display_contacts(contacts)
    elif choice == '2':
        search_contact(contacts)
    elif choice == '3':
        print('''
        1. Menambah
        2. Mengedit
        3. Menghapus
        4. Kembali ke menu utama
        ''')
        choice1 = input('Silahkan Pilih: ')
        if choice1 == '1':
            add_contact(contacts)
        elif choice1 == '2':
            edit_contact(contacts)
        elif choice1 == '3':
            delete_contact(contacts)
        elif choice1 == '4':
            continue
        else:
            print('Pilihan Anda Invalid.')
    elif choice == '4':
        print(f"{'TERIMA KASIH':^50}")
        break
    elif choice == '5':
        num_contacts = int(input("Masukkan jumlah kontak acak yang ingin ditambahkan: "))
        add_random_contacts(contacts, num_contacts)
        print(f"{num_contacts} kontak acak berhasil ditambahkan.")
    else:
        print('Pilihan Anda Invalid.')