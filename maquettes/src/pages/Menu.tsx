import { useState } from "react";
import { motion } from "framer-motion";
import PageTransition from "@/components/PageTransition";
import { MenuByCategory, MenuByDish } from "@/components/MenuViews";
import { useCart } from "@/contexts/CartContext";

type View = "category" | "dish";

export default function MenuPage() {
  const [view, setView] = useState<View>("category");
  const { count, subtotal, open } = useCart();

  return (
    <PageTransition>
      {/* Hero banner */}
      <section className="relative h-[60vh] min-h-[400px] overflow-hidden flex items-end">
        <img
          src="https://images.unsplash.com/photo-1546964124-0cce460f38ef?w=1920&q=85"
          alt="Menu"
          className="absolute inset-0 w-full h-full object-cover"
        />
        <div className="absolute inset-0 bg-black/55" />
        <div className="relative z-10 container-luxe pb-16 text-white">
          <p className="text-xs tracking-[0.32em] uppercase mb-4 text-white/80">
            La Carte
          </p>
          <h1 className="font-display text-6xl sm:text-7xl tracking-tight">
            Le Menu
          </h1>
          <p className="mt-4 max-w-xl text-white/85">
            Saisonnalité, sourcing rigoureux, gestes précis. Une lecture en deux
            chapitres.
          </p>
        </div>
      </section>

      <section className="py-16 md:py-24 bg-base">
        <div className="container-luxe">
          {/* Tab switcher */}
          <div className="flex justify-center mb-14">
            <div
              data-testid="menu-view-switcher"
              className="inline-flex p-1 border border-subtle rounded-full bg-surface"
            >
              {(["category", "dish"] as const).map((v) => (
                <button
                  key={v}
                  data-testid={`menu-view-${v}`}
                  onClick={() => setView(v)}
                  className={`relative px-6 py-2.5 text-sm rounded-full transition-colors ${
                    view === v ? "text-white" : "text-muted-app"
                  }`}
                >
                  {view === v && (
                    <motion.div
                      layoutId="active-view"
                      className="absolute inset-0 rounded-full bg-primary-brand"
                      transition={{
                        type: "spring",
                        stiffness: 380,
                        damping: 30,
                      }}
                    />
                  )}
                  <span className="relative z-10">
                    {v === "category" ? "Par catégorie" : "Par plat"}
                  </span>
                </button>
              ))}
            </div>
          </div>

          <div className="grid lg:grid-cols-12 gap-12">
            <div className="lg:col-span-9">
              {view === "category" ? <MenuByCategory /> : <MenuByDish />}
            </div>

            {/* Sticky cart */}
            <aside className="hidden lg:block lg:col-span-3">
              <div
                data-testid="sticky-cart"
                className="sticky top-28 bg-surface border border-subtle rounded-2xl p-6"
              >
                <p className="eyebrow mb-3">Votre commande</p>
                <h3 className="font-display text-2xl mb-5">
                  {count} article{count !== 1 ? "s" : ""}
                </h3>
                <div className="flex items-baseline justify-between mb-5">
                  <span className="text-xs uppercase tracking-wider text-muted-app">
                    Sous-total
                  </span>
                  <span className="font-display text-2xl">
                    {subtotal.toFixed(2)} €
                  </span>
                </div>
                <button
                  onClick={open}
                  data-testid="sticky-cart-open"
                  disabled={count === 0}
                  className="w-full py-3 rounded-full text-sm tracking-wide transition-opacity disabled:opacity-40"
                  style={{
                    backgroundColor: "var(--color-primary)",
                    color: "var(--bg-surface)",
                  }}
                >
                  Voir le panier
                </button>
                <p className="mt-4 text-[11px] text-soft-app leading-relaxed">
                  Commandez via WhatsApp, Glovo ou Talabat depuis le panier.
                </p>
              </div>
            </aside>
          </div>
        </div>
      </section>
    </PageTransition>
  );
}
