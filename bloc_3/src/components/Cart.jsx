import React, { useContext } from "react";
import { CartContext } from "../CartContext";

const Cart = () => {
  const { cart, removeFromCart, clearCart } = useContext(CartContext);

  // Calcul du total des prix dans le panier
  const totalPrice = cart.reduce((total, item) => total + item.prix, 0);

  return (
    <div>
      <h2>Panier</h2>
      <ul className="list-group">
        {cart.map((item) => (
          <li key={item.cartId} className="list-group-item">
            <div>
              <strong>{item.titre}</strong> - {item.prix} €
              <button
                className="btn btn-danger btn-sm ms-3"
                onClick={() => removeFromCart(item.cartId)}
              >
                Supprimer
              </button>
            </div>
          </li>
        ))}
      </ul>
      {cart.length > 0 && (
        <div className="mt-3">
          <h4>Total : {totalPrice} €</h4>
          <button className="btn btn-primary me-3">Payer</button>
          <button
            className="btn btn-secondary"
            onClick={() => clearCart()}
          >
            Vider le panier
          </button>
        </div>
      )}
    </div>
  );
};

export default Cart;
