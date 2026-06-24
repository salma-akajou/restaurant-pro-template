import { motion } from "framer-motion";
import { Link } from "react-router-dom";
import { Plus, ArrowRight } from "lucide-react";
import { MENU } from "@/data/menu";
import { useCart } from "@/contexts/CartContext";
import { toast } from "sonner";

export default function SignatureDishes() {
  const { add } = useCart();
  const signatures = MENU.filter((m) => m.signature).slice(0, 3);

  return (
    <section
      data-testid="signature-section"
      className="py-24 md:py-32 bg-base"
    >
      <div className="container-luxe">
        <div className="flex flex-col md:flex-row md:items-end justify-between gap-6 mb-14">
          <div>
            <p className="eyebrow">Signatures</p>
            <h2 className="mt-3 font-display text-4xl sm:text-5xl">
              Trois plats,
              <br />
              <span className="italic accent-color">trois obsessions.</span>
            </h2>
          </div>
          <Link
            to="/menu"
            className="text-sm text-muted-app hover:text-primary-app inline-flex items-center gap-2 group"
          >
            Voir la carte complète
            <ArrowRight className="h-4 w-4 group-hover:translate-x-1 transition-transform" />
          </Link>
        </div>

        <div className="grid md:grid-cols-3 gap-6 md:gap-8">
          {signatures.map((dish, idx) => (
            <motion.article
              key={dish.id}
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6, delay: idx * 0.1 }}
              data-testid={`signature-dish-${dish.id}`}
              className="group flex flex-col"
            >
              <div className="relative aspect-[4/5] overflow-hidden rounded-md mb-5">
                <img
                  src={dish.image}
                  alt={dish.name}
                  loading="lazy"
                  className="img-luxe w-full h-full object-cover transition-transform duration-[1200ms] group-hover:scale-[1.04]"
                />
                <div className="absolute top-4 left-4">
                  <span className="text-[10px] tracking-[0.3em] uppercase bg-white/90 text-black px-3 py-1.5 rounded-full backdrop-blur">
                    Signature
                  </span>
                </div>
              </div>
              <div className="flex justify-between items-baseline gap-4 mb-2">
                <h3 className="font-display text-2xl text-primary-app">
                  {dish.name}
                </h3>
                <span className="text-base text-muted-app shrink-0">
                  {dish.price} €
                </span>
              </div>
              <p className="text-muted-app text-sm leading-relaxed mb-4">
                {dish.description}
              </p>
              <button
                onClick={() => {
                  add({
                    id: dish.id,
                    name: dish.name,
                    price: dish.price,
                    image: dish.image,
                  });
                  toast.success(`${dish.name} ajouté au panier`);
                }}
                data-testid={`signature-add-${dish.id}`}
                className="mt-auto inline-flex items-center gap-2 text-sm text-primary-app hover:opacity-70 transition-opacity self-start"
              >
                <Plus className="h-4 w-4" />
                Ajouter au panier
              </button>
            </motion.article>
          ))}
        </div>
      </div>
    </section>
  );
}
