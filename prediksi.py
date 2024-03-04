import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import numpy as np

# Load data dari file CSV
alumni_data = pd.read_csv('alumni_data.csv')
siswa_data = pd.read_csv('siswa_data.csv')

# Skala prioritas data
prioritas_data = ['prestasi_olimpiade', 'minat_jurusan', 'nilai_ujian_sekolah', 'nilai_ujian_nasional', 'nilai_rapor', 'aktivitas_ekstrakurikuler']

# Konversi kolom string menjadi numerik
le = preprocessing.LabelEncoder()
for feature in prioritas_data:
    alumni_data[feature] = le.fit_transform(alumni_data[feature])
    siswa_data[feature] = le.transform(siswa_data[feature])

# Pisahkan data latih dan data uji
train_data, test_data, train_labels, test_labels = train_test_split(alumni_data[prioritas_data], alumni_data['sekolah_sma'], test_size=0.2, random_state=42)

# Inisialisasi model Naive Bayes
model = GaussianNB()

# Latih model
model.fit(train_data, train_labels)

# Prediksi dengan model
predictions = model.predict(test_data)

# Evaluasi model
accuracy = accuracy_score(test_labels, predictions)
print(f'Akurasi model: {accuracy:.2f}')

# Gunakan model untuk prediksi siswa
siswa_predictions = model.predict(siswa_data[prioritas_data])
siswa_probabilities = model.predict_proba(siswa_data[prioritas_data])

# Tambahkan hasil prediksi dan probabilitas ke dalam data siswa
siswa_data['predicted_sekolah_sma'] = siswa_predictions
siswa_data['probabilitas_diterima'] = np.max(siswa_probabilities, axis=1)

# Simpan hasil prediksi dan probabilitas ke dalam file CSV
siswa_data.to_csv('hasil_prediksi_siswa.csv', index=False)

# Tampilkan visualisasi probabilitas
plt.figure(figsize=(12, 6))
plt.scatter(siswa_data.index, siswa_data['probabilitas_diterima'], c='blue', label='Probabilitas Diterima')
plt.title('Probabilitas Diterima Siswa di SMA')
plt.xlabel('Index Siswa')
plt.ylabel('Probabilitas Diterima')
plt.legend()
plt.show()
