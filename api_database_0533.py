import requests
import mysql.connector

mydb = mysql.connector.connect(
	host ="localhost",
	user ="root",
	password="",
	database="db_akademik_0533"
	)

if mydb.is_connected():
	print("Open Connection is Successfull")

def write_db_api():
	url = 'https://api.abcfdab.cfd/students'
	response = requests.get(url)
	data = response.json()
	cursor = mydb.cursor()
	sql = '''INSERT INTO tbl_students_0533(id,nim,nama,jk,jurusan,alamat) VALUES (%s, %s, %s, %s, %s, %s )'''
	for i in data['data'] :
		val = (i['id'],i['nim'], i['nama'] ,i['jk'], i['jurusan'], i['alamat'])
		cursor.execute(sql, val)
		mydb.commit()	

def read_data():
	mycursor = mydb.cursor()
	sql = "SELECT * FROM tbl_students_0533"
	mycursor.execute(sql)
	myresult = mycursor.fetchall()
	if mycursor.rowcount == 0:
		print("Tidak Ada Data yang Ditampilkan")
	else:
		for data in myresult:
			print(data)

def read_data_limit():
	mycursor = mydb.cursor()
	baris = int(input("\nMasukkan Limit : "))
	mycursor.execute("SELECT * FROM tbl_students_0533")
	myresult = mycursor.fetchmany(baris)
	for x in myresult:
		print(x)

def read_nim():
	mycursor = mydb.cursor()
	nomor_mahasiswa = input('Masukan NIM :')
	sql = ("SELECT * FROM tbl_students_0533 WHERE nim LIKE %s")
	val = ("%{}%".format(nomor_mahasiswa),)
	mycursor.execute(sql, val)
	myresult = mycursor.fetchall()
	if mycursor.rowcount == 0:
		print("Tidak Ada Data yang Ditampilkan")
	else:
		for data in myresult:
			print(data)

if __name__ == '__main__':
	write_db_api()

	while True:
		print("")
		print("1. Tampilkan semua data")
		print("2. Tampilkan data berdasarkan limit")
		print("3. Tampilkan data berdasarkan NIM")
		print("4. Exit\n")
		menu = int(input("Masukan Pilihan Menu : "))
		if menu == 1 :
			read_data()
		if menu == 2 :
			read_data_limit()
		if menu == 3:
			read_nim()
		if menu == 4:
			break
		else :
			print('Pilihan yang Anda Masukkan Salah')