import {Component, OnInit} from '@angular/core';
import {OfferService} from "../../services/offer.service";
import {Offer} from "../../models/offer";

@Component({
  selector: 'app-offers-list',
  templateUrl: './offers-list.component.html',
  styleUrls: ['./offers-list.component.css']
})
export class OffersListComponent implements OnInit{
  offers: Offer[] = [];
  activeOffers: Offer[] = [];
  currentPage: number = 1;
  pagesCount: number = 0;
  limit: number = 10;
  pages: number[] = [];
  constructor(private service: OfferService) {
  }
  ngOnInit() {
    this.service.getOffers().subscribe(o => {
      this.offers=o
      this.pagesCount = Math.ceil(this.offers.length/this.limit)
      this.pages = this.range(1, this.pagesCount)
      this.set_active_offers(this.currentPage-1)
    });
  }

  range(start: number, end: number): number[]{
    return  [...Array(end).keys()].map(el => el + start)
  }

  change_page(page: number): void{
    this.currentPage = page;
    this.set_active_offers(this.currentPage-1)
    window.scroll({
      top: 0,
      left: 0,
      behavior: 'smooth'
    });
  }

  set_active_offers(page: number):void{
    let start = page*this.limit;
    let end = start+this.limit;
    console.log(start,end)
    this.activeOffers = this.offers.slice(start,end);
    console.log(this.activeOffers)
  }
}
