import {Component, HostListener} from '@angular/core';
import {OfferService} from "../../services/offer.service";

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent {
  navfixed:boolean = false;
  loading: boolean = false;
  constructor(private service: OfferService) {
  }
  @HostListener('window:scroll',['$event']) onscroll(){
    if(window.scrollY>100){
      this.navfixed = true;
    }
    else {
      this.navfixed = false;
    }
  }

  reload() {
    this.loading = true;
    this.service.reloadDb().subscribe( s =>{
      let holder = s;
      this.loading = false;
      window.location.reload();
    })
  }
}
