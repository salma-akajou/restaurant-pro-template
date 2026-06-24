import React, {
  createContext,
  useCallback,
  useContext,
  useEffect,
  useMemo,
  useReducer,
} from "react";

export type CartItem = {
  id: string;
  name: string;
  price: number;
  image?: string;
  quantity: number;
};

type CartState = {
  items: CartItem[];
  isOpen: boolean;
};

type CartAction =
  | { type: "ADD"; item: Omit<CartItem, "quantity">; quantity?: number }
  | { type: "REMOVE"; id: string }
  | { type: "INC"; id: string }
  | { type: "DEC"; id: string }
  | { type: "CLEAR" }
  | { type: "OPEN" }
  | { type: "CLOSE" }
  | { type: "HYDRATE"; items: CartItem[] };

const STORAGE_KEY = "restoflex.cart.v1";

function reducer(state: CartState, action: CartAction): CartState {
  switch (action.type) {
    case "ADD": {
      const qty = action.quantity ?? 1;
      const existing = state.items.find((i) => i.id === action.item.id);
      if (existing) {
        return {
          ...state,
          items: state.items.map((i) =>
            i.id === action.item.id ? { ...i, quantity: i.quantity + qty } : i
          ),
        };
      }
      return {
        ...state,
        items: [...state.items, { ...action.item, quantity: qty }],
      };
    }
    case "REMOVE":
      return { ...state, items: state.items.filter((i) => i.id !== action.id) };
    case "INC":
      return {
        ...state,
        items: state.items.map((i) =>
          i.id === action.id ? { ...i, quantity: i.quantity + 1 } : i
        ),
      };
    case "DEC":
      return {
        ...state,
        items: state.items
          .map((i) =>
            i.id === action.id ? { ...i, quantity: i.quantity - 1 } : i
          )
          .filter((i) => i.quantity > 0),
      };
    case "CLEAR":
      return { ...state, items: [] };
    case "OPEN":
      return { ...state, isOpen: true };
    case "CLOSE":
      return { ...state, isOpen: false };
    case "HYDRATE":
      return { ...state, items: action.items };
    default:
      return state;
  }
}

type CartContextValue = {
  items: CartItem[];
  isOpen: boolean;
  count: number;
  subtotal: number;
  add: (item: Omit<CartItem, "quantity">, quantity?: number) => void;
  remove: (id: string) => void;
  inc: (id: string) => void;
  dec: (id: string) => void;
  clear: () => void;
  open: () => void;
  close: () => void;
};

const CartContext = createContext<CartContextValue | null>(null);

export function CartProvider({ children }: { children: React.ReactNode }) {
  const [state, dispatch] = useReducer(reducer, { items: [], isOpen: false });

  useEffect(() => {
    try {
      const raw = localStorage.getItem(STORAGE_KEY);
      if (raw) {
        const items = JSON.parse(raw) as CartItem[];
        if (Array.isArray(items)) dispatch({ type: "HYDRATE", items });
      }
    } catch {}
  }, []);

  useEffect(() => {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(state.items));
    } catch {}
  }, [state.items]);

  const count = useMemo(
    () => state.items.reduce((s, i) => s + i.quantity, 0),
    [state.items]
  );
  const subtotal = useMemo(
    () => state.items.reduce((s, i) => s + i.quantity * i.price, 0),
    [state.items]
  );

  const value = useMemo<CartContextValue>(
    () => ({
      items: state.items,
      isOpen: state.isOpen,
      count,
      subtotal,
      add: (item, quantity) => dispatch({ type: "ADD", item, quantity }),
      remove: (id) => dispatch({ type: "REMOVE", id }),
      inc: (id) => dispatch({ type: "INC", id }),
      dec: (id) => dispatch({ type: "DEC", id }),
      clear: () => dispatch({ type: "CLEAR" }),
      open: () => dispatch({ type: "OPEN" }),
      close: () => dispatch({ type: "CLOSE" }),
    }),
    [state, count, subtotal]
  );

  return <CartContext.Provider value={value}>{children}</CartContext.Provider>;
}

export function useCart() {
  const ctx = useContext(CartContext);
  if (!ctx) throw new Error("useCart must be used within CartProvider");
  return ctx;
}

/* Helpers */
export const useWhatsAppOrder = () => {
  const { items, subtotal, clear } = useCart();
  return useCallback(
    (phone: string, brand: string) => {
      if (items.length === 0) return null;
      const lines = [
        `*Bonjour ${brand}* — Je souhaite passer commande :`,
        "",
        ...items.map(
          (i) =>
            `• ${i.quantity}× ${i.name}  —  ${(i.price * i.quantity).toFixed(2)} €`
        ),
        "",
        `*Total :* ${subtotal.toFixed(2)} €`,
        "",
        "Merci !",
      ];
      const msg = encodeURIComponent(lines.join("\n"));
      const cleanPhone = phone.replace(/[^\d]/g, "");
      const url = `https://wa.me/${cleanPhone}?text=${msg}`;
      clear();
      return url;
    },
    [items, subtotal, clear]
  );
};
