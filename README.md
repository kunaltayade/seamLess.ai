# PythonFun

This is a basic Python project initialized in Visual Studio Code. You can start by creating Python scripts for automation, data analysis, or general scripting tasks.

## Getting Started
- Ensure you have Python installed on your system.
- Recommended extensions are already installed: Python, Python Environment Manager.
- Create your first script (e.g., `hello.py`) and run it using the VS Code Run button or the terminal.

## Example
```python
print("Hello, World!")
```

## Project Structure
- `.github/copilot-instructions.md`: Workspace-specific Copilot instructions.
- Add your Python files in the project root.

## How to Run
You can run any Python file by right-clicking and selecting 'Run Python File in Terminal' or using the Run button in the editor.

# Microservice & Angular Frontend Setup

## Python Microservice
- Run the backend:
```sh
/Users/kunaltayade/PythonFun/.venv/bin/python microservice.py
```

## Angular Frontend
1. Install Node.js if not already installed.
2. Run:
```sh
npm install -g @angular/cli
ng new hello-angular --defaults
cd hello-angular
ng generate component hello
```
3. Replace the contents of `src/app/hello/hello.component.ts` and `hello.component.html` as shown below.
4. Start the Angular app:
```sh
ng serve
```

## Angular Component Example
### hello.component.ts
```typescript
import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-hello',
  templateUrl: './hello.component.html'
})
export class HelloComponent implements OnInit {
  message = '';
  constructor(private http: HttpClient) {}
  ngOnInit() {
    this.http.get<any>('http://localhost:5000/api/hello').subscribe(data => {
      this.message = data.message;
    });
  }
}
```

### hello.component.html
```html
<h1>{{ message }}</h1>
```

---
- Ensure CORS is enabled in the Python backend (already set).
- The Angular app will display "Hello World" from the Python microservice.
