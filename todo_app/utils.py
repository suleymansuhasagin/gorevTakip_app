def print_divider():
    """Menü seçenekleri için ayırıcı çizgi yazdırır."""
    print("\n" + "=" * 40 + "\n")

def clear_screen():
    """Konsol ekranını temizler."""
    import os
    # İşletim sistemine göre ekranı temizle
    os.system('cls' if os.name == 'nt' else 'clear')