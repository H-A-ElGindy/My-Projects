import { Link,NavLink  } from "react-router-dom"
import "./Navbar.css"
import {Links} from "../Constants/Links"
import compare from "../../assets/compare.png"
import bigcart from "../../assets/bigcart.png"
import menu from "../../assets/menu.png"
import close from "../../assets/close.png"
import {  useEffect, useState } from "react"




const Navbar = () => {
    
  
    // To Sync number of items in cart 
    const [cartCount, setCartCount] = useState(() => {
    const cart = JSON.parse(localStorage.getItem('cart') || []);
    return cart.length;
    });


    useEffect(() => {
    const updateCartCount = () => {
    const cart = JSON.parse(localStorage.getItem('cart') || []);
    setCartCount(cart.length);
  };

  // For changes within the same tab (e.g., adding to cart)
    const overrideLocalStorage = () => {
        const originalSetItem = localStorage.setItem;
        localStorage.setItem = function (key, value) {
        originalSetItem.apply(this, arguments);
        if (key === 'cart') {
         window.dispatchEvent(new Event('cartUpdated'));
        }
        };
    };

    overrideLocalStorage();
    window.addEventListener('cartUpdated', updateCartCount);

  // For changes from other tabs
    window.addEventListener('storage', updateCartCount);

    return () => {
        window.removeEventListener('cartUpdated', updateCartCount);
        window.removeEventListener('storage', updateCartCount);
    };
    }, []);

    // for nav bar countriies and links for small screen
    const[links,setLinks]=useState(false)
    const[active,setactive]=useState(false)
    
    const countries=[{label:"France",value:"France"},{label:'United Kingdom' , value:'United Kingdom'},{label:'United States',value:'United States'}]
    const[selectedcountry,setCountry]=useState(countries[0].value)
    const [visible,Setvisible]=useState(false)

    function changeCountry(countryValue){
        setCountry(countryValue)
        Setvisible(false)
    }

    function toggleCountry(){
        Setvisible(visible=>!visible)
    }
    
    function toggleLinks(){
        setLinks(links=>!links)
        setactive(!active)
       
    }

    function ShowLinks(){
        return(
        Links.map((item, index) => (
            <li key={index} className="dropdown-item">
                <NavLink to={`/${item.to}`} >
                    {item.value}
                </NavLink>
            </li> ))) 
    }
    
    return (
    
    <div className="nav-container">
        <nav>
            <div className="upper-nav">
                <div className="upper-right-nav">
                    <div className="country-select">
                        <span className="country-selector" onClick={toggleCountry} >{selectedcountry} <img width="10" height="10" src="https://img.icons8.com/ios-filled/50/expand-arrow--v1.png" alt="expand-arrow--v1"/></span>
                        <div className="country-container">
                            {visible &&
                                (<ul name="selected-country" id="selected-country" className="selected-country">

                                    {countries.map((country,index)=>(<li key={index} onClick={()=>changeCountry(country.value)} value={country.value}>{country.label} </li>))} 
              
                                </ul>)
                            }
                        </div>      
                    </div>
                    <div className="currency-select">
                        <select name="selected-currency" className="selected-currency" id="selected-currency">
                            <option value="EUR">EUR</option>
                            <option value="GBR">GBR</option>
                            <option value="USD">USD</option>
                        </select>
                    </div>
                    <span>📱123-456-7890</span>
                </div>
                <div className="upper-left-nav">
                    <span className="compare"><img src={compare} width={20} height={20} alt="compare" /> Compare</span>
                    <span className="wish">❤️ Wishlist</span>
                    <Link to={'/login'}>👤 Login</Link>
                </div>
            </div>
            <hr />
            <div className="lower-nav">
                <div className="brand-title">
                    <img src={bigcart} width={50} height={50} alt="bigcart" />
                    <h1>Shopwise</h1>
                </div>
                
                {/* main screen pages routing */}
                
                <div className="pages-routing">
                    {Links.map((item, index) => (
                    <NavLink to={`/${item.to}`} key={index}>
                        {item.value}
                    </NavLink>
                    ))}
                </div>
                
                
                <div className="search-cart-container">
                    <div className="search-container">
                        <img width="25" height="25" src="https://img.icons8.com/ios-glyphs/30/search--v1.png" alt="search--v1"/>
                    </div>
                    
                    <div className="cart-container">
                        <Link to={'/cart'}>
                            <img width="30" height="30" src="https://img.icons8.com/3d-fluency/94/shopping-cart-loaded.png" alt="shopping-cart-loaded"/>
                            <span id='num'>{cartCount}</span>
                        </Link>

                    </div>
                    
                    {/* small screen pages routing */}
                
                    <div className="pages-routing-2" >
                        <ul className="menu">
                            <li className="dropdown">
                                <button onClick={toggleLinks}>{active? <img src={close} width={20} height={20} alt="" />:<img src={menu} width={20} height={20} alt="" />}</button>
                                {links && (
                                    <ul className="linkslist">
                                        <ShowLinks/>
                                    </ul>   
                                    )     
                                }
                            </li> 
                        </ul>          
                    </div>
                </div>
            </div>
        </nav> 
    </div>
  )
}

export default Navbar