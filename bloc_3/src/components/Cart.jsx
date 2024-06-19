import React, { useContext } from 'react';
import { CartContext } from '../CartContext';
import 'bootstrap/dist/css/bootstrap.min.css';

const Cart = () => {
  const { cartItems, removeFromCart, getTotal } = useContext(CartContext);

  return (
    <div className="container mt-5">
      <h2 className="text-center mb-4">Panier</h2>
      {cartItems.length === 0 ? (
        <p className="text-center">Votre panier est vide.</p>
      ) : (
        <>
          <ul className="list-group mb-4">
            {cartItems.map((item) => (
              <li key={item.id} className="list-group-item d-flex justify-content-between align-items-center">
                <div>
                  <h5>{item.title}</h5>
                  <p>{item.price}</p>
                </div>
                <button
                  className="btn btn-danger btn-sm"
                  onClick={() => removeFromCart(item.id)}
                >
                  Retirer
                </button>
              </li>
            ))}
          </ul>
          <div className="text-right mb-4">
            <h4>Total : {getTotal()}€</h4>
          </div>
          <div className="text-center">
            <button className="btn btn-success">Payer</button>
          </div>
        </>
      )}
    </div>
  );
};

export default Cart;
