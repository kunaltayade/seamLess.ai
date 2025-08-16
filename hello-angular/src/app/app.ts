import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  protected readonly title = signal('hello-angular');
  message = '';
  constructor(private http: HttpClient) {}
  callMicroservice() {
    this.http.get<any>('http://localhost:5000/api/hello').subscribe(data => {
      this.message = data.message;
    });
  }
}
