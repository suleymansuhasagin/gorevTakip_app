# Görev Takip Uygulaması

Bu Python tabanlı komut satırı uygulaması, günlük görevlerinizi takip etmenize, yönetmenize ve organize etmenize yardımcı olur.

## Özellikler

- ✅ Görev ekleme
- 📋 Görevleri listeleme
- 🔄 Görev güncelleme
- 🗑️ Görev silme
- ✓ Görev durumunu değiştirme (Tamamlandı/Tamamlanmadı)
- 💾 Verileri JSON formatında saklama

## Kurulum

1. Repoyu klonlayın:
```bash
git clone https://github.com/suleymansuhasagin/gorevTakip_app.git
```

2. Proje dizinine gidin:
```bash
cd gorevTakip_app
```

## Kullanım

Uygulamayı çalıştırmak için:

```bash
python -m todo_app.user_interface
```

### Menü Seçenekleri

1. **Görev Ekle**: Yeni bir görev eklemek için başlık ve açıklama girin.
2. **Görevleri Listele**: Mevcut tüm görevlerinizi görüntüleyin.
3. **Görev Güncelle**: Mevcut bir görevin başlığını veya açıklamasını değiştirin.
4. **Görev Sil**: Bir görevi tamamen silin.
5. **Görev Durumunu Değiştir**: Görevin tamamlanma durumunu değiştirin.
6. **Çıkış**: Uygulamadan çıkın.

## Proje Yapısı

```
todo_app/
├── __init__.py
├── task_manager.py
├── utils.py
├── user_interface.py
└── data/
    └── tasks.json
```

- **task_manager.py**: Görevleri yönetmek için ana sınıfı içerir.
- **utils.py**: Yardımcı fonksiyonları içerir.
- **user_interface.py**: Komut satırı arayüzünü içerir.
- **data/tasks.json**: Görev verilerini saklar.

## Gereksinimler

- Python 3.6 veya üzeri

