import json
import os
from datetime import datetime

class TaskManager:
    def __init__(self):
        self.data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
        self.tasks_file = os.path.join(self.data_dir, 'tasks.json')
        
        # Veri dizinini oluştur
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
        
        # Veri dosyasını kontrol et, yoksa oluştur
        if not os.path.exists(self.tasks_file):
            with open(self.tasks_file, 'w', encoding='utf-8') as f:
                json.dump([], f, ensure_ascii=False)
    
    def _load_tasks(self):
        try:
            with open(self.tasks_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []
    
    def _save_tasks(self, tasks):
        with open(self.tasks_file, 'w', encoding='utf-8') as f:
            json.dump(tasks, f, ensure_ascii=False, indent=2)
    
    def add_task(self, title, description):
        tasks = self._load_tasks()
        
        # Task ID'sini belirle
        task_id = 1
        if tasks:
            task_id = max(task['id'] for task in tasks) + 1
        
        # Yeni görevi oluştur
        new_task = {
            'id': task_id,
            'title': title,
            'description': description,
            'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'status': 'Tamamlanmadı'
        }
        
        tasks.append(new_task)
        self._save_tasks(tasks)
        print(f"Görev başarıyla eklendi! ID: {task_id}")
    
    def list_tasks(self):
        tasks = self._load_tasks()
        
        if not tasks:
            print("Hiç görev bulunmamaktadır.")
            return
        
        print("\n--- GÖREVLER ---")
        for task in tasks:
            print(f"ID: {task['id']}")
            print(f"Başlık: {task['title']}")
            print(f"Açıklama: {task['description']}")
            print(f"Durum: {task['status']}")
            print(f"Oluşturulma Tarihi: {task['created_at']}")
            print("-" * 30)
    
    def update_task(self, task_id, new_title=None, new_description=None):
        tasks = self._load_tasks()
        
        # Görevi bul
        for task in tasks:
            if task['id'] == task_id:
                if new_title:
                    task['title'] = new_title
                if new_description:
                    task['description'] = new_description
                
                self._save_tasks(tasks)
                print(f"Görev {task_id} başarıyla güncellendi!")
                return
        
        print(f"ID {task_id} olan görev bulunamadı!")
    
    def delete_task(self, task_id):
        tasks = self._load_tasks()
        
        # Görevin mevcut olup olmadığını kontrol et
        task_found = any(task['id'] == task_id for task in tasks)
        
        if task_found:
            tasks = [task for task in tasks if task['id'] != task_id]
            self._save_tasks(tasks)
            print(f"Görev {task_id} başarıyla silindi!")
        else:
            print(f"ID {task_id} olan görev bulunamadı!")
            
    def change_task_status(self, task_id):
        """Görevin durumunu 'Tamamlandı' ve 'Tamamlanmadı' arasında değiştirir."""
        tasks = self._load_tasks()
        
        # Görevi bul
        for task in tasks:
            if task['id'] == task_id:
                # Durumu değiştir
                if task['status'] == 'Tamamlandı':
                    task['status'] = 'Tamamlanmadı'
                else:
                    task['status'] = 'Tamamlandı'
                
                self._save_tasks(tasks)
                print(f"Görev {task_id} durumu '{task['status']}' olarak güncellendi!")
                return
        
        print(f"ID {task_id} olan görev bulunamadı!")