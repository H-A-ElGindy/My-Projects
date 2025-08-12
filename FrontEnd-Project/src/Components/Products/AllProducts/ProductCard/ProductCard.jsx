
import "../ProductCard/ProductCard.css"
import { Link } from 'react-router-dom'


const ProductCard = ({product,Additem}) => {
        
  return (
    <div className="product-card">
        
        <div className="img-container">
            <img src={product.image} alt={product.id} />
        </div>
        <div className="product-details">
            <div className="text-container">
                <h3>{product.title}</h3>
                <p>{product.description}</p>
            </div>
            
        </div>
        <div className="btn-price-rate-container">
            <div className="price-rate-container">
                <h4>Price: ${product.price}</h4>
                <h4>Rate: {product.rating.rate}⭐</h4>   
            </div>   

            <div className="btn-container">
                <Link to={`/product-details/${product.id}`}>
                    <button>Show Details</button>
                </Link>
                <Link to={'/cart'} >
                    <button onClick={()=>{Additem(product)}} >Add to Cart</button>
                </Link>
                
 
            </div>
        </div>
        
    </div>)
}

export default ProductCard