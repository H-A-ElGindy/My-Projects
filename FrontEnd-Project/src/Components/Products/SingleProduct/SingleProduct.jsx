import  { useEffect, useState } from 'react'
import { useParams } from "react-router-dom";
import axios from "axios"
import"../SingleProduct/SingleProduct.css"

const SingleProduct = () => {
  const [product,Setproduct]=useState({})
  const {id}= useParams()
  
  useEffect(()=>{
    async function fetchProduct(){
      try {
        const resp= await axios.get(`https://fakestoreapi.com/products/${id}`)
        console.log(resp.data)
        Setproduct(resp.data)

        
      } catch (error) {
        console.log(error)
      }
    }
    fetchProduct()
  },[id])

  const [cartItems,setCartItems]=useState(JSON.parse(localStorage.getItem('cart'))||[])
    
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
    <div className="product-detail">
      <div className="image-container">
        <img src={product.image} alt={product} />
        <Link to={'/cart'}>
          <button onClick={()=>{Additem(product)}}>Add To Cart</button>
        </Link>
      </div>
      <div className="text-container">
        <h1>{product.title}</h1>
        <p>{product.description}</p>
        <h4>Price: ${product.price}</h4>
        <div className="rating-container">
          <h4 id='rate'>Rate: {product?.rating?.rate}⭐</h4>
          <h4 id='votes'>Votes: {product?.rating?.count}</h4>
        </div>
        
      </div>
      
    </div>
  )
}

export default SingleProduct