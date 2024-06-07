import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';
import { OffersListComponent } from './views/offers-list/offers-list.component';
import { NavbarComponent } from './views/navbar/navbar.component';

@NgModule({
  declarations: [
    AppComponent,
    OffersListComponent,
    NavbarComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
