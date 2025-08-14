import React from 'react'
import "../Home/Home.css"
import 'bootstrap/dist/css/bootstrap.min.css'
import Carousel from "react-bootstrap/Carousel";
import { useEffect, useState } from 'react'
import axios from "axios"
import ProductCard from '../Products/AllProducts/ProductCard/ProductCard'
import "../Products/AllProducts/ProductCard/ProductCard.css"
import { Link } from 'react-router-dom'



const Home = () => {
  const [products,Setproducts]=useState([])
  useEffect(()=>{
    
    async function fetchProducts(){
      try {
        const resp= await axios.get('https://fakestoreapi.com/products')
        Setproducts(resp.data)
      
      } catch (error) {
        console.log(error)
      }
    }
    fetchProducts()
  
  },[])
  
  
  const show_products=[products[13],products[6],products[16]]
  localStorage.setItem('show',JSON.stringify(show_products))
  const show=JSON.parse(localStorage.getItem('show')||[])

  const latest=products.slice(-10)


  const [cartItems,setCartItems]=useState(JSON.parse(localStorage.getItem('cart'))||[])

  // AI Adds item quantity by 1 if exists and if not creates a new one with quantity=1
  const Additem=(productToAdd)=>{
    setCartItems((previtems)=>{const existing= previtems.find((item)=> item.id===productToAdd.id)
      if (existing){          
        return previtems.map((item) => item.id===productToAdd.id ?{...item, quantity: item.quantity + 1}:item)
      }
      
      else{
        return [...previtems ,{...productToAdd, quantity:1}]
      }
    })
            
  }
  localStorage.setItem('cart',JSON.stringify(cartItems))
 
  
  return (
    <>
    <div className="home-container">
      <Carousel className="slider-container">
        <Carousel.Item className="carousel-container">
          <div className="img-container">
            <img src={show[0]?.image} className="carousel-image" alt="Electronics" />
            <div className="shop-container">
              <h1>Electronics</h1>
              <Link to={'/products'}>
                <button>Shop Now</button>
              </Link>
            </div>
          </div>
          
        </Carousel.Item>

        <Carousel.Item className="carousel-container">
          <div className="img-container">
            <img src={show[1]?.image} className="carousel-image" alt="Jewelery" />
            <div className="shop-container">
              <h1>Jewelery</h1>
              <Link to={'/products'}>
                <button>Shop Now</button>
              </Link>
            </div>
            
          </div>
         </Carousel.Item>

         <Carousel.Item className="carousel-container">
          <div className="img-container">
            <img src={show[2]?.image} className="carousel-image" alt="Clothes" />
            <div className="shop-container">
              <h1>Clothes</h1>
              <Link to={'/products'}>
                <button>Shop Now</button>
              </Link>
            </div>
            
          </div>
         </Carousel.Item>
         
      </Carousel>
    </div>
    <div className="latest-text">
      <h1>Latest Products</h1>
    </div>
    <div className="latest-container">
      
      {latest.map((product)=>(<ProductCard key={product.id} product={product} Additem={Additem}/>))}

    </div>
    </>
    
    
    
  );
};

export default Home;

