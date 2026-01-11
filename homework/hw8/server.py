
import json
import os
from http.server import HTTPServer, BaseHTTPRequestHandler

DATA_FILE = "tasks.txt"

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()
    
    def load_tasks(self):
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, 'r') as f:
                    self.tasks = json.load(f)
            except:
                self.tasks = []
        else:
            self.tasks = []
    
    def save_tasks(self):
        with open(DATA_FILE, 'w') as f:
            json.dump(self.tasks, f, ensure_ascii=False, indent=2)
    
    def add_task(self, title, priority):
        new_task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "priority": priority,
            "isDone": False
        }
        self.tasks.append(new_task)
        self.save_tasks()
        return new_task
    
    def get_all_tasks(self):
        return self.tasks
    
    def complete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["isDone"] = True
                self.save_tasks()
                return True
        return False

class TaskHandler(BaseHTTPRequestHandler):  
    task_manager = TaskManager()

    def send_json(self, data, status_code=200):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data, ensure_ascii=False).encode('utf-8'))
    
    def send_error_response(self, message, status_code=400):
        error_data = {"error": message}
        self.send_json(error_data, status_code)
    
    def do_GET(self):
        if self.path == '/tasks':
            tasks = self.task_manager.get_all_tasks()
            self.send_json(tasks)
        else:
            self.send_error_response("Страница не найдена", 404)
    
    def do_POST(self):
        if self.path == '/tasks':
            try:
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length)
                data = json.loads(post_data.decode('utf-8'))
                title = data.get('title')
                priority = data.get('priority')

                if not title or not priority:
                    self.send_error_response("Нужны title и priority")
                    return
                
                if priority not in ['low', 'normal', 'high']:
                    self.send_error_response("Приоритет должен быть: low, normal или high")
                    return
                
                task = self.task_manager.add_task(title, priority)
                self.send_json(task, 201)
                
            except json.JSONDecodeError:
                self.send_error_response("Неверный JSON формат")
            except Exception as e:
                self.send_error_response(f"Ошибка: {str(e)}")
        
        elif self.path.startswith('/tasks/') and self.path.endswith('/complete'):
            try:
                parts = self.path.split('/')
                task_id = int(parts[2])  # parts = ['', 'tasks', '123', 'complete']
                
                if self.task_manager.complete_task(task_id):
                    self.send_response(200)
                    self.end_headers()
                    self.wfile.write(b'') 
                else:
                    self.send_error_response("Задача не найдена", 404)
                    
            except (ValueError, IndexError):
                self.send_error_response("Неверный ID задачи", 400)
        
        else:
            self.send_error_response("Страница не найдена", 404)
    
    def log_message(self, format, *args):
        print(f"{self.address_string()} - {format % args}")

def run_server():
    port = 8000
    server = HTTPServer(('localhost', port), TaskHandler)
    print('Server is started')
    print('http://localhost:8000/tasks')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nСервер остановлен")
        server.server_close()

if __name__ == '__main__':
    run_server()