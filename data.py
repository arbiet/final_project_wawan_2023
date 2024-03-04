import random
import faker
import csv

fake = faker.Faker()

def generate_raw_student_data(num_students, in_kediri_probability=0.8):
    raw_student_data = []

    for _ in range(num_students):
        in_kediri = random.choices([True, False], weights=[in_kediri_probability, 1 - in_kediri_probability])[0]
        
        student = {
            'nama_siswa': fake.name(),
            'alamat_siswa': fake.address() if in_kediri else fake.address() + ' (luar Kota Kediri)',
            'nilai_rapor': int(round(random.uniform(7, 10))),
            'nilai_ujian_sekolah': random.randint(70, 100),
            'nilai_ujian_nasional': random.randint(60, 100),
            'aktivitas_ekstrakurikuler': random.choice(['sains', 'olahraga', 'seni']),
            'prestasi_olimpiade': random.choice([None, 'matematika', 'biologi', 'fisika']),
            'minat_jurusan': random.choice(['IPA', 'IPS', 'Bahasa']),
            'sekolah_asal': 'SMP Negeri 1 Kediri',
            'lokasi': 'Dalam Kota Kediri' if in_kediri else 'Luar Kota Kediri',
        }
        raw_student_data.append(student)

    return raw_student_data

def generate_raw_alumni_data(num_alumni):
    raw_alumni_data = []

    for _ in range(num_alumni):
        alumni = {
            'nama_siswa': fake.name(),
            'alamat_siswa': fake.address(),
            'nilai_rapor': int(round(random.uniform(7, 10))),
            'nilai_ujian_sekolah': random.randint(70, 100),
            'nilai_ujian_nasional': random.randint(60, 100),
            'aktivitas_ekstrakurikuler': random.choice(['sains', 'olahraga', 'seni']),
            'prestasi_olimpiade': random.choice([None, 'matematika', 'biologi', 'fisika']),
            'minat_jurusan': random.choice(['IPA', 'IPS', 'Bahasa']),
            'sekolah_asal': 'SMP Negeri 1 Kediri',
            'lokasi': 'Dalam Kota Kediri',
            'sekolah_sma': f'SMA {random.randint(1, 8)} Kota Kediri',
        }
        raw_alumni_data.append(alumni)

    return raw_alumni_data


def save_to_csv(data, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(data)

# Contoh penggunaan
num_students = 300
num_alumni = 900

raw_student_data = generate_raw_student_data(num_students)
raw_alumni_data = generate_raw_alumni_data(num_alumni)

# Tampilkan contoh data
print("Contoh Data Siswa Lulusan Sekarang:")
print(raw_student_data[:3])  # Tampilkan 3 siswa pertama
print("\nContoh Data Alumni yang Sudah Sekolah:")
print(raw_alumni_data[:3])  # Tampilkan 3 alumni pertama


# Simpan data ke dalam file CSV
save_to_csv(raw_student_data, 'siswa_data.csv')
save_to_csv(raw_alumni_data, 'alumni_data.csv')

print("Data telah disimpan dalam file CSV: siswa_data.csv dan alumni_data.csv")