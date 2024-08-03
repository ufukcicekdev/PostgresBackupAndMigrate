# PostgresBackupAndMigrate
Python ile PostgreSql de Backup Alma ve Migrate

Selamlar arkadaşlar,

Bu yazımda size Python ile PostgreSQL veritabanından yedek alma ve aldığımız yedeği yeni bir veritabanına nasıl taşıyacağımızdan bahsedeceğim. Çok uzun bir yazı olmayacak, kodun GitHub linkini de sizinle paylaşacağım. Oradan alıp inceleyebilirsiniz



Bağlantı Bilgileri

Kodun başında, PostgreSQL veritabanı bağlantı bilgileri tanımlanmıştır:

host: Veritabanının bulunduğu sunucunun adresi.port: Veritabanı sunucusunun kullandığı port numarası.dbname: Yedek almak istediğiniz veritabanının adı.username: Veritabanı kullanıcı adı.password: Veritabanı kullanıcı şifresi.backup_file: Yedeğin kaydedileceği dosyanın adı.



pg_dump Komutunun Oluşturulması

pg_dump komutunun oluşturulması için gerekli bilgileri birleştiriyoruz:

PGPASSWORD={password}: Parolayı çevre değişkeni olarak ayarlıyoruz.pg_dump: PostgreSQL'in yedek alma aracı.-h {host}: Veritabanı sunucusunun adresi.-p {port}: Veritabanı sunucusunun port numarası.-U {username}: Veritabanı kullanıcı adı.-d {dbname}: Yedek almak istediğimiz veritabanının adı.-F c: Yedek dosyasının formatı (custom).-b: Veritabanındaki büyük nesneleri de yedekle.



pg_dump Komutunu Çalıştırma

subprocess.run fonksiyonu ile pg_dump komutunu çalıştırıyoruz:

shell=True: Komutun bir shell içinde çalıştırılmasını sağlıyoruz.check=True: Komutun başarılı bir şekilde tamamlanıp tamamlanmadığını kontrol ediyoruz.Eğer komut başarısız olursa bir CalledProcessError hatası fırlatılır.

Bu kod, PostgreSQL veritabanının yedeğini alarak belirttiğiniz dosyaya kaydeder. pg_dump komutunu kullanarak veritabanını yedekler ve bir hata oluştuğunda bunu yakalayıp ekrana hata mesajı yazdırır.

Migrate



pg_restore Komutunun Oluşturulması

pg_restore komutunun oluşturulması için gerekli bilgileri birleştiriyoruz:

PGPASSWORD={password}: Parolayı çevre değişkeni olarak ayarlıyoruz.pg_restore: PostgreSQL'in yedek geri yükleme aracı.-h {host}: Hedef veritabanı sunucusunun adresi.-p {port}: Hedef veritabanı sunucusunun port numarası.-U {username}: Hedef veritabanı kullanıcı adı.-d {dbname}: Yedeği geri yüklemek istediğimiz veritabanının adı.-v: Daha ayrıntılı çıktı (verbose).{backup_file}: Geri yüklenecek yedek dosyasının adı.



pg_restore Komutunu Çalıştırma

subprocess.run fonksiyonu ile pg_restore komutunu çalıştırıyoruz:

shell=True: Komutun bir shell içinde çalıştırılmasını sağlıyoruz.check=True: Komutun başarılı bir şekilde tamamlanıp tamamlanmadığını kontrol ediyoruz. Eğer komut başarısız olursa bir CalledProcessError hatası fırlatılır.



Hata Yönetimi

Komutun çalıştırılması sırasında bir hata oluşursa, subprocess.CalledProcessError hatasını yakalayıp bir hata mesajı yazdırıyoruz.



Bu kod, bir PostgreSQL veritabanı yedeğini başka bir veritabanına geri yüklemek için pg_restore komutunu kullanır. pg_restore komutunu çalıştırarak yedeği hedef veritabanına geri yükler ve bir hata oluştuğunda bunu yakalayıp ekrana hata mesajı yazdırır.