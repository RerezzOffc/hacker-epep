import random
import string
import time

# Fungsi untuk menghasilkan password acak
def generate_random_password(length=10):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# Fungsi untuk menghasilkan email acak
def generate_random_email():
    domains = ["gmail.com", "yahoo.com", "outlook.com"]
    random_username = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10))
    random_domain = random.choice(domains)
    return f"{random_username}@{random_domain}"

# Fungsi untuk menampilkan akun secara terus-menerus di terminal dengan gaya
def display_accounts():
    while True:
        # Generate random email and password
        email = generate_random_email()
        password = generate_random_password()

        # Tampilkan akun dengan format yang diinginkan dan warna hijau
        print("\033[32m" + "╔━━[ DATA AKUN ]")
        print(f"┃ *[ ♙ ] Email : {email}")
        print(f"┃ *[ ⚿ ] Password : {password}")
        print("╚━━━━━━━━━━━━━❐" + "\033[0m")
        
        # Tunggu sejenak sebelum menampilkan akun berikutnya
        time.sleep(0.5)

# Jalankan fungsi utama
if __name__ == "__main__":
    display_accounts()
