import React, {createContext, useState,useEffect, } from 'react'
import "../Cart/Cart.css"
import CartCard from './CartCard'



const Cart = () => {


  const[cartItems,setCartItems]=useState(JSON.parse(localStorage.getItem('cart'))||[])
    
  let total=0
  let total_qty=0
  
  // AI to get total price
  if (cartItems){
    total=cartItems.reduce((accumulator, currentItem) => {
    return accumulator + (currentItem.price * currentItem.quantity);
    }, 0);

    // modified with previous function to get total quantity
    total_qty=cartItems.reduce((accumulator, currentItem) => {
    return accumulator + (currentItem.quantity);
    }, 0);
  }

  useEffect(()=>{
    function getitems(){
      JSON.parse(localStorage.getItem('cart'))||[]
    }
    getitems()
  },[cartItems])
 
  // clears all cart items
  function clearCart(){
    localStorage.clear()
    setCartItems([])
    
  }

  // removes single item
  const remove_item=(id)=>{
    const updated_items=cartItems.filter(item=>item.id!==id)
    localStorage.setItem('cart', JSON.stringify(updated_items));
    setCartItems(updated_items)
  }

  // increases item quantity by 1 on Clicking + button
  const Increment=(productToincrement)=>{
    setCartItems((previtems)=> previtems.map((item) => item.id===productToincrement.id ?{...item, quantity: item.quantity + 1}:item))
         
  }
  localStorage.setItem('cart',JSON.stringify(cartItems))  
  

  // decreases item by 1 and also removes item that has quantity=0
  const Decrement = (productToDecrement) => {
  setCartItems((prevItems) => {
    const updatedItems = prevItems
      .map(item => {
        if (item.id === productToDecrement.id) {
          return { ...item, quantity: item.quantity - 1 };
        }
        return item;
      })
      .filter(item => item.quantity > 0); 

    localStorage.setItem('cart', JSON.stringify(updatedItems));
    return updatedItems;
  });
};

  return (
    <>
      <div className="cart-items">
        <h1>Shopping Cart</h1>
        
        {cartItems && cartItems.map((item)=>(item.quantity >=1 && <CartCard key={item.id} item={item} remove_item={remove_item} increment={Increment} decrement={Decrement}/>))}
        <hr />
        <div className="total">
          {cartItems.length>0? 
            <div className="summary-container">
              <div className="price">
                <h3>Total Price ({total_qty} items):</h3>
                <h3> ${total.toFixed(2)}</h3>
              </div>
              <div className="clear">
                <button onClick={clearCart} >Remove All Items</button>
              </div>
            </div>
            :<h4>Cart is empty</h4>
          }
          
        </div>
      </div>
      
      
    </>
  )
}

export default Cart