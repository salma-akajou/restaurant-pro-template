import {
  Sheet,
  SheetContent,
  SheetHeader,
  SheetTitle,
} from "@/components/ui/sheet";
import { Button } from "@/components/ui/button";
import { Minus, Plus, X, ShoppingBag } from "lucide-react";
import { useCart, useWhatsAppOrder } from "@/contexts/CartContext";
import { useI18n } from "@/contexts/I18nContext";
import { BRAND } from "@/data/brand";
import { toast } from "sonner";

export default function CartDrawer() {
  const { items, isOpen, close, inc, dec, remove, subtotal } = useCart();
  const { t } = useI18n();
  const generateWhatsApp = useWhatsAppOrder();

  const handleWhatsApp = () => {
    const url = generateWhatsApp(BRAND.whatsapp, BRAND.name);
    if (!url) {
      toast.error("Votre panier est vide.");
      return;
    }
    toast.success("Redirection vers WhatsApp…");
    window.open(url, "_blank", "noopener,noreferrer");
    close();
  };

  return (
    <Sheet open={isOpen} onOpenChange={(v) => !v && close()}>
      <SheetContent
        side="right"
        className="w-full sm:max-w-md flex flex-col p-0 bg-surface border-l border-subtle"
        data-testid="cart-drawer"
      >
        <SheetHeader className="px-6 py-5 border-b border-subtle">
          <SheetTitle className="font-display text-2xl text-primary-app text-left">
            {t("cart.title")}
          </SheetTitle>
        </SheetHeader>

        <div className="flex-1 overflow-y-auto px-6 py-4">
          {items.length === 0 ? (
            <div className="h-full flex flex-col items-center justify-center text-center gap-4 py-20">
              <ShoppingBag className="h-10 w-10 text-soft-app" />
              <p className="text-muted-app max-w-xs">{t("cart.empty")}</p>
            </div>
          ) : (
            <ul className="space-y-4">
              {items.map((item) => (
                <li
                  key={item.id}
                  data-testid={`cart-item-${item.id}`}
                  className="flex gap-4 py-4 border-b border-subtle last:border-0"
                >
                  {item.image && (
                    <img
                      src={item.image}
                      alt={item.name}
                      className="w-20 h-20 object-cover rounded-md img-luxe"
                    />
                  )}
                  <div className="flex-1 min-w-0">
                    <div className="flex justify-between gap-2">
                      <h4 className="font-display text-base text-primary-app truncate">
                        {item.name}
                      </h4>
                      <button
                        onClick={() => remove(item.id)}
                        className="text-soft-app hover:text-primary-app shrink-0"
                        aria-label="Remove"
                        data-testid={`cart-remove-${item.id}`}
                      >
                        <X className="h-4 w-4" />
                      </button>
                    </div>
                    <div className="flex items-center justify-between mt-3">
                      <div className="flex items-center gap-1 border border-subtle rounded-full">
                        <button
                          onClick={() => dec(item.id)}
                          className="p-1.5 hover:bg-base rounded-l-full"
                          data-testid={`cart-dec-${item.id}`}
                          aria-label="Decrease"
                        >
                          <Minus className="h-3 w-3" />
                        </button>
                        <span className="text-sm px-2 min-w-[1.5rem] text-center">
                          {item.quantity}
                        </span>
                        <button
                          onClick={() => inc(item.id)}
                          className="p-1.5 hover:bg-base rounded-r-full"
                          data-testid={`cart-inc-${item.id}`}
                          aria-label="Increase"
                        >
                          <Plus className="h-3 w-3" />
                        </button>
                      </div>
                      <span className="text-sm font-medium text-primary-app">
                        {(item.price * item.quantity).toFixed(2)} €
                      </span>
                    </div>
                  </div>
                </li>
              ))}
            </ul>
          )}
        </div>

        <div className="border-t border-subtle p-6 space-y-4 bg-elevated">
          <div className="flex items-center justify-between text-sm">
            <span className="eyebrow">{t("cart.subtotal")}</span>
            <span
              data-testid="cart-subtotal"
              className="font-display text-2xl text-primary-app"
            >
              {subtotal.toFixed(2)} €
            </span>
          </div>

          <Button
            data-testid="cart-whatsapp-order"
            onClick={handleWhatsApp}
            disabled={items.length === 0}
            className="w-full h-12 rounded-full"
            style={{
              backgroundColor: "#25D366",
              color: "#fff",
            }}
          >
            {t("cart.whatsapp")}
          </Button>

          <div className="grid grid-cols-2 gap-2">
            <a
              href={BRAND.delivery.glovo}
              target="_blank"
              rel="noopener noreferrer"
              data-testid="cart-glovo"
              className={`text-center text-xs uppercase tracking-wider py-3 rounded-full border border-subtle transition-all ${
                items.length === 0
                  ? "opacity-40 pointer-events-none"
                  : "hover:border-strong hover:bg-base"
              }`}
            >
              Glovo
            </a>
            <a
              href={BRAND.delivery.talabat}
              target="_blank"
              rel="noopener noreferrer"
              data-testid="cart-talabat"
              className={`text-center text-xs uppercase tracking-wider py-3 rounded-full border border-subtle transition-all ${
                items.length === 0
                  ? "opacity-40 pointer-events-none"
                  : "hover:border-strong hover:bg-base"
              }`}
            >
              Talabat
            </a>
          </div>
        </div>
      </SheetContent>
    </Sheet>
  );
}
