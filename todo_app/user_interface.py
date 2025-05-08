from .task_manager import TaskManager
from .utils import print_divider, clear_screen

def main():
    manager = TaskManager()
    print("Görev Takip Uygulamasına Hoş Geldiniz!")

    while True:
        print_divider()
        print("1. Görev Ekle")
        print("2. Görevleri Listele")
        print("3. Görev Güncelle")
        print("4. Görev Sil")
        print("5. Görev Durumunu Değiştir")
        print("6. Çıkış")
        
        choice = input("Bir seçenek girin: ")

        if choice == "1":
            title = input("Görev başlığı: ")
            description = input("Görev açıklaması: ")
            manager.add_task(title, description)
        
        elif choice == "2":
            manager.list_tasks()
        
        elif choice == "3":
            try:
                task_id = int(input("Güncellenecek görev ID'si: "))
                new_title = input("Yeni başlık (boş bırakılabilir): ")
                new_description = input("Yeni açıklama (boş bırakılabilir): ")
                manager.update_task(task_id, new_title or None, new_description or None)
            except ValueError:
                print("Geçersiz ID! Tam sayı değeri giriniz.")
        
        elif choice == "4":
            try:
                task_id = int(input("Silinecek görev ID'si: "))
                confirm = input(f"ID {task_id} olan görevi silmek istediğinize emin misiniz? (e/h): ")
                if confirm.lower() == 'e':
                    manager.delete_task(task_id)
                else:
                    print("Silme işlemi iptal edildi.")
            except ValueError:
                print("Geçersiz ID! Tam sayı değeri giriniz.")
        
        elif choice == "5":
            try:
                task_id = int(input("Durumu değiştirilecek görev ID'si: "))
                manager.change_task_status(task_id)
            except ValueError:
                print("Geçersiz ID! Tam sayı değeri giriniz.")
        
        elif choice == "6":
            print("Görev Takip Uygulamasından çıkılıyor...")
            break
        
        else:
            print("Geçersiz seçenek! Lütfen 1-6 arasında bir seçenek girin.")

        input("\nDevam etmek için Enter tuşuna basın...")


if __name__ == "__main__":
    main()