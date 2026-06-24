import React, { createContext, useContext, useMemo, useState } from "react";

type Lang = "fr" | "en";

type Dict = Record<string, { fr: string; en: string }>;

const dict: Dict = {
  "nav.home": { fr: "Accueil", en: "Home" },
  "nav.menu": { fr: "Le Menu", en: "Menu" },
  "nav.blog": { fr: "Bibliothèque", en: "Journal" },
  "nav.about": { fr: "À Propos", en: "About" },
  "cta.reserve": { fr: "Réserver", en: "Reserve" },
  "cta.order": { fr: "Commander", en: "Order" },
  "cta.explore": { fr: "Explorer le menu", en: "Explore the menu" },
  "cta.viewMore": { fr: "Voir plus", en: "View more" },
  "cart.title": { fr: "Votre panier", en: "Your cart" },
  "cart.empty": {
    fr: "Votre panier attend ses premières merveilles.",
    en: "Your cart is waiting for its first wonders.",
  },
  "cart.subtotal": { fr: "Sous-total", en: "Subtotal" },
  "cart.whatsapp": { fr: "Commander via WhatsApp", en: "Order via WhatsApp" },
  "cart.glovo": { fr: "Commander via Glovo", en: "Order via Glovo" },
  "cart.talabat": { fr: "Commander via Talabat", en: "Order via Talabat" },
};

type I18nValue = {
  lang: Lang;
  setLang: (l: Lang) => void;
  t: (key: string) => string;
};

const I18nContext = createContext<I18nValue | null>(null);

export function I18nProvider({ children }: { children: React.ReactNode }) {
  const [lang, setLang] = useState<Lang>("fr");
  const value = useMemo<I18nValue>(
    () => ({
      lang,
      setLang,
      t: (key) => dict[key]?.[lang] ?? key,
    }),
    [lang]
  );
  return <I18nContext.Provider value={value}>{children}</I18nContext.Provider>;
}

export function useI18n() {
  const ctx = useContext(I18nContext);
  if (!ctx) throw new Error("useI18n must be used within I18nProvider");
  return ctx;
}
