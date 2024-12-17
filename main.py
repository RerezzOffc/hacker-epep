import time
import random
import string

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

# Fungsi utama untuk menampilkan "code" selama 5 detik
def display_code_and_change():
    # Tampilkan code selama 5 detik
    print("[*] Generating code... (Hold on!)")
    start_time = time.time()
    while time.time() - start_time < 5:
        print("Code running... ████████████", end="\r")
        time.sleep(0.1)  # Update setiap 0.1 detik
    
    # Setelah 5 detik, tampilkan email dan password acak
    print("\n[*] Generating random email and password...")
    email = generate_random_email()
    password = generate_random_password()

    print(f"Email: {email}")
    print(f"Password: {password}")

# Jalankan fungsi utama
if __name__ == "__main__":
    display_code_and_change()
