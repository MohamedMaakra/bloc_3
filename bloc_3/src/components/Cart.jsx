import React, { useContext } from "react";
import { CartContext } from "../CartContext";

const Cart = () => {
  const { cart, removeFromCart } = useContext(CartContext);

  return (
    <div>
      <h2>Panier</h2>
      <ul>
        {cart.map(item => (
          <li key={item.cartId}>
            {item.title} - {item.price}
            <button onClick={() => removeFromCart(item.cartId)}>Supprimer</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Cart;
