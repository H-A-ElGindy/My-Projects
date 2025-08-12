
import { useState } from 'react'

const CartCard = ({item,remove_item,increment,decrement}) => {
    
    
    return (
    <>
    <hr />
    <div className="cart-container">
        <div className="item-container">
            <div className="img-container">
                <img src={item.image} alt={item.id} />
            </div>
            <div className="text-container">
                <div className="title-container">
                    <h3>{item.title}</h3>
                    <h4>${item.price * item.quantity}</h4>
                </div>
                <div className="description-container">
                    <p>{item.description}</p>
                    <p id='price'>Price: ${item.price}</p>
                    <div className="qty-container">
                        <span> 
                            {item.quantity>1?<button onClick={()=>decrement(item)}>-</button>:<button id='close' onClick={()=>decrement(item)}>❌</button>}
                            <span id='qty'>{item.quantity}</span>
                            <button onClick={()=>increment(item)}>+</button>
                        </span>   
                    </div>
                    <button id='remove' onClick={()=>remove_item(item.id)}>Remove Item</button> 
                </div>
            </div>
        </div>
        
       
    </div>
    </>
  )
}

export default CartCard