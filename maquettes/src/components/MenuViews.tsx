import { useState } from "react";
import { motion } from "framer-motion";
import { Plus, Minus } from "lucide-react";
import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from "@/components/ui/accordion";
import { MenuItem, CATEGORIES, MENU } from "@/data/menu";
import { useCart } from "@/contexts/CartContext";
import { toast } from "sonner";

function QtyControl({ item }: { item: MenuItem }) {
  const { items, add, inc, dec } = useCart();
  const current = items.find((i) => i.id === item.id);
  const qty = current?.quantity ?? 0;

  if (qty === 0) {
    return (
      <button
        data-testid={`menu-add-${item.id}`}
        onClick={() => {
          add({
            id: item.id,
            name: item.name,
            price: item.price,
            image: item.image,
          });
          toast.success(`${item.name} ajouté`);
        }}
        className="inline-flex items-center gap-1.5 text-xs px-3 py-1.5 rounded-full border border-subtle hover:border-strong hover:bg-base transition-all"
      >
        <Plus className="h-3 w-3" />
        Ajouter
      </button>
    );
  }
  return (
    <div className="inline-flex items-center gap-1 border border-strong rounded-full">
      <button
        onClick={() => dec(item.id)}
        className="p-1.5 hover:opacity-70"
        data-testid={`menu-dec-${item.id}`}
        aria-label="Decrease"
      >
        <Minus className="h-3 w-3" />
      </button>
      <span className="text-xs px-2 min-w-[1.25rem] text-center">{qty}</span>
      <button
        onClick={() => inc(item.id)}
        className="p-1.5 hover:opacity-70"
        data-testid={`menu-inc-${item.id}`}
        aria-label="Increase"
      >
        <Plus className="h-3 w-3" />
      </button>
    </div>
  );
}

export function MenuByCategory() {
  const [openCat, setOpenCat] = useState<string>(CATEGORIES[0]);

  return (
    <Accordion
      type="single"
      value={openCat}
      onValueChange={setOpenCat}
      className="w-full"
      data-testid="menu-by-category"
    >
      {CATEGORIES.map((cat) => {
        const items = MENU.filter((m) => m.category === cat);
        return (
          <AccordionItem
            key={cat}
            value={cat}
            className="border-b border-subtle"
          >
            <AccordionTrigger
              data-testid={`menu-cat-${cat}`}
              className="py-8 hover:no-underline group"
            >
              <div className="flex items-baseline gap-6">
                <span className="text-sm text-soft-app font-body tabular-nums">
                  0{CATEGORIES.indexOf(cat) + 1}
                </span>
                <span className="font-display text-3xl sm:text-4xl tracking-tight text-primary-app">
                  {cat}
                </span>
                <span className="text-xs text-muted-app">
                  · {items.length} plats
                </span>
              </div>
            </AccordionTrigger>
            <AccordionContent>
              <div className="grid md:grid-cols-2 gap-6 pb-8">
                {items.map((item, idx) => (
                  <motion.div
                    key={item.id}
                    initial={{ opacity: 0, y: 16 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ duration: 0.4, delay: idx * 0.05 }}
                    data-testid={`menu-item-${item.id}`}
                    className="flex gap-4 group"
                  >
                    <img
                      src={item.image}
                      alt={item.name}
                      loading="lazy"
                      className="img-luxe w-24 h-24 sm:w-28 sm:h-28 object-cover rounded-md shrink-0"
                    />
                    <div className="flex-1 min-w-0">
                      <div className="flex items-baseline justify-between gap-3 mb-1">
                        <h4 className="font-display text-lg text-primary-app leading-snug">
                          {item.name}
                        </h4>
                        <span className="text-sm text-muted-app shrink-0 tabular-nums">
                          {item.price} €
                        </span>
                      </div>
                      <p className="text-sm text-muted-app leading-relaxed mb-3 line-clamp-2">
                        {item.description}
                      </p>
                      <QtyControl item={item} />
                    </div>
                  </motion.div>
                ))}
              </div>
            </AccordionContent>
          </AccordionItem>
        );
      })}
    </Accordion>
  );
}

export function MenuByDish() {
  return (
    <div
      data-testid="menu-by-dish"
      className="grid md:grid-cols-2 lg:grid-cols-3 gap-6 md:gap-8"
    >
      {MENU.map((item, idx) => (
        <motion.article
          key={item.id}
          initial={{ opacity: 0, y: 24 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, margin: "-50px" }}
          transition={{ duration: 0.5, delay: (idx % 6) * 0.05 }}
          data-testid={`menu-dish-card-${item.id}`}
          className="group bg-surface border border-subtle rounded-lg overflow-hidden flex flex-col hover-lift"
        >
          <div className="relative aspect-[4/3] overflow-hidden">
            <img
              src={item.image}
              alt={item.name}
              loading="lazy"
              className="img-luxe w-full h-full object-cover transition-transform duration-[1200ms] group-hover:scale-[1.05]"
            />
            {item.signature && (
              <span className="absolute top-3 left-3 text-[10px] tracking-[0.25em] uppercase bg-white/95 text-black px-2.5 py-1 rounded-full">
                Signature
              </span>
            )}
            <span className="absolute top-3 right-3 text-[10px] tracking-wider uppercase bg-black/60 text-white px-2.5 py-1 rounded-full backdrop-blur">
              {item.category}
            </span>
          </div>
          <div className="p-5 flex-1 flex flex-col">
            <div className="flex items-baseline justify-between gap-3 mb-2">
              <h4 className="font-display text-xl text-primary-app">
                {item.name}
              </h4>
              <span className="text-base text-primary-app shrink-0 tabular-nums">
                {item.price} €
              </span>
            </div>
            <p className="text-sm text-muted-app leading-relaxed mb-4 line-clamp-3">
              {item.description}
            </p>

            <div className="space-y-2 mb-5 text-xs">
              <p>
                <span className="text-soft-app">Ingrédients · </span>
                <span className="text-muted-app">
                  {item.ingredients.join(", ")}
                </span>
              </p>
              {item.allergens.length > 0 && (
                <p>
                  <span className="text-soft-app">Allergènes · </span>
                  <span className="text-muted-app">
                    {item.allergens.join(", ")}
                  </span>
                </p>
              )}
            </div>

            <div className="mt-auto pt-4 border-t border-subtle">
              <QtyControl item={item} />
            </div>
          </div>
        </motion.article>
      ))}
    </div>
  );
}
