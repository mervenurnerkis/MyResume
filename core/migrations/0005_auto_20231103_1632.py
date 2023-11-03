# Bu dosya düzeltilmiş migration işlemleri içermelidir.
# Eğer bu bir yeni migration dosyası ise dosya adı ve sınıf adı otomatik olarak oluşturulurken
# Django tarafından verilen isimlere göre düzenlenmelidir.

from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20231102_1730'),  # Burası önceki migration'a bağlı olmalıdır.
    ]

    operations = [
        # Eski migration işlemleri kaldırıldı.
        # Bu migration dosyası, esasında boş bir migration olarak görev yapacak
        # ve herhangi bir veritabanı değişikliği yapmayacak.
        # AbstractModel abstract olduğu için ve GeneralSetting ile ImageSetting
        # modelleri bu abstract modelden türetildiği için otomatik olarak gerekli alanlar oluşacaktır.
    ]
