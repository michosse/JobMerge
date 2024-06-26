import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {Offer} from "../models/offer"

@Injectable({
  providedIn: 'root'
})
export class OfferService {
  constructor(private http: HttpClient) { }
  getOffers():Observable<Offer[]>{
    return this.http.get<Offer[]>('http://localhost:8000/api/offers');
  }
  reloadDb():Observable<any>{
    return this.http.put<any>('http://localhost:8000/api/reload',null);
  }
}
