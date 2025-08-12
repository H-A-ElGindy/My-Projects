import { useEffect, useState } from 'react'
import axios from "axios"
import ProductCard from './ProductCard/ProductCard'
import "../AllProducts/Products.css"


const Products = () => {
  
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
    <div className="products-container">
      {products.map((product)=>(<ProductCard key={product.id} product={product} Additem={Additem}/>))}
    </div>
  )
}

export default Products