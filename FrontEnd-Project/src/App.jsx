
import './App.css'
import Navbar from './Components/Navbar/Navbar'
import { Routes,Route } from 'react-router-dom'
import Home from './Components/Home/Home'
import Products from './Components/Products/AllProducts/Products'
import SingleProduct from './Components/Products/SingleProduct/SingleProduct'
import NotFound from './Components/NotFound/NotFound'
import Cart from './Components/Cart/Cart'
import Login from './Components/Auth/Login'






function App() {
  

  return (
    
    <>
      
      <Navbar />

      <Routes>
        <Route path='/' Component={Home}/>
        <Route path='/login' Component={Login}/>
        <Route path='/products' Component={Products}/>
        <Route path='/product-details/:id' Component={SingleProduct}/>
        <Route path='/cart' Component={Cart} />
        <Route path='*' Component={NotFound}/>
      </Routes>

      
    </>
  )
}

export default App
